# Instance: keras-team__keras-19844
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
Keras 3.0 load h5 model with Orthogonal initializer fails
Hi guys, 

I'm trying to load an h5 model that was working in earlier versions.

* This is a small part of the h5 file, where you can see (last part of the snippet) a recurrent initializer with a classname of **Orthogonal**.

```
{"name": "decoder_gru0", "class_name": "GRU", "config": {"name": "decoder_gru0", "trainable": true, "return_sequences": true, "return_state": false, "go_backwards": false, "stateful": false, "unroll": false, "implementation": 0, "units": 488, "activation": "tanh", "recurrent_activation": "hard_sigmoid", "use_bias": true, "kernel_initializer": {"class_name": "VarianceScaling", "config": {"scale": 1.0, "mode": "fan_avg", "distribution": "uniform", "seed": null}}, "recurrent_initializer": {"class_name": "Orthogonal", "config": {"gain": 1.0, "seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}
```


* The error returned is:


```bash
  File "..../keras/src/initializers/__init__.py", line 118, in get
    raise ValueError(
ValueError: Could not interpret initializer identifier: {'class_name': 'Orthogonal', 'config': {'gain': 1.0, 'seed': None}}
```

## Addition

I then added the Orthogonal initializer to the custom objects, and it seems to go further, but gets stuck here:

```bash
    raise ValueError(
ValueError: Unrecognized keyword arguments passed to GRU: {'implementation': 0}
```

Any ideas on how to fix this @mehtamansi29 ?
````

