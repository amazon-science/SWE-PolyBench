# Instance: huggingface__transformers-30602
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
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
````

## Operational trajectory

### Turn 1 — tool call call_0001 (rg)

````json
{
 "pattern": "does not appear to have a file named",
 "path": "src/transformers/modeling_utils.py",
 "context": 4
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "does not appear to have a file named",
 "search_path": "/testbed/src/transformers/modeling_utils.py",
 "matches": [
  {
   "path": "modeling_utils.py",
   "line_number": 3332,
   "line": "                                    f\"{pretrained_model_name_or_path} does not appear to have a file named\"",
   "context_before": [
    "                                )",
    "                            cached_file_kwargs[\"revision\"] = revision",
    "                            if resolved_archive_file is None:",
    "                                raise EnvironmentError("
   ],
   "context_after": [
    "                                    f\" {_add_variant(SAFE_WEIGHTS_NAME, variant)} or {_add_variant(SAFE_WEIGHTS_INDEX_NAME, variant)} \"",
    "                                    \"and thus cannot be loaded with `safetensors`. Please make sure that the model has \"",
    "                                    \"been saved with `safe_serialization=True` or do not set `use_safetensors=True`.\"",
    "                                )"
   ]
  },
  {
   "path": "modeling_utils.py",
   "line_number": 3392,
   "line": "                                f\"{pretrained_model_name_or_path} does not appear to have a file named\"",
   "context_before": [
    "                            \"token\": token,",
    "                        }",
    "                        if has_file(pretrained_model_name_or_path, TF2_WEIGHTS_NAME, **has_file_kwargs):",
    "                            raise EnvironmentError("
   ],
   "context_after": [
    "                                f\" {_add_variant(WEIGHTS_NAME, variant)} but there is a file for TensorFlow weights.\"",
    "                                \" Use `from_tf=True` to load this model from those weights.\"",
    "                            )",
    "                        elif has_file(pretrained_model_name_or_path, FLAX_WEIGHTS_NAME, **has_file_kwargs):"
   ]
  },
  {
   "path": "modeling_utils.py",
   "line_number": 3398,
   "line": "                                f\"{pretrained_model_name_or_path} does not appear to have a file named\"",
   "context_before": [
    "                                \" Use `from_tf=True` to load this model from those weights.\"",
    "                            )",
    "                        elif has_file(pretrained_model_name_or_path, FLAX_WEIGHTS_NAME, **has_file_kwargs):",
    "                            raise EnvironmentError("
   ],
   "context_after": [
    "                                f\" {_add_variant(WEIGHTS_NAME, variant)} but there is a file for Flax weights. Use\"",
    "                                \" `from_flax=True` to load this model from those weights.\"",
    "                            )",
    "                        elif variant is not None and has_file("
   ]
  },
  {
   "path": "modeling_utils.py",
   "line_number": 3406,
   "line": "                                f\"{pretrained_model_name_or_path} does not appear to have a file named\"",
   "context_before": [
    "                        elif variant is not None and has_file(",
    "                            pretrained_model_name_or_path, WEIGHTS_NAME, **has_file_kwargs",
    "                        ):",
    "                            raise EnvironmentError("
   ],
   "context_after": [
    "                                f\" {_add_variant(WEIGHTS_NAME, variant)} but there is a file without the variant\"",
    "                                f\" {variant}. Use `variant=None` to load this model from those weights.\"",
    "                            )",
    "                        else:"
   ]
  },
  {
   "path": "modeling_utils.py",
   "line_number": 3412,
   "line": "                                f\"{pretrained_model_name_or_path} does not appear to have a file named\"",
   "context_before": [
    "                                f\" {variant}. Use `variant=None` to load this model from those weights.\"",
    "                            )",
    "                        else:",
    "                            raise EnvironmentError("
   ],
   "context_after": [
    "                                f\" {_add_variant(WEIGHTS_NAME, variant)}, {TF2_WEIGHTS_NAME}, {TF_WEIGHTS_NAME} or\"",
    "                                f\" {FLAX_WEIGHTS_NAME}.\"",
    "                            )",
    "                except EnvironmentError:"
   ]
  }
 ],
 "stats": {
  "files_searched": 1,
  "files_with_matches": 1,
  "matches_found": 5,
  "matches_returned": 5,
  "denied_skips": 0,
  "duration_ms": 6,
  "timing": {
   "walk_ms": 0,
   "search_ms": 4,
   "collect_ms": 1,
   "total_ms": 6
  }
 },
 "truncated": false
}
````

