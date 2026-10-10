# Instance: keras-team__keras-19973

- Final resolved (evaluator, logs/keras-team__keras-19973_result.json): False
- Run state: DONE
- One attempt. Duration 61.7 s, turns 8, actor cost $0.1394646, container commands 5
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/keras-team__keras-19973/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/keras-team__keras-19973/repo. Consider the following issue description:

<issue_description>
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

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/keras-team__keras-19973/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/keras-team__keras-19973/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/keras-team__keras-19973/bin/envrun 'git status --short && ls'
Edits you make under /work/keras-team__keras-19973/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -n "query_shape\|value_shape\|key_shape" keras/src/layers/attention/multi_head_attention.py | head -80
```

tool result:

```
201:        query_shape,
202:        value_shape,
203:        key_shape=None,
208:            query_shape: Shape of the `query` tensor.
209:            value_shape: Shape of the `value` tensor.
212:        key_shape = value_shape if key_shape is None else key_shape
213:        query_rank = len(query_shape)
214:        value_rank = len(value_shape)
215:        key_rank = len(key_shape)
228:        self._query_dense.build(query_shape)
241:        self._key_dense.build(key_shape)
254:        self._value_dense.build(value_shape)
261:            query_shape,
266:            self._query_dense.compute_output_shape(query_shape)
310:    def _make_output_dense(self, query_shape, common_kwargs, name=None):
321:        query_rank = len(query_shape)
328:            output_shape = [query_shape[-1]]
585:        query_shape,
586:        value_shape,
587:        key_shape=None,
589:        if key_shape is None:
590:            key_shape = value_shape
592:        if query_shape[-1] != value_shape[-1]:
594:                "The last dimension of `query_shape` and `value_shape` "
595:                f"must be equal, but are {query_shape[-1]}, {value_shape[-1]}. "
596:                "Received: query_shape={query_shape}, value_shape={value_shape}"
599:        if value_shape[1:-1] != key_shape[1:-1]:
602:                f"must be equal. Received: value_shape={value_shape} and "
603:                f"key_shape={key_shape}"
607:            return query_shape[:-1] + self._output_shape
609:        return query_shape
625:            key_shape = key.shape
627:            key_shape = None
629:            query.shape, value.shape, key_shape
```

**tool call: Bash**

```bash
sed -n 580,640p keras/src/layers/attention/multi_head_attention.py
```

tool result:

```
        col_index = ops.cumsum(ones_mask, axis=-1)
        return ops.greater_equal(row_index, col_index)

    def compute_output_shape(
        self,
        query_shape,
        value_shape,
        key_shape=None,
    ):
        if key_shape is None:
            key_shape = value_shape

        if query_shape[-1] != value_shape[-1]:
            raise ValueError(
                "The last dimension of `query_shape` and `value_shape` "
                f"must be equal, but are {query_shape[-1]}, {value_shape[-1]}. "
                "Received: query_shape={query_shape}, value_shape={value_shape}"
            )

        if value_shape[1:-1] != key_shape[1:-1]:
            raise ValueError(
                "All dimensions of `value` and `key`, except the last one, "
                f"must be equal. Received: value_shape={value_shape} and "
                f"key_shape={key_shape}"
            )

        if self._output_shape:
            return query_shape[:-1] + self._output_shape

        return query_shape

    def compute_output_spec(
        self,
        query,
        value,
        key=None,
        query_mask=None,
        value_mask=None,
        key_mask=None,
        attention_mask=None,
        return_attention_scores=False,
        training=None,
        use_causal_mask=False,
    ):
        if key is not None:
            key_shape = key.shape
        else:
            key_shape = None
        output_shape = self.compute_output_shape(
            query.shape, value.shape, key_shape
        )
        output_spec = backend.KerasTensor(
            output_shape, dtype=self.compute_dtype
        )
        if return_attention_scores:
            length = query.shape[1]
            attention_shape = (query.shape[0], self.num_heads, length, length)
            return output_spec, backend.KerasTensor(
                attention_shape, dtype=self.compute_dtype
            )
        return output_spec
