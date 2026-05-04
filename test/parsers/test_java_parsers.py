"""Tests for PolyBench-Evaluation Java parsers module."""

import pytest

from poly_bench_evaluation.parsers.java_parsers import JavaGenericParser


def test_parsing_build_error():
    """Test the parser with a log that has build error messages"""

    test_content = """\
[INFO] BUILD FAILURE
[ERROR]   mvn <goals> -rf :dubbo-config-api
<?xml version="1.0" encoding="UTF-8"?>
<testsuite xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://maven.apache.org/surefire/maven-surefire-plugin/xsd/surefire-test-report.xsd" name="org.apache.dubbo.config.ServiceConfigTest" time="3.013" tests="1" errors="0" skipped="0" failures="0">
  <properties>
    <property name="java.class.version" value="52.0"/>
  </properties>
  <testcase name="testInterface2" classname="org.apache.dubbo.config.ServiceConfigTest" time="0.001"/>
</testsuite>
Container exited with status code: 0
Container exited with status code: 0
"""
    parser = JavaGenericParser(test_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 0,
        "num_tests_failed": 0,
        "passed_tests": [],
        "failed_tests": [],
    }

    assert result == expected


def test_parsing_compilation_error():
    """Test the parser with a log that has compilation error messages"""

    test_content = """\
[ERROR] COMPILATION ERROR :
[ERROR]   mvn <goals> -rf :dubbo-config-api
<?xml version="1.0" encoding="UTF-8"?>
<testsuite xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://maven.apache.org/surefire/maven-surefire-plugin/xsd/surefire-test-report.xsd" name="org.apache.dubbo.config.ServiceConfigTest" time="3.013" tests="1" errors="0" skipped="0" failures="0">
  <properties>
    <property name="java.class.version" value="52.0"/>
  </properties>
  <testcase name="testInterface2" classname="org.apache.dubbo.config.ServiceConfigTest" time="0.001"/>
</testsuite>
Container exited with status code: 0
Container exited with status code: 0
"""

    parser = JavaGenericParser(test_content)
    result = parser.parse()
    expected = {
        "num_tests_passed": 0,
        "num_tests_failed": 0,
        "passed_tests": [],
        "failed_tests": [],
    }

    assert result == expected


@pytest.fixture
def content_with_test_status():
    return """\
[INFO] BUILD FAILURE
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.22.2:test (default-test) on project dubbo-config-api: There are test failures.
[ERROR]
[ERROR]   mvn <goals> -rf :dubbo-config-api
<?xml version="1.0" encoding="UTF-8"?>
<testsuite xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://maven.apache.org/surefire/maven-surefire-plugin/xsd/surefire-test-report.xsd" name="org.apache.dubbo.config.ServiceConfigTest" time="3.013" tests="5" errors="1" skipped="1" failures="1">
  <properties>
    <property name="java.class.version" value="52.0"/>
  </properties>
  <testcase name="testMetaData" classname="org.apache.dubbo.config.ServiceConfigTest" time="0.014">
    <failure message="Expect empty metadata but found: {registry.required=true} ==&gt; expected: &lt;0&gt; but was: &lt;1&gt;" type="org.opentest4j.AssertionFailedError"><![CDATA[org.opentest4j.AssertionFailedError: Expect empty metadata but found: {registry.required=true} ==> expected: <0> but was: <1>
  at org.apache.dubbo.config.ServiceConfigTest.testMetaDat (ServiceConfigTest.java:300)
]]></failure>
  </testcase>
  <testcase name="testExportWithoutRegistryConfig" classname="org.apache.dubbo.config.ServiceConfigTest" time="0.019">
    <error message="Default registry is not initialized" type="java.lang.IllegalStateException">java.lang.IllegalStateException: Default registry is not initialized
  at org.apache.dubbo.config.ServiceConfigTest.testExportWithoutRegistryConfig(ServiceConfigTest.java:319)
    </error>
  </testcase>
  <testcase name="testUnexport" classname="org.apache.dubbo.config.ServiceConfigTest" time="0">
    <skipped message="cannot pass in travis"/>
  </testcase>
  <testcase name="testInterface1" classname="org.apache.dubbo.config.ServiceConfigTest" time="0.003"/>
  <testcase name="testInterface2" classname="org.apache.dubbo.config.ServiceConfigTest" time="0.001"/>
</testsuite>
Container exited with status code: 0
Container exited with status code: 0
"""


