"""Tests for PolyBench-Evaluation Typescript parsers module."""

from poly_bench_evaluation.parsers.typescript_parsers import (
    TypescriptBazelAngular,
    TypescriptJest,
    TypescriptJestTW,
    TypescriptMocha,
    TypescriptMochaFileName,
)


def test_typescript_bazel_angular_parser():
    test_content = "//sample/test/one PASSED\n//sample/test/two FAILED\n//sample/test/three PASSED"
    parser = TypescriptBazelAngular(test_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 2,
        "num_tests_failed": 1,
        "failed_tests": ["/sample/test/two"],
        "passed_tests": ["/sample/test/one", "/sample/test/three"],
    }
    assert result == expected


def test_typescript_mocha_parser():
    test_content = """{
  "stats": {
    "suites": 2,
    "tests": 2,
    "passes": 1,
    "pending": 0,
    "failures": 1,
    "start": "2025-02-04T00:14:13.618Z",
    "end": "2025-02-04T00:14:13.836Z",
    "duration": 218
  },
  "tests": [
    {
      "title": "onDidChangeValue gets triggered when .value is set",
      "fullTitle": "QuickInput onDidChangeValue gets triggered when .value is set",
      "duration": 213,
      "err": {}
    },
    {
      "title": "should not have unexpected errors",
      "fullTitle": "Unexpected Errors & Loader Errors should not have unexpected errors",
      "duration": 0,
      "err": {}
    }
  ],
  "pending": [],
  "failures": [
  {
      "title": "should not have unexpected errors",
      "fullTitle": "Unexpected Errors & Loader Errors should not have unexpected errors",
      "duration": 0,
      "speed": "fast",
      "err": {}
    }
  ],
  "passes": [
    {
      "title": "onDidChangeValue gets triggered when .value is set",
      "fullTitle": "QuickInput onDidChangeValue gets triggered when .value is set",
      "duration": 213,
      "speed": "slow",
      "err": {}
    }
  ]
}
"""
    parser = TypescriptMocha(test_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 1,
        "num_tests_failed": 1,
        "failed_tests": ["Unexpected Errors & Loader Errors should not have unexpected errors"],
        "passed_tests": ["QuickInput onDidChangeValue gets triggered when .value is set"],
    }
    assert result == expected


def test_typescript_mocha_filename_parser():
    test_content = """{
  "stats": {
    "suites": 13,
    "tests": 73,
    "passes": 65,
    "pending": 8,
    "failures": 0,
    "start": "2025-02-04T03:14:48.067Z",
    "end": "2025-02-04T03:14:49.413Z",
    "duration": 1346
  },
  "tests": [
    {
      "title": "a random title",
      "file": "packages/mui-base/src/Select/Select.test.tsx",
      "suite": "<Select />",
      "fullTitle": "<Select /> sets a value correctly when interacted by a user and external code",
      "functionName": "anonymous",
      "status": "passed",
      "duration": 121
    }
  ],
  "failures": []
}
"""
    parser = TypescriptMochaFileName(test_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 1,
        "num_tests_failed": 0,
        "failed_tests": [],
        "passed_tests": [
            "packages/mui-base/src/Select/Select.test.tsx-><Select /> sets a value correctly when interacted by a user and external code"
        ],
    }
    assert result == expected


def test_typescript_jest_tw_parser():
    test_content = """Now using node v8.9.1 (npm v5.5.1)
{"numFailedTestSuites":0,"numFailedTests":0,"numPassedTestSuites":8,"numPassedTests":18,"numPendingTestSuites":0,"numPendingTests":0,"numRuntimeErrorTestSuites":0,"numTotalTestSuites":8,"numTotalTests":18,"testResults":[
    {"assertionResults":[{"status":"passed","title":"it generates a set of helper classes from a config"}],"name":"/app/__tests__/defineClasses.test.js"},
    {"assertionResults":[
        {"status":"passed","title":"creates a proper single-word class with rules"},
        {"status":"passed","title":"does not modify the case of selector names"},
        {"status":"passed","title":"does not modify the case of property names"},
        {"status":"passed","title":"escapes non-standard characters in selectors"}
    ],"name":"/app/__tests__/defineClass.test.js"}
],"wasInterrupted":false}
Container exited with status code: 0"""

    parser = TypescriptJestTW(test_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 5,
        "num_tests_failed": 0,
        "failed_tests": [],
        "passed_tests": [
            "/app/__tests__/defineClasses.test.js->it generates a set of helper classes from a config",
            "/app/__tests__/defineClass.test.js->creates a proper single-word class with rules",
            "/app/__tests__/defineClass.test.js->does not modify the case of selector names",
            "/app/__tests__/defineClass.test.js->does not modify the case of property names",
            "/app/__tests__/defineClass.test.js->escapes non-standard characters in selectors",
        ],
    }
    assert result == expected


def test_typescript_jest_tw_parser_invalid_input():
    test_content = "Invalid content with no JSON"
    parser = TypescriptJestTW(test_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 0,
        "num_tests_failed": 0,
        "failed_tests": [],
        "passed_tests": [],
    }
    assert result == expected


def test_typescript_jest_parser():
    test_content = """PASS src/tests/first.test.ts
FAIL src/tests/second.test.ts
{"numFailedTestSuites":1,"numFailedTests":2,"numPassedTestSuites":1,"numPassedTests":1,"numPendingTestSuites":0,"numPendingTests":0,"numRuntimeErrorTestSuites":0,"numTotalTestSuites":2,"numTotalTests":3,"testResults":[
    {
        "name":"/app/src/tests/first.test.ts",
        "assertionResults":[
            {
                "fullName": "First test suite should pass this test",
                "status":"passed"
            }
        ]
    },
    {
        "name":"/app/src/tests/second.test.ts",
        "assertionResults":[
            {
                "fullName": "Second test suite should fail this test",
                "status":"failed"
            },
            {
                "fullName": "Second test suite should also fail this test",
                "status":"failed"
            }
        ]
    }
],"wasInterrupted":false}
Container exited with status code: 1"""

    parser = TypescriptJest(test_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 1,
        "num_tests_failed": 2,
        "failed_tests": [
            "/app/src/tests/second.test.ts->Second test suite should fail this test",
            "/app/src/tests/second.test.ts->Second test suite should also fail this test",
        ],
        "passed_tests": ["/app/src/tests/first.test.ts->First test suite should pass this test"],
    }
    assert result == expected
