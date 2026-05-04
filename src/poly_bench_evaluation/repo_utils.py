# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0
import shutil
import subprocess
import threading
import time
from pathlib import Path
from typing import Optional

from git import Repo
from loguru import logger


class RepoManager:
    """A class for repo level operations."""

    # Class-level lock dictionary to handle concurrent access to repositories
    _repo_locks = {}
    _locks_lock = threading.Lock()  # Lock for accessing _repo_locks

    def __init__(self, repo_name: str, repo_path: str):
        self.repo_name = repo_name
        self.repo_path: Path = Path(repo_path)
        self.tmp_repo_dir: Optional[Path] = None
        self.base_repo_dir: Optional[Path] = None

    @classmethod
    def get_repo_lock(cls, repo_name: str) -> threading.Lock:
        """Get or create a lock for a specific repository."""
        with cls._locks_lock:
            if repo_name not in cls._repo_locks:
                cls._repo_locks[repo_name] = threading.Lock()
            return cls._repo_locks[repo_name]

    def clone_repo(self):
        """Clone the repo to a temporary directory."""
        # Get the lock for this specific repository
        repo_lock = self.get_repo_lock(self.repo_name)

        repo_url = f"https://github.com/{self.repo_name}.git"
        self.repo_path = Path(self.repo_path).expanduser()

        # Acquire the lock before performing repository operations
        with repo_lock:
            self.repo_path.mkdir(exist_ok=True)

            short_repo_name = self.repo_name.split("/")[-1]
            self.base_repo_dir = self.repo_path / short_repo_name

            if not self.base_repo_dir.is_dir() or not (self.base_repo_dir / ".git").exists():
                if self.base_repo_dir.exists():
                    shutil.rmtree(self.base_repo_dir)
                self.base_repo_dir.mkdir(parents=True, exist_ok=True)
                try:
                    Repo.clone_from(repo_url, self.base_repo_dir)
                except Exception as e:
                    # Clean up upon unsuccessful clone
                    shutil.rmtree(self.base_repo_dir)
                    raise ValueError(f"Git clone error: {e}")

        # The following operations don't need the lock as they work with temporary directories
        # Copy base repo to temporary directory
        repo_dir = Path("/tmp") / str(time.time()) / short_repo_name
        if repo_dir.exists():
            shutil.rmtree(repo_dir)
        repo_dir.mkdir(parents=True, exist_ok=True)
        shutil.copytree(
            self.base_repo_dir, repo_dir, dirs_exist_ok=True, ignore_dangling_symlinks=True
        )

        # Enable automatic removal on deletion of this object
        self.tmp_repo_dir = repo_dir

    def reset_repo(self):
        """Reset the repo to the base state."""
        # sometimes git fetch gives error and retrying fixes it
        repo = Repo(self.tmp_repo_dir)
        git = repo.git

        max_retries = 5
        retry_count = 0
        while retry_count < max_retries:
            try:
                git.fetch("--all")
                git.reset("--hard")
                git.clean("-f", "-d")
                break
            except Exception:
                retry_count += 1
                time.sleep(5)
        else:
            raise ValueError("Git fetch error. Please check whether this github repo exists.")

    def checkout_commit(self, commit_hash: str):
        """Checkout the repo to a specific commit.

        Args:
            commit_hash (str): The commit hash to checkout to.
        Raises:
            ValueError: If the commit hash is not found in the repo.
        """
        repo = Repo(self.tmp_repo_dir)
        git = repo.git

        # sometimes git fetch gives error and retrying fixes it
        max_retries = 5
        retry_count = 0
        while retry_count < max_retries:
            try:
                git.fetch("--all")
                git.reset("--hard")
                git.clean("-f", "-d")
                break
            except Exception:
                retry_count += 1
                time.sleep(5)
        else:
            raise ValueError("Git fetch error. Please check whether this github repo exists.")
        try:
            git.checkout(commit_hash)
        except Exception as e:
            raise ValueError(f"Git checkout error: {e}")

    def _cleanup(self):
        """Remove the temporary directory used for cloning the repo if needed."""
        if self.tmp_repo_dir and self.tmp_repo_dir.exists():
            shutil.rmtree(self.tmp_repo_dir)

    def apply_patch(self, patch: str):
        """Apply a patch to the repository.

        Args:
            patch (str): The patch content to apply.

        Raises:
            ValueError: If there is an error applying the patch.
        """
        repo = Repo(self.tmp_repo_dir)
        git = repo.git

        try:
            # Write patch to a temporary file
            assert self.tmp_repo_dir is not None
            patch_file = self.tmp_repo_dir / "temp.patch"
            patch_file.write_text(patch)

            # Try to apply the patch
            try:
                git.execute(["git", "apply", "--ignore-whitespace", "--reject", str(patch_file)])
                # git.apply(str(patch_file), ignore_whitespace=True, reject=True, verbose=True)
            except Exception as e:
                # If apply fails, try am as fallback
                logger.warning(f"Failed to apply patch using git apply. Trying patch. {e}")
                try:
                    result = subprocess.run(
                        ["patch", "--fuzz=5", "-p1", "-f", "-i", str(patch_file)],
                        text=True,
                        capture_output=True,
                    )
                    if result.returncode != 0:
                        raise RuntimeError(
                            f"Patch failed with exit code {result.returncode}.\n"
                            f"stdout: {result.stdout}\n"
                            f"stderr: {result.stderr}"
                        )
                except subprocess.CalledProcessError as e:
                    # Patch command failed
                    raise RuntimeError(
                        f"Patch failed with exit code {e.returncode}.\n"
                        f"stdout: {e.stdout}\n"
                        f"stderr: {e.stderr}"
                    ) from e
                except Exception as e:
                    # Any other unexpected error
                    raise RuntimeError(f"Unexpected error while applying patch: {str(e)}") from e

            # Clean up patch file
            patch_file.unlink()

        except Exception as e:
            raise ValueError(f"Error applying patch: {e}")

    def __del__(self):
        """Remove the temporary directory used for cloning the repo if needed."""
        self._cleanup()
