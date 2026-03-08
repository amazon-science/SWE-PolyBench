#!/usr/bin/env python3
"""Build or retag Docker images for SWE-PolyBench instances.

This script ensures that Docker images are available with the correct tags
expected by mini-swe-agent (swebench/sweb.eval.x86_64.{instance_id}:latest).

The script will:
1. Check if the target image already exists locally
2. If not, check if a pre-built image exists (ghcr.io/timesler/... or polybench_...)
3. If found, retag it to the expected format
4. If not found, build the image from the dataset's Dockerfile
"""

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import docker
from datasets import load_dataset
from loguru import logger


def get_target_tag(instance_id: str) -> str:
    """Get the target tag expected by mini-swe-agent.

    mini-swe-agent expects: docker.io/swebench/sweb.eval.x86_64.{instance_id}:latest
    It replaces "__" with "_1776_" because Docker doesn't allow double underscore.
    """
    # Same logic as mini-swe-agent: replace __ with _1776_
    id_docker_compatible = instance_id.replace("__", "_1776_")
    return f"docker.io/swebench/sweb.eval.x86_64.{id_docker_compatible}:latest"


def get_polybench_local_tag(instance_id: str, language: str) -> str:
    """Get the local tag format used by PolyBench evaluation scripts."""
    return f"polybench_{language.lower()}_{instance_id.lower()}:latest"


def get_ghcr_tag(instance_id: str) -> str:
    """Get the GHCR tag for pre-built images (official PolyBench images)."""
    return f"ghcr.io/timesler/swe-polybench.eval.x86_64.{instance_id.lower()}:latest"


def check_image_exists(client: docker.DockerClient, tag: str) -> bool:
    """Check if an image exists locally."""
    try:
        client.images.get(tag)
        return True
    except docker.errors.ImageNotFound:
        return False
    except Exception:
        return False


def check_image_exists_subprocess(tag: str) -> bool:
    """Check if an image exists locally using subprocess (fallback)."""
    result = subprocess.run(
        ["docker", "image", "inspect", tag],
        capture_output=True,
        text=True
    )
    return result.returncode == 0


def retag_image(client: docker.DockerClient, source_tag: str, target_tag: str) -> bool:
    """Retag an existing image."""
    try:
        image = client.images.get(source_tag)
        # Extract repo:tag from target_tag
        if ":" in target_tag:
            repo, tag = target_tag.rsplit(":", 1)
        else:
            repo = target_tag
            tag = "latest"
        image.tag(repo, tag=tag)
        logger.info(f"Retagged: {source_tag} -> {target_tag}")
        return True
    except docker.errors.ImageNotFound:
        logger.debug(f"Source image not found: {source_tag}")
        return False
    except Exception as e:
        logger.error(f"Failed to retag {source_tag} to {target_tag}: {e}")
        return False


def pull_and_retag(client: docker.DockerClient, instance_id: str, target_tag: str) -> bool:
    """Try to pull pre-built image from GHCR and retag it."""
    ghcr_tag = get_ghcr_tag(instance_id)

    try:
        logger.info(f"Attempting to pull pre-built image: {ghcr_tag}")
        client.images.pull(ghcr_tag)

        if retag_image(client, ghcr_tag, target_tag):
            logger.info(f"Successfully pulled and retagged image for {instance_id}")
            return True
    except docker.errors.ImageNotFound:
        logger.info(f"Pre-built image not found in GHCR: {ghcr_tag}")
    except docker.errors.APIError as e:
        logger.info(f"Failed to pull pre-built image: {e}")
    except Exception as e:
        logger.info(f"Unexpected error pulling pre-built image: {e}")

    return False