```

**tool call: Bash**

```bash
grep -n "_output_shape\b\|output_shape =" keras/src/layers/attention/multi_head_attention.py; sed -n 310,335p keras/src/layers/attention/multi_head_attention.py
```

tool result:

```
126:        self._output_shape = output_shape
166:        return self._output_shape
180:            "output_shape": self._output_shape,
221:            output_shape=_get_output_shape(
234:            output_shape=_get_output_shape(
247:            output_shape=_get_output_shape(
266:            self._query_dense.compute_output_shape(query_shape)
322:        if self._output_shape:
323:            if not isinstance(self._output_shape, collections.abc.Sized):
324:                output_shape = [self._output_shape]
326:                output_shape = self._output_shape
328:            output_shape = [query_shape[-1]]
334:            output_shape=_get_output_shape(output_rank - 1, output_shape),
583:    def compute_output_shape(
606:        if self._output_shape:
607:            return query_shape[:-1] + self._output_shape
628:        output_shape = self.compute_output_shape(
738:def _get_output_shape(output_rank, known_last_dims):
    def _make_output_dense(self, query_shape, common_kwargs, name=None):
        """Builds the output projection matrix.

        Args:
            free_dims: Number of free dimensions for einsum equation building.
            common_kwargs: Common keyword arguments for einsum layer.
            name: Name for the projection layer.

        Returns:
            Projection layer.
        """
        query_rank = len(query_shape)
        if self._output_shape:
            if not isinstance(self._output_shape, collections.abc.Sized):
                output_shape = [self._output_shape]
            else:
                output_shape = self._output_shape
        else:
            output_shape = [query_shape[-1]]
        einsum_equation, bias_axes, output_rank = _build_proj_equation(
            query_rank - 1, bound_dims=2, output_dims=len(output_shape)
        )
        return EinsumDense(
            einsum_equation,
            output_shape=_get_output_shape(output_rank - 1, output_shape),
            bias_axes=bias_axes if self._use_bias else None,
```

**assistant:** Let me reproduce first.

**tool call: Bash**

```bash
cat > repro.py <<'EOF'
import numpy as np, keras
q = keras.Input(shape=(256, 16)); k = keras.Input(shape=(128, 16)); v = keras.Input(shape=(128, 8))
mha = keras.layers.MultiHeadAttention(num_heads=8, key_dim=2)
out, sc = mha(query=q, value=v, key=k, return_attention_scores=True)
print(out.shape, sc.shape)
o2, s2 = mha(np.random.rand(2,256,16), np.random.rand(2,128,8), np.random.rand(2,128,16), return_attention_scores=True)
print(o2.shape, s2.shape)
mha2 = keras.layers.MultiHeadAttention(num_heads=8, key_dim=2, output_shape=5)
print(mha2(q, v, k).shape)
EOF
../bin/envrun 'python repro.py 2>&1 | tail -3'
```

tool result:

```
Arguments received by MultiHeadAttention.call():
  • args=<class 'inspect._empty'>
  • kwargs={'query': '<KerasTensor shape=(None, 256, 16), dtype=float32, sparse=False, name=keras_tensor>', 'value': '<KerasTensor shape=(None, 128, 8), dtype=float32, sparse=False, name=keras_tensor_2>', 'key': '<KerasTensor shape=(None, 128, 16), dtype=float32, sparse=False, name=keras_tensor_1>', 'return_attention_scores': 'True', 'query_mask': 'None', 'value_mask': 'None', 'key_mask': 'None'}
```

**tool call: Bash**

```bash
python3 - <<'EOF'
p='keras/src/layers/attention/multi_head_attention.py'
s=open(p).read()
s=s.replace('''        if query_shape[-1] != value_shape[-1]:
            raise ValueError(
                "The last dimension of `query_shape` and `value_shape` "
                f"must be equal, but are {query_shape[-1]}, {value_shape[-1]}. "
                "Received: query_shape={query_shape}, value_shape={value_shape}"
            )

''','')
s=s.replace('''        if self._output_shape:
            return query_shape[:-1] + self._output_shape
''','''        if self._output_shape:
            if not isinstance(self._output_shape, collections.abc.Sized):
                return tuple(query_shape[:-1]) + (self._output_shape,)
            return tuple(query_shape[:-1]) + tuple(self._output_shape)
''')
s=s.replace('''            length = query.shape[1]
            attention_shape = (query.shape[0], self.num_heads, length, length)''','''            query_length = query.shape[1]
            key_length = value.shape[1]
            attention_shape = (
                query.shape[0],
                self.num_heads,
                query_length,
                key_length,
            )''')
open(p,'w').write(s)
EOF
../bin/envrun 'python repro.py 2>&1 | tail -3'
```

tool result:

```
(None, 256, 16) (None, 8, 256, 128)
(2, 256, 16) (2, 8, 256, 128)
(None, 256, 5)
```

**assistant:** Symbolic and eager shapes now agree. Running the existing tests across backends:

**tool call: Bash**

```bash
rm repro.py; for b in tensorflow jax torch; do ../bin/envrun "KERAS_BACKEND=$b python -m pytest -q keras/src/layers/attention/ 2>&1 | tail -3"; done
```

tool result:

```
=========================== short test summary info ============================
FAILED keras/src/layers/attention/multi_head_attention_test.py::MultiHeadAttentionTest::test_shape_mismatch_error_query_value_dim_mismatch
========================= 1 failed, 67 passed in 3.62s =========================

=========================== short test summary info ============================
FAILED keras/src/layers/attention/multi_head_attention_test.py::MultiHeadAttentionTest::test_shape_mismatch_error_query_value_dim_mismatch
======================== 1 failed, 67 passed in 14.60s =========================

keras/src/backend/__init__.py:7: in <module>
    import torch
E   ModuleNotFoundError: No module named 'torch'
```

**tool call: Bash**

```bash
grep -n -B3 -A20 "query_value_dim_mismatch" keras/src/layers/attention/multi_head_attention_test.py
```

tool result:

```
130-        self.assertEqual(output.shape, comp_output_shape)
131-
132-    @parameterized.named_parameters(
133:        ("query_value_dim_mismatch", (2, 4, 8), (2, 2, 7), 2),
134-        ("key_value_dim_mismatch", (2, 4, 8), (2, 2, 8), (2, 1, 7)),
135-        (
136-            "key_value_dim_mismatch_high_dim",
137-            (2, 4, 2, 3, 8),
138-            (2, 1, 1, 5, 8),
139-            (2, 1, 15, 5, 2),
140-        ),
141-    )
142-    def test_shape_mismatch_error(self, query_shape, value_shape, key_shape):
143-        """Test dimension mismatches"""
144-        layer = layers.MultiHeadAttention(
145-            num_heads=4,
146-            key_dim=2,
147-            value_dim=2,
148-        )
149-        with self.assertRaisesRegex(ValueError, r"must be equal"):
150-            layer.compute_output_shape(query_shape, value_shape, key_shape)
151-
152-    def test_initializer(self):
153-        # Test with a specified initializer.
```

**assistant:** I fixed the `MultiHeadAttention` layer so that `query` and `value` can have different last dimensions, as in the issue, no matter what kind of tensor you pass in. All the changes are in `keras/src/layers/attention/multi_head_attention.py`. A rerun of the issue's example, with symbolic Keras inputs and with plain arrays, now gives the same output shapes both ways.

**The cause:** Keras has two code paths here. When you pass real tensors (torch tensors in the issue), it runs the layer directly and never checks shapes. When you pass Keras inputs (`keras.Input`), it first works out the output shape without any data, and only that step required `query` and `value` to have the same last dimension. That rule is wrong: `value` is projected to `value_dim` per head, and the output is projected back to the query's last dimension, so the two never need to match. Batch size had nothing to do with it.

**Changes:**
1. **Removed the wrong check** in the shape calculation (`compute_output_shape`). The valid check stays: `key` and `value` must still match in every dimension except the last.
2. **Fixed the attention-score shape for Keras inputs.** It used the query length for both of the last two dimensions, so it came out wrong whenever key and query lengths differed. It is now `(batch, num_heads, query_len, key_len)`.
3. **Fixed `output_shape` given as a single number.** For example, `output_shape=5` would have broken the shape calculation; it now gives `(..., 5)`.

**Tests:** With the TensorFlow and JAX backends, the attention tests show 67 passed and 1 failed. The failure is the `query_value_dim_mismatch` case of `test_shape_mismatch_error` in `multi_head_attention_test.py`, which expects the old error that this fix removes. I left it alone because you said you're handling the tests; it needs to be removed or updated. The torch backend isn't installed in the container, so I couldn't run the tests there.

I deleted my reproduction script, so only the fix remains.

_session end: success, turns 8, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 4.82 s: python repro.py 2>&1 | tail -3
- `rc=0` 3.97 s: python repro.py 2>&1 | tail -3
- `rc=0` 8.0 s: KERAS_BACKEND=tensorflow python -m pytest -q keras/src/layers/attention/ 2>&1 | tail -3
- `rc=0` 17.56 s: KERAS_BACKEND=jax python -m pytest -q keras/src/layers/attention/ 2>&1 | tail -3
- `rc=0` 0.37 s: KERAS_BACKEND=torch python -m pytest -q keras/src/layers/attention/ 2>&1 | tail -3
