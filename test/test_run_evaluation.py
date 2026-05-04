from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from poly_bench_evaluation.polybench_data import PolyBenchInstance
from poly_bench_evaluation.run_evaluation import evaluate_instance


@pytest.fixture
def mock_instance():
    return PolyBenchInstance(
        instance_id="test_instance",
        model_patch="mock_model_patch",
        patch="mock_gold_patch",
        test_patch="mock_test_patch",
        repo="google/gson",
        base_commit="abc123",
        language="python",
        parser_class="PythonTestParser",
        dockerfile="FROM python:3.8",
        f2p=["test1", "test2"],
        p2p=["test3", "test4"],
        test_command="python -m pytest",
        modified_nodes=["node1", "node2"],
    )


@pytest.fixture
def mock_docker_client():
    return Mock()


def test_empty_model_patch(mock_instance, mock_docker_client, tmp_path):
    """Test behavior when model patch is empty"""
    # Arrange
    mock_instance.model_patch = ""
    result_path = str(tmp_path)

    # Act
    evaluate_instance(
        instance=mock_instance,
        result_path=result_path,
        evaluate_gold=False,
        repo_path=str(tmp_path),
        delete_image=True,
        client=mock_docker_client,
    )

    # Assert
    result_file = Path(result_path) / f"{mock_instance.instance_id}_result.json"
    assert result_file.exists()


@pytest.fixture
def mock_docker_manager():
    with patch("poly_bench_evaluation.run_evaluation.DockerManager") as mock:
        docker_manager = Mock()
        mock.return_value = docker_manager
        yield docker_manager


# def test_docker_build_failure(mock_instance, mock_docker_client, mock_docker_manager, tmp_path):
#   """Test behavior when docker build fails"""
#   # Arrange
#   mock_docker_manager.check_image_ecr.return_value = False
#   mock_docker_manager.docker_build.return_value = 1
#   mock_docker_manager.build_logs = ["Build failed"]
#
#   # Act & Assert
#   with pytest.raises(ValueError, match="Docker build failed"):
#       evaluate_instance(
#           instance=mock_instance,
#           result_path=str(tmp_path),
#           evaluate_gold=False,
#           repo_path=str(tmp_path),
#           delete_image=True,
#           client=mock_docker_client
#       )
#
# def test_successful_evaluation(mock_instance, mock_docker_client, mock_docker_manager, tmp_path):
#    """Test successful evaluation flow"""
#    # Arrange
#    mock_docker_manager.check_image_ecr.return_value = True
#    mock_docker_manager.apply_patch_to_container.return_value = 0
#    mock_docker_manager.run_logs = ["All tests passed"]
#
#    with patch('importlib.import_module') as mock_importlib:
#        # Mock the parser class
#        mock_parser = Mock()
#        mock_parser.parse.return_value = {"passed": True, "total": 1, "failures": 0}
#        mock_parser_class = Mock(return_value=mock_parser)
#        mock_module = Mock()
#        mock_module.PythonTestParser = mock_parser_class
#        mock_importlib.return_value = mock_module
#
#        # Act
#        evaluate_instance(
#            instance=mock_instance,
#            result_path=str(tmp_path),
#            evaluate_gold=False,
#            repo_path=str(tmp_path),
#            delete_image=True,
#            client=mock_docker_client
#        )
#
#        # Assert
#        result_file = Path(tmp_path) / f"{mock_instance.instance_id}_result.json"
#        assert result_file.exists()
#        mock_docker_manager.create_container.assert_called_once()
#        mock_docker_manager.docker_run.assert_called_once()
#
# def test_test_patch_application_failure(mock_instance, mock_docker_client, mock_docker_manager, tmp_path):
#    """Test behavior when test patch application fails"""
#    # Arrange
#    mock_docker_manager.check_image_ecr.return_value = True
#    mock_docker_manager.apply_patch_to_container.side_effect = Exception("Patch failed")
#
#    # Act
#    evaluate_instance(
#        instance=mock_instance,
#        result_path=str(tmp_path),
#        evaluate_gold=False,
#        repo_path=str(tmp_path),
#        delete_image=True,
#        client=mock_docker_client
#    )
#
#    # Assert
#    result_file = Path(tmp_path) / f"{mock_instance.instance_id}_result.json"
#    assert result_file.exists()
#    mock_docker_manager.__del__.assert_called_once()
#
# def test_evaluate_gold_patch(mock_instance, mock_docker_client, mock_docker_manager, tmp_path):
#    """Test evaluation with gold patch"""
#    # Arrange
#    mock_docker_manager.check_image_ecr.return_value = True
#    mock_docker_manager.apply_patch_to_container.return_value = 0
#    mock_docker_manager.run_logs = ["All tests passed"]
#
#    with patch('importlib.import_module') as mock_importlib:
#        mock_parser = Mock()
#        mock_parser.parse.return_value = {"passed": True, "total": 1, "failures": 0}
#        mock_parser_class = Mock(return_value=mock_parser)
#        mock_module = Mock()
#        mock_module.PythonTestParser = mock_parser_class
#        mock_importlib.return_value = mock_module
#
#        # Act
#        evaluate_instance(
#            instance=mock_instance,
#            result_path=str(tmp_path),
#            evaluate_gold=True,  # Key difference
#            repo_path=str(tmp_path),
#            delete_image=True,
#            client=mock_docker_client
#        )
#
#        # Assert
#        # Verify that gold patch was used instead of model patch
#        mock_docker_manager.apply_patch_to_container.assert_any_call(
#            patch_content=mock_instance.patch,
#            patch_type="code"
#        )
