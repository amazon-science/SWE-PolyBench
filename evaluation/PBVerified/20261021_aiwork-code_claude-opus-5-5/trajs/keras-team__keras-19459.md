# Instance: keras-team__keras-19459
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: False

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
Keras with TF backend GaussianDropout gives error with mixed_bfloat16
When using Keras with 3.1.1 with Tensorflow 2.16.1 backend, using GaussianDropout layer with mixed_bfloat16 results in the following error message:
```
TypeError: Exception encountered when calling GaussianDropout.call().

Input 'y' of 'Mul' Op has type float32 that does not match type bfloat16 of argument 'x'.

Arguments received by GaussianDropout.call():
  • inputs=tf.Tensor(shape=(None, 64), dtype=bfloat16)
  • training=True
```

Mixed Precision is set up the following way:
`tf.keras.mixed_precision.set_global_policy('mixed_bfloat16')`

GaussianDropout is used the following way:
`x = tf.keras.layers.GaussianDropout(dropout_rates[idx], name=f"gaussian_dropout_{idx}")(x)`

Specifying dtype as "bfloat16" in GaussianDropout layer does not solve the problem, as I checked the source code I saw that dtype is not sent to backend.random.normal function in the call method of GaussianDropout class. So, backend.random.normal function uses floatx(), and setting floatx with the following code:
```
import tensorflow.keras.backend as K
K.set_floatx('bfloat16')
```

It works without errors, but reported loss in the output is suspicious, takes only 2 distinct values interchangeably through 20 epochs. I guess this also uses bfloat16 for weights, and training gets worse due to numerical instability. I was not getting any errors before TF 2.16.1, which comes with Keras 2.x.
````

## Operational trajectory

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "cat keras/layers/regularization/gaussian_dropout.py; grep -n \"random.normal\" -A6 keras/layers/regularization/gaussian_noise.py"
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
 "stdout": "import math\n\nfrom keras import backend\nfrom keras import layers\nfrom keras import ops\nfrom keras.api_export import keras_export\n\n\n@keras_export(\"keras.layers.GaussianDropout\")\nclass GaussianDropout(layers.Layer):\n    \"\"\"Apply multiplicative 1-centered Gaussian noise.\n\n    As it is a regularization layer, it is only active at training time.\n\n    Args:\n        rate: Float, drop probability (as with `Dropout`).\n            The multiplicative noise will have\n            standard deviation `sqrt(rate / (1 - rate))`.\n        seed: Integer, optional random seed to enable deterministic behavior.\n\n    Call arguments:\n        inputs: Input tensor (of any rank).\n        training: Python boolean indicating whether the layer should behave in\n            training mode (adding dropout) or in inference mode (doing nothing).\n    \"\"\"\n\n    def __init__(self, rate, seed=None, **kwargs):\n        super().__init__(**kwargs)\n        if not 0 <= rate <= 1:\n            raise ValueError(\n                f\"Invalid value received for argument \"\n                \"`rate`. Expected a float value between 0 and 1. \"\n                f\"Received: rate={rate}\"\n            )\n        self.rate = rate\n        self.seed = seed\n        self.seed_generator = backend.random.SeedGenerator(seed)\n        self.supports_masking = True\n\n    def call(self, inputs, training=False):\n        if training and self.rate > 0:\n            stddev = math.sqrt(self.rate / (1.0 - self.rate))\n            return inputs * backend.random.normal(\n                shape=ops.shape(inputs),\n                mean=1.0,\n                stddev=stddev,\n                seed=self.seed_generator,\n            )\n        return inputs\n\n    def compute_output_shape(self, input_shape):\n        return input_shape\n\n    def get_config(self):\n        base_config = super().get_config()\n        config = {\n            \"rate\": self.rate,\n            \"seed\": self.seed,\n        }\n        return {**base_config, **config}\n43:            return inputs + backend.random.normal(\n44-                shape=ops.shape(inputs),\n45-                mean=0.0,\n46-                stddev=self.stddev,\n47-                seed=self.seed_generator,\n48-            )\n49-        return inputs\n",
 "device_targets": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "keras/layers/regularization/gaussian_dropout.py",
   "keras/layers/regularization/gaussian_noise.py"
  ],
  "command_sha256": [
   "59de5814f4e33b24cace6d60fd9fbfbe3fa51740e2ba01a716c82a3e6f3cff1c"
  ]
 },
 "duration_ms": 78
}
````

### Turn 2 — thinking

