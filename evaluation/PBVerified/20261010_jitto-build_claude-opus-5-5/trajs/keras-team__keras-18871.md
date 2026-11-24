# Instance: keras-team__keras-18871

- Final resolved (evaluator, logs/keras-team__keras-18871_result.json): False
- Run state: DONE
- One attempt. Duration 89.8 s, turns 12, actor cost $0.2274908, container commands 4
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/keras-team__keras-18871/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/keras-team__keras-18871/repo. Consider the following issue description:

<issue_description>
Feature duplication on model.save() and keras.saving.save_model()
When I was reading the code of model saving, I got strange feeling.

https://github.com/keras-team/keras/blob/724321c7b39a90f6125b79931284aa9932c673a0/keras/models/model.py#L294-L297
It says `model.save()` is an alias for `keras.saving.save_model()`. But each of these method are implemented same feature.

https://github.com/keras-team/keras/blob/f0b7062e4c6a62c521af491b09d97f009b1add0b/keras/models/model.py#L268
https://github.com/keras-team/keras/blob/f0b7062e4c6a62c521af491b09d97f009b1add0b/keras/saving/saving_api.py#L19

these method's code are almost same. this duplicated feature will cause increase management point of code and It seems already started version fragmentation.

I think `model.save()` method can be removed and be modified to just calling `keras.saving.save_model()`.

Can I refactor this code?

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/keras-team__keras-18871/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/keras-team__keras-18871/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/keras-team__keras-18871/bin/envrun 'git status --short && ls'
Edits you make under /work/keras-team__keras-18871/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

Follow these steps to resolve the issue:
1. As a first step, explore the repo to find and read the code relevant to the <issue_description>.
2. Create a script or a small test to reproduce the error and execute it with envrun, to confirm the error.
3. Edit the source code of the repo to resolve the issue.
4. Rerun your reproduction and confirm that the error is fixed.
5. Think about edge cases and make sure your fix handles them as well; run the existing tests closest to the code you changed.
6. Delete any scripts or files you created only for reproduction or checking, so that only the fix remains in the repository.

