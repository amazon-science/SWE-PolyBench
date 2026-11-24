# Instance: keras-team__keras-19466
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: False

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
Numpy Ops function nonzero(x) appers to be missing check for symbolic tensors
In updating  code from Keras 2 to 3, we noticed that nonzero function continues to throw errors for use of KerasTensor in TF functions, even when run though tf.keras.ops

Digging into the source, it appears that this function does not receive the check for any_symbolic_tensors(), and thus no instantiation of the NonZero() class. In turn failing when used with a KerasTensor

https://github.com/keras-team/keras/blob/42a1535ed7d3d75711a11d295f58a2dc9a59fdae/keras/ops/numpy.py#L3976
````

## Operational trajectory

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "grep -n \"class Nonzero\\|class NonZero\" -A 25 keras/ops/numpy.py; grep -n \"^def nonzero\" -A 15 keras/ops/numpy.py"
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
 "stdout": "3991:class Nonzero(Operation):\n3992-    def call(self, x):\n3993-        return backend.numpy.nonzero(x)\n3994-\n3995-\n3996-@keras_export([\"keras.ops.nonzero\", \"keras.ops.numpy.nonzero\"])\n3997-def nonzero(x):\n3998-    \"\"\"Return the indices of the elements that are non-zero.\n3999-\n4000-    Args:\n4001-        x: Input tensor.\n4002-\n4003-    Returns:\n4004-        Indices of elements that are non-zero.\n4005-    \"\"\"\n4006-    return backend.numpy.nonzero(x)\n4007-\n4008-\n4009-class NotEqual(Operation):\n4010-    def call(self, x1, x2):\n4011-        return backend.numpy.not_equal(x1, x2)\n4012-\n4013-    def compute_output_spec(self, x1, x2):\n4014-        x1_shape = getattr(x1, \"shape\", [])\n4015-        x2_shape = getattr(x2, \"shape\", [])\n4016-        output_shape = broadcast_shapes(x1_shape, x2_shape)\n3997:def nonzero(x):\n3998-    \"\"\"Return the indices of the elements that are non-zero.\n3999-\n4000-    Args:\n4001-        x: Input tensor.\n4002-\n4003-    Returns:\n4004-        Indices of elements that are non-zero.\n4005-    \"\"\"\n4006-    return backend.numpy.nonzero(x)\n4007-\n4008-\n4009-class NotEqual(Operation):\n4010-    def call(self, x1, x2):\n4011-        return backend.numpy.not_equal(x1, x2)\n4012-\n",
 "device_targets": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "15",
   "25",
   "keras/ops/numpy.py"
  ],
  "command_sha256": [
   "02493af93e964c3f3d5b4563ddaefbc2c3d56020655cc4f8ee7ac9e00567cc63"
  ]
 },
 "duration_ms": 75
}
````

### Turn 2 — thinking

````text
I need to figure out the output spec for nonzero, which returns one array per dimension, and I'm checking what dtype each backend uses for these index arrays.
````

### Turn 2 — tool call call_0002 (exec)

