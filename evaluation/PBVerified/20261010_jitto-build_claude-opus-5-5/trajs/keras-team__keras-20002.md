# Instance: keras-team__keras-20002

- Final resolved (evaluator, logs/keras-team__keras-20002_result.json): False
- Run state: DONE
- One attempt. Duration 77.0 s, turns 12, actor cost $0.2480574, container commands 5
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/keras-team__keras-20002/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/keras-team__keras-20002/repo. Consider the following issue description:

<issue_description>
"ValueError: Undefined shapes are not supported." when calling model.call()
hello everybody.

I'm having trouble creating a Siamese network class, which extends keras.Model , from a function that returns the same model. My knowledge about [keras.Model](https://keras.io/api/models/model/) isn't good, so I don't know if it is a bug or my mistake.

This is the function:

```
def siamese_loss_network():
    inputs = keras.layers.Input((128, 128, 3))
    x = keras.applications.efficientnet.preprocess_input(inputs)
    base = keras.applications.EfficientNetB0(include_top=False, input_tensor=inputs, pooling = 'max')
    head = base.output
    x = keras.layers.Dense(256, activation="relu")(head)
    x = keras.layers.Dense(32)(x)
    embedding_network = keras.Model(inputs, x)
    input_1 = keras.layers.Input((128, 128, 3),name="input_layer_base_r")
    input_2 = keras.layers.Input((128, 128, 3),name="input_layer_base_l")
    tower_1 = embedding_network(input_1)
    tower_2 = embedding_network(input_2)
    merge_layer = keras.layers.Lambda(euclidean_distance, output_shape=(1,))(
        [tower_1, tower_2]
    )
    output_layer = keras.layers.Dense(1, activation="sigmoid")(merge_layer)
    siamese = keras.Model(inputs=[input_1, input_2], outputs=output_layer)
    return siamese

def euclidean_distance(vects):
    x, y = vects
    sum_square = ops.sum(ops.square(x - y), axis=1, keepdims=True)
    return ops.sqrt(ops.maximum(sum_square, keras.backend.epsilon()))
```

When running:

``` 
model = siamese_loss_network()
model.compile(optimizer=Adam(), loss=loss())
model.summary()
```


I get the following output:

```
Model: "functional_1"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Layer (type)                  ┃ Output Shape              ┃         Param # ┃ Connected to               ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ input_layer_base_r            │ (None, 128, 128, 3)       │               0 │ -                          │
│ (InputLayer)                  │                           │                 │                            │
├───────────────────────────────┼───────────────────────────┼─────────────────┼────────────────────────────┤
│ input_layer_base_l            │ (None, 128, 128, 3)       │               0 │ -                          │
│ (InputLayer)                  │                           │                 │                            │
├───────────────────────────────┼───────────────────────────┼─────────────────┼────────────────────────────┤
│ functional (Functional)       │ (None, 32)                │       4,385,731 │ input_layer_base_r[0][0],  │
│                               │                           │                 │ input_layer_base_l[0][0]   │
├───────────────────────────────┼───────────────────────────┼─────────────────┼────────────────────────────┤
│ lambda (Lambda)               │ (None, 1)                 │               0 │ functional[0][0],          │
│                               │                           │                 │ functional[1][0]           │
├───────────────────────────────┼───────────────────────────┼─────────────────┼────────────────────────────┤
│ dense_2 (Dense)               │ (None, 1)                 │               2 │ lambda[0][0]               │
└───────────────────────────────┴───────────────────────────┴─────────────────┴────────────────────────────┘
 Total params: 4,385,733 (16.73 MB)
 Trainable params: 4,343,710 (16.57 MB)
 Non-trainable params: 42,023 (164.16 KB)
```


So here is my adaptation for a class that inherits keras.Model:

```
class SiameseModel(keras.Model):
    def __init__(self): 
        super().__init__()
        self.inputs = keras.layers.Input((128, 128, 3))
        self.input_1 = keras.layers.Input((128, 128, 3),name="input_layer_base_r")
        self.input_2 = keras.layers.Input((128, 128, 3),name="input_layer_base_l")
        self.base = keras.applications.EfficientNetB0(include_top=False, input_tensor=self.inputs, pooling = 'max')
        self.dense_1 = keras.layers.Dense(256, activation="relu")
        self.dense_2 = keras.layers.Dense(32)
        self.merge_layer = keras.layers.Lambda(euclidean_distance, output_shape=(1,))
        self.output_layer = keras.layers.Dense(1, activation="sigmoid")

    def call(self, inputs):
        head = self.base.output
        x = self.dense_1(head)
        x = self.dense_2(x)
        embedding_network = keras.Model(inputs, x)
        tower_1 = embedding_network(self.input_1)
        tower_2 = embedding_network(self.input_2)
        merge = self.merge_layer([tower_1, tower_2])
        output = self.output_layer(merge)
        return keras.Model(inputs=[self.input_1, self.input_2], outputs=output)
``` 

When running:

``` 
model = SiameseModel()
model.compile(optimizer=Adam(), loss=loss())
model.summary()
```

i got the error: 

```
Traceback (most recent call last):
  File "D:[project path]\main.py", line 20, in <module>
    model.summary()
  File "C:[user path]\.conda\envs\[env path]\lib\site-packages\keras\src\utils\traceback_utils.py", line 122, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\[user path]\.conda\envs\[env path]\lib\site-packages\optree\ops.py", line 594, in tree_map
    return treespec.unflatten(map(func, *flat_args))
ValueError: Undefined shapes are not supported.
``` 