## Operational trajectory

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "cd /testbed && cat keras/src/initializers/__init__.py | head -80 && grep -n \"implementation\" keras/src/layers/rnn/gru.py keras/src/layers/rnn/lstm.py | head -30 && git log --oneline -2"
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
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed",
   "keras/src/initializers/__init__.py",
   "keras/src/layers/rnn/gru.py",
   "keras/src/layers/rnn/lstm.py"
  ],
  "command_sha256": [
   "fe4c3711d2b7721c0e0893a5d0eadbbc985d454b4681d3fe75f069ddcd700d94"
  ]
 },
 "_agent_context_projection": {
  "schema_version": "agent.exec_tool_result_receipt_preview.v1",
  "content_status": "partial_preview",
  "context_view_limit_bytes": 16384,
  "receipt": {
   "result_id": "tr_bdc1c77eae53419f8c107aa75bfddb56",
   "total_bytes": 6027,
   "total_lines": 104,
   "omitted_bytes": 0,
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "artifact": {
   "result_id": "tr_bdc1c77eae53419f8c107aa75bfddb56",
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "content_preview": "{\"tool_outcome\":{\"schema_version\":1,\"tool_name\":\"exec\",\"status\":\"success\",\"exit_code\":0,\"retr\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=5289; total_bytes=5475; context_view_limit=512 bytes; context_view_strategy=head_tail_compact; guidance=preview_not_failure_outcome_neutral]...\n.py\"],\"command_sha256\":[\"fe4c3711d2b7721c0e0893a5d0eadbbc985d454b4681d3fe75f069ddcd700d94\"]}}",
  "stdout": {
   "total_bytes": 4774,
   "total_lines": 104,
   "omitted_bytes": 0,
   "preview": "import inspect\n\nfrom keras.src.api_export import keras_export\nfrom keras.src.initializers.constant_initializers import Constant\nfrom keras.src.initializers.constant_initializers import Identity\nfrom keras.src.initializers.constant_initializers import Ones\nfrom keras.src.initializers.constant_initializers import Zeros\nfrom keras.src.initializers.initializer import Initializer\nfrom keras.src.initializers.random_initializers import GlorotNormal\nfrom keras.src.initializers.random_initializers import GlorotUniform\nfrom keras.src.initializers.random_initializers import HeNormal\nfrom keras.src.initializers.random_initializers import HeUniform\nfrom keras.src.initializers.random_initializers import LecunNormal\nfrom keras.src.initializers.random_initializers import LecunUniform\nfrom keras.src.initializers.random_initializers import OrthogonalInitializer\nfrom keras.src.initializers.random_initializers import RandomNormal\nfrom keras.src.initializers.random_initializers import RandomUniform\nfrom keras.src.initializers.random_initializers import TruncatedNormal\nfrom keras.src.initializers.random_initializers import VarianceScaling\nfrom keras.src.saving import serialization_lib\nfrom keras.src.utils.naming import to_snake_case\n\nALL_OBJECTS = {\n    Initializer,\n    Constant,\n    Identity,\n    Ones,\n    Zeros,\n    GlorotNormal,\n    GlorotUniform,\n    HeNormal,\n    HeUniform,\n    LecunNormal,\n    LecunUniform,\n    RandomNormal,\n    TruncatedNormal,\n    RandomUniform,\n    VarianceScaling,\n    OrthogonalInitializer,\n}\n\nALL_OBJECTS_DICT = {cls.__name__: cls for cls in ALL_OBJECTS}\nALL_OBJECTS_DICT.update(\n    {to_snake_case(cls.__name__): cls for cls in ALL_OBJECTS}\n)\n# Aliases\nALL_OBJECTS_DICT.update(\n    {\n        \"uniform\": RandomUniform,\n        \"normal\": RandomNormal,\n        \"orthogonal\": OrthogonalInitializer,\n        \"one\": Ones,\n        \"zero\": Zeros,\n    }\n)\n\n\n@keras_export(\"keras.initializers.serialize\")\ndef serialize(initializer):\n    \"\"\"Returns the initializer configuration as a Python dict.\"\"\"\n    return serialization_lib.serialize_keras_object(initializer)\n\n\n@keras_export(\"keras.initializers.deserialize\")\ndef deserialize(config, custom_objects=None):\n    \"\"\"Returns a Keras initializer object via its configuration.\"\"\"\n    return serialization_lib.deserialize_keras_object(\n        config,\n        module_objects=ALL_OBJECTS_DICT,\n        custom_objects=custom_objects,\n    )\n\n\n@keras_export(\"keras.initializers.get\")\ndef get(identifier):\n    \"\"\"Retrieves a Keras initializer object via an identifier.\n\n    The `identifier` may be the string name of a initializers function or class\n    (case-sensitively).\n\nkeras/src/layers/rnn/gru.py:112:        implementation = kwargs.pop(\"implementation\", 2)\nkeras/src/layers/rnn/gru.py:114:        self.implementation = implementation\nkeras/src/layers/rnn/gru.py:201:        if self.implementation == 1:\nkeras/src/layers/rnn/gru.py:335:    will choose different implementations (cuDNN-based or backend-native)\nkeras/src/layers/rnn/gru.py:338:    (see below for details), the layer will use a fast cuDNN implementation\nkeras/src/layers/rnn/gru.py:341:    The requirements to use the cuDNN implementation are:\nkeras/src/layers/rnn/gru.py:352:    There are two variants of the GRU implementation. The default one is based\nkeras/src/layers/rnn/gru.py:434:        use_cudnn: Whether to use a cuDNN-backed implementation. `\"auto\"` will\nkeras/src/layers/rnn/gru.py:436:            default implementation if not.\nkeras/src/layers/rnn/gru.py:553:                    # implementation of the inner GRU loop. In the case of\nkeras/src/layers/rnn/gru.py:582:                \"to a non-cuDNN implementation.\"\nkeras/src/layers/rnn/lstm.py:114:        implementation = kwargs.pop(\"implementation\", 2)\nkeras/src/layers/rnn/lstm.py:141:        self.implementation = implementation\nkeras/src/layers/rnn/lstm.py:239:        if self.implementation == 1:\nkeras/src/layers/rnn/lstm.py:323:    will choose different implementations (cuDNN-based or backend-native)\nkeras/src/layers/rnn/lstm.py:326:    (see below for details), the layer will use a fast cuDNN implementation\nkeras/src/layers/rnn/lstm.py:328:    The requirements to use the cuDNN implementation are:\nkeras/src/layers/rnn/lstm.py:415:        use_cudnn: Whether to use a cuDNN-backed implementation. `\"auto\"` will\nkeras/src/layers/rnn/lstm.py:417:            default implementation if not.\nkeras/src/layers/rnn/lstm.py:484:            implementation=kwargs.pop(\"implementation\", 2),\nkeras/src/layers/rnn/lstm.py:534:                    # implementation of the inner LSTM loop. In the case of\nkeras/src/layers/rnn/lstm.py:563:                \"to a non-cuDNN implementation.\"\n1c60668f6 Fix code style\na8aac9720 Make batch norm mask shape error more descriptive (#19829)\n"
  }
 }
}
````

### Turn 2 — thinking

````text
I'm checking whether "Orthogonal" needs to be added as an alias in the initializer dictionary, recalling how upstream Keras registers its object aliases.
````

### Turn 2 — tool call call_0002 (exec)

````json
{
 "command": "cd /testbed && sed -n 470,530p keras/src/layers/rnn/gru.py; sed -n 470,500p keras/src/layers/rnn/lstm.py"
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
 "stdout": "        dropout=0.0,\n        recurrent_dropout=0.0,\n        seed=None,\n        return_sequences=False,\n        return_state=False,\n        go_backwards=False,\n        stateful=False,\n        unroll=False,\n        reset_after=True,\n        use_cudnn=\"auto\",\n        **kwargs,\n    ):\n        cell = GRUCell(\n            units,\n            activation=activation,\n            recurrent_activation=recurrent_activation,\n            use_bias=use_bias,\n            kernel_initializer=kernel_initializer,\n            recurrent_initializer=recurrent_initializer,\n            bias_initializer=bias_initializer,\n            kernel_regularizer=kernel_regularizer,\n            recurrent_regularizer=recurrent_regularizer,\n            bias_regularizer=bias_regularizer,\n            kernel_constraint=kernel_constraint,\n            recurrent_constraint=recurrent_constraint,\n            bias_constraint=bias_constraint,\n            dropout=dropout,\n            recurrent_dropout=recurrent_dropout,\n            reset_after=reset_after,\n            dtype=kwargs.get(\"dtype\", None),\n            trainable=kwargs.get(\"trainable\", True),\n            name=\"gru_cell\",\n            seed=seed,\n        )\n        super().__init__(\n            cell,\n            return_sequences=return_sequences,\n            return_state=return_state,\n            go_backwards=go_backwards,\n            stateful=stateful,\n            unroll=unroll,\n            activity_regularizer=activity_regularizer,\n            **kwargs,\n        )\n        self.input_spec = InputSpec(ndim=3)\n        if use_cudnn not in (\"auto\", True, False):\n            raise ValueError(\n                \"Invalid valid received for argument `use_cudnn`. \"\n                \"Expected one of {'auto', True, False}. \"\n                f\"Received: use_cudnn={use_cudnn}\"\n            )\n        self.use_cudnn = use_cudnn\n        if (\n            backend.backend() == \"tensorflow\"\n            and backend.cudnn_ok(\n                cell.activation,\n                cell.recurrent_activation,\n                self.unroll,\n                cell.use_bias,\n                reset_after=reset_after,\n            )\n            recurrent_initializer=recurrent_initializer,\n            bias_initializer=bias_initializer,\n            kernel_regularizer=kernel_regularizer,\n            recurrent_regularizer=recurrent_regularizer,\n            bias_regularizer=bias_regularizer,\n            kernel_constraint=kernel_constraint,\n            recurrent_constraint=recurrent_constraint,\n            bias_constraint=bias_constraint,\n            dropout=dropout,\n            recurrent_dropout=recurrent_dropout,\n            dtype=kwargs.get(\"dtype\", None),\n            trainable=kwargs.get(\"trainable\", True),\n            name=\"lstm_cell\",\n            seed=seed,\n            implementation=kwargs.pop(\"implementation\", 2),\n        )\n        super().__init__(\n            cell,\n            return_sequences=return_sequences,\n            return_state=return_state,\n            go_backwards=go_backwards,\n            stateful=stateful,\n            unroll=unroll,\n            activity_regularizer=activity_regularizer,\n            **kwargs,\n        )\n        self.input_spec = InputSpec(ndim=3)\n        if use_cudnn not in (\"auto\", True, False):\n            raise ValueError(\n                \"Invalid valid received for argument `use_cudnn`. \"\n                \"Expected one of {'auto', True, False}. \"\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 45,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed",
   "keras/src/layers/rnn/gru.py",
   "keras/src/layers/rnn/lstm.py"
  ],
  "command_sha256": [
   "30628a464dcc573e3495ca93296a7b0c80abbba630589d0f3d7ab07cc427b346"
  ]
 }
}
````

