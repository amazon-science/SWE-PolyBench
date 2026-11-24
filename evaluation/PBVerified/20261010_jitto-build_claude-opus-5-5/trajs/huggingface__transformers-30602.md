# Instance: huggingface__transformers-30602

- Final resolved (evaluator, logs/huggingface__transformers-30602_result.json): True
- Run state: DONE
- One attempt. Duration 136.2 s, turns 12, actor cost $0.2719446, container commands 8
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/huggingface__transformers-30602/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-30602/repo. Consider the following issue description:

<issue_description>
`model.safetensors` missing in model file not found error in default case
### System Info

System info isn't super relevant here since the confusion is really just an just an error message string. I just reproduced in a CPU instance but this is applicable whenever model loading is needed.
- `transformers` version: 4.40.1
- Platform: Linux-6.1.58+-x86_64-with-glibc2.35
- Python version: 3.10.12
- Huggingface_hub version: 0.22.2
- Safetensors version: 0.4.3
- Accelerate version: 0.29.3
- Accelerate config: 	not found
- PyTorch version (GPU?): 2.2.1+cu121 (False)
- Tensorflow version (GPU?): 2.15.0 (False)
- Flax version (CPU?/GPU?/TPU?): 0.8.2 (cpu)
- Jax version: 0.4.26
- JaxLib version: 0.4.26
- Using GPU in script?: No
- Using distributed or parallel set-up in script?: No


### Who can help?

Not sure who most recently worked on `modeling_util.py` or model loading parts. Please feel free to point me to the right person

### Information

- [ ] The official example scripts
- [X] My own modified scripts

### Tasks

- [ ] An officially supported task in the `examples` folder (such as GLUE/SQuAD, ...)
- [X] My own task or dataset (give details below)

### Reproduction

Setup has safetensors library installed

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# this is just a cloned example GPTQ quant model. 
# The point of this is that this repo contains a `gptq_model-4bit-128g.safetensors` file (default naming by AutoGPTQ library), but not `model.safetensors`.
# Not having a `.safetensors` and/or any modeling files produces the same behavior
# Note how use_safetensors is not passed in
# With safetensors library, it will default to `use_safetensors=None` inside `.from_pretrained()` function
tokenizer = AutoTokenizer.from_pretrained("davidxmle/Llama-3-8B-Instruct-GPTQ-4-Bit-Debug")
model = AutoModelForCausalLM.from_pretrained("davidxmle/Llama-3-8B-Instruct-GPTQ-4-Bit-Debug")
```

An error will get thrown
```
davidxmle/Llama-3-8B-Instruct-GPTQ-4-Bit-Debug does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt or flax_model.msgpack.
```
 Error message has no mention of `.safetensors` file is an accepted model file format.


### Expected behavior

This isn't necessarily a bug but rather a confusing error message. I initially noticed this issue when I uploaded a GPTQ quant model made using the AutoGPTQ library to huggingface but some folks reported that they are getting the error above `does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt or flax_model.msgpack.` One would have immediately assumed `safetensors` is not an accepted file format and I must not use `safetensors` but rather use one of the models listed above, since I do have a `safetensors` file in the repo.

Upon further investigation I realized that the `use_safetensors` is an optional argument to be passed in added in https://github.com/huggingface/transformers/pull/22083. This means `use_safetensors` can either be `False` if explicitly defined as `False` or does not have safetensors package installed, `True` if explicitly defined as so, or, **most importantly `use_safetensors` will default to`None` if not specified but has safetensors installed**.

The pull request added in https://github.com/huggingface/transformers/pull/22083, does add an error message specifically for safe tensors, but it uses `elif use_safetensors:` for the error message specific for safetensors, and used `elif use_safetensors is not False` elsewhere... `elif use_safetensors:` evaluates both the default case with `None` value and explict `False` case to false, so the error message containing safetensors in the default case never reached there. I do believe this is the expected behavior since we do not want to only mention safetensors is missing in the default case. 

However, in the case where the `use_safetensors` is defaulted to `None` when the arg is not passed in and model file is missing, there is no mention of `.safetensors` is supported. This should be comprehensive list of all modeling files that are supported, including `model.safetensors`.

I have put together a super simple PR and changed the unit test to address this.

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-30602/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-30602/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-30602/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-30602/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -n "does not appear to have a file named" -r src/transformers/modeling_*.py
```

tool result:

```
src/transformers/modeling_flax_utils.py:834:                                f"{pretrained_model_name_or_path} does not appear to have a file named"
src/transformers/modeling_flax_utils.py:840:                                f"{pretrained_model_name_or_path} does not appear to have a file named"
src/transformers/modeling_flax_utils.py:846:                                f"{pretrained_model_name_or_path} does not appear to have a file named"
src/transformers/modeling_tf_utils.py:2872:                                f"{pretrained_model_name_or_path} does not appear to have a file named"
src/transformers/modeling_tf_utils.py:2878:                                f"{pretrained_model_name_or_path} does not appear to have a file named {WEIGHTS_NAME},"
src/transformers/modeling_utils.py:3332:                                    f"{pretrained_model_name_or_path} does not appear to have a file named"
src/transformers/modeling_utils.py:3392:                                f"{pretrained_model_name_or_path} does not appear to have a file named"
src/transformers/modeling_utils.py:3398:                                f"{pretrained_model_name_or_path} does not appear to have a file named"
src/transformers/modeling_utils.py:3406:                                f"{pretrained_model_name_or_path} does not appear to have a file named"
src/transformers/modeling_utils.py:3412:                                f"{pretrained_model_name_or_path} does not appear to have a file named"
```

**tool call: Bash**

```bash
sed -n 3200,3240p src/transformers/modeling_utils.py; echo ----; sed -n 3320,3425p src/transformers/modeling_utils.py; grep -rn "does not appear to have a file named" tests/test_modeling_utils.py
```

tool result:

```
                    # Load from a TF 1.0 checkpoint in priority if from_tf
                    archive_file = os.path.join(pretrained_model_name_or_path, subfolder, TF_WEIGHTS_NAME + ".index")
                elif from_tf and os.path.isfile(
                    os.path.join(pretrained_model_name_or_path, subfolder, TF2_WEIGHTS_NAME)
                ):
                    # Load from a TF 2.0 checkpoint in priority if from_tf
                    archive_file = os.path.join(pretrained_model_name_or_path, subfolder, TF2_WEIGHTS_NAME)
                elif from_flax and os.path.isfile(
                    os.path.join(pretrained_model_name_or_path, subfolder, FLAX_WEIGHTS_NAME)
                ):
                    # Load from a Flax checkpoint in priority if from_flax
                    archive_file = os.path.join(pretrained_model_name_or_path, subfolder, FLAX_WEIGHTS_NAME)
                elif use_safetensors is not False and os.path.isfile(
                    os.path.join(pretrained_model_name_or_path, subfolder, _add_variant(SAFE_WEIGHTS_NAME, variant))
                ):
                    # Load from a safetensors checkpoint
                    archive_file = os.path.join(
                        pretrained_model_name_or_path, subfolder, _add_variant(SAFE_WEIGHTS_NAME, variant)
                    )
                elif use_safetensors is not False and os.path.isfile(
                    os.path.join(
                        pretrained_model_name_or_path, subfolder, _add_variant(SAFE_WEIGHTS_INDEX_NAME, variant)
                    )
                ):
                    # Load from a sharded safetensors checkpoint
                    archive_file = os.path.join(
                        pretrained_model_name_or_path, subfolder, _add_variant(SAFE_WEIGHTS_INDEX_NAME, variant)
                    )
                    is_sharded = True
                elif os.path.isfile(
                    os.path.join(pretrained_model_name_or_path, subfolder, _add_variant(WEIGHTS_NAME, variant))
                ):
                    # Load from a PyTorch checkpoint
                    archive_file = os.path.join(
                        pretrained_model_name_or_path, subfolder, _add_variant(WEIGHTS_NAME, variant)
                    )
                elif os.path.isfile(
                    os.path.join(pretrained_model_name_or_path, subfolder, _add_variant(WEIGHTS_INDEX_NAME, variant))
                ):
                    # Load from a sharded PyTorch checkpoint
                    archive_file = os.path.join(
----
                            **cached_file_kwargs,
                        )
                        if resolved_archive_file is not None:
                            is_sharded = True
                        elif use_safetensors:
                            if revision == "main":
                                resolved_archive_file, revision, is_sharded = auto_conversion(
                                    pretrained_model_name_or_path, **cached_file_kwargs
                                )
                            cached_file_kwargs["revision"] = revision
                            if resolved_archive_file is None:
                                raise EnvironmentError(
                                    f"{pretrained_model_name_or_path} does not appear to have a file named"
                                    f" {_add_variant(SAFE_WEIGHTS_NAME, variant)} or {_add_variant(SAFE_WEIGHTS_INDEX_NAME, variant)} "
                                    "and thus cannot be loaded with `safetensors`. Please make sure that the model has "
                                    "been saved with `safe_serialization=True` or do not set `use_safetensors=True`."
                                )
                        else:
                            # This repo has no safetensors file of any kind, we switch to PyTorch.
                            filename = _add_variant(WEIGHTS_NAME, variant)
                            resolved_archive_file = cached_file(
                                pretrained_model_name_or_path, filename, **cached_file_kwargs
                            )
                    if resolved_archive_file is None and filename == _add_variant(WEIGHTS_NAME, variant):
                        # Maybe the checkpoint is sharded, we try to grab the index name in this case.
                        resolved_archive_file = cached_file(
                            pretrained_model_name_or_path,
                            _add_variant(WEIGHTS_INDEX_NAME, variant),
                            **cached_file_kwargs,
                        )
                        if resolved_archive_file is not None:
                            is_sharded = True

                    if resolved_archive_file is not None:
                        if filename in [WEIGHTS_NAME, WEIGHTS_INDEX_NAME]:
                            # If the PyTorch file was found, check if there is a safetensors file on the repository
                            # If there is no safetensors file on the repositories, start an auto conversion
                            safe_weights_name = SAFE_WEIGHTS_INDEX_NAME if is_sharded else SAFE_WEIGHTS_NAME
                            has_file_kwargs = {
                                "revision": revision,
                                "proxies": proxies,
                                "token": token,
                            }
                            cached_file_kwargs = {
                                "cache_dir": cache_dir,
                                "force_download": force_download,
                                "resume_download": resume_download,
                                "local_files_only": local_files_only,
                                "user_agent": user_agent,
                                "subfolder": subfolder,
                                "_raise_exceptions_for_gated_repo": False,
                                "_raise_exceptions_for_missing_entr
[... 3938 more characters not shown]
```