````text
I should fix both GaussianDropout and GaussianNoise the same way, using inputs.dtype rather than assuming float, matching the approach other Keras layers take. I recall the upstream fix (PR #19415) used exactly this pattern for both layers.
````

### Turn 2 — tool call call_0002 (exec)

````json
{
 "command": "sed -i 's/                seed=self.seed_generator,\\n            )/X/' keras/layers/regularization/gaussian_dropout.py\npython - <<'EOF'\nfor f in [\"keras/layers/regularization/gaussian_dropout.py\",\"keras/layers/regularization/gaussian_noise.py\"]:\n    s=open(f).read()\n    s=s.replace(\"                seed=self.seed_generator,\\n            )\",\"                seed=self.seed_generator,\\n                dtype=self.compute_dtype,\\n            )\",1)\n    open(f,\"w\").write(s)\nEOF\ngit diff --stat\npython -c \"\nimport keras,numpy as np\nfor L in [keras.layers.GaussianDropout(0.3,dtype='mixed_bfloat16'),keras.layers.GaussianNoise(0.3,dtype='mixed_bfloat16')]:\n    x=keras.ops.ones((2,4),dtype='bfloat16'); print(L(x,training=True).dtype)\n\"\npython -m pytest -q keras/layers/regularization/gaussian_dropout_test.py keras/layers/regularization/gaussian_noise_test.py 2>&1 | tail -3"
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
 "stdout": " keras/layers/regularization/gaussian_dropout.py | 1 +\n keras/layers/regularization/gaussian_noise.py   | 1 +\n 2 files changed, 2 insertions(+)\n<dtype: 'bfloat16'>\n<dtype: 'bfloat16'>\nkeras/layers/regularization/gaussian_noise_test.py::GaussianNoiseTest::test_gaussian_noise_correctness PASSED [100%]\n\n============================== 4 passed in 0.78s ===============================\n",
 "stderr": "2026-10-17 02:20:47.083917: I external/local_xla/xla/tsl/cuda/cudart_stub.cc:31] Could not find cuda drivers on your machine, GPU will not be used.\n2026-10-17 02:20:47.084444: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.\n2026-10-17 02:20:47.154691: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.\nTo enable the following instructions: AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.\n2026-10-17 02:20:50.890448: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)\n",
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "guidance": "stderr contains error-like diagnostics while the final exit code is 0. Inspect stderr before treating this command as successful; shell control flow may have masked a failed subcommand.",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "write",
    "paths": [
     "keras/layers/regularization/gaussian_dropout.py"
    ]
   }
  ],
  "reads": [],
  "command_sha256": [
   "e908e8a5a2e195f9296db00870ef50a57bda29e95c158454ebd05b65a9108eaf"
  ]
 },
 "device_targets": [],
 "duration_ms": 12883
}
````

### Turn 3 — thinking

````text
That sed command turned out to be a no-op since the pattern wouldn't match across single lines, but that's fine here.
````

### Turn 4 — assistant text

I fixed the `mixed_bfloat16` error in `GaussianDropout`. Its random noise is now created in the layer's compute dtype (bfloat16 under that policy) instead of always float32, so the multiply no longer fails.

The change is one line in `keras/layers/regularization/gaussian_dropout.py`: `dtype=self.compute_dtype` is passed to `backend.random.normal(...)` in `call()`. `GaussianNoise` (`keras/layers/regularization/gaussian_noise.py`) had the same problem, and I made the same one-line fix there.

I tested both layers with `dtype='mixed_bfloat16'` on bfloat16 inputs with `training=True`, on the TensorFlow backend. Both returned bfloat16 output with no error. The existing tests for the two layers also pass (4 tests). I didn't run the other backends.

This should also remove the need to call `set_floatx('bfloat16')`, the workaround that gave the suspicious loss values in the report.

### Turn 5 — assistant text

I fixed the bfloat16 error in `GaussianDropout`. The layer was making its random noise in the default float type, even when the input was bfloat16. Now it makes the noise in the layer's own compute type (`dtype=self.compute_dtype`), so with `mixed_bfloat16` the noise and the input are both bfloat16 and the multiply works.

`GaussianNoise` had the same problem, so I made the same one-line change in `keras/layers/regularization/gaussian_noise.py`. The other changed file is `keras/layers/regularization/gaussian_dropout.py`.

I tested both layers on the TensorFlow backend: with `dtype='mixed_bfloat16'`, a bfloat16 input with `training=True` now gives a bfloat16 output with no error. The 4 existing tests for the two layers pass. I didn't run the other backends or the full test suite.

This also means you shouldn't need the `set_floatx('bfloat16')` workaround from the report. That setting stores the weights in bfloat16 too, which likely explains the suspicious loss values.

## Final answer

I fixed the bfloat16 error in `GaussianDropout`. The layer was making its random noise in the default float type, even when the input was bfloat16. Now it makes the noise in the layer's own compute type (`dtype=self.compute_dtype`), so with `mixed_bfloat16` the noise and the input are both bfloat16 and the multiply works.

`GaussianNoise` had the same problem, so I made the same one-line change in `keras/layers/regularization/gaussian_noise.py`. The other changed file is `keras/layers/regularization/gaussian_dropout.py`.

I tested both layers on the TensorFlow backend: with `dtype='mixed_bfloat16'`, a bfloat16 input with `training=True` now gives a bfloat16 output with no error. The 4 existing tests for the two layers pass. I didn't run the other backends or the full test suite.

This also means you shouldn't need the `set_floatx('bfloat16')` workaround from the report. That setting stores the weights in bfloat16 too, which likely explains the suspicious loss values.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 56019 | 1427 | 40785 | 15222 | 57446 |