I read [this other issue](https://github.com/keras-team/keras/issues/19482), but i honestly didn't understand the reason for the error, nor how to resolve it. Could anyone enlighten me about this?

Python version: Python 3.10.13
pip version: 24.0
Tensorflow version: 2.16.1
Keras version: Version: 3.4.1

Grateful for the attention and hard work!



</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/keras-team__keras-20002/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/keras-team__keras-20002/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/keras-team__keras-20002/bin/envrun 'git status --short && ls'
Edits you make under /work/keras-team__keras-20002/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/keras-team__keras-20002/repo; git log --oneline -2; grep -n "Undefined shapes" -r keras/src | head; sed -n 1,80p keras/src/utils/summary_utils.py | grep -n "def \|shape" 
```

tool result:

```
576daec84 Fix CI
24b853618 Touch up test
keras/src/backend/common/variables.py:509:            raise ValueError("Undefined shapes are not supported.")
keras/src/backend/common/variables_test.py:207:            ValueError, "Undefined shapes are not supported."
19:def count_params(weights):
20:    shapes = [v.shape for v in weights]
21:    return int(sum(math.prod(p) for p in shapes))
24:def weight_memory_size(weights):
36:        weight_shape = math.prod(w.shape)
39:        total_memory_size += weight_shape * per_param_size
43:def readable_memory_size(weight_memory_size):
55:def highlight_number(x):
58:    We use a separate color for `None`s, e.g. in a layer shape.
66:def highlight_symbol(x):
71:def bold_text(x, color=None):
78:def format_layer_shape(layer):
79:    if not layer._inbound_nodes and not layer._build_shapes_dict:
```

**tool call: Bash**

```bash
cd /work/keras-team__keras-20002/repo; sed -n 75,120p keras/src/utils/summary_utils.py; sed -n 490,520p keras/src/backend/common/variables.py; git status
```

tool result:

```
    return f"[bold]{x}[/]"


def format_layer_shape(layer):
    if not layer._inbound_nodes and not layer._build_shapes_dict:
        return "?"

    def format_shape(shape):
        highlighted = [highlight_number(x) for x in shape]
        return "(" + ", ".join(highlighted) + ")"

    # There are 2 approaches to get output shapes:
    # 1. Using `layer._inbound_nodes`, which is possible if the model is a
    # Sequential or Functional.
    # 2. Using `layer._build_shapes_dict`, which is possible if users manually
    # build the layer.
    if len(layer._inbound_nodes) > 0:
        for i in range(len(layer._inbound_nodes)):
            outputs = layer._inbound_nodes[i].output_tensors
            output_shapes = tree.map_structure(
                lambda x: format_shape(x.shape), outputs
            )
    else:
        try:
            outputs = layer.compute_output_shape(**layer._build_shapes_dict)
        except NotImplementedError:
            return "?"
        output_shapes = tree.map_shape_structure(
            lambda x: format_shape(x), outputs
        )
    if len(output_shapes) == 1:
        return output_shapes[0]
    out = str(output_shapes)
    out = out.replace("'", "")
    return out


def print_summary(
    model,
    line_length=None,
    positions=None,
    print_fn=None,
    expand_nested=False,
    show_trainable=False,
    layer_range=None,
):
        return config.floatx()
    dtype = dtypes.PYTHON_DTYPES_MAP.get(dtype, dtype)
    if hasattr(dtype, "name"):
        dtype = dtype.name
    elif hasattr(dtype, "__str__") and (
        "torch" in str(dtype) or "jax.numpy" in str(dtype)
    ):
        dtype = str(dtype).split(".")[-1]
    elif hasattr(dtype, "__name__"):
        dtype = dtype.__name__

    if dtype not in dtypes.ALLOWED_DTYPES:
        raise ValueError(f"Invalid dtype: {dtype}")
    return dtype


def standardize_shape(shape):
    if not isinstance(shape, tuple):
        if shape is None:
            raise ValueError("Undefined shapes are not supported.")
        if not hasattr(shape, "__iter__"):
            raise ValueError(f"Cannot convert '{shape}' to a shape.")
        if config.backend() == "tensorflow":
            if isinstance(shape, tf.TensorShape):
                # `tf.TensorShape` may contain `Dimension` objects.
                # We need to convert the items in it to either int or `None`
                shape = shape.as_list()
        shape = tuple(shape)

    if config.backend() == "torch":
        # `shape` might be `torch.Size`. We need to convert the items in it to
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Dockerfile

nothing added to commit but untracked files present (use "git add" to track)
```

**assistant:** Let me reproduce with a smaller version of the issue's model.

**tool call: Bash**

```bash
cd /work/keras-team__keras-20002/repo; cat > repro_tmp.py <<'EOF'
import keras
class M(keras.Model):
    def __init__(self):
        super().__init__()
        self.inp = keras.layers.Input((8,))
        self.dense_1 = keras.layers.Dense(4)
        self.base = keras.Model(self.inp, keras.layers.Dense(3)(self.inp))
    def call(self, x):
        return self.dense_1(self.base(x))
m = M()
m.compile(optimizer="adam", loss="mse")
m.summary()
EOF
../bin/envrun 'python repro_tmp.py 2>&1 | tail -30'
```

tool result:

```
2026-10-09 04:03:13.756931: I external/local_xla/xla/tsl/cuda/cudart_stub.cc:31] Could not find cuda drivers on your machine, GPU will not be used.
2026-10-09 04:03:14.070423: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2026-10-09 04:03:16.790976: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)
Traceback (most recent call last):
  File "/testbed/repro_tmp.py", line 12, in <module>
    m.summary()
  File "/testbed/keras/src/utils/traceback_utils.py", line 122, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "/usr/local/lib/python3.9/site-packages/optree/ops.py", line 766, in tree_map
    return treespec.unflatten(map(func, *flat_args))