### Turn 2 — thinking

````text
I should also check the local directory case, so let me look around line 3270 for that error handling.
````

### Turn 2 — tool call call_0002 (rg)

````json
{
 "context": 3,
 "path": "src/transformers/modeling_utils.py",
 "pattern": "Error no file named"
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "Error no file named",
 "search_path": "/testbed/src/transformers/modeling_utils.py",
 "matches": [
  {
   "path": "modeling_utils.py",
   "line_number": 3249,
   "line": "                        f\"Error no file named {_add_variant(WEIGHTS_NAME, variant)} found in directory\"",
   "context_before": [
    "                    os.path.join(pretrained_model_name_or_path, subfolder, TF_WEIGHTS_NAME + \".index\")",
    "                ) or os.path.isfile(os.path.join(pretrained_model_name_or_path, subfolder, TF2_WEIGHTS_NAME)):",
    "                    raise EnvironmentError("
   ],
   "context_after": [
    "                        f\" {pretrained_model_name_or_path} but there is a file for TensorFlow weights. Use\"",
    "                        \" `from_tf=True` to load this model from those weights.\"",
    "                    )"
   ]
  },
  {
   "path": "modeling_utils.py",
   "line_number": 3255,
   "line": "                        f\"Error no file named {_add_variant(WEIGHTS_NAME, variant)} found in directory\"",
   "context_before": [
    "                    )",
    "                elif os.path.isfile(os.path.join(pretrained_model_name_or_path, subfolder, FLAX_WEIGHTS_NAME)):",
    "                    raise EnvironmentError("
   ],
   "context_after": [
    "                        f\" {pretrained_model_name_or_path} but there is a file for Flax weights. Use `from_flax=True`\"",
    "                        \" to load this model from those weights.\"",
    "                    )"
   ]
  },
  {
   "path": "modeling_utils.py",
   "line_number": 3261,
   "line": "                        f\"Error no file named {_add_variant(SAFE_WEIGHTS_NAME, variant)} found in directory\"",
   "context_before": [
    "                    )",
    "                elif use_safetensors:",
    "                    raise EnvironmentError("
   ],
   "context_after": [
    "                        f\" {pretrained_model_name_or_path}.\"",
    "                    )",
    "                else:"
   ]
  },
  {
   "path": "modeling_utils.py",
   "line_number": 3266,
   "line": "                        f\"Error no file named {_add_variant(WEIGHTS_NAME, variant)}, {TF2_WEIGHTS_NAME},\"",
   "context_before": [
    "                    )",
    "                else:",
    "                    raise EnvironmentError("
   ],
   "context_after": [
    "                        f\" {TF_WEIGHTS_NAME + '.index'} or {FLAX_WEIGHTS_NAME} found in directory\"",
    "                        f\" {pretrained_model_name_or_path}.\"",
    "                    )"
   ]
  }
 ],
 "stats": {
  "files_searched": 1,
  "files_with_matches": 1,
  "matches_found": 4,
  "matches_returned": 4,
  "denied_skips": 0,
  "duration_ms": 3,
  "timing": {
   "walk_ms": 0,
   "search_ms": 1,
   "collect_ms": 1,
   "total_ms": 3
  }
 },
 "truncated": false
}
````

### Turn 3 — thinking

````text
I'm recalling how upstream transformers formats its error message listing the possible weight filenames when none are found in the local directory.

The hub-based loading error message is phrased similarly but slightly differently, mentioning the model path doesn't appear to have those files. I should check the actual tests to see if they assert on exact wording.
````

### Turn 3 — tool call call_0003 (rg)

