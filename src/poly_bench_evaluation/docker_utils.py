# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0
import io
import json
import tarfile
import tempfile
import threading
import time
from pathlib import Path
from typing import List, Literal

import docker
from loguru import logger
from .constants import LANGUAGE_TO_BASE_DOCKERFILE


class DockerManager:
    """A class for managing docker related operations."""

    def __init__(self, image_id: str, delete_image: bool, client: docker.DockerClient):
        self.client = client
        self.image_id = image_id
        self.container = None
        self.delete_image = delete_image
        self.build_logs: List[str] = []
        self.run_logs: List[str] = []
        self.ghcr_image_name = None

    def check_image_local(self, local_image_name: str) -> bool:
        """Check if image exists locally in Docker"""

        try:
            _ = self.client.images.get(local_image_name)
            return True
        except docker.errors.ImageNotFound:
            return False
        except Exception as e:
            return False

    def try_pull_prebuilt_image(self, instance_id: str, version: str = "latest") -> bool:
        """Try to pull a pre-built image from GHCR
        
        Args:
            instance_id: The instance ID for the image
            version: Image version tag (default: "latest")
            
        Returns:
            bool: True if image was successfully pulled, False otherwise
        """
        ghcr_image_name = f"ghcr.io/timesler/swe-polybench.eval.x86_64.{instance_id.lower()}:{version}"
        
        try:
            logger.info(f"Attempting to pull pre-built image: {ghcr_image_name}")
            
            # Try to pull the image from GHCR
            self.client.images.pull(ghcr_image_name)
            
            # Tag the pulled image with our local naming convention
            pulled_image = self.client.images.get(ghcr_image_name)
            pulled_image.tag(self.image_id)
            
            # Store GHCR image name for cleanup
            self.ghcr_image_name = ghcr_image_name
            
            logger.info(f"Successfully pulled and tagged pre-built image for {instance_id}")
            return True
            
        except docker.errors.ImageNotFound:
            logger.info(f"Pre-built image not found in GHCR: {ghcr_image_name}")
            return False
        except docker.errors.APIError as e:
            logger.info(f"Failed to pull pre-built image: {e}")
            return False
        except Exception as e:
            logger.info(f"Unexpected error pulling pre-built image: {e}")
            return False

    def docker_build(self, repo_path: Path, dockerfile_content: str) -> int:
        """Build docker image from dockerfile content.

        Args:
            repo_path: Path to the repository
            dockerfile_content: Content of the dockerfile
            tag: The name of the docker image (optional)
        Returns:
            success: 0 if build was successful, 1 otherwise
        """
        # Create a Dockerfile in the temporary directory with the dockerfile content
        (repo_path / "Dockerfile").write_text(dockerfile_content)

        # Clear any .dockerignore if exists
        if (repo_path / ".dockerignore").exists():
            (repo_path / ".dockerignore").unlink()

        success = 1
        try:
            image, build_logs = self.client.images.build(
                path=str(repo_path), tag=self.image_id, rm=True, platform="linux/amd64"
            )
            for log in build_logs:
                if "stream" in log:
                    self.build_logs.append(log["stream"].strip())
                elif "error" in log:
                    self.build_logs.append(f"Error: {log['error']}")
                elif "errorDetail" in log:
                    self.build_logs.append(f"Error Detail: {log['errorDetail']['message']}")
                else:
                    self.build_logs.append(json.dumps(log))
            # If we get here without exceptions, build was successful
            success = 0
        except docker.errors.BuildError as e:
            self.build_logs.append(f"Build Error: {str(e)}")
            success = 1
        except Exception as e:
            self.build_logs.append(f"Unexpected Error: {str(e)}")
            success = 1

        return success

    def create_container(self):
        """Creates and starts a docker container from the docker image."""
        self.container = self.client.containers.create(
            image=self.image_id,
            detach=True,
            tty=True,
            working_dir=self._get_workdir_from_image(),
            name=f"container_{self.image_id}",
            command="tail -f /dev/null",
        )

        assert self.container is not None, "Container not created"
        self.container.start()

    def copy_file_to_container(
        self, content: str, container_filename: str, target_path: str
    ) -> bool:
        """Copy a file with given content to the container.

        Args:
            content: Content to write to the file
            container_filename: Name of the file as it should appear in the container
            target_path: Target path in the container

        Returns:
            bool: True if successful, False otherwise
        """
        assert self.container is not None, "Container not created"

        # Create unique identifier for local files
        unique_id = f"{int(time.time() * 1000)}_{threading.get_ident()}"
        local_filename = f"temp_{unique_id}_{container_filename}"

        # Create a temporary file locally
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=local_filename) as tmp_file:
            tmp_file.write(content)
            tmp_file.flush()

            # Copy the file into the container
            try:
                with open(tmp_file.name, "rb") as f:
                    # Create tar with the desired container filename, not the local filename
                    self.container.put_archive(
                        target_path, self._create_tar(container_filename, f.read())
                    )
                return True
            except Exception as e:
                logger.error(f"Failed to copy file to container: {e}")
                return False
            finally:
                # Clean up the temporary file
                Path(tmp_file.name).unlink(missing_ok=True)

    def apply_patch_to_container(
        self, patch_content: str, patch_type: Literal["code", "test"]
    ) -> int:
        """Apply patch inside the running container
        Args:
            patch_content: Content of the patch file
            patch_type: The type of patch, "code" or "test"

        Returns:
            int: 0 if patch was applied successfully, 1 otherwise
        """
        success = 1
        workdir = str(self._get_workdir_from_image())
        assert self.container is not None, "Container not created"

        # The filename as it should appear inside the container
        container_patch_filename = f"patch_{patch_type}.diff"

        if not self.copy_file_to_container(patch_content, container_patch_filename, workdir):
            raise ValueError("Failed to create patch file in container")

        try:
            # First try: git apply
            exec_result = self.container.exec_run(
                cmd=f"git apply -v --ignore-whitespace --reject {workdir}/{container_patch_filename}",
                workdir=workdir,
                user="root",
            )
            if exec_result.exit_code != 0:
                # Second try: patch command
                exec_result = self.container.exec_run(
                    cmd=f"patch --batch --fuzz=5 -p1 -f -i {workdir}/{container_patch_filename}",
                    workdir=workdir,
                    user="root",
                )
                if exec_result.exit_code != 0:
                    raise ValueError("Failed to apply patch.")
                else:
                    success = 0
            else:
                success = 0

        finally:
            # Clean up if patch failed
            if success != 0:
                self._cleanup()
                self.container = None

        return success

    def docker_run(self, test_command: str, timeout: int) -> int:
        """Run the CMD command from dockerfile inside the running container.
        Args:
            test_command: The test command to run
            timeout: The timout of the run function
        Returns:
            success: 0 if run was successful, 1 otherwise
        """
        assert self.container is not None, "Container not created"

        # Local variables to store the result
        result = None
        timed_out = False
        success_stream = 1

        def run_container():
            nonlocal result, success_stream
            workdir = self._get_workdir_from_image()
            exec_result = b""
            eval_script_list = [test_command]

            eval_script = "\n".join(["#!/bin/bash", "set -uxo pipefail"] + eval_script_list)
            write_command = f"""cat << 'EOF' > /{workdir}/eval.sh
{eval_script}
EOF"""

            eval_result = self.container.exec_run(
                cmd=["bash", "-c", write_command], workdir=workdir
            )
            if eval_result.exit_code != 0:
                raise Exception(f"Failed to create eval.sh file: {eval_result.output.decode()}")
            chmod_result = self.container.exec_run(
                cmd=["bash", "-c", f"chmod 777 {workdir}/eval.sh"]
            )
            if chmod_result.exit_code != 0:
                raise Exception(f"Failed to chmod: {eval_result.output.decode()}")
            try:
                exec_id = self.container.client.api.exec_create(
                    self.container.id, f"/bin/bash {workdir}/eval.sh", stderr=True
                )["Id"]

                exec_stream = self.container.client.api.exec_start(exec_id, stream=True, demux=True)
                stdout_data = b""
                stderr_data = b""

                for chunk in exec_stream:
                    if chunk:
                        stdout_chunk, stderr_chunk = chunk
                        if stdout_chunk:
                            stdout_data += stdout_chunk
                        if stderr_chunk:
                            stderr_data += stderr_chunk

                # Combine stderr and stdout, with stderr at the beginning
                error_output = stderr_data.decode("utf-8")
                stdout_output = stdout_data.decode("utf-8")
                exec_result = error_output + stdout_output

                exit_code = self.container.client.api.exec_inspect(exec_id).get("ExitCode", -1)
            except Exception:
                pass

            self.run_logs.append(exec_result)
            self.run_logs.append(f"Container exited with status code: {exit_code}")
            success_stream = exit_code

        # Start the container operation in a separate thread
        thread = threading.Thread(target=run_container)
        thread.start()
        thread.join(timeout)

        # If the thread is still alive, the operation timed out
        if thread.is_alive():
            timed_out = True
            # Force stop the container
            try:
                self.container.stop(timeout=20)
                self.run_logs.append("Container operation timed out")
            except Exception:
                pass
            success = 1
        else:
            success = success_stream
            self.run_logs.append(f"Container exited with status code: {success}")

        if timed_out:
            logger.info("docker run timed out.")

        self._cleanup()
        self.container = None

        return success

    def build_base_image(self, language: str, retry: int = 3):
        """Build base images.
        Args:
            language: Polybench language
            retry: Number of times to retry building the image if it fails (default: 3)
        Raise:
            ValueError: If dockerfile is not built successfully after all retries
        """

        if self.check_image_local(local_image_name=f"polybench_{language.lower()}_base"):
            logger.info(f"Base image for {language} already exists locally.")
            return

        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_base_path = Path(tmp_dir)

            for attempt in range(retry):
                base_build_success = self.docker_build(
                    repo_path=tmp_base_path,
                    dockerfile_content=LANGUAGE_TO_BASE_DOCKERFILE[language],
                )

                if base_build_success == 0:
                    logger.info(
                        f"Successfully built base image for {language} on attempt {attempt + 1}"
                    )
                    return

                if attempt < retry - 1:
                    logger.info(
                        f"Failed to build base image for {language} on attempt {attempt + 1}, retrying..."
                    )

            # If we get here, all retries failed
            raise ValueError(f"Failed to build base image for {language} after {retry} attempts")

    def _create_tar(self, name: str, content: bytes) -> bytes:
        """Create a tar archive containing a single file."""

        # Create unique identifier for tar file
        tar_stream = io.BytesIO()
        with tarfile.open(fileobj=tar_stream, mode="w") as tar:
            tarinfo = tarfile.TarInfo(name=name)  # Use the container filename here
            tarinfo.size = len(content)
            tar.addfile(tarinfo, io.BytesIO(content))

        return tar_stream.getvalue()

    def _get_workdir_from_image(self) -> str:
        try:
            image = self.client.images.get(self.full_image_uri)
        except Exception:
            image = self.client.images.get(self.image_id)
        workdir = str(image.attrs["Config"]["WorkingDir"])

        return workdir

    def _cleanup(self):
        """Stop and remove the container, and delete the image if provided."""
        # Stop and remove the container
        if self.container:
            try:
                self.container.stop(timeout=10)
                self.container.remove()
            except Exception:
                pass
        # Delete the image if needed
        if self.delete_image:
            try:
                self.client.images.remove(self.image_id, force=True)
                logger.debug(f"Removed local image tag: {self.image_id}")
            except docker.errors.ImageNotFound:
                pass  # Image doesn't exist, nothing to delete
            except Exception as e:
                logger.debug(f"Failed to remove local image tag {self.image_id}: {e}")
            
            if self.ghcr_image_name:
                try:
                    self.client.images.remove(self.ghcr_image_name, force=True)
                    logger.debug(f"Removed GHCR image tag: {self.ghcr_image_name}")
                except docker.errors.ImageNotFound:
                    pass  # Image doesn't exist, nothing to delete
                except Exception as e:
                    logger.debug(f"Failed to remove GHCR image tag {self.ghcr_image_name}: {e}")

    def __del__(self):
        """Stop and remove the container, and delete the image if provided."""
        # Stop and remove the container, and delete the image if provided
        self._cleanup()
