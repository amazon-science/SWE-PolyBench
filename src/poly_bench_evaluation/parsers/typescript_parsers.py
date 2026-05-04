# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0
import json
import re
from dataclasses import asdict
from typing import Dict

from poly_bench_evaluation.parsers.parser_protocol import TestOutputParser  # noqa: F401
from poly_bench_evaluation.parsers.parser_results import ParserResults


class TypescriptJest:
    """A class for Typescript Jest test framework parser"""

    def __init__(self, test_content: str):
        self.content = test_content

    def parse(self) -> Dict:
        """Parse function that parses the run logs string.
        Returns:
            Dict: A dictionary containing the parsed test results.
        """
        try:
            # Find the start of the JSON object
            pattern = r'{\s*"numFailedTestSuites"'
            match = re.search(pattern, self.content)
            if not match:
                json_object = None
            else:
                json_start = match.start()
                # Find "Container exited" after the JSON start
                container_exit_pos = self.content.find("Container exited", json_start)

                # Get the substring between JSON start and "Container exited"
                substring = self.content[json_start:container_exit_pos]

                # Find the last closing curly bracket in this substring
                last_brace_pos = substring.rindex("}")
                # Extract the JSON text
                json_text = substring[: last_brace_pos + 1]

                json_object = json.loads(json_text)
        except (json.JSONDecodeError, ValueError):
            json_object = None

        try:
            parsed_tests = self._typescript_jest_json_helper(json_object)
        except Exception:
            parsed_tests = {}

        return parsed_tests

    def _typescript_jest_json_helper(self, json_data):
        result = ParserResults()
        for test_suite in json_data["testResults"]:
            test_file_name = test_suite["name"]

            # Go through each assertion in the test suite
            for assertion in test_suite["assertionResults"]:
                # Create the full test name by combining file name and test title
                full_test_name = f"{test_file_name}->{assertion['fullName']}"
                # Add to appropriate list based on status
                if assertion["status"] == "passed":
                    result.passed_tests.append(full_test_name)
                elif assertion["status"] == "failed":
                    result.failed_tests.append(full_test_name)
            result.num_tests_passed = len(result.passed_tests)
            result.num_tests_failed = len(result.failed_tests)

        return asdict(result)


class TypescriptJestTW:
    """A class for Typescript Jest test framework for tailwindcss repo"""

    def __init__(self, test_content: str):
        self.content = test_content

    def parse(self) -> Dict:
        """Parse function that parses the run logs string.
        Returns:
            Dict: A dictionary containing the parsed test results.
        """
        try:
            pattern = r'{\s*"numFailedTestSuites"'
            match = re.search(pattern, self.content)
            if not match:
                json_object = None
            else:
                json_start = match.start()

                # Look for either "wasInterrupted":false} or "wasInterrupted":true}
                end_pattern = r'"wasInterrupted":(true|false)}'
                end_match = re.search(end_pattern, self.content[json_start:])

                if not end_match:
                    json_object = None
                else:
                    # Get the end position by adding the start position and the end match position
                    json_end = json_start + end_match.end()

                    # Extract the JSON text
                    json_text = self.content[json_start:json_end]

                    json_object = json.loads(json_text)
        except json.JSONDecodeError:
            json_object = None

        try:
            parsed_tests = self._typescript_jest_tw_json_helper(json_object)
        except Exception:
            parsed_tests = ParserResults()
            parsed_tests = asdict(parsed_tests)

        return parsed_tests

    def _typescript_jest_tw_json_helper(self, json_data):
        result = ParserResults()
        for test_suite in json_data["testResults"]:
            test_file_name = test_suite["name"]

            # Go through each assertion in the test suite
            for assertion in test_suite["assertionResults"]:
                # Create the full test name by combining file name and test title
                full_test_name = f"{test_file_name}->{assertion['title']}"
                # Add to appropriate list based on status
                if assertion["status"] == "passed":
                    result.passed_tests.append(full_test_name)
                elif assertion["status"] == "failed":
                    result.failed_tests.append(full_test_name)
            result.num_tests_passed = len(result.passed_tests)
            result.num_tests_failed = len(result.failed_tests)

        return asdict(result)