### Turn 3 — thinking

````text
I should fix both the Orthogonal alias and the GRU implementation pass-through to the cell, confirming that implementation 0 just falls through to the same branch as implementation 2 in GRUCell, so that's fine. I also want to verify Keras's public API exports Orthogonal correctly, likely via an alias to OrthogonalInitializer.
````

### Turn 3 — tool call call_0003 (apply_patch)

````json
{
 "patch_text": "*** Begin Patch\n*** Update File: keras/src/initializers/__init__.py\n@@\n         \"orthogonal\": OrthogonalInitializer,\n+        \"Orthogonal\": OrthogonalInitializer,  # Legacy\n         \"one\": Ones,\n*** Update File: keras/src/layers/rnn/gru.py\n@@\n             name=\"gru_cell\",\n             seed=seed,\n+            implementation=kwargs.pop(\"implementation\", 2),\n         )\n*** End Patch"
}
````

Result:

````text
{
 "plan_id": "d47f290e0d09d71c70de41bcc811928f9c0c7e30fcc59c6fbce2d2fff1f7aaa5",
 "applied": true,
 "files_modified": [
  "keras/src/initializers/__init__.py",
  "keras/src/layers/rnn/gru.py"
 ],
 "conflicts": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "apply_patch",
    "paths": [
     "keras/src/initializers/__init__.py",
     "keras/src/layers/rnn/gru.py"
    ]
   }
  ]
 }
}
````