```

## Trajectory

_session start: model claude-opus-5-5, tools ['Bash', 'Edit', 'Glob', 'Grep', 'Read', 'Write'], MCP servers []_

**tool call: Bash**

```bash
cd /work/keras-team__keras-18871/repo; grep -n "def save\b" -A80 keras/models/model.py; cat keras/saving/saving_api.py | head -120
```

tool result:

````
268:    def save(self, filepath, overwrite=True, **kwargs):
269-        """Saves a model as a `.keras` file.
270-
271-        Args:
272-            filepath: `str` or `pathlib.Path` object.
273-                Path where to save the model. Must end in `.keras`.
274-            overwrite: Whether we should overwrite any existing model
275-                at the target location, or instead ask the user
276-                via an interactive prompt.
277-            save_format: Format to use, as a string. Only the `"keras"`
278-                format is supported at this time.
279-
280-        Example:
281-
282-        ```python
283-        model = keras.Sequential(
284-            [
285-                keras.layers.Dense(5, input_shape=(3,)),
286-                keras.layers.Softmax(),
287-            ],
288-        )
289-        model.save("model.keras")
290-        loaded_model = keras.saving.load_model("model.keras")
291-        x = keras.random.uniform((10, 3))
292-        assert np.allclose(model.predict(x), loaded_model.predict(x))
293-        ```
294-
295-        Note that `model.save()` is an alias for
296-        `keras.saving.save_model()`.
297-
298-        The saved `.keras` file contains:
299-
300-        - The model's configuration (architecture)
301-        - The model's weights
302-        - The model's optimizer's state (if any)
303-
304-        Thus models can be reinstantiated in the exact same state.
305-        """
306-        include_optimizer = kwargs.pop("include_optimizer", True)
307-        save_format = kwargs.pop("save_format", None)
308-        if kwargs:
309-            raise ValueError(
310-                "The following argument(s) are not supported: "
311-                f"{list(kwargs.keys())}"
312-            )
313-        if save_format:
314-            if str(filepath).endswith((".h5", ".hdf5")) or str(
315-                filepath
316-            ).endswith(".keras"):
317-                warnings.warn(
318-                    "The `save_format` argument is deprecated in Keras 3. "
319-                    "We recommend removing this argument as it can be inferred "
320-                    "from the file path. "
321-                    f"Received: save_format={save_format}"
322-                )
323-            else:
324-                raise ValueError(
325-                    "The `save_format` argument is deprecated in Keras 3. "
326-                    "Please remove this argument and pass a file path with "
327-                    "either `.keras` or `.h5` extension."
328-                    f"Received: save_format={save_format}"
329-                )
330-        try:
331-            exists = os.path.exists(filepath)
332-        except TypeError:
333-            exists = False
334-        if exists and not overwrite:
335-            proceed = io_utils.ask_to_proceed_with_overwrite(filepath)
336-            if not proceed:
337-                return
338-        if str(filepath).endswith(".keras"):
339-            saving_lib.save_model(self, filepath)
340-        elif str(filepath).endswith((".h5", ".hdf5")):
341-            # Deprecation warnings
342-            warnings.warn(
343-                "You are saving your model as an HDF5 file via `model.save()`. "
344-                "This file format is considered legacy. "
345-                "We recommend using instead the native Keras format, "
346-                "e.g. `model.save('my_model.keras')`."
347-            )
348-            legacy_h5_format.save_model_to_hdf5(
import os
import zipfile

from absl import logging

from keras.api_export import keras_export
from keras.legacy.saving import legacy_h5_format
from keras.saving import saving_lib
from keras.utils import file_utils
from keras.utils import io_utils

try:
    import h5py
except ImportError:
    h5py = None


@keras_export(["keras.saving.save_model", "keras.models.save_model"])
def save_model(model, filepath, overwrite=True, **kwargs):
    """Saves a model as a `.keras` file.

    Args:
        model: Keras model instance to be saved.
        filepath: `str` or `pathlib.Path` object. Path where to save the model.
        overwrite: Whether we should overwrite any existing model at the target
            location, or instead ask the user via an interactive prompt.

    Example:

    ```python
    model = keras.Sequential(
        [
            keras.layers.Dense(5, input_shape=(3,)),
            keras.layers.Softmax(),
        ],
    )
    model.save("model.keras")
    loaded_model = keras.saving.load_model("model.keras")
    x = keras.random.uniform((10, 3))
    assert np.allclose(model.predict(x), loaded_model.predict(x))
    ```

    Note that `model.save()` is an alias for `keras.saving.save_model()`.

    The saved `.keras` file contains:

    - The model's configuration (architecture)
    - The model's weights
    - The model's optimizer's state (if any)

    Thus models can be reinstantiated in the exact same state.
    """
    include_optimizer = kwargs.pop("include_optimizer", True)
    save_format = kwargs.pop("save_format", False)
    if save_format:
        if str(filepath).endswith((".h5", ".hdf5")) or str(filepath).endswith(
            ".keras"
        ):
            logging.warning(
                "The `save_format` argument is deprecated in Keras 3. "
                "We recommend removing this argument as it can be inferred "
                "from the file path. "
                f"Received: save_format={save_format}"
            )
        else:
            raise ValueError(
                "The `save_format` argument is deprecated in Keras 3. "
                "Please remove this argument and pass a file path with "
                "either `.keras` or `.h5` extension."
                f"Received: save_format={save_format}"
            )
    if kwargs:
        raise ValueError(
            "The following argument(s) are not supported: "
            f"{list(kwargs.keys())}"
        )

    # Deprecation warnings
    if st
[... 1715 more characters not shown]
````

**tool call: Bash**

```bash
cd /work/keras-team__keras-18871/repo; sed -n 348,375p keras/models/model.py; sed -n 1,30p keras/models/model.py; grep -n "warn\|save_format\|overwrite\|mock" keras/saving/saving_api_test.py keras/models/model_test.py | head -40
```

tool result:

```
            legacy_h5_format.save_model_to_hdf5(
                self, filepath, overwrite, include_optimizer
            )
        else:
            raise ValueError(
                "Invalid filepath extension for saving. "
                "Please add either a `.keras` extension for the native Keras "
                f"format (recommended) or a `.h5` extension. "
                "Use `tf.saved_model.save()` if you want to export a "
                "SavedModel for use with TFLite/TFServing/etc. "
                f"Received: filepath={filepath}."
            )

    @traceback_utils.filter_traceback
    def save_weights(self, filepath, overwrite=True):
        """Saves all layer weights to a `.weights.h5` file.

        Args:
            filepath: `str` or `pathlib.Path` object.
                Path where to save the model. Must end in `.weights.h5`.
            overwrite: Whether we should overwrite any existing model
                at the target location, or instead ask the user
                via an interactive prompt.
        """
        if not str(filepath).endswith(".weights.h5"):
            raise ValueError(
                "The filename must end in `.weights.h5`. "
                f"Received: filepath={filepath}"
import inspect
import json
import os
import warnings

from keras import backend
from keras import utils
from keras.api_export import keras_export
from keras.layers.layer import Layer
from keras.legacy.saving import legacy_h5_format
from keras.models.variable_mapping import map_trackable_variables
from keras.saving import saving_api
from keras.saving import saving_lib
from keras.trainers import trainer as base_trainer
from keras.utils import io_utils
from keras.utils import summary_utils
from keras.utils import traceback_utils

if backend.backend() == "tensorflow":
    from keras.backend.tensorflow.trainer import TensorFlowTrainer as Trainer
elif backend.backend() == "jax":
    from keras.backend.jax.trainer import JAXTrainer as Trainer
elif backend.backend() == "torch":
    from keras.backend.torch.trainer import TorchTrainer as Trainer
elif backend.backend() == "numpy":
    from keras.backend.numpy.trainer import NumpyTrainer as Trainer
else:
    raise RuntimeError(
        f"Backend '{backend.backend()}' must implement the Trainer class."
    )
keras/saving/saving_api_test.py:2:import unittest.mock as mock
keras/saving/saving_api_test.py:32:    def test_invalid_save_format(self):
keras/saving/saving_api_test.py:33:        """Test deprecated save_format argument."""
keras/saving/saving_api_test.py:36:            ValueError, "The `save_format` argument is deprecated"
keras/saving/saving_api_test.py:38:            saving_api.save_model(model, "model.txt", save_format=True)
keras/saving/saving_api_test.py:166:    def test_h5_deprecation_warning(self):
keras/saving/saving_api_test.py:167:        """Test deprecation warning for h5 format."""
keras/saving/saving_api_test.py:171:        with mock.patch.object(logging, "warning") as mock_warn:
keras/saving/saving_api_test.py:173:            mock_warn.assert_called_once_with(
```

**tool call: Bash**

```bash
cd /work/keras-team__keras-18871/repo; sed -n 1,60p keras/saving/saving_api_test.py; sed -n 155,200p keras/saving/saving_api_test.py; grep -rn "\.save(" keras/models/model_test.py | head
```

tool result:

```
import os
import unittest.mock as mock

import numpy as np
from absl import logging

from keras import layers
from keras.models import Sequential
from keras.saving import saving_api
from keras.testing import test_case


class SaveModelTests(test_case.TestCase):
    def get_model(self):
        return Sequential(
            [
                layers.Dense(5, input_shape=(3,)),
                layers.Softmax(),
            ]
        )

    def test_basic_saving(self):
        """Test basic model saving and loading."""
        model = self.get_model()
        filepath = os.path.join(self.get_temp_dir(), "test_model.keras")
        saving_api.save_model(model, filepath)

        loaded_model = saving_api.load_model(filepath)
        x = np.random.uniform(size=(10, 3))
        self.assertTrue(np.allclose(model.predict(x), loaded_model.predict(x)))

    def test_invalid_save_format(self):
        """Test deprecated save_format argument."""
        model = self.get_model()
        with self.assertRaisesRegex(
            ValueError, "The `save_format` argument is deprecated"
        ):
            saving_api.save_model(model, "model.txt", save_format=True)

    def test_unsupported_arguments(self):
        """Test unsupported argument during model save."""
        model = self.get_model()
        filepath = os.path.join(self.get_temp_dir(), "test_model.keras")
        with self.assertRaisesRegex(
            ValueError, r"The following argument\(s\) are not supported"
        ):
            saving_api.save_model(model, filepath, random_arg=True)

    def test_save_h5_format(self):
        """Test saving model in h5 format."""
        model = self.get_model()
        filepath_h5 = os.path.join(self.get_temp_dir(), "test_model.h5")
        saving_api.save_model(model, filepath_h5)
        self.assertTrue(os.path.exists(filepath_h5))
        os.remove(filepath_h5)

    def test_save_unsupported_extension(self):
        """Test saving model with unsupported extension."""
        model = self.get_model()
        with self.assertRaisesRegex(


class SaveModelTestsWarning(test_case.TestCase):
    def get_model(self):
        return Sequential(
            [
                layers.Dense(5, input_shape=(3,)),
                layers.Softmax(),
            ]
        )

    def test_h5_deprecation_warning(self):
        """Test deprecation warning for h5 format."""
        model = self.get_model()
        filepath = os.path.join(self.get_temp_dir(), "test_model.h5")

        with mock.patch.object(logging, "warning") as mock_warn:
            saving_api.save_model(model, filepath)
            mock_warn.assert_called_once_with(
                "You are saving your model as an HDF5 file via `model.save()`. "
                "This file format is considered legacy. "
                "We recommend using instead the native Keras format, "
                "e.g. `model.save('my_model.keras')`."
            )
```

**tool call: Bash**

```bash
cd /work/keras-team__keras-18871/repo; grep -rn "save_format\|assertWarns\|HDF5 file via" keras --include=*_test.py | head -20
```

tool result:

```
(eval):1: no matches found: --include=*_test.py
```

**tool call: Bash**

```bash
cd /work/keras-team__keras-18871/repo; grep -rn "save_format\|assertWarns\|HDF5 file via" keras --include='*_test.py' | head -20
```

tool result:

```
keras/layers/core/input_layer_test.py:117:        with self.assertWarnsRegex(
keras/backend/common/backend_utils_test.py:213:        with self.assertWarns(Warning):
keras/saving/saving_api_test.py:32:    def test_invalid_save_format(self):
keras/saving/saving_api_test.py:33:        """Test deprecated save_format argument."""
keras/saving/saving_api_test.py:36:            ValueError, "The `save_format` argument is deprecated"
keras/saving/saving_api_test.py:38:            saving_api.save_model(model, "model.txt", save_format=True)
keras/saving/saving_api_test.py:174:                "You are saving your model as an HDF5 file via `model.save()`. "
keras/saving/saving_lib_test.py:534:            saving_api.save_model(model, temp_filepath, save_format="keras")
keras/saving/saving_lib_test.py:579:            model.save(temp_filepath, save_format="keras")
keras/export/export_lib_test.py:663:        model.save(temp_model_filepath, save_format="keras_v3")
```

**tool call: Bash**

```bash
cd /work/keras-team__keras-18871/repo; sed -n 525,590p keras/saving/saving_lib_test.py; sed -n 655,670p keras/export/export_lib_test.py
```

tool result:

```
class SavingAPITest(testing.TestCase):
    def test_saving_api_errors(self):
        from keras.saving import saving_api

        model = _get_basic_functional_model()

        # Saving API errors
        temp_filepath = os.path.join(self.get_temp_dir(), "mymodel")
        with self.assertRaisesRegex(ValueError, "argument is deprecated"):
            saving_api.save_model(model, temp_filepath, save_format="keras")

        temp_filepath = os.path.join(self.get_temp_dir(), "mymodel.notkeras")
        with self.assertRaisesRegex(ValueError, "Invalid filepath extension"):
            saving_api.save_model(model, temp_filepath)

        temp_filepath = os.path.join(self.get_temp_dir(), "mymodel.keras")
        with self.assertRaisesRegex(ValueError, "are not supported"):
            saving_api.save_model(model, temp_filepath, invalid_arg="hello")

        # Loading API errors
        temp_filepath = os.path.join(self.get_temp_dir(), "non_existent.keras")
        with self.assertRaisesRegex(
            ValueError, "Please ensure the file is an accessible"
        ):
            _ = saving_api.load_model(temp_filepath)

        temp_filepath = os.path.join(self.get_temp_dir(), "my_saved_model")
        with self.assertRaisesRegex(ValueError, "File format not supported"):
            _ = saving_api.load_model(temp_filepath)

    def test_model_api_endpoint(self):
        temp_filepath = Path(os.path.join(self.get_temp_dir(), "mymodel.keras"))
        model = _get_basic_functional_model()
        ref_input = np.random.random((2, 4))
        ref_output = model.predict(ref_input)
        model.save(temp_filepath)
        model = keras.saving.load_model(temp_filepath)
        self.assertAllClose(model.predict(ref_input), ref_output, atol=1e-6)

    def test_model_api_endpoint_h5(self):
        temp_filepath = Path(os.path.join(self.get_temp_dir(), "mymodel.h5"))
        model = _get_basic_functional_model()
        ref_input = np.random.random((2, 4))
        ref_output = model.predict(ref_input)
        model.save(temp_filepath)
        model = keras.saving.load_model(temp_filepath)
        self.assertAllClose(model.predict(ref_input), ref_output, atol=1e-6)

    def test_model_api_errors(self):
        model = _get_basic_functional_model()

        # Saving API errors
        temp_filepath = os.path.join(self.get_temp_dir(), "mymodel")
        with self.assertRaisesRegex(ValueError, "argument is deprecated"):
            model.save(temp_filepath, save_format="keras")

        temp_filepath = os.path.join(self.get_temp_dir(), "mymodel.notkeras")
        with self.assertRaisesRegex(ValueError, "Invalid filepath extension"):
            model.save(temp_filepath)

        temp_filepath = os.path.join(self.get_temp_dir(), "mymodel.keras")
        with self.assertRaisesRegex(ValueError, "are not supported"):
            model.save(temp_filepath, invalid_arg="hello")

    def test_safe_mode(self):
        temp_filepath = os.path.join(self.get_temp_dir(), "unsafe_model.keras")
        # Test reinstantiation from config
        config = reloaded_layer.get_config()
        rereloaded_layer = export_lib.TFSMLayer.from_config(config)
        self.assertAllClose(rereloaded_layer(ref_input), ref_output, atol=1e-7)

        # Test whole model saving with reloaded layer inside
        model = models.Sequential([reloaded_layer])
        temp_model_filepath = os.path.join(self.get_temp_dir(), "m.keras")
        model.save(temp_model_filepath, save_format="keras_v3")
        reloaded_model = saving_lib.load_model(
            temp_model_filepath,
            custom_objects={"TFSMLayer": export_lib.TFSMLayer},
        )
        self.assertAllClose(reloaded_model(ref_input), ref_output, atol=1e-7)

    def test_errors(self):
```

**assistant:** Both functions implement the same logic separately. I'll make `Model.save()` delegate to `saving_api.save_model()`. First, a quick repro confirming `model.save` doesn't route through `saving_api`:

**tool call: Bash**

```bash
cd /work/keras-team__keras-18871/repo; cat > repro_save.py <<'EOF'
from unittest import mock
from keras import layers, Sequential
from keras.saving import saving_api
m = Sequential([layers.Dense(2, input_shape=(3,))])
with mock.patch.object(saving_api, "save_model") as sm:
    m.save("/tmp/x.keras")
    print("delegated:", sm.called)
EOF
../bin/envrun 'python repro_save.py 2>&1 | tail -2'
```

tool result:

```
2026-10-09 04:18:45.402757: E external/local_xla/xla/stream_executor/cuda/cuda_platform.cc:51] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)
delegated: False
```

**assistant:** Now replace the duplicated body with a delegation:

**tool call: Bash**

```bash
cd /work/keras-team__keras-18871/repo; python3 - <<'EOF'
p = "keras/models/model.py"
s = open(p).read()
start = s.index('        include_optimizer = kwargs.pop("include_optimizer", True)\n        save_format = kwargs.pop("save_format", None)')
end = s.index('    @traceback_utils.filter_traceback\n    def save_weights')
s = s[:start] + "        return saving_api.save_model(self, filepath, overwrite, **kwargs)\n\n" + s[end:]
open(p, "w").write(s)
EOF
sed -n 260,312p keras/models/model.py; grep -n "warnings\.\|legacy_h5_format\|saving_lib\.\|io_utils\.\|os\." keras/models/model.py
```

tool result:

````
            positions=positions,
            print_fn=print_fn,
            expand_nested=expand_nested,
            show_trainable=show_trainable,
            layer_range=layer_range,
        )

    @traceback_utils.filter_traceback
    def save(self, filepath, overwrite=True, **kwargs):
        """Saves a model as a `.keras` file.

        Args:
            filepath: `str` or `pathlib.Path` object.
                Path where to save the model. Must end in `.keras`.
            overwrite: Whether we should overwrite any existing model
                at the target location, or instead ask the user
                via an interactive prompt.
            save_format: Format to use, as a string. Only the `"keras"`
                format is supported at this time.

        Example:

        ```python
        model = keras.Sequential(
            [
                keras.layers.Dense(5, input_shape=(3,)),
                keras.layers.Softmax(),
            ],
        )
        model.save("model.keras")
        loaded_model = keras.saving.load_model("model.keras")
        x = keras.random.uniform((10, 3))
        assert np.allclose(model.predict(x), loaded_model.predict(x))
        ```

        Note that `model.save()` is an alias for
        `keras.saving.save_model()`.

        The saved `.keras` file contains:

        - The model's configuration (architecture)
        - The model's weights
        - The model's optimizer's state (if any)

        Thus models can be reinstantiated in the exact same state.
        """
        return saving_api.save_model(self, filepath, overwrite, **kwargs)

    @traceback_utils.filter_traceback
    def save_weights(self, filepath, overwrite=True):
        """Saves all layer weights to a `.weights.h5` file.

        Args:
10:from keras.legacy.saving import legacy_h5_format
325:            exists = os.path.exists(filepath)
329:            proceed = io_utils.ask_to_proceed_with_overwrite(filepath)
332:        saving_lib.save_weights_only(self, filepath)
395:            warnings.warn(
````

**assistant:** `legacy_h5_format` is now unused in model.py; remove the import, then rerun the repro and tests.

**tool call: Bash**

```bash
cd /work/keras-team__keras-18871/repo; sed -i '' '/^from keras.legacy.saving import legacy_h5_format$/d' keras/models/model.py
../bin/envrun 'python repro_save.py 2>&1 | tail -1; flake8 keras/models/model.py; python -m pytest -q keras/saving keras/models 2>&1 | tail -5'
```

tool result:

```
delegated: True
bash: line 1: flake8: command not found
keras/models/sequential_test.py::SequentialTest::test_serialization PASSED [ 98%]
keras/models/sequential_test.py::SequentialTest::test_shape_inference_failure PASSED [ 99%]
keras/models/variable_mapping_test.py::VariableMappingTest::test_basics PASSED [100%]

============================= 124 passed in 15.40s =============================
```

**tool call: Bash**

```bash
cd /work/keras-team__keras-18871/repo; rm repro_save.py; ../bin/envrun 'python -m pytest -q keras/legacy/saving keras/export/export_lib_test.py keras/callbacks/model_checkpoint_test.py 2>&1 | tail -2'; git status --short
```

tool result:

```
FAILED keras/callbacks/model_checkpoint_test.py::ModelCheckpointTest::test_model_checkpoint_options
=================== 2 failed, 26 passed, 1 skipped in 4.73s ====================

 M keras/models/model.py
?? Dockerfile
```

**tool call: Bash**

```bash
cd /work/keras-team__keras-18871/repo; ../bin/envrun 'python -m pytest -q keras/legacy/saving keras/export/export_lib_test.py keras/callbacks/model_checkpoint_test.py 2>&1 | grep -E "FAILED|Error" | head; git stash -q; python -m pytest -q keras/legacy/saving keras/export/export_lib_test.py keras/callbacks/model_checkpoint_test.py 2>&1 | tail -3; git stash pop -q'
```

tool result:

```
keras/callbacks/model_checkpoint_test.py::ModelCheckpointTest::test_model_checkpoint_loading FAILED [ 96%]
keras/callbacks/model_checkpoint_test.py::ModelCheckpointTest::test_model_checkpoint_options FAILED [100%]
            raise AttributeError("`numpy.array_api` is not available from "
                raise AttributeError("`numpy.distutils` is not available from "
            # the AttributeError
            raise AttributeError(__former_attrs__[attr])
>           raise AttributeError(
E           AttributeError: `np.Inf` was removed in the NumPy 2.0 release. Use `np.inf` instead.
/usr/local/lib/python3.9/site-packages/numpy/__init__.py:397: AttributeError
            raise AttributeError("`numpy.array_api` is not available from "
FAILED keras/callbacks/model_checkpoint_test.py::ModelCheckpointTest::test_model_checkpoint_loading
FAILED keras/callbacks/model_checkpoint_test.py::ModelCheckpointTest::test_model_checkpoint_options
=================== 2 failed, 26 passed, 1 skipped in 4.52s ====================
```

**assistant:** `Model.save()` now just calls `keras.saving.save_model()`, so the saving logic lives in one place.

**Change, all in `keras/models/model.py`:**
- I replaced the copied body of `Model.save()` with `return saving_api.save_model(self, filepath, overwrite, **kwargs)` and kept its docstring. That docstring already called the method an alias, and now it really is one.
- I removed the `legacy_h5_format` import, which nothing else in that file used.

**Behaviour differences:** the two copies had already drifted apart, which was the issue's point. `model.save()` now behaves exactly like `save_model()`:
- The deprecation warnings for `save_format` and for saving to `.h5` now go through `absl.logging.warning` instead of Python's `warnings.warn`. The existing saving tests already expect the logging version.
- For `.h5` files, the "ask before overwriting" check is now done inside the legacy HDF5 saver rather than up front in `model.save()`. The overwrite behaviour itself is the same.

**Checks:**
- **Repro:** a small script mocked `saving_api.save_model` and called `model.save()`. Before the fix it printed `delegated: False`, and after it printed `delegated: True`. I deleted the script afterwards.
- **Main suites:** `keras/saving` and `keras/models` pass (124 tests).
- **Related suites:** `keras/legacy/saving`, the export tests and the model-checkpoint tests give 26 passed, 1 skipped and 2 failed. The 2 failures are in `model_checkpoint_test.py` and come from `np.Inf`, which no longer exists in NumPy 2.0, the version in the container. They fail the same way with my change removed, so they aren't caused by it.
- **Lint:** I couldn't run flake8 because it isn't installed in the container.

There's an untracked `Dockerfile` in the repo that I didn't create, and I left it alone.

_session end: success, turns 12, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 6.03 s: python repro_save.py 2>&1 | tail -2
- `rc=0` 23.18 s: python repro_save.py 2>&1 | tail -1; flake8 keras/models/model.py; python -m pytest -q keras/saving keras/models 2>&1 | tail -5
- `rc=0` 8.91 s: python -m pytest -q keras/legacy/saving keras/export/export_lib_test.py keras/callbacks/model_checkpoint_test.py 2>&1 | tail -2
- `rc=0` 17.6 s: python -m pytest -q keras/legacy/saving keras/export/export_lib_test.py keras/callbacks/model_checkpoint_test.py 2>&1 | grep -E "FAILED|Error" | head; git stash -q; python -m pytest -q keras/legacy/saving keras/export/export_lib_test.py keras/callbacks/model_checkpoint_test.py 2>&1 | tail -3; git stash pop -q
