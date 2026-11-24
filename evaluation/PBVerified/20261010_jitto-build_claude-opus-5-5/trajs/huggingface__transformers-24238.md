# Instance: huggingface__transformers-24238

- Final resolved (evaluator, logs/huggingface__transformers-24238_result.json): True
- Run state: DONE
- One attempt. Duration 21.0 s, turns 5, actor cost $0.1215854, container commands 3
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/huggingface__transformers-24238/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-24238/repo. Consider the following issue description:

<issue_description>
Error when overriding generation config: GenerationConfig() got multiple values for keyword argument 'num_beams'
### System Info

- `transformers` version: 4.30.0.dev0 (commit: 4aa13224a5bca560147a29c06b2e0597137caf3e)
- Platform: Linux-5.15.0-1013-oracle-x86_64-with-glibc2.31
- Python version: 3.10.11
- Huggingface_hub version: 0.15.1
- Safetensors version: 0.3.1
- PyTorch version (GPU?): 2.0.1+cu117 (True)
- Tensorflow version (GPU?): not installed (NA)
- Flax version (CPU?/GPU?/TPU?): not installed (NA)
- Jax version: not installed
- JaxLib version: not installed
- Using GPU in script?: Yes
- Using distributed or parallel set-up in script?: Yes (launching with `accelerate`)

### Who can help?

@gante @sgugger 

### Information

- [ ] The official example scripts
- [X] My own modified scripts

### Tasks

- [ ] An officially supported task in the `examples` folder (such as GLUE/SQuAD, ...)
- [X] My own task or dataset (give details below)

### Reproduction


Calling `GenerationConfig.from_pretrained` with a model that already defines `num_beams` in its configuration, and attempting to override the `num_beams` parameter (and presumably any other parameter), results in a runtime exception `got multiple values for keyword argument 'num_beams'` 

```python
generation_config: GenerationConfig = GenerationConfig.from_pretrained(
        "My-private-model",
        num_beams=num_beams)
```

Results in : 
```
  File "/app/scripts/fine_tune/./fine_tune_and_evaluate.py", line 1481, in <module>
    main()
  File "/app/scripts/fine_tune/./fine_tune_and_evaluate.py", line 1267, in main
    generation_config: GenerationConfig = GenerationConfig.from_pretrained(
  File "/app/ai_categorize_env/lib/python3.10/site-packages/transformers/generation/configuration_utils.py", line 541, in from_pretrained
    return cls.from_dict(config_dict, **kwargs)
  File "/app/ai_categorize_env/lib/python3.10/site-packages/transformers/generation/configuration_utils.py", line 574, in from_dict
    config = cls(**config_dict, **kwargs)
TypeError: transformers.generation.configuration_utils.GenerationConfig() got multiple values for keyword argument 'num_beams'
```

This appears to be because of this code:
https://github.com/huggingface/transformers/blob/ba695c1efd55091e394eb59c90fb33ac3f9f0d41/src/transformers/generation/configuration_utils.py#L572-L576

That is calling `cls(**config_dict, **kwargs)`, which might pass the same keyword values in twice if the `config_dict` has the property that `kwargs` does, right? I don't see a step where we remove the properties from `config_dict` that are mentioned in `kwargs`, although there is a comment right above that says: `# remove all the arguments that are in the config_dict`

Wouldn't the code need to do something more like this?
```
config_dict_copy = config_dict.copy()
config_dict_copy.update(kwargs)
config = cls(**config_dict_copy)
```

My generation_config.json from my model is this:
```json
{
  "decoder_start_token_id": 0,
  "eos_token_id": 1,
  "length_penalty": 0,
  "max_length": 32,
  "num_beams": 2,
  "num_return_sequences": 2,
  "output_scores": true,
  "pad_token_id": 0,
  "return_dict_in_generate": true,
  "transformers_version": "4.30.0.dev0"
}
```





### Expected behavior

