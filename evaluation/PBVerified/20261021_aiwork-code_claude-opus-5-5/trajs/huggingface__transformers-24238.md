# Instance: huggingface__transformers-24238
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
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
````

## Operational trajectory

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "grep -n \"def from_dict\" -A 40 src/transformers/generation/configuration_utils.py"
}
````

Result:

````text
{
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "success",
  "exit_code": 0,
  "retryability": "not_needed",
  "open_work_at_failure": false
 },
 "stdout": "550:    def from_dict(cls, config_dict: Dict[str, Any], **kwargs) -> \"GenerationConfig\":\n551-        \"\"\"\n552-        Instantiates a [`GenerationConfig`] from a Python dictionary of parameters.\n553-\n554-        Args:\n555-            config_dict (`Dict[str, Any]`):\n556-                Dictionary that will be used to instantiate the configuration object.\n557-            kwargs (`Dict[str, Any]`):\n558-                Additional parameters from which to initialize the configuration object.\n559-\n560-        Returns:\n561-            [`GenerationConfig`]: The configuration object instantiated from those parameters.\n562-        \"\"\"\n563-        return_unused_kwargs = kwargs.pop(\"return_unused_kwargs\", False)\n564-        # Those arguments may be passed along for our internal telemetry.\n565-        # We remove them so they don't appear in `return_unused_kwargs`.\n566-        kwargs.pop(\"_from_auto\", None)\n567-        kwargs.pop(\"_from_pipeline\", None)\n568-        # The commit hash might have been updated in the `config_dict`, we don't want the kwargs to erase that update.\n569-        if \"_commit_hash\" in kwargs and \"_commit_hash\" in config_dict:\n570-            kwargs[\"_commit_hash\"] = config_dict[\"_commit_hash\"]\n571-\n572-        # remove all the arguments that are in the config_dict\n573-\n574-        config = cls(**config_dict, **kwargs)\n575-        unused_kwargs = config.update(**kwargs)\n576-\n577-        logger.info(f\"Generate config {config}\")\n578-        if return_unused_kwargs:\n579-            return config, unused_kwargs\n580-        else:\n581-            return config\n582-\n583-    def dict_torch_dtype_to_str(self, d: Dict[str, Any]) -> None:\n584-        \"\"\"\n585-        Checks whether the passed dictionary and its nested dicts have a *torch_dtype* key and if it's not None,\n586-        converts torch.dtype to a string of just the type. For example, `torch.float32` get converted into *\"float32\"*\n587-        string, which can then be stored in the json format.\n588-        \"\"\"\n589-        if d.get(\"torch_dtype\", None) is not None and not isinstance(d[\"torch_dtype\"], str):\n590-            d[\"torch_dtype\"] = str(d[\"torch_dtype\"]).split(\".\")[1]\n",
 "device_targets": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "40",
   "src/transformers/generation/configuration_utils.py"
  ],
  "command_sha256": [
   "861b950b705bc643a411cb39f0bd16ed2987ba77afc39480e2ca3ddf2da47bd2"
  ]
 },
 "duration_ms": 324
}
````

### Turn 2 — thinking

````text
I'm fixing this upstream by merging the config dict with kwargs when constructing the instance, then letting the update call return any unused kwargs afterward.
````

### Turn 2 — tool call call_0002 (edit)

````json
{
 "file_path": "src/transformers/generation/configuration_utils.py",
 "old_string": "        # remove all the arguments that are in the config_dict\n\n        config = cls(**config_dict, **kwargs)",
 "new_string": "        # kwargs take precedence over the values in `config_dict`, avoiding duplicate keyword arguments\n        config = cls(**{**config_dict, **kwargs})"
}
````

Result:

````text
{
 "path": "src/transformers/generation/configuration_utils.py",
 "edited": true,
 "replacements": 1,
 "total_file_lines": 715,
 "total_file_size_bytes": 38992,
 "diff": "-         # remove all the arguments that are in the config_dict\n- \n-         config = cls(**config_dict, **kwargs)\n+         # kwargs take precedence over the values in `config_dict`, avoiding duplicate keyword arguments\n+         config = cls(**{**config_dict, **kwargs})",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "edit",
    "paths": [
     "src/transformers/generation/configuration_utils.py"
    ]
   }
  ]
 },
 "file_change": {
  "kind": "diff",
  "operation": "update",
  "path": "src/transformers/generation/configuration_utils.py",
  "patch": "-         # remove all the arguments that are in the config_dict\n- \n-         config = cls(**config_dict, **kwargs)\n+         # kwargs take precedence over the values in `config_dict`, avoiding duplicate keyword arguments\n+         config = cls(**{**config_dict, **kwargs})",
  "additions": 2,
  "deletions": 3,
  "truncated": false,
  "omitted_lines": 0
 }
}
````

### Turn 3 — tool call call_0003 (exec)

````json
{
 "command": "cd /testbed && python -c \"\nfrom transformers import GenerationConfig\nc,u=GenerationConfig.from_dict({'num_beams':2,'max_length':32},num_beams=5,foo=1,return_unused_kwargs=True)\nprint(c.num_beams,c.max_length,u)\n\""
}
````

Result:

````text
{
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "success",
  "exit_code": 0,
  "retryability": "not_needed",
  "open_work_at_failure": false
 },
 "stdout": "5 32 {}\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 977,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed"
  ],
  "command_sha256": [
   "cdb29b82c3bc8f6f7b0bab2e0e6b7a8935a7bf2a12ba5234b24ae39d6f491af2"
  ]
 }
}
````

### Turn 4 — thinking

````text
That foo kwarg just becomes an attribute set via arbitrary kwargs on GenerationConfig, consistent with prior behavior, so existing tests should still pass.
````

