from pathlib import Path

from poly_bench_evaluation.repo_utils import RepoManager


def test_init():
    """Test RepoManager initialization."""
    repo_manager = RepoManager("test_repo", "/path/to/repo")
    assert repo_manager.repo_name == "test_repo"
    assert repo_manager.repo_path == Path("/path/to/repo")
    assert repo_manager.tmp_repo_dir is None
    assert repo_manager.base_repo_dir is None

    # Clean up
    repo_manager._cleanup()
