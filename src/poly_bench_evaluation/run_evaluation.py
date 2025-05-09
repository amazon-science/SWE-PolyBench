# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0

import argparse
import importlib
from multiprocessing.pool import ThreadPool
from pathlib import Path
from typing import Union
import json

import docker
import pandas as pd
from loguru import logger

from poly_bench_evaluation.constants import DEFAULT_TIMEOUT, JAVA_TIMEOUT, REPO_TO_PARSER_CLASS
from poly_bench_evaluation.docker_utils import DockerManager
from poly_bench_evaluation.metrics.metric_scoring import (
    _get_zero_result,
    instance_level_metric_scoring,
)
from poly_bench_evaluation.polybench_data import (
    PolyBenchInstance,
    PolyBenchOutput,
    PolyBenchRetrievalMetrics,
    dataset_generator,
)
from poly_bench_evaluation.repo_utils import RepoManager
from poly_bench_evaluation.scoring import (
    aggregate_logs,
    instance_level_scoring,
    store_instance_level_output,
)
from datasets import load_dataset


def evaluate_instance(
    instance: PolyBenchInstance,
    result_path: str,
    evaluate_gold: bool,
    repo_path: str,
    delete_image: bool,
    client: docker.DockerClient,
    retrieval_metrics_only: bool = False,
    node_retrieval_metrics: bool = False,
):
    """Instance level evaluation function.
    Args:
        instance: PolyBench row instance
        result_path: Path to store the output results.
        evaluate_gold: whether to evaluate the gold patch
        repo_path: Base repo close path.
        delete_image: whether to delete the image after docker build
        client: The docker client
        retrieval_metrics_only: Whether to only compute retrieval metrics.
        node_retrieval_metrics: Whether to compute compute-heavy node retrieval metrics.
    Raises:
        ValueError: if the docker build fails
    """
    instance_id = instance.instance_id
    model_patch = instance.model_patch if instance.model_patch else ""
    test_patch = instance.test_patch
    repo = instance.repo
    base_commit = instance.base_commit
    language = instance.language
    parser_class_name = REPO_TO_PARSER_CLASS.get(repo, None)

    if not parser_class_name:
        raise ValueError(f"Parser class not found for repo: {repo}. Please check the repo name.")

    f2p = instance.f2p
    p2p = instance.p2p
    test_command = instance.test_command

    if evaluate_gold:
        model_patch = instance.patch

    instance_output: Union[PolyBenchOutput, PolyBenchRetrievalMetrics]
    if retrieval_metrics_only:
        logger.info(f"Computing only retrieval metrics for {instance_id}")
        instance_output = instance_level_metric_scoring(
            instance=instance,
            repo_path=repo_path,
            node_retrieval_metrics=node_retrieval_metrics,
            modified_nodes=instance.modified_nodes,
        )
        store_instance_level_output(
            instance_output=instance_output, result_path=result_path, suffix="_metrics"
        )
        return

    if not model_patch.strip():  # if model patch is empty
        # Store pass rate results
        logger.info(f"model patch empty for {instance_id}")
        instance_output = instance_level_scoring(
            instance_id=instance_id,
            result={},
            f2p=f2p,
            p2p=p2p,
            patch_applied=False,
            generation=False,
        )
        store_instance_level_output(instance_output=instance_output, result_path=result_path)

        # Store retrieval metrics
        zero_metrics = _get_zero_result(
            instance_id=instance_id, node_retrieval_metrics=node_retrieval_metrics
        )
        store_instance_level_output(
            instance_output=zero_metrics, result_path=result_path, suffix="_metrics"
        )

        return

    image_id = f"polybench_{language.lower()}_{instance_id.lower()}"

    # build docker if image id is not available in local or public.ecr
    docker_manager = DockerManager(image_id=image_id, delete_image=delete_image, client=client)

    repo_manager = None
    if not docker_manager.check_image_local(local_image_name=image_id):
        logger.info("Image not found locally, building docker images...")
        # clone the repo and build docker image
        repo_manager = RepoManager(repo_name=repo, repo_path=repo_path)
        repo_manager.clone_repo()
        repo_manager.checkout_commit(commit_hash=base_commit)

        assert repo_manager.tmp_repo_dir is not None, "Repo not properly cloned."

        build_logs_path = Path("./build_logs")
        build_logs_path.mkdir(exist_ok=True)
        retry = 3
        for attempt in range(retry):
            logger.info(f"Docker building - Attempt {attempt + 1}/{retry}")
            build_success = docker_manager.docker_build(
                repo_path=repo_manager.tmp_repo_dir, dockerfile_content=instance.dockerfile
            )

            # Save build logs regardless of success/failure
            build_logs_string = "\n".join(docker_manager.build_logs)
            log_file_path = build_logs_path / f"{instance_id}_build.log"
            with open(log_file_path, "w") as f:
                f.write(build_logs_string)

            if build_success == 0:
                logger.info(f"Docker build successful for {instance_id}")
                break

            if attempt < retry - 1:  # Don't log "retrying" on the last attempt
                logger.warning(
                    f"Docker build failed for {instance_id} on attempt {attempt + 1}, retrying..."
                )

        # If we get here, all retries failed
        if build_success != 0:
            raise ValueError(
                f"Docker build failed for {instance_id} after {retry} attempts. Please check the dockerfile content and build logs."
            )

    # Create a docker container and run the image
    docker_manager.create_container()

    # Apply the test patch
    try:
        _ = docker_manager.apply_patch_to_container(patch_content=test_patch, patch_type="test")
    except Exception:
        logger.debug(f"test patch apply error for instance id: {instance_id}, please check.")
        instance_output = instance_level_scoring(
            instance_id=instance_id,
            result={},
            f2p=f2p,
            p2p=p2p,
            patch_applied=False,
            generation=False,
        )
        store_instance_level_output(instance_output=instance_output, result_path=result_path)

        # Store retrieval metrics
        instance_metric_output = instance_level_metric_scoring(
            instance=instance, repo_path=repo_path, node_retrieval_metrics=node_retrieval_metrics, modified_nodes=instance.modified_nodes
        )
        store_instance_level_output(
            instance_output=instance_metric_output, result_path=result_path, suffix="_metrics"
        )

        docker_manager.__del__()
        return

    # Apply the code patch
    try:
        patch_success = docker_manager.apply_patch_to_container(
            patch_content=model_patch, patch_type="code"
        )
    except Exception:
        patch_success = 1
        logger.debug(f"patch error for instance id: {instance_id}")

    if patch_success != 0:
        logger.info(f"patch apply error for instance id: {instance_id}")
        instance_output = instance_level_scoring(
            instance_id=instance_id,
            result={},
            f2p=f2p,
            p2p=p2p,
            patch_applied=False,
            generation=True,
        )
        store_instance_level_output(instance_output=instance_output, result_path=result_path)

        # Store retrieval metrics
        zero_metrics = _get_zero_result(
            instance_id=instance_id, node_retrieval_metrics=node_retrieval_metrics
        )
        store_instance_level_output(
            instance_output=zero_metrics, result_path=result_path, suffix="_metrics"
        )

        docker_manager.__del__()
        return

    logger.info(f"docker running for {instance_id}")
    run_timeout = JAVA_TIMEOUT if language.lower() == "java" else DEFAULT_TIMEOUT

    _ = docker_manager.docker_run(test_command=test_command, timeout=run_timeout)

    # log the run logs
    run_logs_string = "\n".join(docker_manager.run_logs)
    run_logs_path = Path(f"./run_logs_{language.lower()}")
    run_logs_path.mkdir(exist_ok=True)

    with open(str(run_logs_path) + f"/{instance_id}_run.log", "w") as f:
        f.write(run_logs_string)

    # parse the log of docker run
    all_parsers = importlib.import_module("poly_bench_evaluation.parsers")
    if hasattr(all_parsers, parser_class_name):
        parser_class = getattr(all_parsers, parser_class_name)
        log_parser = parser_class(test_content=run_logs_string)
        result = log_parser.parse()
    else:
        raise ValueError(
            f"Parser class {parser_class_name} not found in the parsers module. Please ensure proper paraser class name."
        )

    instance_output = instance_level_scoring(
        instance_id=instance_id,
        result=result,
        f2p=f2p,
        p2p=p2p,
        patch_applied=True,
        generation=True,
    )
    store_instance_level_output(instance_output=instance_output, result_path=result_path)

    # Store retrieval metrics
    instance_metric_output = instance_level_metric_scoring(
        instance=instance, repo_path=repo_path, node_retrieval_metrics=node_retrieval_metrics, modified_nodes=instance.modified_nodes
    )
    store_instance_level_output(
        instance_output=instance_metric_output, result_path=result_path, suffix="_metrics"
    )

    docker_manager.__del__()
    if repo_manager is not None:
        repo_manager.__del__()