**tool call: Bash**

```bash
sed -n 3240,3275p src/transformers/modeling_utils.py; echo ----; sed -n 955,985p tests/test_modeling_utils.py; grep -n "safetensors\b.*does not appear\|model.safetensors" tests/test_modeling_utils.py | head
```

tool result:

```
                    archive_file = os.path.join(
                        pretrained_model_name_or_path, subfolder, _add_variant(WEIGHTS_INDEX_NAME, variant)
                    )
                    is_sharded = True
                # At this stage we don't have a weight file so we will raise an error.
                elif os.path.isfile(
                    os.path.join(pretrained_model_name_or_path, subfolder, TF_WEIGHTS_NAME + ".index")
                ) or os.path.isfile(os.path.join(pretrained_model_name_or_path, subfolder, TF2_WEIGHTS_NAME)):
                    raise EnvironmentError(
                        f"Error no file named {_add_variant(WEIGHTS_NAME, variant)} found in directory"
                        f" {pretrained_model_name_or_path} but there is a file for TensorFlow weights. Use"
                        " `from_tf=True` to load this model from those weights."
                    )
                elif os.path.isfile(os.path.join(pretrained_model_name_or_path, subfolder, FLAX_WEIGHTS_NAME)):
                    raise EnvironmentError(
                        f"Error no file named {_add_variant(WEIGHTS_NAME, variant)} found in directory"
                        f" {pretrained_model_name_or_path} but there is a file for Flax weights. Use `from_flax=True`"
                        " to load this model from those weights."
                    )
                elif use_safetensors:
                    raise EnvironmentError(
                        f"Error no file named {_add_variant(SAFE_WEIGHTS_NAME, variant)} found in directory"
                        f" {pretrained_model_name_or_path}."
                    )
                else:
                    raise EnvironmentError(
                        f"Error no file named {_add_variant(WEIGHTS_NAME, variant)}, {TF2_WEIGHTS_NAME},"
                        f" {TF_WEIGHTS_NAME + '.index'} or {FLAX_WEIGHTS_NAME} found in directory"
                        f" {pretrained_model_name_or_path}."
                    )
            elif os.path.isfile(os.path.join(subfolder, pretrained_model_name_or_path)):
                archive_file = pretrained_model_name_or_path
                is_local = True
            elif os.path.isfile(os.path.join(subfolder, pretrained_model_name_or_path + ".index")):
                if not from_tf:
                    raise ValueError(
----
        response_mock.raise_for_status.side_effect = HTTPError
        response_mock.json.return_value = {}

        # Download this model to make sure it's in the cache.
        _ = BertModel.from_pretrained("hf-internal-testing/tiny-random-bert")

        # Under the mock environment we get a 500 error when trying to reach the model.
        with mock.patch("requests.Session.request", return_value=response_mock) as mock_head:
            _ = BertModel.from_pretrained("hf-internal-testing/tiny-random-bert")
            # This check we did call the fake head request
            mock_head.assert_called()

    @require_safetensors
    def test_use_safetensors(self):
        # Should not raise anymore
        AutoModel.from_pretrained("hf-internal-testing/tiny-random-RobertaModel", use_safetensors=True)

        # test that error if only safetensors is available
        with self.assertRaises(OSError) as env_error:
            BertModel.from_pretrained("hf-internal-testing/tiny-random-bert-safetensors", use_safetensors=False)

        self.assertTrue("does not appear to have a file named pytorch_model.bin" in str(env_error.exception))

        # test that only safetensors if both available and use_safetensors=False
        with tempfile.TemporaryDirectory() as tmp_dir:
            CLIPTextModel.from_pretrained(
                "hf-internal-testing/diffusers-stable-diffusion-tiny-all",
                subfolder="text_encoder",
                use_safetensors=False,
                cache_dir=tmp_dir,
            )
1009:            # No pytorch_model.bin file, only a model.safetensors
1033:            # No pytorch_model.bin index file, only a model.safetensors index
1333:            with safe_open(os.path.join(tmp_dir, "model.safetensors"), framework="pt") as f:
```

