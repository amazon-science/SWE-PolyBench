# Instance: keras-team__keras-19973
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: False

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
Inconsistent assertion in keras.layers.MultiHeadAttention
I've noticed that depending on what is fed as the key, query and value to the keras.layers.MultiHeadAttention the assertion query_shape==value_shape is only _sometimes_ activated.

Minimal working example (no assertion error):
```
`import os`
`os.environ["KERAS_BACKEND"] = "torch"`
`import torch  # ==2.3.0`
`import keras  # ==3.3.0`

`batch_size = 32`
`seq_len = 256`
`key_dim = 16`
`value_dim = 8`
`num_heads = 8`

`query = torch.randn(batch_size, seq_len, key_dim)`
`key = torch.randn(batch_size, seq_len, key_dim)`
`value = torch.randn(batch_size, seq_len, value_dim)`

`mha = keras.layers.MultiHeadAttention(num_heads=num_heads, key_dim=key_dim//num_heads)`
`attn_out = mha(query=query, value=value, key=key)`

In contrast, I've tried the same procedure with keras tensors instead (assertion error):
`query = keras.Input(shape=(seq_len, key_dim))`
`key = keras.Input(shape=(seq_len, key_dim))`
`value = keras.Input(shape=(seq_len, value_dim))`

`mha = keras.layers.MultiHeadAttention(num_heads=num_heads, key_dim=key_dim//num_heads)`
`attn_out = mha(query=query, value=value, key=key)`
```

which yields:
_The last dimension of `query_shape` and `value_shape` must be equal, but are 16, 8. Received: query_shape={query_shape}, value_shape={value_shape}_

I realise that the former has a static batch shape of 32 while the latter a dynamic one, is that where the problem lies? 
Or perhaps the former uses the torch version of [MultiHeadAttention ](https://keras.io/api/layers/attention_layers/multi_head_attention/)in which, according to to this [issue](https://github.com/pytorch/pytorch/pull/39402), the assertion has been removed?
````

## Operational trajectory

### Turn 1 — tool call call_0001 (rg)

````json
{
 "pattern": "must be equal",
 "path": "keras/src/layers/attention/multi_head_attention.py",
 "context": 25
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "must be equal",
 "search_path": "/testbed/keras/src/layers/attention/multi_head_attention.py",
 "matches": [
  {
   "path": "multi_head_attention.py",
   "line_number": 595,
   "line": "                f\"must be equal, but are {query_shape[-1]}, {value_shape[-1]}. \"",
   "context_before": [
    "        \"\"\"",
    "        q_seq_length = ops.shape(query)[1]",
    "        v_seq_length = q_seq_length if value is None else ops.shape(value)[1]",
    "        ones_mask = ops.ones((1, q_seq_length, v_seq_length), dtype=\"int32\")",
    "        row_index = ops.cumsum(ones_mask, axis=-2)",
    "        col_index = ops.cumsum(ones_mask, axis=-1)",
    "        return ops.greater_equal(row_index, col_index)",
    "",
    "    def compute_output_shape(",
    "        self,",
    "        query_shape,",
    "        value_shape,",
    "        key_shape=None,",
    "    ):",
    "        if key_shape is None:",
    "            key_shape = value_shape",
    "",
    "        if query_shape[-1] != value_shape[-1]:",
    "            raise ValueError(",
    "                \"The last dimension of `query_shape` and `value_shape` \""
   ],
   "context_after": [
    "                \"Received: query_shape={query_shape}, value_shape={value_shape}\"",
    "            )",
    "",
    "        if value_shape[1:-1] != key_shape[1:-1]:",
    "            raise ValueError(",
    "                \"All dimensions of `value` and `key`, except the last one, \"",
    "                f\"must be equal. Received: value_shape={value_shape} and \"",
    "                f\"key_shape={key_shape}\"",
    "            )",
    "",
    "        if self._output_shape:",
    "            return query_shape[:-1] + self._output_shape",
    "",
    "        return query_shape",
    "",
    "    def compute_output_spec(",
    "        self,",
    "        query,",
    "        value,",
    "        key=None,"
   ]
  },
  {
   "path": "multi_head_attention.py",
   "line_number": 602,
   "line": "                f\"must be equal. Received: value_shape={value_shape} and \"",
   "context_before": [
    "",
    "    def compute_output_shape(",
    "        self,",
    "        query_shape,",
    "        value_shape,",
    "        key_shape=None,",
    "    ):",
    "        if key_shape is None:",
    "            key_shape = value_shape",
    "",
    "        if query_shape[-1] != value_shape[-1]:",
    "            raise ValueError(",
    "                \"The last dimension of `query_shape` and `value_shape` \"",
    "                f\"must be equal, but are {query_shape[-1]}, {value_shape[-1]}. \"",
    "                \"Received: query_shape={query_shape}, value_shape={value_shape}\"",
    "            )",
    "",
    "        if value_shape[1:-1] != key_shape[1:-1]:",
    "            raise ValueError(",
    "                \"All dimensions of `value` and `key`, except the last one, \""
   ],
   "context_after": [
    "                f\"key_shape={key_shape}\"",
    "            )",
    "",
    "        if self._output_shape:",
    "            return query_shape[:-1] + self._output_shape",
    "",
    "        return query_shape",
    "",
    "    def compute_output_spec(",
    "        self,",
    "        query,",
    "        value,",
    "        key=None,",
    "        query_mask=None,",
    "        value_mask=None,",
    "        key_mask=None,",
    "        attention_mask=None,",
    "        return_attention_scores=False,",
    "        training=None,",
    "        use_causal_mask=False,"
   ]
  }
 ],
 "stats": {
  "files_searched": 1,
  "files_with_matches": 1,
  "matches_found": 2,
  "matches_returned": 2,
  "denied_skips": 0,
  "duration_ms": 8,
  "timing": {
   "walk_ms": 0,
   "search_ms": 7,
   "collect_ms": 0,
   "total_ms": 8
  }
 },
 "truncated": false
}
````

### Turn 2 — thinking

````text
Since the output dense layer projects back to query_shape[-1], the output's last dimension actually matches the query's, so that check seems incorrect and should be removed. I want to check the existing tests first to see if any expect this error before changing anything.
````

### Turn 2 — tool call call_0002 (rg)

````json
{
 "path": "keras/src/layers/attention/multi_head_attention_test.py",
 "pattern": "compute_output_shape|ValueError|must be equal",
 "context": 8
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "compute_output_shape|ValueError|must be equal",
 "search_path": "/testbed/keras/src/layers/attention/multi_head_attention_test.py",
 "matches": [
  {
   "path": "multi_head_attention_test.py",
   "line_number": 108,
   "line": "    def test_compute_output_shape(",
   "context_before": [
    "        (",
    "            \"high_dim_different_proj\",",
    "            (4, 2, 3, 8),",
    "            (1, 1, 5, 8),",
    "            (1, 1, 5, 2),",
    "            (3, 2),",
    "        ),",
    "    )"
   ],
   "context_after": [
    "        self, query_dims, value_dims, key_dims, output_shape",
    "    ):",
    "        \"\"\"Test computed shape is equal to the layer output's shape.\"\"\"",
    "        layer = layers.MultiHeadAttention(",
    "            num_heads=2,",
    "            key_dim=2,",
    "            value_dim=2,",
    "            output_shape=output_shape,"
   ]
  },
  {
   "path": "multi_head_attention_test.py",
   "line_number": 127,
   "line": "        comp_output_shape = layer.compute_output_shape(",
   "context_before": [
    "        query_shape = (batch_size,) + query_dims",
    "        value_shape = (batch_size,) + value_dims",
    "        key_shape = (batch_size,) + key_dims if key_dims else None",
    "",
    "        query = np.ones(query_shape)",
    "        value = np.ones(value_shape)",
    "        key = np.ones(key_shape) if key_shape else None",
    "        output = layer(query=query, value=value, key=key)"
   ],
   "context_after": [
    "            query_shape, value_shape, key_shape",
    "        )",
    "        self.assertEqual(output.shape, comp_output_shape)",
    "",
    "    @parameterized.named_parameters(",
    "        (\"query_value_dim_mismatch\", (2, 4, 8), (2, 2, 7), 2),",
    "        (\"key_value_dim_mismatch\", (2, 4, 8), (2, 2, 8), (2, 1, 7)),",
    "        ("
   ]
  },
  {
   "path": "multi_head_attention_test.py",
   "line_number": 149,
   "line": "        with self.assertRaisesRegex(ValueError, r\"must be equal\"):",
   "context_before": [
    "    )",
    "    def test_shape_mismatch_error(self, query_shape, value_shape, key_shape):",
    "        \"\"\"Test dimension mismatches\"\"\"",
    "        layer = layers.MultiHeadAttention(",
    "            num_heads=4,",
    "            key_dim=2,",
    "            value_dim=2,",
    "        )"
   ],
   "context_after": [
    "            layer.compute_output_shape(query_shape, value_shape, key_shape)",
    "",
    "    def test_initializer(self):",
    "        # Test with a specified initializer.",
    "        layer = layers.MultiHeadAttention(",
    "            num_heads=12,",
    "            key_dim=64,",
    "            kernel_initializer=initializers.TruncatedNormal(stddev=0.02),"
   ]
  },
  {
   "path": "multi_head_attention_test.py",
   "line_number": 150,
   "line": "            layer.compute_output_shape(query_shape, value_shape, key_shape)",
   "context_before": [
    "    def test_shape_mismatch_error(self, query_shape, value_shape, key_shape):",
    "        \"\"\"Test dimension mismatches\"\"\"",
    "        layer = layers.MultiHeadAttention(",
    "            num_heads=4,",
    "            key_dim=2,",
    "            value_dim=2,",
    "        )",
    "        with self.assertRaisesRegex(ValueError, r\"must be equal\"):"
   ],
   "context_after": [
    "",
    "    def test_initializer(self):",
    "        # Test with a specified initializer.",
    "        layer = layers.MultiHeadAttention(",
    "            num_heads=12,",
    "            key_dim=64,",
    "            kernel_initializer=initializers.TruncatedNormal(stddev=0.02),",
    "        )"
   ]
  }
 ],
 "stats": {
  "files_searched": 1,
  "files_with_matches": 1,
  "matches_found": 4,
  "matches_returned": 4,
  "denied_skips": 0,
  "duration_ms": 5,
  "timing": {
   "walk_ms": 0,
   "search_ms": 4,
   "collect_ms": 0,
   "total_ms": 5
  }
 },
 "truncated": false
}
````

### Turn 3 — thinking

````text
The existing test expects a dimension mismatch error, but the upstream Keras fix seems to have removed that validation case, so I'm checking how the newer compute_output_shape logic handles key_shape and value_shape comparisons differently.
````

### Turn 3 — tool call call_0003 (edit)

````json
{
 "file_path": "keras/src/layers/attention/multi_head_attention.py",
 "old_string": "        if query_shape[-1] != value_shape[-1]:\n            raise ValueError(\n                \"The last dimension of `query_shape` and `value_shape` \"\n                f\"must be equal, but are {query_shape[-1]}, {value_shape[-1]}. \"\n                \"Received: query_shape={query_shape}, value_shape={value_shape}\"\n            )\n\n        if value_shape",
 "new_string": "        if value_shape"
}
````

Result:

````text
{
 "path": "keras/src/layers/attention/multi_head_attention.py",
 "edited": true,
 "replacements": 1,
 "total_file_lines": 732,
 "total_file_size_bytes": 28175,
 "diff": "-         if query_shape[-1] != value_shape[-1]:\n-             raise ValueError(\n-                 \"The last dimension of `query_shape` and `value_shape` \"\n-                 f\"must be equal, but are {query_shape[-1]}, {value_shape[-1]}. \"\n-                 \"Received: query_shape={query_shape}, value_shape={value_shape}\"\n-             )\n- ",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "edit",
    "paths": [
     "keras/src/layers/attention/multi_head_attention.py"
    ]
   }
  ]
 },
 "file_change": {
  "kind": "diff",
  "operation": "update",
  "path": "keras/src/layers/attention/multi_head_attention.py",
  "patch": "-         if query_shape[-1] != value_shape[-1]:\n-             raise ValueError(\n-                 \"The last dimension of `query_shape` and `value_shape` \"\n-                 f\"must be equal, but are {query_shape[-1]}, {value_shape[-1]}. \"\n-                 \"Received: query_shape={query_shape}, value_shape={value_shape}\"\n-             )\n- ",
  "additions": 0,
  "deletions": 7,
  "truncated": false,
  "omitted_lines": 0
 }
}
````

### Turn 4 — tool call call_0004 (exec)

````json
{
 "command": "cd /testbed && KERAS_BACKEND=tensorflow timeout 300 python -c \"\nimport keras\nq=keras.Input(shape=(256,16));k=keras.Input(shape=(256,16));v=keras.Input(shape=(256,8))\nprint(keras.layers.MultiHeadAttention(num_heads=8,key_dim=2)(query=q,value=v,key=k).shape)\nimport numpy as np\nprint(keras.layers.MultiHeadAttention(num_heads=8,key_dim=2)(query=np.ones((2,256,16)),value=np.ones((2,256,8)),key=np.ones((2,256,16))).shape)\n\" 2>&1 | tail -3; timeout 600 python -m pytest -q keras/src/layers/attention/multi_head_attention_test.py 2>&1 | tail -5"
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
 "stdout": "2026-10-17 05:18:01.378489: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n(None, 256, 16)\n(2, 256, 16)\n\nkeras/src/layers/attention/multi_head_attention.py:592: TypeError\n=========================== short test summary info ============================\nFAILED keras/src/layers/attention/multi_head_attention_test.py::MultiHeadAttentionTest::test_shape_mismatch_error_query_value_dim_mismatch\n========================= 1 failed, 25 passed in 3.87s =========================\n",
 "duration_ms": 14994,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed"
  ],
  "command_sha256": [
   "be5f4739280b2c60f8cfbd61522c7bab846486ede4f025c28136b8b19c633546"
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

### Turn 5 — thinking

````text
The failing test expects the old behavior where a query/value mismatch raises an error, which is actually the bug being fixed. I'm checking a TypeError around line 592, where query_shape is a tuple and gets concatenated with the output shape.
````

### Turn 5 — tool call call_0005 (exec)

````json
{
 "command": "cd /testbed && timeout 600 python -m pytest -q keras/src/layers/attention/multi_head_attention_test.py -k query_value_dim 2>&1 | grep -B5 Error | head -30"
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
 "stdout": "        layer = layers.MultiHeadAttention(\n            num_heads=4,\n            key_dim=2,\n            value_dim=2,\n        )\n        with self.assertRaisesRegex(ValueError, r\"must be equal\"):\n--\n    ):\n        if key_shape is None:\n            key_shape = value_shape\n    \n>       if value_shape[1:-1] != key_shape[1:-1]:\nE       TypeError: 'int' object is not subscriptable\n\nkeras/src/layers/attention/multi_head_attention.py:592: TypeError\n",
 "duration_ms": 6107,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed"
  ],
  "command_sha256": [
   "d85569c0c1963aa7f5e5a173427ee10b31e245bb40d1b02eb5df5ad5dafef733"
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

### Turn 6 — thinking

````text
That test case with an int key_shape only exercises the old buggy check, so it's expected to be removed along with the fix—no need to preserve it or convert shapes to tuples.

That test case passes an int for key_shape, which is malformed — it's now failing only because it expected the old removed check, so this is an expected test change from the upstream removal. I can consider this done and move to reporting.
````

### Turn 6 — assistant text

I removed the check that made `MultiHeadAttention` require the last dimension of `query` and `value` to match. Your Keras-tensor example now builds instead of raising the error.

**Cause:** that check only lived in `compute_output_shape` in `keras/src/layers/attention/multi_head_attention.py`. With symbolic inputs like `keras.Input`, Keras computes the output shape ahead of time, so the check ran and failed. With eager tensors the layer just runs and that method is never called, which is why your torch example worked. It wasn't about the static vs. dynamic batch size, or about PyTorch's own attention.

The check was also wrong: the layer projects query, key and value separately and maps the output back to the query's last dimension, so query and value don't need to match. The check that key and value must agree in every dimension except the last one is still there.

**Checks run** (TensorFlow backend):
- Your symbolic example (query 16, key 16, value 8) now gives output shape `(None, 256, 16)`. The eager NumPy version gives `(2, 256, 16)`, so both paths agree.
- `multi_head_attention_test.py`: 25 passed, 1 failed. The failure is `test_shape_mismatch_error_query_value_dim_mismatch`, which expects the error that was removed. That case also passes `key_shape=2`, a plain int rather than a shape, so it now stops with a `TypeError` at the remaining key/value check. That test case should be removed alongside this fix; I left it alone because you asked me not to modify tests.

### Turn 7 — assistant text

I removed the check that made the query and value last dimensions match. Your `keras.Input` example now builds, and its output shape is `(None, 256, 16)`. One existing test still fails, and that's expected: it checks for the error I removed.

**Why only sometimes:** the check lived only in `compute_output_shape` in `keras/src/layers/attention/multi_head_attention.py`. Keras runs that method when you call the layer on symbolic `keras.Input` tensors, but not when you call it on real tensors. Batch size had nothing to do with it, and so did Torch's own MultiHeadAttention.

**Why the check was wrong:** the layer projects query, key and value separately, and the output projection maps back to the query's last dimension. So the query and value last dimensions never need to match, and running the layer on real tensors already worked without the check.

**The fix:** I deleted that one check (7 lines). The other check, that value and key match on every dimension except the last, is unchanged.

**Checks:**
- With the TensorFlow backend, symbolic inputs of shape `(256,16)` for query and key and `(256,8)` for value give `(None, 256, 16)`. Real arrays of the same shapes with batch size 2 give `(2, 256, 16)`.
- `keras/src/layers/attention/multi_head_attention_test.py`: 25 passed, 1 failed.

**The failing test:** `test_shape_mismatch_error_query_value_dim_mismatch` expects the old error. Its input is also malformed: it passes the integer `2` as `key_shape`, which now causes a `TypeError` instead. You asked me not to modify tests, so it still needs updating or removing.

## Final answer

I removed the check that made the query and value last dimensions match. Your `keras.Input` example now builds, and its output shape is `(None, 256, 16)`. One existing test still fails, and that's expected: it checks for the error I removed.

**Why only sometimes:** the check lived only in `compute_output_shape` in `keras/src/layers/attention/multi_head_attention.py`. Keras runs that method when you call the layer on symbolic `keras.Input` tensors, but not when you call it on real tensors. Batch size had nothing to do with it, and so did Torch's own MultiHeadAttention.

**Why the check was wrong:** the layer projects query, key and value separately, and the output projection maps back to the query's last dimension. So the query and value last dimensions never need to match, and running the layer on real tensors already worked without the check.

**The fix:** I deleted that one check (7 lines). The other check, that value and key match on every dimension except the last, is unchanged.

**Checks:**
- With the TensorFlow backend, symbolic inputs of shape `(256,16)` for query and key and `(256,8)` for value give `(None, 256, 16)`. Real arrays of the same shapes with batch size 2 give `(2, 256, 16)`.
- `keras/src/layers/attention/multi_head_attention_test.py`: 25 passed, 1 failed.

**The failing test:** `test_shape_mismatch_error_query_value_dim_mismatch` expects the old error. Its input is also malformed: it passes the integer `2` as `key_shape`, which now causes a `TypeError` instead. You asked me not to modify tests, so it still needs updating or removing.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 94912 | 2500 | 88361 | 6535 | 97412 |