````json
{
 "command": "grep -rn \"def nonzero\" -A 8 keras/backend/*/numpy.py"
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
 "stdout": "keras/backend/jax/numpy.py:772:def nonzero(x):\nkeras/backend/jax/numpy.py-773-    return jnp.nonzero(x)\nkeras/backend/jax/numpy.py-774-\nkeras/backend/jax/numpy.py-775-\nkeras/backend/jax/numpy.py-776-def not_equal(x1, x2):\nkeras/backend/jax/numpy.py-777-    x1 = convert_to_tensor(x1)\nkeras/backend/jax/numpy.py-778-    x2 = convert_to_tensor(x2)\nkeras/backend/jax/numpy.py-779-    return jnp.not_equal(x1, x2)\nkeras/backend/jax/numpy.py-780-\n--\nkeras/backend/numpy/numpy.py:699:def nonzero(x):\nkeras/backend/numpy/numpy.py-700-    return tuple(indices.astype(\"int32\") for indices in np.nonzero(x))\nkeras/backend/numpy/numpy.py-701-\nkeras/backend/numpy/numpy.py-702-\nkeras/backend/numpy/numpy.py-703-def not_equal(x1, x2):\nkeras/backend/numpy/numpy.py-704-    return np.not_equal(x1, x2)\nkeras/backend/numpy/numpy.py-705-\nkeras/backend/numpy/numpy.py-706-\nkeras/backend/numpy/numpy.py-707-def zeros_like(x, dtype=None):\n--\nkeras/backend/tensorflow/numpy.py:1402:def nonzero(x):\nkeras/backend/tensorflow/numpy.py-1403-    x = convert_to_tensor(x)\nkeras/backend/tensorflow/numpy.py-1404-    result = tf.unstack(tf.where(tf.cast(x, \"bool\")), x.shape.rank, axis=1)\nkeras/backend/tensorflow/numpy.py-1405-    return tree.map_structure(lambda indices: tf.cast(indices, \"int32\"), result)\nkeras/backend/tensorflow/numpy.py-1406-\nkeras/backend/tensorflow/numpy.py-1407-\nkeras/backend/tensorflow/numpy.py-1408-def not_equal(x1, x2):\nkeras/backend/tensorflow/numpy.py-1409-    x1 = convert_to_tensor(x1)\nkeras/backend/tensorflow/numpy.py-1410-    x2 = convert_to_tensor(x2)\n--\nkeras/backend/torch/numpy.py:996:def nonzero(x):\nkeras/backend/torch/numpy.py-997-    x = convert_to_tensor(x)\nkeras/backend/torch/numpy.py-998-    return tuple(cast(indices, \"int32\") for indices in torch.nonzero(x).T)\nkeras/backend/torch/numpy.py-999-\nkeras/backend/torch/numpy.py-1000-\nkeras/backend/torch/numpy.py-1001-def not_equal(x1, x2):\nkeras/backend/torch/numpy.py-1002-    x1, x2 = convert_to_tensor(x1), convert_to_tensor(x2)\nkeras/backend/torch/numpy.py-1003-    return torch.not_equal(x1, x2)\nkeras/backend/torch/numpy.py-1004-\n",
 "device_targets": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "8",
   "keras/backend/*/numpy.py"
  ],
  "command_sha256": [
   "07f3d050705ffc38f333aa2fcde601526d39f696fc513dd479c46af97869421a"
  ]
 },
 "duration_ms": 17
}
````

### Turn 3 — thinking

````text
I'm looking at how the Nonzero operation should produce its output spec — a tuple of int32 tensors with unknown shape matching the input's rank, matching what upstream Keras does.
````

### Turn 3 — tool call call_0003 (apply_patch)

````json
{
 "patch_text": "*** Begin Patch\n*** Update File: keras/ops/numpy.py\n@@\n class Nonzero(Operation):\n     def call(self, x):\n         return backend.numpy.nonzero(x)\n \n+    def compute_output_spec(self, x):\n+        return tuple(\n+            [KerasTensor((None,), dtype=\"int32\") for _ in range(len(x.shape))]\n+        )\n+\n \n@@\n         Indices of elements that are non-zero.\n     \"\"\"\n+    if any_symbolic_tensors((x,)):\n+        return Nonzero().symbolic_call(x)\n     return backend.numpy.nonzero(x)\n*** End Patch"
}
````

Result:

````text
{
 "plan_id": "4f31e5def24852daa6c672d029138104c912fc75e03185e10633213eb281516a",
 "applied": true,
 "files_modified": [
  "keras/ops/numpy.py"
 ],
 "conflicts": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "apply_patch",
    "paths": [
     "keras/ops/numpy.py"
    ]
   }
  ]
 }
}
````

### Turn 4 — tool call call_0004 (exec)