**tool call: Bash**

```bash
grep -rn "does not appear to have\|Error no file named" tests/ | grep -v "^tests/.*fixtures" | head -20; git log --oneline -1
```

tool result:

```
tests/utils/test_hub_utils.py:71:        with self.assertRaisesRegex(EnvironmentError, "does not appear to have a file named"):
tests/utils/test_hub_utils.py:75:        with self.assertRaisesRegex(EnvironmentError, "does not appear to have a file named"):
tests/models/auto/test_image_processing_auto.py:132:            "hf-internal-testing/config-no-model does not appear to have a file named preprocessor_config.json.",
tests/models/auto/test_feature_extraction_auto.py:98:            "hf-internal-testing/config-no-model does not appear to have a file named preprocessor_config.json.",
tests/models/auto/test_modeling_auto.py:486:            "hf-internal-testing/config-no-model does not appear to have a file named pytorch_model.bin",
tests/models/auto/test_modeling_flax_auto.py:96:            "hf-internal-testing/config-no-model does not appear to have a file named flax_model.msgpack",
tests/models/auto/test_configuration_auto.py:110:            "hf-internal-testing/no-config-test-repo does not appear to have a file named config.json.",
tests/models/auto/test_modeling_tf_auto.py:287:            "hf-internal-testing/config-no-model does not appear to have a file named pytorch_model.bin",
tests/test_modeling_utils.py:976:        self.assertTrue("does not appear to have a file named pytorch_model.bin" in str(env_error.exception))
c681b58b0 Bump torch from 1.9.0+cpu to 1.13.1 in /examples/flax/vision (#21168)
```

**assistant:** Reproducing with an empty local directory, since the container has no network access:

**tool call: Bash**

```bash
cat > repro_tmp.py <<'EOF'
import tempfile
from transformers import BertConfig, BertModel
with tempfile.TemporaryDirectory() as d:
    BertConfig().save_pretrained(d)
    try:
        BertModel.from_pretrained(d)
    except OSError as e:
        print(e)
EOF
/work/huggingface__transformers-30602/bin/envrun 'python repro_tmp.py 2>&1 | tail -3'
```

tool result:

```
Error no file named pytorch_model.bin, tf_model.h5, model.ckpt.index or flax_model.msgpack found in directory /tmp/tmpr8ezgtyv.
```

**assistant:** Reproduced. Now I'll update both the local-directory and Hub messages:

**tool call: Bash**

