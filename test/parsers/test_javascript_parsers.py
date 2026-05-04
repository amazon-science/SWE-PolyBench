"""Tests for PolyBench-Evaluation JavaScript parsers module."""

import pytest

from poly_bench_evaluation.parsers.javascript_parsers import (
    JavascriptGenericParser,
    JavascriptJestPR,
    JavascriptMocha,
)

MOCHA_TEST_CASES = [
    # Valid Mocha test case
    (
        """> mocha --reporter json
{
    "stats": {
        "suites": 2,
        "tests": 3,
        "passes": 2,
        "failures": 1
    },
    "passes": [
        {
            "fullTitle": "Calculator add should add two numbers correctly",
            "duration": 15
        },
        {
            "fullTitle": "Calculator subtract should subtract two numbers correctly",
            "duration": 10
        }
    ],
    "failures": [
        {
            "fullTitle": "Calculator divide should handle division by zero",
            "duration": 5
        }
    ]
}
Container exited with status code: 1""",
        {
            "num_tests_passed": 2,
            "num_tests_failed": 1,
            "passed_tests": [
                "Calculator add should add two numbers correctly",
                "Calculator subtract should subtract two numbers correctly",
            ],
            "failed_tests": ["Calculator divide should handle division by zero"],
        },
    ),
    # Invalid JSON case
    (
        "> mocha --reporter json\n{invalid json}",
        {
            "num_tests_passed": 0,
            "num_tests_failed": 0,
            "passed_tests": [],
            "failed_tests": [],
        },
    ),
    # Empty content case
    (
        "",
        {
            "num_tests_passed": 0,
            "num_tests_failed": 0,
            "passed_tests": [],
            "failed_tests": [],
        },
    ),
]


@pytest.mark.parametrize("test_content,expected", MOCHA_TEST_CASES)
def test_javascript_generic_parser(test_content, expected):
    parser = JavascriptGenericParser(test_content)
    result = parser.parse()
    assert result == expected


@pytest.mark.parametrize("test_content,expected", MOCHA_TEST_CASES)
def test_javascript_mocha_parser(test_content, expected):
    parser = JavascriptMocha(test_content)
    result = parser.parse()
    assert result == expected


def test_javascript_generic_parser_tap():
    test_content = """TAP version 13
ok 1 Calculator add should add two numbers correctly
not ok 2 Calculator divide should handle division by zero
ok 3 Calculator subtract should subtract two numbers correctly"""

    parser = JavascriptGenericParser(test_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 2,
        "num_tests_failed": 1,
        "passed_tests": [
            "1 Calculator add should add two numbers correctly",
            "3 Calculator subtract should subtract two numbers correctly",
        ],
        "failed_tests": ["2 Calculator divide should handle division by zero"],
    }
    assert result == expected


def test_javascript_jest_pr_parser():
    test_content = """Running tests...
{"numFailedTestSuites":1,"numFailedTests":2,"numPassedTestSuites":1,"numPassedTests":3,"numPendingTestSuites":0,"numPendingTests":0,"numRuntimeErrorTestSuites":0,"numTotalTestSuites":2,"numTotalTests":5,"testResults":[
    {
        "name": "/app/src/components/__tests__/Button.test.js",
        "assertionResults": [
            {
                "title": "renders correctly",
                "fullName": "Button component renders correctly",
                "status": "passed"
            },
            {
                "title": "handles click events",
                "fullName": "Button component handles click events",
                "status": "passed"
            },
            {
                "title": "applies custom styles",
                "fullName": "Button component applies custom styles",
                "status": "passed"
            }
        ]
    },
    {
        "name": "/app/src/components/__tests__/Form.test.js",
        "assertionResults": [
            {
                "title": "validates email correctly",
                "status": "failed"
            },
            {
                "title": "submits form data",
                "status": "failed"
            }
        ]
    }
],"wasInterrupted":false}"""
    parser = JavascriptJestPR(test_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 3,
        "num_tests_failed": 2,
        "passed_tests": [
            "/app/src/components/__tests__/Button.test.js->Button component renders correctly",
            "/app/src/components/__tests__/Button.test.js->Button component handles click events",
            "/app/src/components/__tests__/Button.test.js->Button component applies custom styles",
        ],
        "failed_tests": [
            "/app/src/components/__tests__/Form.test.js->validates email correctly",
            "/app/src/components/__tests__/Form.test.js->submits form data",
        ],
    }
    assert result == expected


def test_javascript_jest_pr_parser_no_fullname():
    test_content = """Running tests...
{"numFailedTestSuites":0,"numFailedTests":0,"numPassedTestSuites":1,"numPassedTests":2,"numPendingTestSuites":0,"numPendingTests":0,"numRuntimeErrorTestSuites":0,"numTotalTestSuites":1,"numTotalTests":2,"testResults":[
    {
        "name": "/app/src/utils/__tests__/helpers.test.js",
        "assertionResults": [
            {
                "title": "formats date correctly",
                "status": "passed"
            },
            {
                "title": "validates phone number",
                "status": "passed"
            }
        ]
    }
],"wasInterrupted":false}"""
    parser = JavascriptJestPR(test_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 2,
        "num_tests_failed": 0,
        "passed_tests": [
            "/app/src/utils/__tests__/helpers.test.js->formats date correctly",
            "/app/src/utils/__tests__/helpers.test.js->validates phone number",
        ],
        "failed_tests": [],
    }
    assert result == expected
