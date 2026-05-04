# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0
from dataclasses import asdict
from typing import Dict, Optional, Set

from loguru import logger
from sklearn.metrics import f1_score, precision_score, recall_score

from poly_bench_evaluation.polybench_data import PolyBenchInstance, PolyBenchRetrievalMetrics
from poly_bench_evaluation.repo_utils import RepoManager

from .patch_metrics import _get_node_metric_inputs, file_retrieval_metrics
from .patch_utils import Patch


def instance_level_metric_scoring(
    instance: PolyBenchInstance,
    repo_path: str,
    node_retrieval_metrics: bool = False,
    modified_nodes: list = None,
) -> PolyBenchRetrievalMetrics:
    repo = instance.repo
    model_patch = instance.model_patch
    patch = instance.patch
    repo = instance.repo
    # Compute file retrieval metrics
    reference_patch = Patch(patch)
    predicted_patch = Patch(model_patch)

    file_metrics = file_retrieval_metrics(
        reference_patch=reference_patch, predicted_patch=predicted_patch
    )
    ref_nodes: Optional[Set[str]] = None
    pred_nodes: Optional[Set[str]] = None

    if node_retrieval_metrics:
        # Set up repository
        rm = RepoManager(repo_name=repo, repo_path=repo_path)
        rm.clone_repo()
        rm.checkout_commit(instance.base_commit)

        # Compute metrics
        node_metrics: Dict[str, Optional[float]] = {}
        prediction_problem = False
        reference_problem = False
        failed_gt_patch_apply = False
        try:
            y_true, y_pred, num_ref_nodes, ref_nodes, pred_nodes = _get_node_metric_inputs(
                reference_patch,
                predicted_patch,
                rm,
                return_nodes=True,
                reference_nodes_full=set(modified_nodes),
            )
            if num_ref_nodes == 0:
                # No nodes were extracted
                reference_problem = True
        except ValueError as e:
            if "predicted nodes" in str(e):
                prediction_problem = True
            elif "reference nodes" in str(e):
                failed_gt_patch_apply = True
            else:
                logger.error(f"Problems computing node_metrics {e}")
                raise e

        if failed_gt_patch_apply:
            node_metrics = {"recall": -1.0, "precision": -1.0, "f1": -1.0}
        elif reference_problem:
            node_metrics = {"recall": None, "precision": None, "f1": None}
        elif prediction_problem:
            node_metrics = {"recall": 0.0, "precision": 0.0, "f1": 0.0}
        else:
            node_metrics = {
                "recall": recall_score(y_true, y_pred),
                "precision": precision_score(y_true, y_pred),
                "f1": f1_score(y_true, y_pred),
            }

    return PolyBenchRetrievalMetrics(
        instance_id=instance.instance_id,
        file_retrieval_metrics=asdict(file_metrics),
        node_retrieval_metrics=node_metrics if node_retrieval_metrics else None,
        reference_nodes=list(ref_nodes) if ref_nodes else [],
        predicted_nodes=list(pred_nodes) if pred_nodes else [],
    )


def _get_zero_result(instance_id: str, node_retrieval_metrics: bool = False):
    return PolyBenchRetrievalMetrics(
        instance_id=instance_id,
        file_retrieval_metrics={
            "recall": 0.0,
            "precision": 0.0,
            "f1": 0.0,
        },
        node_retrieval_metrics=(
            {
                "recall": 0.0,
                "precision": 0.0,
                "f1": 0.0,
            }
            if node_retrieval_metrics
            else None
        ),
        reference_nodes=[],
        predicted_nodes=[],
    )