def build_image(client: docker.DockerClient, instance: dict, target_tag: str, repo_path: str = "/tmp/polybench_repos") -> bool:
    """Build a Docker image from the instance's Dockerfile."""
    instance_id = instance["instance_id"]
    language = instance["language"]
    repo = instance["repo"]
    base_commit = instance["base_commit"]
    dockerfile_content = instance.get("Dockerfile", instance.get("dockerfile", ""))

    if not dockerfile_content:
        logger.error(f"No Dockerfile found for instance {instance_id}")
        return False

    # First, ensure base image exists for non-Python languages
    if language != "Python":
        from poly_bench_evaluation.constants import LANGUAGE_TO_BASE_DOCKERFILE
        base_image_id = f"polybench_{language.lower()}_base"

        if not check_image_exists(client, base_image_id):
            logger.info(f"Building base image for {language}...")
            with tempfile.TemporaryDirectory() as tmpdir:
                tmp_path = Path(tmpdir)
                (tmp_path / "Dockerfile").write_text(LANGUAGE_TO_BASE_DOCKERFILE[language])

                try:
                    _, build_logs = client.images.build(
                        path=str(tmp_path),
                        tag=base_image_id,
                        rm=True,
                        platform="linux/amd64"
                    )
                    logger.info(f"Successfully built base image for {language}")
                except Exception as e:
                    logger.error(f"Failed to build base image for {language}: {e}")
                    return False
        else:
            logger.info(f"Base image for {language} already exists")

    # Clone repo if needed
    repo_dir = Path(repo_path) / repo.replace("/", "_")

    if not repo_dir.exists():
        logger.info(f"Cloning repository {repo}...")
        repo_dir.parent.mkdir(parents=True, exist_ok=True)
        result = subprocess.run(
            ["git", "clone", f"https://github.com/{repo}.git", str(repo_dir)],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            logger.error(f"Failed to clone {repo}: {result.stderr}")
            return False

    # Checkout base commit
    logger.info(f"Checking out {base_commit[:8]}...")
    result = subprocess.run(
        ["git", "checkout", base_commit],
        cwd=repo_dir,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        logger.error(f"Failed to checkout {base_commit}: {result.stderr}")
        return False

    # Write Dockerfile and build
    dockerfile_path = repo_dir / "Dockerfile"
    dockerfile_path.write_text(dockerfile_content)

    # Remove .dockerignore if exists (can cause issues)
    dockerignore_path = repo_dir / ".dockerignore"
    if dockerignore_path.exists():
        dockerignore_path.unlink()

    logger.info(f"Building Docker image {target_tag}...")

    try:
        # Extract repo:tag from target_tag
        if ":" in target_tag:
            repo_tag, tag = target_tag.rsplit(":", 1)
        else:
            repo_tag = target_tag
            tag = "latest"

        image, build_logs = client.images.build(
            path=str(repo_dir),
            tag=f"{repo_tag}:{tag}",
            rm=True,
            platform="linux/amd64"
        )

        for log in build_logs:
            if "stream" in log and log["stream"].strip():
                logger.debug(log["stream"].strip())
            elif "error" in log:
                logger.error(f"Build error: {log['error']}")

        logger.info(f"Successfully built image {target_tag}")
        return True

    except docker.errors.BuildError as e:
        logger.error(f"Build error for {instance_id}: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error building image for {instance_id}: {e}")
        return False


def process_instance(client: docker.DockerClient, instance: dict, force_build: bool = False, repo_path: str = "/tmp/polybench_repos") -> str:
    """Process a single instance: retag or build its Docker image.

    Returns:
        str: "exists", "retagged", "built", or "failed"
    """
    instance_id = instance["instance_id"]
    language = instance["language"]
    target_tag = get_target_tag(instance_id)

    # 1. Check if target image already exists
    if not force_build and check_image_exists(client, target_tag):
        logger.info(f"[SKIP] {instance_id}: Target image already exists: {target_tag}")
        return "exists"

    # 2. Try to find and retag existing local images
    if not force_build:
        # Check polybench local tag
        polybench_tag = get_polybench_local_tag(instance_id, language)
        if check_image_exists(client, polybench_tag):
            if retag_image(client, polybench_tag, target_tag):
                return "retagged"

        # Check docker.io/library prefix (from your existing images)
        docker_io_tag = f"docker.io/library/polybench_{language.lower()}_{instance_id.lower()}:latest"
        if check_image_exists(client, docker_io_tag):
            if retag_image(client, docker_io_tag, target_tag):
                return "retagged"

        # Try to pull from GHCR
        if pull_and_retag(client, instance_id, target_tag):
            return "retagged"

    # 3. Build the image
    logger.info(f"[BUILD] {instance_id}: Building image...")
    if build_image(client, instance, target_tag, repo_path):
        return "built"

    return "failed"


def main():
    parser = argparse.ArgumentParser(
        description="Build or retag Docker images for SWE-PolyBench instances"
    )
    parser.add_argument(
        "dataset",
        nargs="?",
        default="AmazonScience/SWE-PolyBench_Verified",
        help="HuggingFace dataset name or path to CSV file"
    )
    parser.add_argument(
        "--split", "-s",
        default="test",
        help="Dataset split to use (default: test)"
    )
    parser.add_argument(
        "--limit", "-l",
        type=int,
        default=None,
        help="Limit number of instances to process"
    )
    parser.add_argument(
        "--offset", "-o",
        type=int,
        default=0,
        help="Skip first N instances (for resuming)"
    )
    parser.add_argument(
        "--instance-ids", "-i",
        nargs="+",
        default=None,
        help="Specific instance IDs to process"
    )
    parser.add_argument(
        "--force-build", "-f",
        action="store_true",
        help="Force build even if image exists"
    )
    parser.add_argument(
        "--repo-path",
        default="/tmp/polybench_repos",
        help="Path to store cloned repositories"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes"
    )
    parser.add_argument(
        "--lang",
        choices=["Python", "Java", "JavaScript", "TypeScript"],
        default=None,
        help="Only process instances of this language"
    )

    args = parser.parse_args()

    # Initialize Docker client
    try:
        client = docker.from_env(timeout=720)
    except Exception as e:
        logger.error(f"Failed to connect to Docker: {e}")
        sys.exit(1)

    # Load dataset
    logger.info(f"Loading dataset from {args.dataset}...")

    try:
        if args.dataset.endswith('.csv'):
            import pandas as pd
            df = pd.read_csv(args.dataset)
            instances = df.to_dict('records')
        else:
            ds = load_dataset(args.dataset, split=args.split)
            instances = list(ds)
    except Exception as e:
        logger.error(f"Failed to load dataset: {e}")
        sys.exit(1)

    logger.info(f"Loaded {len(instances)} instances")

    # Filter by instance IDs if specified
    if args.instance_ids:
        instances = [i for i in instances if i.get("instance_id") in args.instance_ids]
        logger.info(f"Filtered to {len(instances)} specified instances")

    # Filter by language if specified
    if args.lang:
        instances = [i for i in instances if i.get("language") == args.lang]
        logger.info(f"Filtered to {len(instances)} {args.lang} instances")

    # Apply offset and limit
    if args.offset > 0:
        instances = instances[args.offset:]
        logger.info(f"Skipped first {args.offset} instances")

    if args.limit:
        instances = instances[:args.limit]
        logger.info(f"Limited to {len(instances)} instances")

    # Process each instance
    stats = {"exists": 0, "retagged": 0, "built": 0, "failed": 0}
    failed_instances = []

    for i, instance in enumerate(instances, 1):
        instance_id = instance.get("instance_id", "unknown")
        logger.info(f"\n[{i}/{len(instances)}] Processing {instance_id}...")

        if args.dry_run:
            target_tag = get_target_tag(instance_id)
            if check_image_exists(client, target_tag):
                logger.info(f"  [DRY-RUN] Would skip (image exists): {target_tag}")
                stats["exists"] += 1
            else:
                logger.info(f"  [DRY-RUN] Would build/retag: {target_tag}")
                stats["built"] += 1
        else:
            result = process_instance(
                client, instance,
                force_build=args.force_build,
                repo_path=args.repo_path
            )
            stats[result] += 1

            if result == "failed":
                failed_instances.append(instance_id)

    # Print summary
    print("\n" + "=" * 60)
    print("Summary:")
    print(f"  Already exists: {stats['exists']}")
    print(f"  Retagged:       {stats['retagged']}")
    print(f"  Built:          {stats['built']}")
    print(f"  Failed:         {stats['failed']}")

    if failed_instances:
        print("\nFailed instances:")
        for iid in failed_instances:
            print(f"  - {iid}")

    return 0 if stats["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
