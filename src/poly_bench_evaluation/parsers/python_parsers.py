# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0
import re
from dataclasses import asdict
from typing import Dict, List, Optional

from poly_bench_evaluation.parsers.parser_protocol import TestOutputParser  # noqa: F401
from poly_bench_evaluation.parsers.parser_results import ParserResults


class PythonPyUnit:
    """A class for Python Pyunit and unittest frameworks parser"""

    def __init__(self, test_content: str):
        self.content = test_content

    def parse(self) -> Dict:
        """Parse function that parses the run logs string.
        Returns:
            Dict: A dictionary containing the parsed test results.
        """
        # determine test type
        if (
            "= test session starts =" in self.content
            or "= short test summary info =" in self.content
        ):
            test_type = "pytest"
        else:
            test_type = "unittest"

        # Create an array with test objects
        if test_type == "pytest":
            test_arr = self._parse_pytest_output(self.content)
        elif test_type == "unittest":
            test_arr = self._parse_unittest_output(self.content)

        # Iterate over array and get string representation
        result = ParserResults()

        if test_arr:
            for test in test_arr:
                if (
                    test
                    and "status" in test
                    and (test["status"] == "PASSED" or test["status"] == "ok")
                ):
                    if test["status"] == "ok":
                        test_str = self._get_test_str(test, test_type="unittest")
                    elif test["status"] == "PASSED":
                        test_str = self._get_test_str(test, test_type="pytest")

                    result.passed_tests.append(test_str)

                if (
                    test
                    and "status" in test
                    and (test["status"] == "FAILED" or test["status"] == "FAIL")
                ):
                    if test["status"] == "FAIL":
                        test_str = self._get_test_str(test, test_type="unittest")
                    elif test["status"] == "FAILED":
                        test_str = self._get_test_str(test, test_type="pytest")

                    result.failed_tests.append(test_str)
        result.num_tests_passed = len(result.passed_tests)
        result.num_tests_failed = len(result.failed_tests)

        return asdict(result)

    def _get_test_str(self, test_obj: Dict, test_type: str) -> str:
        if test_type == "unittest":
            fields = ["class_path", "test_name", "parameters"]
            final_str = ":".join([str(test_obj[k]) for k in fields])
        elif test_type == "pytest":
            fields = ["file", "class", "test"]
            final_str = ":".join([str(test_obj[k]) for k in fields])
        return final_str

    def _parse_pytest_output(self, output_lines: str) -> Optional[List]:
        # Make sure we only consider the right parts
        output_lines = self._extract_test_output(output_lines)

        # Standard format (test path first)
        standard_pattern = r"([\w/]+\.py)::(?:([\w]+)::)?([\w_]+(?:\[[\w\-\d]+\])?)(?:\s<-\s[\w/]+\.py)?(?:[\s\S]*?)(PASSED|FAILED|SKIPPED|ERROR|XFAIL|XPASS)"

        # Reversed format (status first)
        reversed_pattern = r"(PASSED|FAILED|SKIPPED|ERROR|XFAIL|XPASS)\s([\w/]+\.py)::(?:([\w]+)::)?([\w_]+(?:\[[\w\-\d]+\])?)(?:\s<-\s[\w/]+\.py)?"

        # Try standard format first
        all_results = []
        matches = re.findall(standard_pattern, output_lines)
        if matches:
            for match in matches:
                all_results.append(
                    {
                        "file": match[0] if match[0] else "None",
                        "class": match[1] if match[1] else "None",
                        "test": match[2] if match[2] else "None",
                        "status": match[3] if match[3] else "None",
                    }
                )

        # Try reversed format
        if not all_results:
            matches = re.findall(reversed_pattern, output_lines)
            if matches:
                for match in matches:
                    all_results.append(
                        {
                            "file": match[1] if match[1] else "None",
                            "class": match[2] if match[2] else "None",
                            "test": match[3] if match[3] else "None",
                            "status": match[0] if match[0] else "None",
                        }
                    )

        if all_results:
            return all_results
        else:
            return None

    def _parse_unittest_output(self, text: str) -> List:
        pattern = (
            r"(?:"
            r"(?:(\w+) \(([\w.]+)\)\n.*\n)?(\w+)(?: \(([\w.]+)\))?(?:\((.+?)\))? \.{3} (?:.*\n)*?(ok|FAIL|ERROR|skipped|expected failure|unexpected success)"
            r"|"
            r"(FAIL|ERROR|skipped|expected failure|unexpected success): (\w+)(?: \(([\w.]+)\))?(?:\((.+?)\))?"
            r")"
        )

        matches = re.findall(pattern, text)
        results = []

        for match in matches:
            is_multiline = bool(match[0] and match[1])
            results.append(
                {
                    "test_name": match[0] if is_multiline else match[2],
                    "class_path": match[1] if is_multiline else match[3],
                    "parameters": match[4],
                    "status": match[5],
                }
            )

        return results

    def _extract_test_output(self, output: str) -> str:
        # Look for the full marker lines
        test_start = output.find("===== test session starts =====")
        warnings_start = output.find("===== warnings summary =====")
        summary_start = output.find("===== short test summary info =====")
        collecting_start = output.find("collecting ...")

        # If we have no test session start but we have a summary, return the summary section
        if test_start == -1 and collecting_start == -1 and summary_start != -1:
            # If there's a warnings section after the summary, only return up to that point
            if warnings_start > summary_start:
                return output[summary_start:warnings_start].strip()
            return output[summary_start:].strip()

        # Normal test output extraction logic
        start_indices = []
        if collecting_start != -1:
            start_indices.append(collecting_start)
        if test_start != -1:
            start_indices.append(test_start)

        if not start_indices:
            return ""

        start_index = min(start_indices)

        end_indices = []
        if warnings_start != -1:
            end_indices.append(warnings_start)
        if summary_start != -1:
            end_indices.append(summary_start)

        if not end_indices:
            return output[start_index:]

        end_index = min(end_indices)
        return output[start_index:end_index].strip()
