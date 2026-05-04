# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0
from dataclasses import dataclass
from typing import List, Optional, Set, Tuple

from sklearn.metrics import f1_score, precision_score, recall_score

from poly_bench_evaluation.repo_utils import RepoManager

from .patch_utils import Patch


@dataclass
class RetrievalMetrics:
    """Dataclass to store retrieval metrics."""

    recall: float
    precision: float
    f1: float


def _get_file_metric_inputs(
    reference_patch: Patch, predicted_patch: Patch, to_basename: bool = False
) -> Tuple[List[int], List[int]]:
    """Compute the common part of file retrieval metrics.

    Args:
        reference_patch: The reference patch.
        predicted_patch: The predicted patch.
        to_basename: Whether to use the basenames of the files.

    Returns:
        A tuple containing y_true and y_pred lists.
    """
    reference_files = reference_patch.get_modified_files(to_basename=to_basename)
    predicted_files = predicted_patch.get_modified_files(to_basename=to_basename)

    # Create binary labels for each file in the union of reference and predicted files
    all_files = list(reference_files.union(predicted_files))
    y_true = [int(file in reference_files) for file in all_files]
    y_pred = [int(file in predicted_files) for file in all_files]

    return y_true, y_pred


def file_recall(reference_patch: Patch, predicted_patch: Patch, to_basename: bool = False) -> float:
    """Compute the recall of modified files in the predicted_patch over the ground truth modified files in the reference_patch.

    Args:
        reference_patch: The reference patch.
        predicted_patch: The predicted patch.
        to_basename: Whether to use the basenames of the files.

    Returns:
        The recall score.
    """
    y_true, y_pred = _get_file_metric_inputs(reference_patch, predicted_patch, to_basename)
    return recall_score(y_true, y_pred)


def file_precision(
    reference_patch: Patch, predicted_patch: Patch, to_basename: bool = False
) -> float:
    """Compute the precision of modified files in the predicted_patch over the ground truth modified files in the reference_patch.

    Args:
        reference_patch: The reference patch.
        predicted_patch: The predicted patch.
        to_basename: Whether to use the basenames of the files.

    Returns:
        The precision score.
    """
    y_true, y_pred = _get_file_metric_inputs(reference_patch, predicted_patch, to_basename)
    return precision_score(y_true, y_pred)


def file_f1_score(
    reference_patch: Patch, predicted_patch: Patch, to_basename: bool = False
) -> float:
    """Compute the f1 score of modified files in the predicted_patch over the ground truth modified files in the reference_patch.

    Args:
        reference_patch: The reference patch.
        predicted_patch: The predicted patch.
        to_basename: Whether to use the basenames of the files.

    Returns:
        The f1 score.
    """
    y_true, y_pred = _get_file_metric_inputs(reference_patch, predicted_patch, to_basename)
    return f1_score(y_true, y_pred)


def file_retrieval_metrics(
    reference_patch: Patch, predicted_patch: Patch, to_basename: bool = False
) -> RetrievalMetrics:
    """Compute the recall, precision, and f1 score of modified files in the predicted_patch over the ground truth modified files in the reference_patch.

    Args:
        reference_patch: The reference patch.
        predicted_patch: The predicted patch.
        to_basename: Whether to use the basenames of the files.

    Returns:
        A dictionary containing the recall, precision, and f1 score.
    """
    recall = file_recall(reference_patch, predicted_patch, to_basename)
    precision = file_precision(reference_patch, predicted_patch, to_basename)
    f1 = file_f1_score(reference_patch, predicted_patch, to_basename)
    return RetrievalMetrics(recall=recall, precision=precision, f1=f1)


def _get_node_metric_inputs(
    reference_patch: Patch,
    predicted_patch: Patch,
    repo_manager: RepoManager,
    return_nodes: bool = False,
    reference_nodes_full: set = None,
) -> Tuple[List[int], List[int], int, Optional[Set[str]], Optional[Set[str]]]:
    """Compute the common part of node retrieval metrics.

    Args:
        reference_patch: The reference patch.
        predicted_patch: The predicted patch.
        repo_manager: The repo manager object.

    Returns:
        A tuple containing y_true and y_pred lists.
    """

    # We are now getting reference nodes from the data set, this is no longer needed
    # but kept in case we want to compute nodes for different datasets.
    # try:
    #   reference_nodes = reference_patch.get_modified_nodes(repo_manager=repo_manager)
    # except Exception as e:
    #   raise ValueError(f"Error in getting reference nodes: {e}") from e

    # reference_nodes_full = set(
    #   [
    #       f"{file}->{cst_path}"
    #       for file, cst_path_set in reference_nodes.items()
    #       for cst_path in cst_path_set
    #   ]
    # )

    ## the above will apply `reference_patch` to the repo, hence we reset it
    # repo_manager.reset_repo()

    try:
        predicted_nodes = predicted_patch.get_modified_nodes(repo_manager=repo_manager)
    except Exception as e:
        raise ValueError(f"Error in getting predicted nodes: {e}") from e

    predicted_nodes_full = set(
        [
            f"{file}->{cst_path}"
            for file, cst_path_set in predicted_nodes.items()
            for cst_path in cst_path_set
        ]
    )

    # Create binary labels for each node in the union of reference and predicted nodes
    all_nodes = list(reference_nodes_full.union(predicted_nodes_full))
    y_true = [int(cst_path in reference_nodes_full) for cst_path in all_nodes]
    y_pred = [int(cst_path in predicted_nodes_full) for cst_path in all_nodes]

    if return_nodes:
        return y_true, y_pred, len(reference_nodes_full), reference_nodes_full, predicted_nodes_full
    else:
        return y_true, y_pred, len(reference_nodes_full), None, None


def node_retrieval_metrics(
    reference_patch: Patch, predicted_patch: Patch, repo_manager: RepoManager
) -> Optional[RetrievalMetrics]:
    """Compute the recall, precision, and f1 score of retrieved nodes in the predicted_patch over the ground truth modified nodes in the reference_patch.

    Args:
        reference_patch: The reference patch.
        predicted_patch: The predicted patch.

    Returns:
        A dictionary containing the recall, precision, and f1 score.
    """

    y_true, y_pred, _, _, _ = _get_node_metric_inputs(
        reference_patch=reference_patch, predicted_patch=predicted_patch, repo_manager=repo_manager
    )
    # It's possible that no nodes are found (e.g., changes in module level only)
    if not y_true:
        return None

    recall = recall_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    return RetrievalMetrics(recall=recall, precision=precision, f1=f1)
