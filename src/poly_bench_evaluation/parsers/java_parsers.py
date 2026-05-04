# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0
import re
import xml.etree.ElementTree as Et
from dataclasses import asdict
from typing import Dict, List

from poly_bench_evaluation.parsers.parser_protocol import TestOutputParser  # noqa: F401
from poly_bench_evaluation.parsers.parser_results import ParserResults


class JavaGenericParser:
    """A class for Java Maven framework parser"""

    def __init__(self, test_content: str):
        self.content = test_content

    def parse(self) -> Dict:
        """
        Parse a test log produced by Java Maven framework and extract test method status.

        Returns:
            Dict: Dictionary mapping test method names to their status ('PASS' or 'FAIL')
        """

        # Remove the string `+ read -r file` from the test log. otherwise it can appear in the xml and make it not parsable.
        test_log = re.sub(r"\+ read -r file\s*", "", self.content, re.DOTALL)

        # Extract messages that indicate build/compilation failure
        has_build_failure = re.search(r"build failure", test_log, re.IGNORECASE) is not None
        has_compilation_error = re.search(r"compilation error", test_log, re.IGNORECASE) is not None

        # A build/compilation error message would be present in the report if 1) the code can't be built, or 2) some tests fail.
        # To distinguish these two cases, we need to search the string "there are test failures". If it exists, 2) is the case and we can proceed to extract test status. Otherwise the code can't be build/compiled.
        has_test_failure = (
            re.search(r"there are test failures", test_log, re.IGNORECASE) is not None
        )

        result = ParserResults()
        if has_build_failure or has_compilation_error:
            if not has_test_failure:
                return asdict(result)

        # Extract xmls from the log
        test_xmls = re.findall(r"(<testsuite[^>]*>.*?</testsuite>)", test_log, re.DOTALL)

        # Extract test status from the xmls
        for test_xml in test_xmls:
            test_status = self._xml_parser_helper(test_xml)
            result.failed_tests.extend(test_status["FAILED"])
            result.passed_tests.extend(test_status["PASSED"])

        result.num_tests_passed = len(result.passed_tests)
        result.num_tests_failed = len(result.failed_tests)

        return asdict(result)

    def _xml_parser_helper(self, xml_content: str) -> Dict[str, List[str]]:
        """
        Parse a Maven Surefire XML report content and extract test method status.

        Args:
            xml_content (str): Content of the XML file

        Returns:
            Dict: Dictionary mapping test method names to their status ('PASS' or 'FAIL')
        """
        test_results: Dict[str, List[str]] = {
            "PASSED": [],
            "FAILED": [],
        }
        try:
            root = Et.fromstring(xml_content)
        except Exception:
            return test_results

        for testcase in root.findall(".//testcase"):
            name = testcase.get("name")
            classname = testcase.get("classname")
            classname = "" if classname is None else classname + "."

            name = f"{classname}{name}"
            if testcase.find("failure") is not None or testcase.find("error") is not None:
                test_results["FAILED"].append(name)
            elif testcase.find("skipped") is not None:
                # Exclude test cases that are skipped
                continue
            else:
                test_results["PASSED"].append(name)

        return test_results
