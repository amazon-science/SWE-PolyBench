import json
import tempfile
from pathlib import Path

import pytest

from poly_bench_evaluation.polybench_data import PolyBenchOutput, PolyBenchRetrievalMetrics
from poly_bench_evaluation.scoring import (
    _get_all_instance_results,
    aggregate_logs,
    instance_level_scoring,
    store_instance_level_output,
)


@pytest.fixture
def mock_resolved_instance():
    return PolyBenchOutput(
        instance_id="resolved_test_instance",
        patch_applied=True,
        generation=True,
        with_logs=True,
        all_f2p_passed=True,
        no_p2p_failed=True,
        resolved=True,
        passed_tests=["test1"],
        failed_tests=[],
    )


@pytest.fixture
def mock_metrics():
    return PolyBenchRetrievalMetrics(
        instance_id="resolved_test_instance",
        file_retrieval_metrics={"recall": 0.5, "precision": 0.5, "f1": 0.5},
        node_retrieval_metrics={"recall": 0.5, "precision": 0.5, "f1": 0.5},
        reference_nodes=[],
        predicted_nodes=[],
    )


@pytest.fixture
def mock_unresolved_instance():
    return PolyBenchOutput(
        instance_id="unresolved_test_instance",
        patch_applied=True,
        generation=True,
        with_logs=True,
        all_f2p_passed=True,
        no_p2p_failed=True,
        resolved=False,
        passed_tests=[],
        failed_tests=["test1"],
    )


def test_instance_level_scoring():
    # Test case for successful patch with all tests passing
    instance_id = "test1"
    result = {"passed_tests": ["test1", "test2"], "failed_tests": []}
    f2p = ["test1"]
    p2p = ["test2"]
    output = instance_level_scoring(
        instance_id=instance_id,
        result=result,
        f2p=f2p,
        p2p=p2p,
        patch_applied=True,
        generation=True,
    )
    assert output.resolved
    assert output.all_f2p_passed
    assert output.no_p2p_failed
    assert output.patch_applied
    assert output.generation

    # Test case for failed f2p test
    result = {"passed_tests": ["test2"], "failed_tests": ["test1"]}
    output = instance_level_scoring(
        instance_id=instance_id,
        result=result,
        f2p=f2p,
        p2p=p2p,
        patch_applied=True,
        generation=True,
    )
    assert not output.resolved
    assert not output.all_f2p_passed
    assert output.no_p2p_failed

    # Test case for failed p2p test
    result = {"passed_tests": ["test1"], "failed_tests": ["test2"]}
    output = instance_level_scoring(
        instance_id=instance_id,
        result=result,
        f2p=f2p,
        p2p=p2p,
        patch_applied=True,
        generation=True,
    )
    assert not output.resolved
    assert output.all_f2p_passed
    assert not output.no_p2p_failed

    # Test case for no result (empty dict)
    output = instance_level_scoring(
        instance_id=instance_id, result={}, f2p=f2p, p2p=p2p, patch_applied=False, generation=False
    )
    assert not output.resolved
    assert not output.with_logs
    assert not output.patch_applied
    assert not output.generation


def test_store_instance_level_output():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test data
        instance_output = PolyBenchOutput(
            instance_id="test_instance",
            patch_applied=True,
            generation=True,
            with_logs=True,
            all_f2p_passed=True,
            no_p2p_failed=True,
            resolved=True,
            passed_tests=["test1", "test2"],
            failed_tests=[],
        )

        # Store output
        store_instance_level_output(instance_output, temp_dir)

        # Verify file was created and contains correct data
        output_file = Path(temp_dir) / "test_instance_result.json"
        assert output_file.exists()

        with open(output_file, "r") as f:
            stored_data = json.load(f)
            assert stored_data["instance_id"] == "test_instance"
            assert stored_data["patch_applied"]
            assert stored_data["generation"]
            assert stored_data["with_logs"]
            assert stored_data["resolved"]
            assert stored_data["passed_tests"] == ["test1", "test2"]
            assert stored_data["failed_tests"] == []


def test_get_all_instance_results_happy(mock_resolved_instance, mock_unresolved_instance):
    with tempfile.TemporaryDirectory() as temp_dir:
        store_instance_level_output(mock_resolved_instance, temp_dir)
        store_instance_level_output(mock_unresolved_instance, temp_dir)

        all_results = _get_all_instance_results(temp_dir)

        assert len(all_results) == 2


def test_get_all_instance_results_wrong_path():
    non_existent_path = "/non/existent/path"

    with pytest.raises(FileNotFoundError):
        _get_all_instance_results(non_existent_path)

    with pytest.raises(TypeError):
        _get_all_instance_results(None)


def test_aggregate_logs(mock_resolved_instance, mock_unresolved_instance, mock_metrics):
    with tempfile.TemporaryDirectory() as temp_dir:
        store_instance_level_output(mock_resolved_instance, temp_dir)
        store_instance_level_output(mock_unresolved_instance, temp_dir)
        store_instance_level_output(mock_metrics, temp_dir, suffix="_metrics")

        # Test aggregation
        project_root = Path(__file__).parent.parent
        csv_path = project_root / "datasets" / "polybench_sampled_500.csv"
        aggregate_logs(temp_dir, dataset_path=csv_path, output_path=temp_dir)

        # Verify aggregated result file
        result_file = Path(temp_dir) / "result.json"
        assert result_file.exists()

        with open(result_file, "r") as f:
            data = json.load(f)
            assert data["total_resolved"] == 1
            assert data["total_unresolved"] == 1
            assert len(data["patch_applied"]) == 2
            assert len(data["with_logs"]) == 2
            assert len(data["generation"]) == 2
            assert len(data["no_generation"]) == 0
            assert data["file_retrieval"] == [
                {
                    "file_recall": 0.5,
                    "file_precision": 0.5,
                    "file_f1": 0.5,
                    "instance_id": "resolved_test_instance",
                }
            ]
            assert data["node_retrieval"] == [
                {
                    "node_recall": 0.5,
                    "node_precision": 0.5,
                    "node_f1": 0.5,
                    "instance_id": "resolved_test_instance",
                }
            ]


def test_aggregate_logs_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Test aggregation with empty directory
        with pytest.raises(ValueError):
            project_root = Path(__file__).parent.parent
            csv_path = project_root / "datasets" / "polybench_sampled_500.csv"
            aggregate_logs(temp_dir, dataset_path=csv_path)


def test_store_instance_level_output_type_error():
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(TypeError):
            store_instance_level_output({"invalid": "type"}, temp_dir)