class TypescriptMocha:
    """A class for Typescript Mocha test framework parser"""

    def __init__(self, test_content: str):
        self.content = test_content

    def parse(self) -> Dict:
        """Parse function that parses the run logs string.
        Returns:
            Dict: A dictionary containing the parsed test results.
        """
        try:
            # Find the start of the JSON object
            pattern = r'{\s*"stats"'
            match = re.search(pattern, self.content)
            if not match:
                json_object = None
            else:
                json_start = match.start()
                # Find "Container exited" after the JSON start
                container_exit_pos = self.content.find("Container exited", json_start)

                # Get the substring between JSON start and "Container exited"
                substring = self.content[json_start:container_exit_pos]

                # Find the last closing curly bracket in this substring
                last_brace_pos = substring.rindex("}")
                # Extract the JSON text
                json_text = substring[: last_brace_pos + 1]
                json_object = json.loads(json_text)
        except (json.JSONDecodeError, ValueError):
            json_object = None

        try:
            parsed_tests = self._typescript_mocha_json_helper(json_object)
        except Exception:
            parsed_tests = {}

        return parsed_tests

    def _typescript_mocha_json_helper(self, json_data):
        result = ParserResults()
        # Iterate through test results
        for test in json_data["passes"]:
            # Create the full test name by combining file name and test title
            full_test_name = f"{test['fullTitle']}"
            result.passed_tests.append(full_test_name)
        for test in json_data["failures"]:
            full_test_name = f"{test['fullTitle']}"
            result.failed_tests.append(full_test_name)
        result.num_tests_passed = len(result.passed_tests)
        result.num_tests_failed = len(result.failed_tests)

        return asdict(result)


class TypescriptMochaFileName:
    """A class for Typescript Mocha test framework parser. This parser is for a custom build parser that includes the file name in the report json."""

    def __init__(self, test_content: str):
        self.content = test_content

    def parse(self) -> Dict:
        """Parse function that parses the run logs string.
        Returns:
            Dict: A dictionary containing the parsed test results.
        """
        try:
            pattern = r'{\s*"stats"'
            match = re.search(pattern, self.content)
            if not match:
                json_object = None
            else:
                json_start = match.start()
                # Find "Container exited" after the JSON start
                container_exit_pos = self.content.find("Container exited", json_start)

                # Get the substring between JSON start and "Container exited"
                substring = self.content[json_start:container_exit_pos]

                # Find the last closing curly bracket in this substring
                last_brace_pos = substring.rindex("}")
                # Extract the JSON text
                json_text = substring[: last_brace_pos + 1]
                json_object = json.loads(json_text)
        except (json.JSONDecodeError, ValueError):
            json_object = None

        try:
            parsed_tests = self._typescript_mocha_filename_json_helper(json_object)
        except Exception:
            parsed_tests = {}

        return parsed_tests

    def _typescript_mocha_filename_json_helper(self, json_data):
        result = ParserResults()
        for test in json_data["tests"]:
            # Create the full test name by combining file name and test title
            full_test_name = f"{test['file']}->{test['fullTitle']}"
            # Add to appropriate list based on status
            if test["status"] == "passed":
                result.passed_tests.append(full_test_name)
            elif test["status"] == "failed":
                result.failed_tests.append(full_test_name)
        result.num_tests_passed = len(result.passed_tests)
        result.num_tests_failed = len(result.failed_tests)

        return asdict(result)


class TypescriptBazelAngular:
    """A class for Typescript Bazel test framework parser. This parser is for angular repo."""

    def __init__(self, test_content: str):
        self.content = test_content

    def parse(self) -> Dict:
        """Parse function that parses the run logs string.
        Returns:
            Dict: A dictionary containing the parsed test results.
        """
        result = ParserResults()
        lines = self.content.split("\n")
        for line in lines:
            if not line.strip():
                continue
            # Look for test results
            clean_line = (
                line.replace("\u001b[0m", "")
                .replace("\u001b[32m", "")
                .replace("\u001b[31m", "")
                .replace("\u001b[1m", "")
            )
            if "PASSED" in clean_line or "FAILED" in clean_line:
                # Split on PASSED or FAILED and take the first part
                if "PASSED" in clean_line:
                    test_name = clean_line.split("PASSED")[0]
                else:
                    test_name = clean_line.split("FAILED")[0]
                if test_name.startswith("//"):
                    test_name = test_name[1:]
                if "PASSED" in line:
                    result.passed_tests.append(test_name.strip())
                elif "FAILED" in line:
                    result.failed_tests.append(test_name.strip())
        result.num_tests_passed = len(result.passed_tests)
        result.num_tests_failed = len(result.failed_tests)

        return asdict(result)
