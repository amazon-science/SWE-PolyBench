"""Build a single SWE-PolyBench instance Docker image.

This script handles the Docker image building process for a single instance,
including base image creation and instance-specific image building.
"""

import sys
import json
import argparse
from pathlib import Path

import docker

from poly_bench_evaluation.docker_utils import DockerManager
from poly_bench_evaluation.repo_utils import RepoManager


def parse_args():
    parser = argparse.ArgumentParser(
        description="Build a single SWE-PolyBench instance Docker image"
    )
    parser.add_argument(
        "instance_id",
        help="Instance ID for the image"
    )
    parser.add_argument(
        "language", 
        help="Programming language (Java, JavaScript, TypeScript, Python)"
    )
    parser.add_argument(
        "repo",
        help="Repository name (e.g., google/gson)"
    )
    parser.add_argument(
        "base_commit",
        help="Base commit hash to checkout"
    )
    parser.add_argument(
        "dockerfile",
        help="Dockerfile content as string"
    )
    parser.add_argument(
        "repo_path",
        help="Base path for repository cloning"
    )
    
    return parser.parse_args()


def main():
    args = parse_args()
    
    instance_id = args.instance_id
    language = args.language
    repo = args.repo
    base_commit = args.base_commit
    dockerfile = args.dockerfile
    repo_path = args.repo_path
    
    try:
        # Create docker client
        client = docker.from_env(timeout=720)
        
        # Build base image if needed (non-Python languages)
        if language != "Python":
            base_image_id = f"polybench_{language.lower()}_base"
            base_docker_manager = DockerManager(image_id=base_image_id, delete_image=False, client=client)
            
            # Check if base image exists, build if not
            if not base_docker_manager.check_image_local(local_image_name=base_image_id):
                print(f"Building base image for {language}...")
                base_docker_manager.build_base_image(language=language)
            else:
                print(f"Base image for {language} already exists")
        
        # Build instance image
        image_id = f"polybench_{language.lower()}_{instance_id.lower()}"
        docker_manager = DockerManager(image_id=image_id, delete_image=False, client=client)
        
        # Check if image already exists locally
        if docker_manager.check_image_local(local_image_name=image_id):
            print(f"Image {image_id} already exists locally")
            return 0
        
        print(f"Cloning repository {repo} and checking out {base_commit[:8]}...")
        
        # Clone repo and checkout commit
        repo_manager = RepoManager(repo_name=repo, repo_path=repo_path)
        repo_manager.clone_repo()
        repo_manager.checkout_commit(commit_hash=base_commit)
        
        print(f"Building Docker image {image_id}...")
        
        # Build docker image
        build_success = docker_manager.docker_build(
            repo_path=repo_manager.tmp_repo_dir,
            dockerfile_content=dockerfile
        )
        
        # Clean up repo manager
        repo_manager.__del__()
        
        if build_success != 0:
            print(f"Failed to build image for {instance_id}")
            # Print build logs for debugging
            if docker_manager.build_logs:
                print("Build logs:")
                for log in docker_manager.build_logs[-10:]:  # Last 10 lines
                    print(f"  {log}")
            return 1
        
        print(f"Successfully built image {image_id}")
        return 0
        
    except Exception as e:
        print(f"Error building image for {instance_id}: {e}")
        return 1


if __name__ == "__main__":
    main()