### Turn 4 — tool call call_0004 (exec)

````json
{
 "command": "cd /testbed && sed -n 100,116p keras/src/layers/rnn/gru.py"
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
 "stdout": "        bias_constraint=None,\n        dropout=0.0,\n        recurrent_dropout=0.0,\n        reset_after=True,\n        seed=None,\n        **kwargs,\n    ):\n        if units <= 0:\n            raise ValueError(\n                \"Received an invalid value for argument `units`, \"\n                f\"expected a positive integer, got {units}.\"\n            )\n        implementation = kwargs.pop(\"implementation\", 2)\n        super().__init__(**kwargs)\n        self.implementation = implementation\n        self.units = units\n        self.activation = activations.get(activation)\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 116,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed",
   "keras/src/layers/rnn/gru.py"
  ],
  "command_sha256": [
   "f2cb16e6a6b9ea4f5ff8ceaa52cb4e332cc4cef1b4a776dd6bfc88b5d06435ee"
  ]
 }
}
````

### Turn 5 — tool call call_0005 (exec)

````json
{
 "command": "cd /testbed && timeout 300 python -c \"\nfrom keras.src import initializers, layers\nprint(initializers.get({'class_name': 'Orthogonal', 'config': {'gain': 1.0, 'seed': None}}))\nl=layers.GRU(4, implementation=0, recurrent_initializer={'class_name': 'Orthogonal', 'config': {'gain': 1.0, 'seed': None}})\nimport numpy as np; print(l(np.ones((2,3,5))).shape)\n\" 2>&1 | tail -3 && timeout 600 python -m pytest -q keras/src/layers/rnn/gru_test.py keras/src/initializers 2>&1 | tail -3"
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
 "stdout": "2026-10-17 04:33:54.967667: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n<keras.src.initializers.random_initializers.OrthogonalInitializer object at 0x7b74884f1550>\n(2, 4)\nkeras/src/initializers/random_initializers_test.py::InitializersTest::test_variance_scaling_invalid_scale PASSED [100%]\n\n============================== 19 passed in 3.41s ==============================\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 12208,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed"
  ],
  "command_sha256": [
   "b40c8e26053347c1d31352554a1cab2789d6cbfd2c1a55ad0c8741787e6aa994"
  ]
 }
}
````

