# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0
import ast
import json
from dataclasses import dataclass
from typing import Dict, List, Optional

import pandas as pd
from pydantic import BaseModel, ConfigDict


class PolyBenchInstance(BaseModel):
    """Model to represent the required components of a PolyBench instance."""

    model_config = ConfigDict(protected_namespaces=(), extra="allow")

    instance_id: str
    model_patch: str
    patch: str
    test_patch: str
    repo: str
    base_commit: str
    language: str
    dockerfile: str
    f2p: List[str]
    p2p: List[str]
    test_command: str
    modified_nodes: List[str]


@dataclass
class PolyBenchOutput:
    """Class to represent instance level polybench outputs."""

    instance_id: str
    patch_applied: bool
    generation: bool
    with_logs: bool
    all_f2p_passed: bool
    no_p2p_failed: bool
    resolved: bool
    passed_tests: List[str]
    failed_tests: List[str]


@dataclass
class PolyBenchRetrievalMetrics:
    """Class to represent instance level retrieval metrics."""

    instance_id: str
    file_retrieval_metrics: Dict[str, Optional[float]]
    node_retrieval_metrics: Optional[Dict[str, Optional[float]]]
    reference_nodes: Optional[List[str]]
    predicted_nodes: Optional[List[str]]


@dataclass
class AggregateOutput:
    """Class to represent aggregate of instances outputs."""

    no_generation: List[str]
    generation: List[str]
    patch_applied: List[str]
    with_logs: List[str]
    resolved: List[str]
    not_resolved: List[str]
    total_empty_patch_instances: int
    total_instances: int
    total_resolved: int
    total_unresolved: int
    file_retrieval: List[Dict[str, float]]
    node_retrieval: Optional[List[Dict[str, float]]]


def dataset_generator(data: pd.DataFrame):
    """Generate a PolyBench instance from the dataframe."""

    for _, row in data.iterrows():
        yield PolyBenchInstance.model_validate(
            {
                "instance_id": row.instance_id,
                "model_patch": row.model_patch if "model_patch" in row else "",
                "patch": row.patch,
                "test_patch": row.test_patch,
                "repo": row.repo,
                "base_commit": row.base_commit,
                "language": row.language,
                "dockerfile": row.Dockerfile,
                "f2p": ast.literal_eval(row.F2P),
                "p2p": ast.literal_eval(row.P2P),
                "test_command": row.test_command,
                "modified_nodes": json.loads(row.modified_nodes),
            }
        )