````json
{
 "path": "tests",
 "pattern": "does not appear to have a file named|Error no file named"
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "does not appear to have a file named|Error no file named",
 "search_path": "/testbed/tests",
 "matches": [
  {
   "path": "models/auto/test_configuration_auto.py",
   "line_number": 110,
   "line": "            \"hf-internal-testing/no-config-test-repo does not appear to have a file named config.json.\","
  },
  {
   "path": "models/auto/test_feature_extraction_auto.py",
   "line_number": 98,
   "line": "            \"hf-internal-testing/config-no-model does not appear to have a file named preprocessor_config.json.\","
  },
  {
   "path": "models/auto/test_image_processing_auto.py",
   "line_number": 132,
   "line": "            \"hf-internal-testing/config-no-model does not appear to have a file named preprocessor_config.json.\","
  },
  {
   "path": "models/auto/test_modeling_auto.py",
   "line_number": 486,
   "line": "            \"hf-internal-testing/config-no-model does not appear to have a file named pytorch_model.bin\","
  },
  {
   "path": "models/auto/test_modeling_flax_auto.py",
   "line_number": 96,
   "line": "            \"hf-internal-testing/config-no-model does not appear to have a file named flax_model.msgpack\","
  },
  {
   "path": "models/auto/test_modeling_tf_auto.py",
   "line_number": 287,
   "line": "            \"hf-internal-testing/config-no-model does not appear to have a file named pytorch_model.bin\","
  },
  {
   "path": "test_modeling_utils.py",
   "line_number": 976,
   "line": "        self.assertTrue(\"does not appear to have a file named pytorch_model.bin\" in str(env_error.exception))"
  },
  {
   "path": "utils/test_hub_utils.py",
   "line_number": 71,
   "line": "        with self.assertRaisesRegex(EnvironmentError, \"does not appear to have a file named\"):"
  },
  {
   "path": "utils/test_hub_utils.py",
   "line_number": 75,
   "line": "        with self.assertRaisesRegex(EnvironmentError, \"does not appear to have a file named\"):"
  }
 ],
 "stats": {
  "files_searched": 1025,
  "files_with_matches": 8,
  "matches_found": 9,
  "matches_returned": 9,
  "denied_skips": 0,
  "duration_ms": 267,
  "timing": {
   "walk_ms": 0,
   "search_ms": 266,
   "collect_ms": 1,
   "total_ms": 267
  }
 },
 "truncated": false
}
````

### Turn 4 — thinking

````text
The upstream fix in PR #30544 reorders the error message to list pytorch_model.bin and model.safetensors variants before the TF2 weights name, so I should match that order and update the test expectation accordingly.
````

### Turn 4 — tool call call_0004 (read)

````json
{
 "file_path": "src/transformers/modeling_utils.py",
 "offset": 3264,
 "limit": 6
}
````

Result:

````text
{
 "type": "file",
 "path": "src/transformers/modeling_utils.py",
 "full_read": false,
 "output": "src/transformers/modeling_utils.py\n\n3264:                 else:\n3265:                     raise EnvironmentError(\n3266:                         f\"Error no file named {_add_variant(WEIGHTS_NAME, variant)}, {TF2_WEIGHTS_NAME},\"\n3267:                         f\" {TF_WEIGHTS_NAME + '.index'} or {FLAX_WEIGHTS_NAME} found in directory\"\n3268:                         f\" {pretrained_model_name_or_path}.\"\n3269:                     )\n\n(Returned 6 lines starting at 3264; observed at least 3270 total lines; output truncated at the 102400 byte read window — continue with offset=3270)",
 "offset": 3264,
 "limit": 6,
 "lines_returned": 6,
 "total_lines": null,
 "observed_lines": 3270,
 "total_lines_lower_bound": 3270,
 "total_lines_exact": false,
 "truncated": true,
 "next_offset": 3270,
 "window_bytes_limit": 102400,
 "size_bytes": 238511
}
````

### Turn 5 — tool call call_0005 (read)

