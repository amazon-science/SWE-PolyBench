# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0
from typing import Dict, Protocol


class TestOutputParser(Protocol):
    """Protocol for all test output parsers."""

    def parse(self) -> Dict:
        """Prunes the given code node.

        Returns:
            a dictionary of parsed results.
        """
        ...