ValueError: Undefined shapes are not supported.
```

**tool call: Bash**

```bash
cd /work/keras-team__keras-20002/repo; ../bin/envrun 'KERAS_TRACEBACK_FILTERING=0 python -c "
import keras; keras.config.disable_traceback_filtering()
exec(open(\"repro_tmp.py\").read())" 2>&1 | grep -v "^20" | tail -40'
```

tool result:

```
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "<string>", line 12, in <module>
  File "/testbed/keras/src/utils/traceback_utils.py", line 113, in error_handler
    return fn(*args, **kwargs)
  File "/testbed/keras/src/models/model.py", line 257, in summary
    summary_utils.print_summary(
  File "/testbed/keras/src/utils/summary_utils.py", line 309, in print_summary
    for row in print_layer(layer):
  File "/testbed/keras/src/utils/summary_utils.py", line 294, in print_layer
    fields = get_layer_fields(layer, prefix=prefix)
  File "/testbed/keras/src/utils/summary_utils.py", line 261, in get_layer_fields
    output_shape = format_layer_shape(layer)
  File "/testbed/keras/src/utils/summary_utils.py", line 99, in format_layer_shape
    outputs = layer.compute_output_shape(**layer._build_shapes_dict)
  File "/testbed/keras/src/models/functional.py", line 186, in compute_output_shape
    return super().compute_output_shape(input_shape)
  File "/testbed/keras/src/ops/function.py", line 124, in compute_output_shape
    input_shape_struct = tree.map_shape_structure(
  File "/testbed/keras/src/tree/tree_api.py", line 275, in map_shape_structure
    return tree_impl.map_shape_structure(func, structure)
  File "/testbed/keras/src/tree/optree_impl.py", line 187, in map_shape_structure
    return optree.tree_map(
  File "/usr/local/lib/python3.9/site-packages/optree/ops.py", line 766, in tree_map
    return treespec.unflatten(map(func, *flat_args))
  File "/testbed/keras/src/ops/function.py", line 125, in <lambda>
    lambda x: KerasTensor(shape=x), input_shape
  File "/testbed/keras/src/backend/common/keras_tensor.py", line 40, in __init__
    self._shape = backend.standardize_shape(shape)
  File "/testbed/keras/src/backend/common/variables.py", line 509, in standardize_shape
    raise ValueError("Undefined shapes are not supported.")
ValueError: Undefined shapes are not supported.
```

**tool call: Bash**

```bash
cd /work/keras-team__keras-20002/repo; ../bin/envrun 'python -c "
exec(open(\"repro_tmp.py\").read().replace(\"m.summary()\",\"\"))
print(m.base._build_shapes_dict, m.base.built, m.base._inbound_nodes)" 2>&1 | tail -2'; grep -n "_build_shapes_dict" -r keras/src --include=*.py | grep -v _test
```

tool result:

```
2026-10-09 04:03:29.671811: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)
{'input_shape': None} True ListWrapper([])

(eval):3: no matches found: --include=*.py
```

**tool call: Bash**

```bash
cd /work/keras-team__keras-20002/repo; grep -rn "_build_shapes_dict" keras/src | grep -v _test; grep -n "def build\|built = True\|_build_shapes" keras/src/models/functional.py keras/src/ops/function.py
```

tool result:

```
Binary file keras/src/layers/__pycache__/layer.cpython-39.pyc matches
keras/src/layers/layer.py:228:            obj._build_shapes_dict = signature.bind(*args, **kwargs).arguments
keras/src/layers/layer.py:296:        self._build_shapes_dict = None
keras/src/layers/layer.py:411:        if self._build_shapes_dict is not None:
keras/src/layers/layer.py:412:            if len(self._build_shapes_dict) == 1:
keras/src/layers/layer.py:414:                    "input_shape": tuple(self._build_shapes_dict.values())[0],
keras/src/layers/layer.py:417:                return {"shapes_dict": self._build_shapes_dict}
keras/src/utils/summary_utils.py:79:    if not layer._inbound_nodes and not layer._build_shapes_dict:
keras/src/utils/summary_utils.py:89:    # 2. Using `layer._build_shapes_dict`, which is possible if users manually
keras/src/utils/summary_utils.py:99:            outputs = layer.compute_output_shape(**layer._build_shapes_dict)
Binary file keras/src/utils/__pycache__/summary_utils.cpython-39.pyc matches
Binary file keras/src/backend/tensorflow/__pycache__/layer.cpython-39.pyc matches
keras/src/backend/tensorflow/layer.py:107:                for value in self._build_shapes_dict.values()
Binary file keras/src/models/__pycache__/model.cpython-39.pyc matches
keras/src/models/model.py:410:            self._build_shapes_dict = config
keras/src/models/model.py:422:            self._build_shapes_dict = config["shapes_dict"]
keras/src/export/export_lib.py:648:    shapes_dict = getattr(model, "_build_shapes_dict", None)
Binary file keras/src/export/__pycache__/export_lib.cpython-39.pyc matches
keras/src/models/functional.py:188:    def build(self, input_shape):
keras/src/models/functional.py:189:        self.built = True
```

**tool call: Bash**

```bash
cd /work/keras-team__keras-20002/repo; sed -n 210,240p keras/src/layers/layer.py; grep -n "self.build(\|\.build(" keras/src/models/functional.py keras/src/models/model.py keras/src/layers/layer.py | head -20
```

tool result:

````
    assert my_sum.trainable_weights == []
    ```
    """

    def __new__(cls, *args, **kwargs):
        # Wrap the user-provided build method in the build_decorator
        # to add name scope support and serialization support.
        obj = super().__new__(cls, *args, **kwargs)

        original_build_method = obj.build

        @wraps(original_build_method)
        def build_wrapper(*args, **kwargs):
            with obj._open_name_scope():
                obj._path = current_path()
                original_build_method(*args, **kwargs)
            # Record build config.
            signature = inspect.signature(original_build_method)
            obj._build_shapes_dict = signature.bind(*args, **kwargs).arguments
            # Set built, post build actions, and lock state.
            obj.built = True
            obj._post_build()
            obj._lock_state()

        obj.build = build_wrapper
        return obj

    def __init__(
        self,
        *,
        activity_regularizer=None,
keras/src/models/functional.py:141:        self.build(None)
keras/src/models/model.py:406:                    self.build(config["input_shape"])
keras/src/models/model.py:418:                    self.build(**config["shapes_dict"])
keras/src/layers/layer.py:432:                self.build(config["input_shape"])
keras/src/layers/layer.py:434:                self.build(**config["shapes_dict"])
keras/src/layers/layer.py:1299:                f"`layer.build(input_shape)`."
keras/src/layers/layer.py:1318:            self.build(**shapes_dict)
keras/src/layers/layer.py:1345:                    "layer (e.g. by calling `layer.build()` on all its "
keras/src/layers/layer.py:1349:        self.build(first_shape)
````

**tool call: Bash**

```bash
cd /work/keras-team__keras-20002/repo; grep -rn "def output_shape\|def output\b" -A12 keras/src/models keras/src/ops/function.py keras/src/ops/operation.py keras/src/layers/layer.py | head -60
```

tool result:

```
keras/src/models/sequential.py:273:    def output_shape(self):
keras/src/models/sequential.py-274-        if self._functional:
keras/src/models/sequential.py-275-            return self._functional.output_shape
keras/src/models/sequential.py-276-        raise ValueError(
keras/src/models/sequential.py-277-            f"Sequential model '{self.name}' has no defined output shape yet."
keras/src/models/sequential.py-278-        )
keras/src/models/sequential.py-279-
keras/src/models/sequential.py-280-    @property
keras/src/models/sequential.py-281-    def inputs(self):
keras/src/models/sequential.py-282-        if self._functional:
keras/src/models/sequential.py-283-            return self._functional.inputs
keras/src/models/sequential.py-284-        raise ValueError(
keras/src/models/sequential.py-285-            f"Sequential model '{self.name}' has no defined inputs yet."
--
keras/src/models/functional.py:199:    def output_shape(self):
keras/src/models/functional.py-200-        output_shapes = tree.map_structure(lambda x: x.shape, self.outputs)
keras/src/models/functional.py-201-        if isinstance(output_shapes, list) and len(output_shapes) == 1:
keras/src/models/functional.py-202-            return output_shapes[0]
keras/src/models/functional.py-203-        return output_shapes
keras/src/models/functional.py-204-
keras/src/models/functional.py-205-    def _assert_input_compatibility(self, *args):
keras/src/models/functional.py-206-        return super(Model, self)._assert_input_compatibility(*args)
keras/src/models/functional.py-207-
keras/src/models/functional.py-208-    def _flatten_to_reference_inputs(self, inputs):
keras/src/models/functional.py-209-        return tree.flatten(inputs)
keras/src/models/functional.py-210-
keras/src/models/functional.py-211-    def _convert_inputs_to_tensors(self, flat_inputs):
--
keras/src/models/functional.py:269:    def output(self):
keras/src/models/functional.py-270-        return self._outputs_struct
keras/src/models/functional.py-271-
keras/src/models/functional.py-272-    def add_loss(self, loss):
keras/src/models/functional.py-273-        # Symbolic only. TODO
keras/src/models/functional.py-274-        raise NotImplementedError
keras/src/models/functional.py-275-
keras/src/models/functional.py-276-    @property
keras/src/models/functional.py-277-    def input_spec(self):
keras/src/models/functional.py-278-        if hasattr(self, "_manual_input_spec"):
keras/src/models/functional.py-279-            return self._manual_input_spec
keras/src/models/functional.py-280-
keras/src/models/functional.py-281-        def shape_with_no_batch_size(x):
--
keras/src/ops/operation.py:257:    def output(self):
keras/src/ops/operation.py-258-        """Retrieves the output tensor(s) of a layer.
keras/src/ops/operation.py-259-
keras/src/ops/operation.py-260-        Only returns the tensor(s) corresponding to the *first time*
keras/src/ops/operation.py-261-        the operation was called.
keras/src/ops/operation.py-262-
keras/src/ops/operation.py-263-        Returns:
keras/src/ops/operation.py-264-            Output tensor or list of output tensors.
keras/src/ops/operation.py-265-        """
keras/src/ops/operation.py-266-        return self._get_node_attribute_at_index(0, "output_tensors", "output")
keras/src/ops/operation.py-267-
keras/src/ops/operation.py-268-    def _get_node_attribute_at_index(self, node_index, attr, attr_name):
keras/src/ops/operation.py-269-        """Private utility to retrieves an attribute (e.g. inputs) from a node.
```

**thinking:**

```
Found the cause: Functional models call `self.build(None)` in their constructor, so `format_layer_shape` ends up calling `compute_output_shape(input_shape=None)` on nested models with no inbound nodes, which fails. Since Functional and Sequential models already expose `output_shape`, I'll update the summary logic to use that instead.


```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/keras-team__keras-20002/repo/keras/src/utils/summary_utils.py",
 "old_string": "        try:\n            outputs = layer.compute_output_shape(**layer._build_shapes_dict)\n        except NotImplementedError:\n            return \"?\"",
 "new_string": "        try:\n            if hasattr(layer, \"output_shape\"):\n                # Functional and Sequential models already know their\n                # output shapes.\n                outputs = layer.output_shape\n            else:\n                outputs = layer.compute_output_shape(\n                    **layer._build_shapes_dict\n                )\n        except NotImplementedError:\n            return \"?\""
}
```

tool result:

```
The file /work/keras-team__keras-20002/repo/keras/src/utils/summary_utils.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
cd /work/keras-team__keras-20002/repo; cat >> repro_tmp.py <<'EOF'
# multi-output nested functional + nested built sequential
class M2(keras.Model):
    def __init__(self):
        super().__init__()
        i = keras.layers.Input((8,))
        self.base = keras.Model(i, [keras.layers.Dense(3)(i), keras.layers.Dense(2)(i)])
        self.seq = keras.Sequential([keras.layers.Dense(5)]); self.seq.build((None, 3))
    def call(self, x):
        a, b = self.base(x); return self.seq(a)
M2().summary()
EOF
../bin/envrun 'python repro_tmp.py 2>&1 | grep -v "^20\|AVX"'
```

tool result:

```
Model: "m"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ dense (Dense)                   │ ?                      │   0 (unbuilt) │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ functional (Functional)         │ (None, 3)              │            27 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 27 (108.00 B)
 Trainable params: 27 (108.00 B)
 Non-trainable params: 0 (0.00 B)
Model: "m2"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ functional_1 (Functional)       │ [(None, 3), (None, 2)] │            45 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ sequential (Sequential)         │ (None, 5)              │            20 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 65 (260.00 B)
 Trainable params: 65 (260.00 B)
 Non-trainable params: 0 (0.00 B)
```

**assistant:** The summary works now, including for nested multi-output Functional models and nested Sequential models that have been built. Next I'll run the related tests and clean up.

**tool call: Bash**

```bash
cd /work/keras-team__keras-20002/repo; rm repro_tmp.py; ../bin/envrun 'python -m pytest -q keras/src/utils/summary_utils_test.py keras/src/models/model_test.py keras/src/models/sequential_test.py keras/src/models/functional_test.py 2>&1 | tail -3'; git status --short
```

tool result:

```
keras/src/models/functional_test.py::FunctionalTest::test_training_arg PASSED [100%]

============================= 82 passed in 10.86s ==============================

 M keras/src/utils/summary_utils.py
?? Dockerfile
```

**assistant:** `model.summary()` no longer crashes with "Undefined shapes are not supported." when a subclassed model holds a nested Functional model and hasn't been called yet.

**Cause:** A Functional model builds itself with `self.build(None)` when it's created, so the shape it records is `{"input_shape": None}`. In a subclassed model that hasn't been called, the nested model has no call history (inbound nodes). So `format_layer_shape` in `keras/src/utils/summary_utils.py` fell back to `layer.compute_output_shape(input_shape=None)`, which raised the error.

**Fix:** One change in `keras/src/utils/summary_utils.py`. If the layer has an `output_shape` property, the summary now uses it. Functional models have this property, and so do Sequential models once built, since they already know their output shapes. All other layers still go through `compute_output_shape`.

**Verification:**
- I reproduced the error with a cut-down version of the issue's model. After the fix, the summary prints `functional (Functional) │ (None, 3)`.
- I also checked a nested multi-output Functional model, which shows `[(None, 3), (None, 2)]`, and a nested Sequential model that had been built, which shows `(None, 5)`.
- The summary, model, sequential and functional tests all pass (82 tests).
- I deleted the reproduction script. The untracked `Dockerfile` was there before I started, so I left it alone.

One caveat for the issue's own example: its `call()` creates and returns a new `keras.Model` instead of returning tensors. That's a mistake in the user's code, separate from this bug. The model will print a summary now, but it won't train or predict correctly until `call()` returns output tensors.

_session end: success, turns 12, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 4.58 s: python repro_tmp.py 2>&1 | tail -30
- `rc=0` 3.65 s: KERAS_TRACEBACK_FILTERING=0 python -c " import keras; keras.config.disable_traceback_filtering() exec(open(\"repro_tmp.py\").read())" 2>&1 | grep -v "^20" | tail -40
- `rc=0` 3.68 s: python -c " exec(open(\"repro_tmp.py\").read().replace(\"m.summary()\",\"\")) print(m.base._build_shapes_dict, m.base.built, m.base._inbound_nodes)" 2>&1 | tail -2
- `rc=0` 3.66 s: python repro_tmp.py 2>&1 | grep -v "^20\|AVX"
- `rc=0` 15.17 s: python -m pytest -q keras/src/utils/summary_utils_test.py keras/src/models/model_test.py keras/src/models/sequential_test.py keras/src/models/functional_test.py 2>&1 | tail -3