```bash
python3 - <<'EOF'
p='src/transformers/modeling_utils.py'
s=open(p).read()
a='''                        f"Error no file named {_add_variant(WEIGHTS_NAME, variant)}, {TF2_WEIGHTS_NAME},"
                        f" {TF_WEIGHTS_NAME + '.index'} or {FLAX_WEIGHTS_NAME} found in directory"'''
b='''                        f"Error no file named {_add_variant(WEIGHTS_NAME, variant)}, {_add_variant(SAFE_WEIGHTS_NAME, variant)},"
                        f" {TF2_WEIGHTS_NAME}, {TF_WEIGHTS_NAME + '.index'} or {FLAX_WEIGHTS_NAME} found in directory"'''
c='''                                f" {_add_variant(WEIGHTS_NAME, variant)}, {TF2_WEIGHTS_NAME}, {TF_WEIGHTS_NAME} or"
                                f" {FLAX_WEIGHTS_NAME}."'''
d='''                                f" {_add_variant(WEIGHTS_NAME, variant)}, {_add_variant(SAFE_WEIGHTS_NAME, variant)},"
                                f" {TF2_WEIGHTS_NAME}, {TF_WEIGHTS_NAME} or {FLAX_WEIGHTS_NAME}."'''
assert s.count(a)==1 and s.count(c)==1
open(p,'w').write(s.replace(a,b).replace(c,d))
EOF
git diff --stat
/work/huggingface__transformers-30602/bin/envrun 'python repro_tmp.py 2>&1 | tail -3; ruff check src/transformers/modeling_utils.py; ruff format --check src/transformers/modeling_utils.py'
```

tool result:

```
 src/transformers/modeling_utils.py | 8 ++++----
 1 file changed, 4 insertions(+), 4 deletions(-)
Error no file named pytorch_model.bin, model.safetensors, tf_model.h5, model.ckpt.index or flax_model.msgpack found in directory /tmp/tmpzeibph_i.
1 file left unchanged
```

**assistant:** The local-directory message is fixed. The Hub path needs network, so I'll check it with mocks instead:

**tool call: Bash**

```bash
cat > repro_tmp2.py <<'EOF'
from unittest import mock
from transformers import BertConfig, BertModel
import transformers.modeling_utils as mu
with mock.patch.object(mu, "cached_file", return_value=None), mock.patch.object(mu, "has_file", return_value=False):
    try:
        BertModel.from_pretrained("some-org/some-repo", config=BertConfig())
    except OSError as e:
        print(e)
EOF
/work/huggingface__transformers-30602/bin/envrun 'python repro_tmp2.py 2>&1 | tail -3'
```

tool result:

```
some-org/some-repo does not appear to have a file named pytorch_model.bin, model.safetensors, tf_model.h5, model.ckpt or flax_model.msgpack.
```

**assistant:** Both paths are fixed. Now I'll delete the scripts and run the closest offline tests:

**tool call: Bash**

```bash
rm repro_tmp.py repro_tmp2.py
/work/huggingface__transformers-30602/bin/envrun 'HF_HUB_OFFLINE=1 python -m pytest tests/test_modeling_utils.py -q -x -k "not hub and not Hub" 2>&1 | tail -5'; git status --short
```

tool result:

```
-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED tests/test_modeling_utils.py::ModelUtilsTest::test_cached_files_are_used_when_internet_is_down
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
1 failed, 1 passed, 14 deselected, 4 warnings in 0.68s

 M src/transformers/modeling_utils.py
?? Dockerfile
```

**tool call: Bash**

```bash
/work/huggingface__transformers-30602/bin/envrun 'HF_HUB_OFFLINE=1 python -m pytest tests/test_modeling_utils.py -q 2>&1 | grep -E "FAILED|passed|failed" | head -40'; /work/huggingface__transformers-30602/bin/envrun 'git stash -q && HF_HUB_OFFLINE=1 python -m pytest tests/test_modeling_utils.py -q 2>&1 | tail -1; git stash pop -q && git diff --stat'
```

tool result:

```
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        #     _commit_hash: passed when we are chaining several calls to various files (e.g. when loading a tokenizer or

39 failed, 15 passed, 34 skipped, 42 warnings in 9.23s
 src/transformers/modeling_utils.py | 8 ++++----
 1 file changed, 4 insertions(+), 4 deletions(-)
```

**tool call: Bash**

```bash
/work/huggingface__transformers-30602/bin/envrun 'HF_HUB_OFFLINE=1 python -m pytest tests/test_modeling_utils.py -q -rf 2>&1 | grep -E "^FAILED" | sort > /tmp/after.txt; tail -1 /tmp/after.txt; wc -l < /tmp/after.txt; git stash -q && HF_HUB_OFFLINE=1 python -m pytest tests/test_modeling_utils.py -q -rf 2>&1 | grep -E "^FAILED" | sort > /tmp/before.txt; git stash pop -q; diff <(cut -d" " -f2 /tmp/before.txt) <(cut -d" " -f2 /tmp/after.txt) && echo SAME_FAILURES; grep -c OfflineModeIsEnabled /tmp/after.txt'
```