This should not throw an exception:
```python
generation_config: GenerationConfig = GenerationConfig.from_pretrained(
        "My-model",
        num_beams=num_beams)
```


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-24238/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-24238/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-24238/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-24238/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -n "def from_dict" -A 40 src/transformers/generation/configuration_utils.py
```

tool result:

```
550:    def from_dict(cls, config_dict: Dict[str, Any], **kwargs) -> "GenerationConfig":
551-        """
552-        Instantiates a [`GenerationConfig`] from a Python dictionary of parameters.
553-
554-        Args:
555-            config_dict (`Dict[str, Any]`):
556-                Dictionary that will be used to instantiate the configuration object.
557-            kwargs (`Dict[str, Any]`):
558-                Additional parameters from which to initialize the configuration object.
559-
560-        Returns:
561-            [`GenerationConfig`]: The configuration object instantiated from those parameters.
562-        """
563-        return_unused_kwargs = kwargs.pop("return_unused_kwargs", False)
564-        # Those arguments may be passed along for our internal telemetry.
565-        # We remove them so they don't appear in `return_unused_kwargs`.
566-        kwargs.pop("_from_auto", None)
567-        kwargs.pop("_from_pipeline", None)
568-        # The commit hash might have been updated in the `config_dict`, we don't want the kwargs to erase that update.
569-        if "_commit_hash" in kwargs and "_commit_hash" in config_dict:
570-            kwargs["_commit_hash"] = config_dict["_commit_hash"]
571-
572-        # remove all the arguments that are in the config_dict
573-
574-        config = cls(**config_dict, **kwargs)
575-        unused_kwargs = config.update(**kwargs)
576-
577-        logger.info(f"Generate config {config}")
578-        if return_unused_kwargs:
579-            return config, unused_kwargs
580-        else:
581-            return config
582-
583-    def dict_torch_dtype_to_str(self, d: Dict[str, Any]) -> None:
584-        """
585-        Checks whether the passed dictionary and its nested dicts have a *torch_dtype* key and if it's not None,
586-        converts torch.dtype to a string of just the type. For example, `torch.float32` get converted into *"float32"*
587-        string, which can then be stored in the json format.
588-        """
589-        if d.get("torch_dtype", None) is not None and not isinstance(d["torch_dtype"], str):
590-            d["torch_dtype"] = str(d["torch_dtype"]).split(".")[1]
```

**assistant:** Reproducing first:

**tool call: Bash**

```bash
/work/huggingface__transformers-24238/bin/envrun 'python -c "
from transformers import GenerationConfig
c = GenerationConfig.from_dict({\"num_beams\": 2, \"max_length\": 32}, num_beams=5, foo=1, return_unused_kwargs=True)
print(c)
"' 2>&1 | tail -3
```

tool result:

```
    config = cls(**config_dict, **kwargs)
TypeError: transformers.generation.configuration_utils.GenerationConfig() got multiple values for keyword argument 'num_beams'
```

**tool call: Bash**

```bash
sed -i '' 's/        config = cls(\*\*config_dict, \*\*kwargs)/        config = cls(**{**config_dict, **kwargs})/' src/transformers/generation/configuration_utils.py && git diff && ../bin/envrun 'python -c "
from transformers import GenerationConfig
c, u = GenerationConfig.from_dict({\"num_beams\": 2, \"max_length\": 32}, num_beams=5, foo=1, return_unused_kwargs=True)
print(c.num_beams, c.max_length, u)
"' 2>&1 | tail -3
```

tool result:

```
diff --git a/src/transformers/generation/configuration_utils.py b/src/transformers/generation/configuration_utils.py
index 9f3bedcde..00201a9e1 100644
--- a/src/transformers/generation/configuration_utils.py
+++ b/src/transformers/generation/configuration_utils.py
@@ -571,7 +571,7 @@ class GenerationConfig(PushToHubMixin):
 
         # remove all the arguments that are in the config_dict
 
-        config = cls(**config_dict, **kwargs)
+        config = cls(**{**config_dict, **kwargs})
         unused_kwargs = config.update(**kwargs)
 
         logger.info(f"Generate config {config}")
5 32 {}
```

**assistant:** The override now works: `num_beams=5` wins over the dict's `2`. Running the existing tests:

**tool call: Bash**

```bash
../bin/envrun 'python -m pytest tests/generation/test_configuration_utils.py -q 2>&1 | tail -5'
```

tool result:

```
  /usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py:945: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
5 passed, 2 skipped, 2 warnings in 0.29s
```

**assistant:** I fixed the bug: `GenerationConfig.from_pretrained` / `from_dict` no longer crashes when you pass a keyword argument that's already set in the model's saved generation config.

**Cause:** In `src/transformers/generation/configuration_utils.py:574`, `from_dict` built the config with `cls(**config_dict, **kwargs)`. When a key such as `num_beams` was in both dicts, Python raised `TypeError: got multiple values for keyword argument`. The comment just above that line says overlapping keys are removed, but no code actually did it.

**Fix:** One line. It merges the two dicts first, so the value you pass overrides the saved one:

```python
config = cls(**{**config_dict, **kwargs})
```

The existing `config.update(**kwargs)` call after it is unchanged, so `return_unused_kwargs` and attribute updates behave as before.

**Checks:**
- **Before:** `GenerationConfig.from_dict({"num_beams": 2, "max_length": 32}, num_beams=5)` raised the `TypeError` from the issue.
- **After:** it returns a config with `num_beams=5` and `max_length=32`, so the override is applied and the other saved values are kept.
- `tests/generation/test_configuration_utils.py`: 5 passed, 2 skipped.

I ran the reproduction inline, so there are no scratch files to clean up. The only change in the repo is that one line.

_session end: success, turns 5, is_error False_

## Container commands (task container, no network; broker log)

- `rc=1` 0.84 s: python -c " from transformers import GenerationConfig c = GenerationConfig.from_dict({\"num_beams\": 2, \"max_length\": 32}, num_beams=5, foo=1, return_unused_kwargs=True) print(c) "
- `rc=0` 0.73 s: python -c " from transformers import GenerationConfig c, u = GenerationConfig.from_dict({\"num_beams\": 2, \"max_length\": 32}, num_beams=5, foo=1, return_unused_kwargs=True) print(c.num_beams, c.max_length, u) "
- `rc=0` 2.73 s: python -m pytest tests/generation/test_configuration_utils.py -q 2>&1 | tail -5