````json
{
 "command": "cd /testbed && python -c \"\nfrom keras import ops, KerasTensor\nimport numpy as np\nprint(ops.nonzero(KerasTensor((None,3,4))))\nprint(ops.nonzero(np.array([[0,1],[2,0]])))\n\" 2>&1 | tail -5; python -m pytest -q keras/ops/numpy_test.py -k \"nonzero or Nonzero\" 2>&1 | tail -3"
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
 "stdout": "2026-10-17 02:26:28.535701: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.\nTo enable the following instructions: AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.\n2026-10-17 02:26:31.875815: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n(<KerasTensor shape=(None,), dtype=int32, sparse=False, name=keras_tensor_1>, <KerasTensor shape=(None,), dtype=int32, sparse=False, name=keras_tensor_2>, <KerasTensor shape=(None,), dtype=int32, sparse=False, name=keras_tensor_3>)\n[<tf.Tensor: shape=(2,), dtype=int32, numpy=array([0, 1], dtype=int32)>, <tf.Tensor: shape=(2,), dtype=int32, numpy=array([1, 0], dtype=int32)>]\nkeras/ops/numpy_test.py::NumpyDtypeTest::test_nonzero_uint8 PASSED       [100%]\n\n===================== 30 passed, 5439 deselected in 2.78s ======================\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 13822,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed"
  ],
  "command_sha256": [
   "6654281668d282c961610119836961627ceb122e0c2e35b667ebf917854c4157"
  ]
 }
}
````

### Turn 5 — assistant text

I fixed it: `keras.ops.nonzero` now accepts symbolic `KerasTensor` inputs instead of handing them straight to the backend.

The change is in `keras/ops/numpy.py`:
- **`nonzero(x)`**: added the missing `any_symbolic_tensors((x,))` check. For symbolic input it now returns `Nonzero().symbolic_call(x)`.
- **`Nonzero`**: added a `compute_output_spec` method. It returns one `KerasTensor` per dimension of the input, each with shape `(None,)` and dtype `int32`. That matches what the backends return.

**Checks:**
- `ops.nonzero(KerasTensor((None, 3, 4)))` now returns three symbolic tensors with shape `(None,)` and dtype `int32`.
- A concrete NumPy input still gives the right indices.
- The nonzero tests in `keras/ops/numpy_test.py` pass (30 passed). They ran only on the TensorFlow backend; I didn't test JAX, PyTorch or NumPy.

### Turn 6 — assistant text

I fixed `keras.ops.nonzero` so it now accepts symbolic `KerasTensor` inputs instead of failing.

The change is in `keras/ops/numpy.py`:
- **The function:** `nonzero(x)` now checks `any_symbolic_tensors((x,))`. When the input is symbolic, it calls `Nonzero().symbolic_call(x)` instead of passing the tensor straight to the backend.
- **The `Nonzero` class:** I added `compute_output_spec`. It returns one `KerasTensor` per input dimension, each with shape `(None,)` and dtype `int32`. That matches what the backends return.

I checked it on the TensorFlow backend:
- `ops.nonzero(KerasTensor((None, 3, 4)))` now returns 3 symbolic `KerasTensor`s, each with shape `(None,)` and dtype `int32`.
- A plain NumPy input still gives the same concrete result as before.
- The existing nonzero tests in `keras/ops/numpy_test.py` pass (30 tests).

I didn't run the tests on the JAX, Torch or NumPy backends.

## Final answer

I fixed `keras.ops.nonzero` so it now accepts symbolic `KerasTensor` inputs instead of failing.

The change is in `keras/ops/numpy.py`:
- **The function:** `nonzero(x)` now checks `any_symbolic_tensors((x,))`. When the input is symbolic, it calls `Nonzero().symbolic_call(x)` instead of passing the tensor straight to the backend.
- **The `Nonzero` class:** I added `compute_output_spec`. It returns one `KerasTensor` per input dimension, each with shape `(None,)` and dtype `int32`. That matches what the backends return.

I checked it on the TensorFlow backend:
- `ops.nonzero(KerasTensor((None, 3, 4)))` now returns 3 symbolic `KerasTensor`s, each with shape `(None,)` and dtype `int32`.
- A plain NumPy input still gives the same concrete result as before.
- The existing nonzero tests in `keras/ops/numpy_test.py` pass (30 tests).

I didn't run the tests on the JAX, Torch or NumPy backends.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 71727 | 1686 | 52144 | 19569 | 73413 |