````json
{
 "file_path": "src/transformers/modeling_utils.py",
 "offset": 3410,
 "limit": 5
}
````

Result:

````text
{
 "type": "file",
 "path": "src/transformers/modeling_utils.py",
 "full_read": false,
 "output": "src/transformers/modeling_utils.py\n\n3410:                         else:\n3411:                             raise EnvironmentError(\n3412:                                 f\"{pretrained_model_name_or_path} does not appear to have a file named\"\n3413:                                 f\" {_add_variant(WEIGHTS_NAME, variant)}, {TF2_WEIGHTS_NAME}, {TF_WEIGHTS_NAME} or\"\n3414:                                 f\" {FLAX_WEIGHTS_NAME}.\"\n\n(Returned 5 lines starting at 3410; observed at least 3415 total lines; output truncated at the 102400 byte read window — continue with offset=3415)",
 "offset": 3410,
 "limit": 5,
 "lines_returned": 5,
 "total_lines": null,
 "observed_lines": 3415,
 "total_lines_lower_bound": 3415,
 "total_lines_exact": false,
 "truncated": true,
 "next_offset": 3415,
 "window_bytes_limit": 102400,
 "size_bytes": 238511
}
````

### Turn 6 — tool call call_0006 (apply_patch)

````json
{
 "patch_text": "*** Begin Patch\n*** Update File: src/transformers/modeling_utils.py\n@@\n                     raise EnvironmentError(\n-                        f\"Error no file named {_add_variant(WEIGHTS_NAME, variant)}, {TF2_WEIGHTS_NAME},\"\n-                        f\" {TF_WEIGHTS_NAME + '.index'} or {FLAX_WEIGHTS_NAME} found in directory\"\n+                        f\"Error no file named {_add_variant(WEIGHTS_NAME, variant)}, {_add_variant(SAFE_WEIGHTS_NAME, variant)},\"\n+                        f\" {TF2_WEIGHTS_NAME}, {TF_WEIGHTS_NAME + '.index'} or {FLAX_WEIGHTS_NAME} found in directory\"\n                         f\" {pretrained_model_name_or_path}.\"\n                     )\n@@\n                                 f\"{pretrained_model_name_or_path} does not appear to have a file named\"\n-                                f\" {_add_variant(WEIGHTS_NAME, variant)}, {TF2_WEIGHTS_NAME}, {TF_WEIGHTS_NAME} or\"\n-                                f\" {FLAX_WEIGHTS_NAME}.\"\n+                                f\" {_add_variant(WEIGHTS_NAME, variant)}, {_add_variant(SAFE_WEIGHTS_NAME, variant)},\"\n+                                f\" {TF2_WEIGHTS_NAME}, {TF_WEIGHTS_NAME} or {FLAX_WEIGHTS_NAME}.\"\n                             )\n*** End Patch"
}
````

Result:

````text
{
 "plan_id": "278067cefee617f6c5d59ecbc1579b4ef67bd7bffe739a42b7ca18de1e26be92",
 "applied": true,
 "files_modified": [
  "src/transformers/modeling_utils.py"
 ],
 "conflicts": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "apply_patch",
    "paths": [
     "src/transformers/modeling_utils.py"
    ]
   }
  ]
 }
}
````

### Turn 7 — assistant text

Quick smoke check on the local-directory path:

### Turn 7 — tool call call_0007 (exec)

````json
{
 "command": "cd /tmp && rm -rf smk && mkdir smk && python -c \"\nfrom transformers import BertConfig, BertModel\nBertConfig(hidden_size=32,num_hidden_layers=1,num_attention_heads=2,intermediate_size=37).save_pretrained('smk')\ntry: BertModel.from_pretrained('smk')\nexcept EnvironmentError as e: print(e)\n\"; rm -rf smk",
 "timeout_secs": 120
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
 "stdout": "Error no file named pytorch_model.bin, model.safetensors, tf_model.h5, model.ckpt.index or flax_model.msgpack found in directory smk.\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 3675,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "write",
    "paths": [
     "smk"
    ]
   }
  ],
  "reads": [
   "/tmp"
  ],
  "command_sha256": [
   "9a29f95544269336d60d542a38d15c6c0920882b80ffa987b8070dd580bb86b8"
  ]
 }
}
````

