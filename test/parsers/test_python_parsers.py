"""Tests for PolyBench-Evaluation Python parsers module."""

import pytest

from poly_bench_evaluation.parsers.python_parsers import PythonPyUnit


@pytest.fixture
def pytest_test_content():
    return """===== test session starts =====
test_calculator.py::TestCalculator::test_add PASSED
test_calculator.py::TestCalculator::test_subtract PASSED
test_calculator.py::TestCalculator::test_divide FAILED
===== short test summary info =====
FAILED test_calculator.py::TestCalculator::test_divide - AssertionError: Division by zero should raise error"""


@pytest.fixture
def unittest_test_content():
    return """test_add (test_calculator.TestCalculator) ... ok
test_subtract (test_calculator.TestCalculator) ... ok
test_divide (test_calculator.TestCalculator) ... FAIL

======================================================================
FAIL: test_divide (test_calculator.TestCalculator)
----------------------------------------------------------------------
AssertionError: Division by zero should raise error"""


def test_python_pyunit_pytest_format(pytest_test_content):
    parser = PythonPyUnit(pytest_test_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 2,
        "num_tests_failed": 1,
        "passed_tests": [
            "test_calculator.py:TestCalculator:test_add",
            "test_calculator.py:TestCalculator:test_subtract",
        ],
        "failed_tests": ["test_calculator.py:TestCalculator:test_divide"],
    }
    assert result == expected


def test_python_pyunit_unittest_format(unittest_test_content):
    parser = PythonPyUnit(unittest_test_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 2,
        "num_tests_failed": 1,
        "passed_tests": [
            "test_calculator.TestCalculator:test_add:",
            "test_calculator.TestCalculator:test_subtract:",
        ],
        "failed_tests": ["test_calculator.TestCalculator:test_divide:"],
    }
    assert result == expected


@pytest.fixture
def pytest_parameterized_test_content():
    return """===== test session starts =====
test_calculator.py::TestCalculator::test_multiply[2-3-6] PASSED
test_calculator.py::TestCalculator::test_multiply[4-5-20] PASSED
test_calculator.py::TestCalculator::test_multiply[-1-1--1] FAILED
===== short test summary info ====="""


def test_python_pyunit_pytest_parameterized(pytest_parameterized_test_content):
    parser = PythonPyUnit(pytest_parameterized_test_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 2,
        "num_tests_failed": 1,
        "passed_tests": [
            "test_calculator.py:TestCalculator:test_multiply[2-3-6]",
            "test_calculator.py:TestCalculator:test_multiply[4-5-20]",
        ],
        "failed_tests": ["test_calculator.py:TestCalculator:test_multiply[-1-1--1]"],
    }
    assert result == expected


def test_python_pyunit_invalid_input():
    test_content = "Invalid test output format"
    parser = PythonPyUnit(test_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 0,
        "num_tests_failed": 0,
        "passed_tests": [],
        "failed_tests": [],
    }
    assert result == expected


@pytest.fixture
def pytest_reversed_format_content():
    return """===== test session starts =====
test_calculator.py::test_simple_add PASSED
test_calculator.py::TestCalculator::test_complex_divide FAILED
===== short test summary info ====="""


def test_python_pyunit_pytest_reversed_format(pytest_reversed_format_content):
    parser = PythonPyUnit(pytest_reversed_format_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 1,
        "num_tests_failed": 1,
        "passed_tests": ["test_calculator.py:None:test_simple_add"],
        "failed_tests": ["test_calculator.py:TestCalculator:test_complex_divide"],
    }
    assert result == expected
