# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0
from dataclasses import dataclass, field
from typing import List


@dataclass
class ParserResults:
    """Class to represent parser results from test executions."""

    num_tests_passed: int = 0
    num_tests_failed: int = 0
    failed_tests: List[str] = field(default_factory=list)
    passed_tests: List[str] = field(default_factory=list)
