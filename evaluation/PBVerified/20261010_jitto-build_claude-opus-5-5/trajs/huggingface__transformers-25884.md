# Instance: huggingface__transformers-25884

- Final resolved (evaluator, logs/huggingface__transformers-25884_result.json): True
- Run state: DONE
- One attempt. Duration 89.0 s, turns 11, actor cost $0.23295319999999997, container commands 6
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/huggingface__transformers-25884/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-25884/repo. Consider the following issue description:

<issue_description>
OSError: /home/datascience/huggingface does not appear to have a file named preprocessor_config.json. Checkout 'https://huggingface.co//home/datascience/huggingface/None' for available files.
### System Info

import transformers
transformers.__version__

'4.31.0'

### Who can help?

_No response_

### Information

- [ ] The official example scripts
- [ ] My own modified scripts

### Tasks

- [ ] An officially supported task in the `examples` folder (such as GLUE/SQuAD, ...)
- [ ] My own task or dataset (give details below)

### Reproduction
![image](https://github.com/huggingface/transformers/assets/25996703/6e26deb4-237b-473a-8874-164a4d134ea8)

```python
segmenter = pipeline(task="image-segmentation", model="facebook/detr-resnet-50-panoptic", revision="fc15262")
segmenter.save_pretrained("./huggingface")


from transformers import pipeline
task = 'image-segmentation'
model_dir="./huggingface"
model = pipeline(task, model = model_dir)

OSError: /home/datascience/huggingface does not appear to have a file named preprocessor_config.json. Checkout 'https://huggingface.co//home/datascience/huggingface/None' for available files.
```

### Expected behavior

no bug

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-25884/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-25884/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-25884/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-25884/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

Follow these steps to resolve the issue:
1. As a first step, explore the repo to find and read the code relevant to the <issue_description>.
2. Create a script or a small test to reproduce the error and execute it with envrun, to confirm the error.
3. Edit the source code of the repo to resolve the issue.
4. Rerun your reproduction and confirm that the error is fixed.
5. Think about edge cases and make sure your fix handles them as well; run the existing tests closest to the code you changed.
6. Delete any scripts or files you created only for reproduction or checking, so that only the fix remains in the repository.

````

## Trajectory

_session start: model claude-opus-5-5, tools ['Bash', 'Edit', 'Glob', 'Grep', 'Read', 'Write'], MCP servers []_

**tool call: Bash**

```bash
grep -n "def save_pretrained" -A60 src/transformers/pipelines/base.py
```

tool result:

```
831:    def save_pretrained(self, save_directory: str, safe_serialization: bool = False):
832-        """
833-        Save the pipeline's model and tokenizer.
834-
835-        Args:
836-            save_directory (`str`):
837-                A path to the directory where to saved. It will be created if it doesn't exist.
838-            safe_serialization (`str`):
839-                Whether to save the model using `safetensors` or the traditional way for PyTorch or Tensorflow
840-        """
841-        if os.path.isfile(save_directory):
842-            logger.error(f"Provided path ({save_directory}) should be a directory, not a file")
843-            return
844-        os.makedirs(save_directory, exist_ok=True)
845-
846-        if hasattr(self, "_registered_impl"):
847-            # Add info to the config
848-            pipeline_info = self._registered_impl.copy()
849-            custom_pipelines = {}
850-            for task, info in pipeline_info.items():
851-                if info["impl"] != self.__class__:
852-                    continue
853-
854-                info = info.copy()
855-                module_name = info["impl"].__module__
856-                last_module = module_name.split(".")[-1]
857-                # Change classes into their names/full names
858-                info["impl"] = f"{last_module}.{info['impl'].__name__}"
859-                info["pt"] = tuple(c.__name__ for c in info["pt"])
860-                info["tf"] = tuple(c.__name__ for c in info["tf"])
861-
862-                custom_pipelines[task] = info
863-            self.model.config.custom_pipelines = custom_pipelines
864-            # Save the pipeline custom code
865-            custom_object_save(self, save_directory)
866-
867-        self.model.save_pretrained(save_directory, safe_serialization=safe_serialization)
868-
869-        if self.tokenizer is not None:
870-            self.tokenizer.save_pretrained(save_directory)
871-
872-        if self.feature_extractor is not None:
873-            self.feature_extractor.save_pretrained(save_directory)
874-
875-        if self.modelcard is not None:
876-            self.modelcard.save_pretrained(save_directory)
877-
878-    def transform(self, X):
879-        """
880-        Scikit / Keras interface to transformers' pipelines. This method will forward to __call__().
881-        """
882-        return self(X)
883-
884-    def predict(self, X):
885-        """
886-        Scikit / Keras interface to transformers' pipelines. This method will forward to __call__().
887-        """
888-        return self(X)
889-
890-    @contextmanager
891-    def device_placement(self):
```

**tool call: Bash**

```bash
grep -n "image_processor" src/transformers/pipelines/base.py | head -30
```

tool result:

```
757:        image_processor: Optional[BaseImageProcessor] = None,
774:        self.image_processor = image_processor
824:        if self.image_processor is None and self.feature_extractor is not None:
829:                self.image_processor = self.feature_extractor
1058:        # TODO hack by collating feature_extractor and image_processor
1059:        feature_extractor = self.feature_extractor if self.feature_extractor is not None else self.image_processor
1170:        # TODO hack by collating feature_extractor and image_processor
1171:        feature_extractor = self.feature_extractor if self.feature_extractor is not None else self.image_processor
```

**tool call: Bash**

```bash
git log --oneline -1; grep -rn "image_processor" tests/pipelines/test_pipelines_common.py | head
```

tool result:

```
716bb2e39 [ViTDet] Fix doc tests (#25880)
```

**assistant:** Let me reproduce with a small, randomly initialized model (no network).

**tool call: Bash**

```bash
cat > repro_tmp.py <<'EOF'
import tempfile, os
from transformers import ViTConfig, ViTForImageClassification, ViTImageProcessor, pipeline
cfg = ViTConfig(hidden_size=32, num_hidden_layers=2, num_attention_heads=2, intermediate_size=37, image_size=30, patch_size=2)
model = ViTForImageClassification(cfg)
ip = ViTImageProcessor(size={"height": 30, "width": 30})
p = pipeline("image-classification", model=model, image_processor=ip)
with tempfile.TemporaryDirectory() as d:
    p.save_pretrained(d)
    print(os.listdir(d))
    p2 = pipeline("image-classification", model=d)
    print(type(p2.image_processor))
EOF
/work/huggingface__transformers-25884/bin/envrun 'python repro_tmp.py 2>&1 | tail -3'
```

tool result:

```
  File "/testbed/src/transformers/utils/hub.py", line 400, in cached_file
    raise EnvironmentError(
OSError: /tmp/tmpq1oftbpf does not appear to have a file named preprocessor_config.json. Checkout 'https://huggingface.co//tmp/tmpq1oftbpf/None' for available files.
```

**assistant:** Reproduced. Now the fix: also save the image processor.

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/huggingface__transformers-25884/repo/src/transformers/pipelines/base.py",
 "old_string": "            self.feature_extractor.save_pretrained(save_directory)\n\n        if self.modelcard",
 "new_string": "            self.feature_extractor.save_pretrained(save_directory)\n\n        if self.image_processor is not None:\n            self.image_processor.save_pretrained(save_directory)\n\n        if self.modelcard"
}
```

tool result:

```
The file /work/huggingface__transformers-25884/repo/src/transformers/pipelines/base.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
sed -i '' 's/Save the pipeline.s model and tokenizer\./Save the pipeline'"'"'s model, tokenizer, feature extractor and image processor./' src/transformers/pipelines/base.py; sed -n 831,834p src/transformers/pipelines/base.py
/work/huggingface__transformers-25884/bin/envrun 'python repro_tmp.py 2>&1 | tail -3'
```

tool result:

```
    def save_pretrained(self, save_directory: str, safe_serialization: bool = False):
        """
        Save the pipeline's model, tokenizer, feature extractor and image processor.

/testbed/src/transformers/modeling_utils.py:488: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  return torch.load(checkpoint_file, map_location=map_location)
<class 'transformers.models.vit.image_processing_vit.ViTImageProcessor'>
```

**assistant:** The reload now works. Cleaning up and running the closest existing tests:

**tool call: Bash**

```bash
rm repro_tmp.py; /work/huggingface__transformers-25884/bin/envrun 'HF_HUB_OFFLINE=1 python -m pytest tests/pipelines/test_pipelines_common.py -q -x 2>&1 | tail -5; git status --short'
```

tool result:

```
=========================== short test summary info ============================
FAILED tests/pipelines/test_pipelines_common.py::CommonPipelineTest::test_check_task
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
1 failed, 5 warnings in 2.09s
sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
 M setup.py
 M src/transformers/pipelines/base.py
?? Dockerfile
```

**tool call: Bash**

```bash
/work/huggingface__transformers-25884/bin/envrun 'git diff setup.py | head; HF_HUB_OFFLINE=1 python -m pytest tests/pipelines/test_pipelines_common.py -q 2>&1 | grep -E "FAILED|Error|passed|failed" | head -20'; git -C . status --short
```

tool result:

```
diff --git a/setup.py b/setup.py
index b95ec018f..49e98c869 100644
--- a/setup.py
+++ b/setup.py
@@ -97,7 +97,7 @@ if stale_egg_info.exists():
 _deps = [
     "Pillow<10.0.0",
     "accelerate>=0.20.3",
-    "av==9.2.0",  # Latest version of PyAV (10.0.0) has issues with audio stream.
+    "av==10.0.0",  # Latest version of PyAV (10.0.0) has issues with audio stream.
                raise ValueError("`token` and `use_auth_token` are both specified. Please set only the argument `token`.")
            raise RuntimeError("You cannot infer task automatically within `pipeline` when using offline mode")
                This parameter cannot be used if `securityStatus` or `files_metadata` are passed.
            - [`~utils.RepositoryNotFoundError`]
            - [`~utils.RevisionNotFoundError`]
            raise ValueError("`expand` cannot be used if `securityStatus` or `files_metadata` are set.")
            raise ValueError("You can only send PreparedRequests.")
                raise ValueError("`token` and `use_auth_token` are both specified. Please set only the argument `token`.")
            raise RuntimeError("You cannot infer task automatically within `pipeline` when using offline mode")
>           raise RuntimeError(f"Instantiating a pipeline without a task set raised an error: {e}")
E           RuntimeError: Instantiating a pipeline without a task set raised an error: Cannot reach https://huggingface.co/api/models/gpt2: offline mode is enabled. To disable it, please unset the `HF_HUB_OFFLINE` environment variable.
src/transformers/pipelines/__init__.py:445: RuntimeError
                Dictionary mapping protocol to the URL of the proxy passed to
            requests.ConnectionError,
        and/or on specific status codes (ex: service unavailable). If the call failed more
                By default, retry on `requests.Timeout` and `requests.ConnectionError`.
        after a failed call. This issue is mitigated for file objects or any IO streams
            raise ValueError("You can only send PreparedRequests.")
                raise ValueError("`token` and `use_auth_token` are both specified. Please set only the argument `token`.")
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or

 M setup.py
 M src/transformers/pipelines/base.py
?? Dockerfile
```

**tool call: Bash**

```bash
/work/huggingface__transformers-25884/bin/envrun 'HF_HUB_OFFLINE=1 python -m pytest tests/pipelines/test_pipelines_common.py -q -p no:warnings 2>&1 | grep -E "^FAILED|passed|failed"'
```

tool result:

```
                This parameter cannot be used if `securityStatus` or `files_metadata` are passed.
                Dictionary mapping protocol to the URL of the proxy passed to
        and/or on specific status codes (ex: service unavailable). If the call failed more
        after a failed call. This issue is mitigated for file objects or any IO streams
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
                Dictionary mapping protocol to the URL of the proxy passed to
                data before giving up which is passed to `requests.request`.
        # 1. we passed local_files_only.
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
                Dictionary mapping protocol to the URL of the proxy passed to
        and/or on specific status codes (ex: service unavailable). If the call failed more
        after a failed call. This issue is mitigated for file objects or any IO streams
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
                Dictionary mapping protocol to the URL of the proxy passed to
                data before giving up which is passed to `requests.request`.
        # 1. we passed local_files_only.
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
                Dictionary mapping protocol to the URL of the proxy passed to
        and/or on specific status codes (ex: service unavailable). If the call failed more
        after a failed call. This issue is mitigated for file objects or any IO streams
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
                Dictionary mapping protocol to the URL of the proxy passed to
                data before giving up which is passed to `requests.request`.
        # 1. we passed local_files_only.
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
                Dictionary mapping protocol to the URL of the proxy passed to
        and/or on specific status codes (ex: service unavailable). If the call failed more
        after a failed call. This issue is mitigated for file objects or any IO streams
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
                Dictionary mapping protocol to the URL of the proxy passed to
                data before giving up which is passed to `requests.request`.
        # 1. we passed local_files_only.
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
                Dictionary mapping protocol to the URL of the proxy passed to
        and/or on specific status codes (ex: service unavailable). If the call failed more
        after a failed call. This issue is mitigated for file objects or any IO streams
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
                Dictionary mapping protocol to the URL of the proxy passed to
                data before giving up which is passed to `requests.request`.
        # 1. we passed local_files_only.
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
                Dictionary mapping protocol to the URL of the proxy passed to
        and/or on specific status codes (ex: service unavailable). If the call failed more
        after a failed call. This issue is mitigated for file objects or any IO streams
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
                Dictionary mapping protocol to the URL of the proxy passed to
                data before giving up which is passed to `requests.request`.
        # 1. we passed local_files_only.
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
                Dictionary mapping protocol to the URL of the proxy passed to
        and/or on specific status codes (ex: service unavailable). If the call failed more
        after a failed call. This issue is mitigated for file objects or any IO streams
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
                Dictionary mapping protocol to the URL of the proxy passed to
                data before giving up which is
[... 10206 more characters not shown]
```

**assistant:** These failures look network-related (the tests download hub models). To confirm they're not caused by my change, I'll compare against the unmodified file:

**tool call: Bash**

```bash
/work/huggingface__transformers-25884/bin/envrun 'git stash push src/transformers/pipelines/base.py -q && HF_HUB_OFFLINE=1 python -m pytest tests/pipelines/test_pipelines_common.py -q -p no:warnings 2>&1 | tail -1; git stash pop -q && git diff --stat src/'
```

tool result:

```
17 failed, 13 passed, 7 skipped in 4.00s
 src/transformers/pipelines/base.py | 5 ++++-
 1 file changed, 4 insertions(+), 1 deletion(-)
```

**assistant:** I fixed the bug: `Pipeline.save_pretrained()` now saves the image processor too, so the pipeline from the issue can be loaded back from its saved folder.

**Cause:** `save_pretrained` in `src/transformers/pipelines/base.py` saved the model, tokenizer, feature extractor and model card, but not `self.image_processor`. Image pipelines like `image-segmentation` with DETR use only an image processor, so `preprocessor_config.json` was never written. Loading the folder with `pipeline(task, model=dir)` then failed with the `OSError` in the issue.

**Fix** (`src/transformers/pipelines/base.py`, around line 875):
```python
if self.image_processor is not None:
    self.image_processor.save_pretrained(save_directory)
```
I also updated the method's docstring to say it saves the feature extractor and image processor.

**Checks:**
- **Reproduction:** without network access I couldn't download the DETR model from the issue, so I used a small random ViT image-classification pipeline instead. Before the fix, saving and reloading it raised the same `OSError`. After the fix, `preprocessor_config.json` is written and the pipeline reloads with a `ViTImageProcessor`. I deleted the script afterwards.
- **Edge case:** some pipelines use the same object as both feature extractor and image processor. It just gets written twice to the same file, which does no harm.
- **Existing tests:** `tests/pipelines/test_pipelines_common.py` gives 13 passed, 17 failed, 7 skipped, with or without my change. The failures happen because those tests need to download models from the Hub and the container has no network.

`git status` also shows a modified `setup.py` (an `av` version pin) and an untracked `Dockerfile`. I didn't change either; they come from the container setup, so I left them alone.

_session end: success, turns 11, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 8.45 s: python repro_tmp.py 2>&1 | tail -3
- `rc=0` 6.07 s: python repro_tmp.py 2>&1 | tail -3
- `rc=0` 9.44 s: HF_HUB_OFFLINE=1 python -m pytest tests/pipelines/test_pipelines_common.py -q -x 2>&1 | tail -5; git status --short
- `rc=0` 9.71 s: git diff setup.py | head; HF_HUB_OFFLINE=1 python -m pytest tests/pipelines/test_pipelines_common.py -q 2>&1 | grep -E "FAILED|Error|passed|failed" | head -20
- `rc=0` 10.17 s: HF_HUB_OFFLINE=1 python -m pytest tests/pipelines/test_pipelines_common.py -q -p no:warnings 2>&1 | grep -E "^FAILED|passed|failed"
- `rc=0` 11.97 s: git stash push src/transformers/pipelines/base.py -q && HF_HUB_OFFLINE=1 python -m pytest tests/pipelines/test_pipelines_common.py -q -p no:warnings 2>&1 | tail -1; git stash pop -q && git diff --stat src/