def test_parsing_test_status(content_with_test_status):
    """Test if the parser can extract the passed and failed tests"""

    parser = JavaGenericParser(content_with_test_status)
    result = parser.parse()
    expected = {
        "num_tests_passed": 2,
        "num_tests_failed": 2,
        "passed_tests": [
            "org.apache.dubbo.config.ServiceConfigTest.testInterface1",
            "org.apache.dubbo.config.ServiceConfigTest.testInterface2",
        ],
        "failed_tests": [
            "org.apache.dubbo.config.ServiceConfigTest.testMetaData",
            "org.apache.dubbo.config.ServiceConfigTest.testExportWithoutRegistryConfig",
        ],
    }

    assert result == expected


@pytest.fixture
def content_with_messy_xml():
    return """\
[INFO] BUILD FAILURE
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.22.2:test (default-test) on project dubbo-config-api: There are test failures.
[ERROR]
[ERROR]   mvn <goals> -rf :dubbo-config-api
<?xml version="1.0" encoding="UTF-8"?>
<testsuite xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://maven.apache.org/surefire/maven-surefire-plugin/xsd/surefire-test-report.xsd" name="org.apache.dubbo.config.ServiceConfigTest" time="3.013" tests="5" errors="1" skipped="1" failures="1">+ read -r file
  <properties>
    <property name="java.class.version" value="52.0"/>
  </properties>+ read -r file
  <testcase name="testMetaData" classname="org.apache.dubbo.config.ServiceConfigTest" time="0.014">
    <failure message="Expect empty metadata but found: {registry.required=true} ==&gt; expected: &lt;0&gt; but was: &lt;1&gt;" type="org.opentest4j.AssertionFailedError"><![CDATA[org.opentest4j.AssertionFailedError: Expect empty metadata but found: {registry.required=true} ==> expected: <0> but was: <1>
  at org.apache.dubbo.config.ServiceConfigTest.testMetaData(ServiceConfigTest.java:300)
]]></failure>
  </testcase>
  <testcase name="testExportWithoutRegistryConfig" classname="org.apache.dubbo.config.ServiceConfigTest" time="0.019">+ read -r file
    <error message="Default registry is not initialized" type="java.lang.IllegalStateException">java.lang.IllegalStateException: Default registry is not initialized
  at org.apache.dubbo.config.ServiceConfigTest.testExportWithoutRegistryConfig(ServiceConfigTest.java:319)
    </error>
  </testcase>
  <testcase name="testUnexport" classname="org.apache.dubbo.config.ServiceConfigTest" time="0">
    <skipped message="cannot pass in travis"/>+ read -r file
  </testcase>
  <testcase name="testInterface1" classname="org.apache.dubbo.config.ServiceConfigTest" time="0.003"/>
  <testcase name="testInterface2" classname="org.apache.dubbo.config.ServiceConfigTest" time="0.001"/>
</testsuite>+ read -r file
Container exited with status code: 0
Container exited with status code: 0
"""


def test_parsing_test_status_with_messy_xml(content_with_messy_xml):
    """Test if the parser can extract test results when the string `read -r file` is in the xml"""

    parser = JavaGenericParser(content_with_messy_xml)
    result = parser.parse()
    expected = {
        "num_tests_passed": 2,
        "num_tests_failed": 2,
        "passed_tests": [
            "org.apache.dubbo.config.ServiceConfigTest.testInterface1",
            "org.apache.dubbo.config.ServiceConfigTest.testInterface2",
        ],
        "failed_tests": [
            "org.apache.dubbo.config.ServiceConfigTest.testMetaData",
            "org.apache.dubbo.config.ServiceConfigTest.testExportWithoutRegistryConfig",
        ],
    }

    assert result == expected