### Turn 8 — thinking

````text
I should double check the line length against the 119-character limit, since that indented f-string line might run over.
````

### Turn 8 — tool call call_0008 (exec)

````json
{
 "command": "cd /testbed && (ruff check src/transformers/modeling_utils.py && ruff format --check src/transformers/modeling_utils.py) 2>&1 | tail -5"
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
 "stdout": "1 file left unchanged\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 572,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed"
  ],
  "command_sha256": [
   "971016e99e7e0d986610f03e1e391c87a5595360a00f1ab15f9de74be70b6b50"
  ]
 }
}
````

### Turn 9 — thinking

````text
That looks complete.
````

### Turn 9 — assistant text

I fixed the error message: when `use_safetensors` isn't set, it now lists `model.safetensors` among the expected weight files. The change is in two `else` branches in `src/transformers/modeling_utils.py`:

- **Local directory** now says: `Error no file named pytorch_model.bin, model.safetensors, tf_model.h5, model.ckpt.index or flax_model.msgpack found in directory ...`
- **Hub repo** now says: `... does not appear to have a file named pytorch_model.bin, model.safetensors, tf_model.h5, model.ckpt or flax_model.msgpack.`

The safetensors filename gets the same `variant` suffix as `pytorch_model.bin`. I didn't touch the `use_safetensors=True` branch, which already had its own safetensors-specific message.

I checked the local-directory case by loading a `BertModel` from a folder that has only a config, and got the new message shown above. `ruff check` and `ruff format --check` pass on the file. I didn't run the Hub-repo case, since it needs network access, or the test suite.

The existing tests still pass with the new message, because they look for `does not appear to have a file named pytorch_model.bin` as a substring and the message still starts that way.

### Turn 10 — assistant text

I fixed the error message: when no model file is found and `use_safetensors` isn't set, it now lists `model.safetensors` along with the other supported file names.

There were two error branches that left it out, both in `src/transformers/modeling_utils.py`. In each one I added `{_add_variant(SAFE_WEIGHTS_NAME, variant)}` to the list:

- **Hub repo:** the message now reads `<repo> does not appear to have a file named pytorch_model.bin, model.safetensors, tf_model.h5, model.ckpt or flax_model.msgpack.`
- **Local directory:** the message now reads `Error no file named pytorch_model.bin, model.safetensors, tf_model.h5, model.ckpt.index or flax_model.msgpack found in directory <dir>.`

The new name comes right after `pytorch_model.bin`, so tests that check for the `... file named pytorch_model.bin` prefix still match.

**Checks run:**
- Loading a model from a local directory with only a config file produced the new local-directory message shown above.
- `ruff check` and `ruff format --check` pass on the file.

I didn't run the hub-repo case (it needs network access) or the existing test suite.

## Final answer

I fixed the error message: when no model file is found and `use_safetensors` isn't set, it now lists `model.safetensors` along with the other supported file names.

There were two error branches that left it out, both in `src/transformers/modeling_utils.py`. In each one I added `{_add_variant(SAFE_WEIGHTS_NAME, variant)}` to the list:

- **Hub repo:** the message now reads `<repo> does not appear to have a file named pytorch_model.bin, model.safetensors, tf_model.h5, model.ckpt or flax_model.msgpack.`
- **Local directory:** the message now reads `Error no file named pytorch_model.bin, model.safetensors, tf_model.h5, model.ckpt.index or flax_model.msgpack found in directory <dir>.`

The new name comes right after `pytorch_model.bin`, so tests that check for the `... file named pytorch_model.bin` prefix still match.

**Checks run:**
- Loading a model from a local directory with only a config file produced the new local-directory message shown above.
- `ruff check` and `ruff format --check` pass on the file.

I didn't run the hub-repo case (it needs network access) or the existing test suite.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 157751 | 2808 | 135996 | 21733 | 160559 |