### Turn 6 — thinking

````text
Only 19 passed, which seems fine since gru_test was likely included. That's good enough.

I'm not sure the gru_test was actually covered in that run—the 19 passed might just reflect the initializers, so I should just report what I actually observed rather than assume more.
````

### Turn 6 — assistant text

I fixed both errors from the report. Old saved models that use the `Orthogonal` initializer name, and GRU layers saved with an `implementation` setting, now load in Keras 3.

- **Orthogonal initializer:** in `keras/src/initializers/__init__.py`, I added `"Orthogonal"` as another name for `OrthogonalInitializer`. Before, only `"orthogonal"` (lowercase) and `"OrthogonalInitializer"` were recognised, so the old config failed.
- **GRU `implementation` argument:** in `keras/src/layers/rnn/gru.py`, `GRU.__init__` now pops `implementation` (default 2) and passes it to `GRUCell`, the same way `LSTM` already does. Before, the argument was handed to the base layer, which rejected it. `implementation=0` from the old file now runs with the default behaviour.

**Checks:**
- Resolving `{'class_name': 'Orthogonal', 'config': {'gain': 1.0, 'seed': None}}` returns an `OrthogonalInitializer`.
- `GRU(4, implementation=0, recurrent_initializer=<that config>)` runs on a `(2, 3, 5)` input and gives output shape `(2, 4)`.
- The GRU and initializer tests ran with 19 passed.

I did not test with an actual `.h5` model file.

### Turn 7 — assistant text

I fixed both errors from the report, so an older h5 config with an `Orthogonal` initializer and a GRU `implementation` setting now loads.

- **Initializer error:** in `keras/src/initializers/__init__.py`, I added `"Orthogonal"` as another name for `OrthogonalInitializer`. Before, only `OrthogonalInitializer`, `orthogonal_initializer` and `orthogonal` were recognized, so the old `{"class_name": "Orthogonal", ...}` config was rejected.
- **GRU error:** in `keras/src/layers/rnn/gru.py`, `GRU.__init__` now takes `implementation` out of `kwargs` and passes it to `GRUCell`, which already accepts it. `LSTM` already did this. Before, the argument was passed on to the base layer, which raised "Unrecognized keyword arguments passed to GRU".

**Checks run:**
- I built a GRU with `implementation=0` and the issue's `Orthogonal` config. It now works and gives an output of shape `(2, 4)`.
- `initializers.get(...)` on that config now returns the initializer instead of raising.
- I ran `keras/src/layers/rnn/gru_test.py` and the initializer tests together: 19 passed. I only read the end of the output, so I didn't confirm the GRU tests were among them.

I didn't load an actual h5 model file.

## Final answer

I fixed both errors from the report, so an older h5 config with an `Orthogonal` initializer and a GRU `implementation` setting now loads.

- **Initializer error:** in `keras/src/initializers/__init__.py`, I added `"Orthogonal"` as another name for `OrthogonalInitializer`. Before, only `OrthogonalInitializer`, `orthogonal_initializer` and `orthogonal` were recognized, so the old `{"class_name": "Orthogonal", ...}` config was rejected.
- **GRU error:** in `keras/src/layers/rnn/gru.py`, `GRU.__init__` now takes `implementation` out of `kwargs` and passes it to `GRUCell`, which already accepts it. `LSTM` already did this. Before, the argument was passed on to the base layer, which raised "Unrecognized keyword arguments passed to GRU".

**Checks run:**
- I built a GRU with `implementation=0` and the issue's `Orthogonal` config. It now works and gives an output of shape `(2, 4)`.
- `initializers.get(...)` on that config now returns the initializer instead of raising.
- I ran `keras/src/layers/rnn/gru_test.py` and the initializer tests together: 19 passed. I only read the end of the output, so I didn't confirm the GRU tests were among them.

I didn't load an actual h5 model file.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 102301 | 2283 | 82156 | 20129 | 104584 |