### Turn 4 — tool call call_0004 (exec)

````json
{
 "command": "cd /testbed && python -m pytest tests/generation/test_configuration_utils.py -q 2>&1 | tail -3"
}
````

Result:

````text
{
 "tool_diagnostic": {
  "schema_version": 1,
  "code": "exec.execution.nonzero_exit",
  "failure_stage": "execution",
  "cause_domain": "local_process",
  "owner": "exec",
  "classification_source": "producer_explicit",
  "failure_scope": "invocation",
  "action": "run"
 },
 "stdout": "=========================== short test summary info ============================\nFAILED tests/generation/test_configuration_utils.py::GenerationConfigTest::test_from_model_config\n1 failed, 4 passed, 2 skipped, 2 warnings in 0.29s\n",
 "duration_ms": 2967,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed"
  ],
  "command_sha256": [
   "816da6d27c4f82fb9e45d88ea5bdc77d2dd647809159e3280a6effb4cd7661c6"
  ]
 },
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "failed",
  "exit_code": 1,
  "failure_class": "unknown",
  "retryability": "retry_after_change",
  "open_work_at_failure": false
 },
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "device_targets": []
}
````

### Turn 5 — tool call call_0005 (exec)

````json
{
 "command": "cd /testbed && python -m pytest tests/generation/test_configuration_utils.py -q -k test_from_model_config 2>&1 | grep -E \"Error|assert\" | head; git stash -q && python -m pytest tests/generation/test_configuration_utils.py -q -k test_from_model_config 2>&1 | tail -1; git stash pop -q"
}
````

Result:

````text
{
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "success",
  "exit_code": 0,
  "retryability": "not_needed",
  "open_work_at_failure": false
 },
 "stdout": "redirect = False, assert_same_host = False\n        assert_same_host: bool = True,\n            :class:`~urllib3.exceptions.MaxRetryError` exception.\n            immediately. Also, instead of raising a MaxRetryError on redirects,\n        :param assert_same_host:\n            consistent else will raise HostChangedError. When ``False``, you can\n            block for ``pool_timeout`` seconds and raise EmptyPoolError if no\n        if assert_same_host and not self.is_same_host(url):\n            raise HostChangedError(self, url, retries)\n        # complains about UnboundLocalError.\n1 failed, 6 deselected, 2 warnings in 0.31s\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 5572,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed"
  ],
  "command_sha256": [
   "b26f677a0b2f75245802d6786eca69a021f24156ad8a62e492316e66a7b142d0"
  ]
 }
}
````

### Turn 6 — assistant text

I fixed the bug in `GenerationConfig.from_dict` (`src/transformers/generation/configuration_utils.py`). It was passing the same key twice to the constructor, once from `config_dict` and once from `kwargs`. It now merges the two dicts first, so the values you pass in override the saved ones:

```python
# kwargs take precedence over the values in `config_dict`, avoiding duplicate keyword arguments
config = cls(**{**config_dict, **kwargs})
```

I also replaced the old comment ("remove all the arguments that are in the config_dict"), since the code never did that.

**Checks:**
- Calling `GenerationConfig.from_dict({'num_beams': 2, 'max_length': 32}, num_beams=5, foo=1, return_unused_kwargs=True)` no longer raises. It gives `num_beams=5`, keeps `max_length=32`, and returns empty unused kwargs.
- `tests/generation/test_configuration_utils.py`: 4 passed, 2 skipped, 1 failed. The failure is `test_from_model_config`, which needs network access to the Hugging Face Hub and isn't available here. It fails the same way with my change removed, so the fix didn't cause it.

I tested `from_dict` directly rather than `from_pretrained`, but the error in the report comes from that same line.

### Turn 7 — assistant text

I fixed the crash: `GenerationConfig.from_pretrained(..., num_beams=...)` now works when the model's saved config already sets `num_beams`. The value you pass in wins over the saved one.

The cause was the one you spotted. In `src/transformers/generation/configuration_utils.py`, `from_dict` called `cls(**config_dict, **kwargs)`, so any key in both got passed twice. I merged the two dicts first, with your arguments taking precedence:

```python
config = cls(**{**config_dict, **kwargs})
```

I also replaced the misleading comment ("remove all the arguments that are in the config_dict").

**Checks:**
- `GenerationConfig.from_dict({'num_beams': 2, 'max_length': 32}, num_beams=5, foo=1, return_unused_kwargs=True)` gives `num_beams=5` and `max_length=32`, with no error.
- In `tests/generation/test_configuration_utils.py`, 4 tests passed, 2 were skipped and 1 failed. The failure is `test_from_model_config`. It errors out trying to reach the network, and it fails the same way with my change removed, so it isn't caused by this fix.

## Final answer

I fixed the crash: `GenerationConfig.from_pretrained(..., num_beams=...)` now works when the model's saved config already sets `num_beams`. The value you pass in wins over the saved one.

The cause was the one you spotted. In `src/transformers/generation/configuration_utils.py`, `from_dict` called `cls(**config_dict, **kwargs)`, so any key in both got passed twice. I merged the two dicts first, with your arguments taking precedence:

```python
config = cls(**{**config_dict, **kwargs})
```

I also replaced the misleading comment ("remove all the arguments that are in the config_dict").

**Checks:**
- `GenerationConfig.from_dict({'num_beams': 2, 'max_length': 32}, num_beams=5, foo=1, return_unused_kwargs=True)` gives `num_beams=5` and `max_length=32`, with no error.
- In `tests/generation/test_configuration_utils.py`, 4 tests passed, 2 were skipped and 1 failed. The failure is `test_from_model_config`. It errors out trying to reach the network, and it fails the same way with my change removed, so it isn't caused by this fix.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 92372 | 1660 | 84804 | 7552 | 94032 |
