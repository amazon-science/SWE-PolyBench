# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0
import json
import re
from dataclasses import asdict
from typing import Dict

from poly_bench_evaluation.parsers.parser_protocol import TestOutputParser  # noqa: F401
from poly_bench_evaluation.parsers.parser_results import ParserResults


class JavascriptGenericParser:
    """A class for Javascript Mocha and TAP frameworks parser"""

    def __init__(self, test_content: str):
        self.content = test_content

    def parse(self) -> Dict:
        """Parse function that parses the run logs string.
        Returns:
            Dict: A dictionary containing the parsed test results.
        """
        result = ParserResults()
        js_test_commands_found = re.findall(r"(^>.*--reporter json)", self.content, re.MULTILINE)
        if js_test_commands_found and "mocha" in js_test_commands_found[0]:
            # return self._get_json_report_mocha()
            return self._get_javascript_mocha()

        if re.findall(r"^TAP\sversion\s\d+", self.content, re.MULTILINE):
            return self._get_json_report_tap()

        return asdict(result)

    def _get_javascript_mocha(self) -> Dict:
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

        if json_object:
            try:
                parsed_tests = self._javascript_mocha_json_helper(json_object)
            except Exception:
                parsed_tests = asdict(ParserResults())
        else:
            parsed_tests = asdict(ParserResults())

        return parsed_tests

    def _javascript_mocha_json_helper(self, json_data: Dict) -> Dict:
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

    def _get_json_report_mocha(self) -> Dict:
        json_reports_found = re.findall(r"(^\{\n[\s\S]*[\}\]]\n\})", self.content, re.MULTILINE)
        json_report = None
        result = ParserResults()
        if json_reports_found:
            for report in json_reports_found:
                try:
                    json_report = json.loads(report)
                    break
                except Exception:
                    pass
        if not json_report:
            return asdict(result)
        for tc in json_report["passes"]:
            result.passed_tests.append(tc["fullTitle"])
        for tc in json_report["failures"]:
            result.failed_tests.append(tc["fullTitle"])
        result.num_tests_passed = len(result.passed_tests)
        result.num_tests_failed = len(result.failed_tests)

        return asdict(result)

    def _get_json_report_tap(self) -> Dict:
        result = ParserResults()
        lines = self.content.split("\n")
        for line in lines:
            if line.startswith("ok "):
                result.passed_tests.append(line[3:])

            if line.startswith("not ok "):
                result.failed_tests.append(line[7:])
        result.num_tests_passed = len(result.passed_tests)
        result.num_tests_failed = len(result.failed_tests)

        return asdict(result)


class JavascriptJestPR:
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

        if json_object:
            try:
                parsed_tests = self._jest_json_helper(json_object)
            except Exception:
                parsed_tests = asdict(ParserResults())
        else:
            parsed_tests = asdict(ParserResults())

        return parsed_tests

    def _jest_json_helper(self, json_data: Dict) -> Dict:
        result = ParserResults()
        for test_suite in json_data["testResults"]:
            test_file_name = test_suite["name"]

            # Go through each assertion in the test suite
            for assertion in test_suite["assertionResults"]:
                # Create the full test name by combining file name and test title
                assertion_name = (
                    assertion["fullName"] if "fullName" in assertion else assertion["title"]
                )
                full_test_name = f"{test_file_name}->{assertion_name}"
                # Add to appropriate list based on status
                if assertion["status"] == "passed":
                    result.passed_tests.append(full_test_name)
                elif assertion["status"] == "failed":
                    result.failed_tests.append(full_test_name)
            result.num_tests_passed = len(result.passed_tests)
            result.num_tests_failed = len(result.failed_tests)

        return asdict(result)


class JavascriptMocha:
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
                return asdict(ParserResults())

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

        if json_object:
            try:
                parsed_tests = self._mocha_json_helper(json_object)
            except Exception:
                parsed_tests = asdict(ParserResults())
        else:
            parsed_tests = asdict(ParserResults())

        return parsed_tests

    def _mocha_json_helper(self, json_data: Dict) -> Dict:
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