def evaluate_predictions(
    dataset_path: str,
    predictions_path: str,
    result_path: str,
    num_threads: int,
    evaluate_gold: bool,
    repo_path: str,
    delete_image: bool,
    skip_existing: bool,
    retrieval_metrics_only: bool = False,
    node_retrieval_metrics: bool = False,
):
    """Predictions file evaluation function.
    Args:
        dataset_path: Path to the dataset file (csv) or huggingface.
        predictions_path: Path to the predictions file.
        result_path: Path to store the output results.
        num_threads: Number of threads to use.
        evaluate_gold: Whether to evaluate the gold patches.
        repo_path: Base repo close path.
        delete_image: Whether to delete the image after docker build/ecr pull.
        skip_existing: Whether to skip the existing evaluations in result_path.
        retrieval_metrics_only: Whether to only compute retrieval metrics.
        node_retrieval_metrics: Whether to compute compute-heavy node retrieval metrics.
    Raises:
        ValueError: If the predictions file is not in the correct format.
    """
    client = docker.from_env(timeout=720)
    try:
        dataset = (
            pd.read_csv(dataset_path)
            if dataset_path.endswith(".csv")
            else load_dataset(dataset_path, split="test").to_pandas()
        )
    except Exception:
        raise ValueError("Please provide a correct dataset file or huggingface path.")

    suffix = "_result" if not retrieval_metrics_only else "_metrics"

    if skip_existing:
        dataset = dataset[
            ~dataset["instance_id"].isin(
                [f.stem.replace(suffix, "") for f in Path(result_path).glob(f"*{suffix}.json")]
            )
        ]

    logger.info(f"Remaining samples to evaluate: {len(dataset)}")
    assert "language" in dataset.columns, "language column not found in dataset file."

    logger.info("Building base images...")
    for language in dataset["language"].unique():
        if language != "Python":
            base_image_id = f"polybench_{language.lower()}_base"
            base_docker_manager = DockerManager(
                image_id=base_image_id, delete_image=False, client=client
            )
            base_docker_manager.build_base_image(language=language)

    if predictions_path:
        try:
            predictions = pd.read_json(predictions_path, lines=True)

            assert (
                "model_patch" in predictions.columns
            ), "model_patch column not found in predictions file."
            assert (
                "instance_id" in predictions.columns
            ), "instance_id column not found in predictions file."

            dataset = pd.merge(
                dataset,
                predictions[["instance_id", "model_patch"]],
                how="left",
                on="instance_id",
            )
            # Fill any missing model_patch values with empty string
            dataset.fillna({"model_patch": ""}, inplace=True)
        except Exception:
            raise ValueError("Please provide a correct predictions jsonl file.")

    with ThreadPool(num_threads) as pool:

        def process_wrapper(instance: PolyBenchInstance):
            return evaluate_instance(
                instance=instance,
                result_path=result_path,
                evaluate_gold=evaluate_gold,
                repo_path=repo_path,
                delete_image=delete_image,
                client=client,
                retrieval_metrics_only=retrieval_metrics_only,
                node_retrieval_metrics=node_retrieval_metrics,
            )

        data_gen = dataset_generator(dataset)

        results = pool.imap_unordered(process_wrapper, data_gen)
        results_list = list(results)  # noqa: F841

    # aggregate the logs of all instance_ids into one json
    aggregate_logs(
        result_path=result_path, dataset_path=dataset_path, metrics_only=retrieval_metrics_only
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-path", type=str, required=True)
    parser.add_argument("--predictions-path", type=str, required=False)
    parser.add_argument("--result-path", type=str, required=True)
    parser.add_argument("--num-threads", type=int, default=1, required=False)
    parser.add_argument("--evaluate-gold", action="store_true", default=False)
    parser.add_argument("--repo-path", type=str, default="~/polybench_repos", required=False)
    parser.add_argument("--delete-image", action="store_true", default=False)
    parser.add_argument("--skip-existing", action="store_true", default=False)
    parser.add_argument(
        "--metrics-only",
        action="store_true",
        default=False,
        help="If set, no pass rates will be computed.",
    )
    parser.add_argument(
        "--node-metrics",
        action="store_true",
        default=False,
        help="If set, node retrieval metrics will be computed.",
    )

    args = parser.parse_args()

    evaluate_predictions(
        dataset_path=args.dataset_path,
        predictions_path=args.predictions_path,
        result_path=args.result_path,
        num_threads=args.num_threads,
        evaluate_gold=args.evaluate_gold,
        repo_path=args.repo_path,
        delete_image=args.delete_image,
        skip_existing=args.skip_existing,
        retrieval_metrics_only=args.metrics_only,
        node_retrieval_metrics=args.node_metrics,
    )