tool result:

```
Exit code 1
FAILED tests/test_modeling_utils.py::TestAttentionImplementation::test_not_available_flash_with_config
39
SAME_FAILURES
0
```

**tool call: Bash**

```bash
/work/huggingface__transformers-30602/bin/envrun 'cut -c1-220 /tmp/after.txt | head -5; git diff --stat'
```

tool result:

```
FAILED tests/test_modeling_utils.py::ModelUtilsTest::test_cached_files_are_used_when_internet_is_down
FAILED tests/test_modeling_utils.py::ModelUtilsTest::test_checkpoint_sharding_from_hub
FAILED tests/test_modeling_utils.py::ModelUtilsTest::test_checkpoint_sharding_local_bin
FAILED tests/test_modeling_utils.py::ModelUtilsTest::test_checkpoint_variant_hub
FAILED tests/test_modeling_utils.py::ModelUtilsTest::test_checkpoint_variant_hub_safe
 src/transformers/modeling_utils.py | 8 ++++----
 1 file changed, 4 insertions(+), 4 deletions(-)
```

**assistant:** I fixed the error message: when no weights file is found, it now lists `model.safetensors` along with the other supported formats. The change is in `src/transformers/modeling_utils.py` and affects two messages.

- **Hub repos** (the case in the issue):
  `... does not appear to have a file named pytorch_model.bin, model.safetensors, tf_model.h5, model.ckpt or flax_model.msgpack.`
- **Local directories** (same problem):
  `Error no file named pytorch_model.bin, model.safetensors, tf_model.h5, model.ckpt.index or flax_model.msgpack found in directory ...`

The safetensors name respects `variant` the same way the PyTorch name does. `pytorch_model.bin` is still listed first, so existing tests that check for `"does not appear to have a file named pytorch_model.bin"` still match. I left the explicit `use_safetensors=True` error alone, since it already names the safetensors files.

**Verification:**
- **Local-directory path:** I loaded a model from a directory with only a config. The old message didn't mention safetensors; the new one does.
- **Hub path:** the container has no network, so I tested it by stubbing out the file lookups (`cached_file` and `has_file`). It now produces the new message shown above. It hasn't been run against the real Hub.
- **Tests:** `tests/test_modeling_utils.py` gives 15 passed, 34 skipped and 39 failed offline. The same 39 tests fail without my change, so the failures come from the missing network, not from this fix.

I deleted my reproduction scripts. There's an untracked `Dockerfile` in the repo root that I didn't create, and I left it alone.

_session end: success, turns 12, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 2.79 s: python repro_tmp.py 2>&1 | tail -3
- `rc=0` 2.77 s: python repro_tmp.py 2>&1 | tail -3; ruff check src/transformers/modeling_utils.py; ruff format --check src/transformers/modeling_utils.py
- `rc=0` 2.37 s: python repro_tmp2.py 2>&1 | tail -3
- `rc=0` 3.37 s: HF_HUB_OFFLINE=1 python -m pytest tests/test_modeling_utils.py -q -x -k "not hub and not Hub" 2>&1 | tail -5
- `rc=0` 21.67 s: HF_HUB_OFFLINE=1 python -m pytest tests/test_modeling_utils.py -q 2>&1 | grep -E "FAILED|passed|failed" | head -40
- `rc=0` 13.52 s: git stash -q && HF_HUB_OFFLINE=1 python -m pytest tests/test_modeling_utils.py -q 2>&1 | tail -1; git stash pop -q && git diff --stat
- `rc=1` 24.42 s: HF_HUB_OFFLINE=1 python -m pytest tests/test_modeling_utils.py -q -rf 2>&1 | grep -E "^FAILED" | sort > /tmp/after.txt; tail -1 /tmp/after.txt; wc -l < /tmp/after.txt; git stash -q && HF_HUB_OFFLINE=1 python -m pytest tests/test_modeling_utils.py -q -rf 2>&1 | grep -E "^FAILED" | sort > /tmp/before.txt; git stash pop -q; diff <(cut -d" " -f2 /tmp/before.txt) <(cut -d" " -f2 /tmp/after.txt) && echo SAME_FAILURES; grep -c OfflineModeIsEnabled /tmp/after.txt
- `rc=0` 0.2 s: cut -c1-220 /tmp/after.txt | head -5; git diff --stat
