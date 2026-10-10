# Instance: huggingface__transformers-22158

- Final resolved (evaluator, logs/huggingface__transformers-22158_result.json): True
- Run state: DONE
- One attempt. Duration 175.9 s, turns 20, actor cost $0.5449362, container commands 12
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/huggingface__transformers-22158/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-22158/repo. Consider the following issue description:

<issue_description>
OneFormerProcessor、MaskFormerImageProcessor will cause errors if segmentation_maps only have elements 0 and 1
### System Info

transformers-4.26.0  do not have this bug
but transformers-4.27.0.dev0 has.

### Who can help?

_No response_

### Information

- [ ] The official example scripts
- [X] My own modified scripts

### Tasks

- [ ] An officially supported task in the `examples` folder (such as GLUE/SQuAD, ...)
- [X] My own task or dataset (give details below)

### Reproduction

```python
from transformers import OneFormerProcessor, OneFormerForUniversalSegmentation, OneFormerImageProcessor, OneFormerConfig
from transformers import Mask2FormerImageProcessor, Mask2FormerForUniversalSegmentation
from PIL import Image
import requests
import torch
import numpy as np
import matplotlib

processor = OneFormerProcessor.from_pretrained("shi-labs/oneformer_ade20k_swin_tiny",num_text=134,do_reduce_labels=True,)

image_np=np.random.randint(0,255,(3,512,512))

#segmentation_maps only have elements 0 and 1
segmentation_maps = torch.randint(0, 2, (image_np.shape[1], image_np.shape[2]), dtype=torch.long)

inst2class={1: 4}

raw_inputs=processor.image_processor([image_np],
                   task_inputs=["panoptic"],
                   segmentation_maps=[segmentation_maps],
                   return_tensors="pt",
                   instance_id_to_semantic_id=inst2class,
                   do_reduce_labels=True,
                   ignore_index=None)

```
#ERROR
```
E:\condaenv\yaogan\lib\site-packages\transformers\models\oneformer\image_processing_oneformer.py:419: FutureWarning: The `reduce_labels` argument is deprecated and will be removed in v4.27. Please use `do_reduce_labels` instead.
  warnings.warn(
Traceback (most recent call last):
  File "E:\condaenv\yaogan\lib\site-packages\IPython\core\interactiveshell.py", line 3460, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-2-ed9733992fe8>", line 23, in <module>
    raw_inputs=processor.image_processor([image_np],
  File "E:\condaenv\yaogan\lib\site-packages\transformers\models\oneformer\image_processing_oneformer.py", line 524, in __call__
    return self.preprocess(images, task_inputs=task_inputs, segmentation_maps=segmentation_maps, **kwargs)
  File "E:\condaenv\yaogan\lib\site-packages\transformers\models\oneformer\image_processing_oneformer.py", line 708, in preprocess
    encoded_inputs = self.encode_inputs(
  File "E:\condaenv\yaogan\lib\site-packages\transformers\models\oneformer\image_processing_oneformer.py", line 962, in encode_inputs
    masks, classes = self.convert_segmentation_map_to_binary_masks(
  File "E:\condaenv\yaogan\lib\site-packages\transformers\models\oneformer\image_processing_oneformer.py", line 516, in convert_segmentation_map_to_binary_masks
    return convert_segmentation_map_to_binary_masks(
  File "E:\condaenv\yaogan\lib\site-packages\transformers\models\oneformer\image_processing_oneformer.py", line 288, in convert_segmentation_map_to_binary_masks
    class_id = instance_id_to_semantic_id[label + 1 if reduce_labels else label]
KeyError: 255
```
This bug is caused by a **resize** function of OneFormerProcessor, which convert segmentation_maps to PIL.Image and then convert to np.ndarray. After **resize**, segmentation_maps have elements 0 and 255, so the bug arise. 

### Expected behavior

fix this bug before release 4.27.0 as stable version
transformers-4.26.0  do not have this bug

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-22158/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-22158/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-22158/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-22158/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/huggingface__transformers-22158/repo; grep -n "def to_pil_image" -A50 src/transformers/image_transforms.py; grep -n "def resize" -A70 src/transformers/image_transforms.py | grep -n "pil\|rescale"
```

tool result:

```
121:def to_pil_image(
122-    image: Union[np.ndarray, "PIL.Image.Image", "torch.Tensor", "tf.Tensor", "jnp.ndarray"],
123-    do_rescale: Optional[bool] = None,
124-) -> "PIL.Image.Image":
125-    """
126-    Converts `image` to a PIL Image. Optionally rescales it and puts the channel dimension back as the last axis if
127-    needed.
128-
129-    Args:
130-        image (`PIL.Image.Image` or `numpy.ndarray` or `torch.Tensor` or `tf.Tensor`):
131-            The image to convert to the `PIL.Image` format.
132-        do_rescale (`bool`, *optional*):
133-            Whether or not to apply the scaling factor (to make pixel values integers between 0 and 255). Will default
134-            to `True` if the image type is a floating type and casting to `int` would result in a loss of precision,
135-            and `False` otherwise.
136-
137-    Returns:
138-        `PIL.Image.Image`: The converted image.
139-    """
140-    requires_backends(to_pil_image, ["vision"])
141-
142-    if isinstance(image, PIL.Image.Image):
143-        return image
144-
145-    # Convert all tensors to numpy arrays before converting to PIL image
146-    if is_torch_tensor(image) or is_tf_tensor(image):
147-        image = image.numpy()
148-    elif is_jax_tensor(image):
149-        image = np.array(image)
150-    elif not isinstance(image, np.ndarray):
151-        raise ValueError("Input image type not supported: {}".format(type(image)))
152-
153-    # If the channel as been moved to first dim, we put it back at the end.
154-    image = to_channel_dimension_format(image, ChannelDimension.LAST)
155-
156-    # If there is a single channel, we squeeze it, as otherwise PIL can't handle it.
157-    image = np.squeeze(image, axis=-1) if image.shape[-1] == 1 else image
158-
159-    # PIL.Image can only store uint8 values, so we rescale the image to be between 0 and 255 if needed.
160-    if do_rescale is None:
161-        if np.all(0 <= image) and np.all(image <= 1):
162-            do_rescale = True
163-        elif np.allclose(image, image.astype(int)):
164-            do_rescale = False
165-        else:
166-            raise ValueError(
167-                "The image to be converted to a PIL image contains values outside the range [0, 1], "
168-                f"got [{image.min()}, {image.max()}] which cannot be converted to uint8."
169-            )
170-
171-    if do_rescale:
43:285-    # the pillow library to resize the image and then convert back to numpy
45:287-        image = to_pil_image(image)
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; grep -n "def resize" -A75 src/transformers/image_transforms.py
```

tool result:

```
243:def resize(
244-    image,
245-    size: Tuple[int, int],
246-    resample: "PILImageResampling" = None,
247-    reducing_gap: Optional[int] = None,
248-    data_format: Optional[ChannelDimension] = None,
249-    return_numpy: bool = True,
250-) -> np.ndarray:
251-    """
252-    Resizes `image` to `(height, width)` specified by `size` using the PIL library.
253-
254-    Args:
255-        image (`PIL.Image.Image` or `np.ndarray` or `torch.Tensor`):
256-            The image to resize.
257-        size (`Tuple[int, int]`):
258-            The size to use for resizing the image.
259-        resample (`int`, *optional*, defaults to `PILImageResampling.BILINEAR`):
260-            The filter to user for resampling.
261-        reducing_gap (`int`, *optional*):
262-            Apply optimization by resizing the image in two steps. The bigger `reducing_gap`, the closer the result to
263-            the fair resampling. See corresponding Pillow documentation for more details.
264-        data_format (`ChannelDimension`, *optional*):
265-            The channel dimension format of the output image. If unset, will use the inferred format from the input.
266-        return_numpy (`bool`, *optional*, defaults to `True`):
267-            Whether or not to return the resized image as a numpy array. If False a `PIL.Image.Image` object is
268-            returned.
269-
270-    Returns:
271-        `np.ndarray`: The resized image.
272-    """
273-    requires_backends(resize, ["vision"])
274-
275-    resample = resample if resample is not None else PILImageResampling.BILINEAR
276-
277-    if not len(size) == 2:
278-        raise ValueError("size must have 2 elements")
279-
280-    # For all transformations, we want to keep the same data format as the input image unless otherwise specified.
281-    # The resized image from PIL will always have channels last, so find the input format first.
282-    data_format = infer_channel_dimension_format(image) if data_format is None else data_format
283-
284-    # To maintain backwards compatibility with the resizing done in previous image feature extractors, we use
285-    # the pillow library to resize the image and then convert back to numpy
286-    if not isinstance(image, PIL.Image.Image):
287-        image = to_pil_image(image)
288-    height, width = size
289-    # PIL images are in the format (width, height)
290-    resized_image = image.resize((width, height), resample=resample, reducing_gap=reducing_gap)
291-
292-    if return_numpy:
293-        resized_image = np.array(resized_image)
294-        # If the input image channel dimension was of size 1, then it is dropped when converting to a PIL image
295-        # so we need to add it back if necessary.
296-        resized_image = np.expand_dims(resized_image, axis=-1) if resized_image.ndim == 2 else resized_image
297-        # The image is always in channels last format after converting from a PIL image
298-        resized_image = to_channel_dimension_format(
299-            resized_image, data_format, input_channel_dim=ChannelDimension.LAST
300-        )
301-    return resized_image
302-
303-
304-def normalize(
305-    image: np.ndarray,
306-    mean: Union[float, Iterable[float]],
307-    std: Union[float, Iterable[float]],
308-    data_format: Optional[ChannelDimension] = None,
309-) -> np.ndarray:
310-    """
311-    Normalizes `image` using the mean and standard deviation specified by `mean` and `std`.
312-
313-    image = (image - mean) / std
314-
315-    Args:
316-        image (`np.ndarray`):
317-            The image to normalize.
318-        mean (`float` or `Iterable[float]`):
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; sed -n 165,185p src/transformers/image_transforms.py; grep -n "to_pil_image\|def test_resize" -A3 tests/test_image_transforms.py | head -80
```

tool result:

```
        else:
            raise ValueError(
                "The image to be converted to a PIL image contains values outside the range [0, 1], "
                f"got [{image.min()}, {image.max()}] which cannot be converted to uint8."
            )

    if do_rescale:
        image = rescale(image, 255)

    image = image.astype(np.uint8)
    return PIL.Image.fromarray(image)


# Logic adapted from torchvision resizing logic: https://github.com/pytorch/vision/blob/511924c1ced4ce0461197e5caa64ce5b9e558aab/torchvision/transforms/functional.py#L366
def get_resize_output_image_size(
    input_image: np.ndarray,
    size: Union[int, Tuple[int, int], List[int], Tuple[int]],
    default_to_square: bool = True,
    max_size: Optional[int] = None,
) -> tuple:
    """
49:        to_pil_image,
50-    )
51-
52-
--
72:    def test_to_pil_image(self, name, image_shape, dtype):
73-        image = np.random.randint(0, 256, image_shape).astype(dtype)
74:        pil_image = to_pil_image(image)
75-        self.assertIsInstance(pil_image, PIL.Image.Image)
76-        self.assertEqual(pil_image.size, (5, 4))
77-
--
90:    def test_to_pil_image_from_float(self, name, image_shape, dtype):
91-        image = np.random.rand(*image_shape).astype(dtype)
92:        pil_image = to_pil_image(image)
93-        self.assertIsInstance(pil_image, PIL.Image.Image)
94-        self.assertEqual(pil_image.size, (5, 4))
95-
--
102:            to_pil_image(image)
103-
104-    @require_tf
105:    def test_to_pil_image_from_tensorflow(self):
106-        # channels_first
107-        image = tf.random.uniform((3, 4, 5))
108:        pil_image = to_pil_image(image)
109-        self.assertIsInstance(pil_image, PIL.Image.Image)
110-        self.assertEqual(pil_image.size, (5, 4))
111-
--
114:        pil_image = to_pil_image(image)
115-        self.assertIsInstance(pil_image, PIL.Image.Image)
116-        self.assertEqual(pil_image.size, (5, 4))
117-
--
119:    def test_to_pil_image_from_torch(self):
120-        # channels first
121-        image = torch.rand((3, 4, 5))
122:        pil_image = to_pil_image(image)
123-        self.assertIsInstance(pil_image, PIL.Image.Image)
124-        self.assertEqual(pil_image.size, (5, 4))
125-
--
128:        pil_image = to_pil_image(image)
129-        self.assertIsInstance(pil_image, PIL.Image.Image)
130-        self.assertEqual(pil_image.size, (5, 4))
131-
--
133:    def test_to_pil_image_from_jax(self):
134-        key = jax.random.PRNGKey(0)
135-        # channel first
136-        image = jax.random.uniform(key, (3, 4, 5))
137:        pil_image = to_pil_image(image)
138-        self.assertIsInstance(pil_image, PIL.Image.Image)
139-        self.assertEqual(pil_image.size, (5, 4))
140-
--
143:        pil_image = to_pil_image(image)
144-        self.assertIsInstance(pil_image, PIL.Image.Image)
145-        self.assertEqual(pil_image.size, (5, 4))
146-
--
212:    def test_resize(self):
213-        image = np.random.randint(0, 256, (3, 224, 224))
214-
215-        # Check the channel order is the same by default
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; sed -n 60,103p tests/test_image_transforms.py; sed -n 210,260p tests/test_image_transforms.py
```

tool result:

```
class ImageTransformsTester(unittest.TestCase):
    @parameterized.expand(
        [
            ("numpy_float_channels_first", (3, 4, 5), np.float32),
            ("numpy_float_channels_last", (4, 5, 3), np.float32),
            ("numpy_float_channels_first", (3, 4, 5), np.float64),
            ("numpy_float_channels_last", (4, 5, 3), np.float64),
            ("numpy_int_channels_first", (3, 4, 5), np.int32),
            ("numpy_uint_channels_first", (3, 4, 5), np.uint8),
        ]
    )
    @require_vision
    def test_to_pil_image(self, name, image_shape, dtype):
        image = np.random.randint(0, 256, image_shape).astype(dtype)
        pil_image = to_pil_image(image)
        self.assertIsInstance(pil_image, PIL.Image.Image)
        self.assertEqual(pil_image.size, (5, 4))

        # make sure image is correctly rescaled
        self.assertTrue(np.abs(np.asarray(pil_image)).sum() > 0)

    @parameterized.expand(
        [
            ("numpy_float_channels_first", (3, 4, 5), np.float32),
            ("numpy_float_channels_first", (3, 4, 5), np.float64),
            ("numpy_float_channels_last", (4, 5, 3), np.float32),
            ("numpy_float_channels_last", (4, 5, 3), np.float64),
        ]
    )
    @require_vision
    def test_to_pil_image_from_float(self, name, image_shape, dtype):
        image = np.random.rand(*image_shape).astype(dtype)
        pil_image = to_pil_image(image)
        self.assertIsInstance(pil_image, PIL.Image.Image)
        self.assertEqual(pil_image.size, (5, 4))

        # make sure image is correctly rescaled
        self.assertTrue(np.abs(np.asarray(pil_image)).sum() > 0)

        # Make sure that an exception is raised if image is not in [0, 1]
        image = np.random.randn(*image_shape).astype(dtype)
        with self.assertRaises(ValueError):
            to_pil_image(image)

        self.assertEqual(resized_image.shape, (3, 3, 20))

    def test_resize(self):
        image = np.random.randint(0, 256, (3, 224, 224))

        # Check the channel order is the same by default
        resized_image = resize(image, (30, 40))
        self.assertIsInstance(resized_image, np.ndarray)
        self.assertEqual(resized_image.shape, (3, 30, 40))

        # Check channel order is changed if specified
        resized_image = resize(image, (30, 40), data_format="channels_last")
        self.assertIsInstance(resized_image, np.ndarray)
        self.assertEqual(resized_image.shape, (30, 40, 3))

        # Check PIL.Image.Image is return if return_numpy=False
        resized_image = resize(image, (30, 40), return_numpy=False)
        self.assertIsInstance(resized_image, PIL.Image.Image)
        # PIL size is in (width, height) order
        self.assertEqual(resized_image.size, (40, 30))

    def test_normalize(self):
        image = np.random.randint(0, 256, (224, 224, 3)) / 255

        # Test that exception is raised if inputs are incorrect
        # Not a numpy array image
        with self.assertRaises(ValueError):
            normalize(5, 5, 5)

        # Number of mean values != number of channels
        with self.assertRaises(ValueError):
            normalize(image, mean=(0.5, 0.6), std=1)

        # Number of std values != number of channels
        with self.assertRaises(ValueError):
            normalize(image, mean=1, std=(0.5, 0.6))

        # Test result is correct - output data format is channels_first and normalization
        # correctly computed
        mean = (0.5, 0.6, 0.7)
        std = (0.1, 0.2, 0.3)
        expected_image = ((image - mean) / std).transpose((2, 0, 1))

        normalized_image = normalize(image, mean=mean, std=std, data_format="channels_first")
        self.assertIsInstance(normalized_image, np.ndarray)
        self.assertEqual(normalized_image.shape, (3, 224, 224))
        self.assertTrue(np.allclose(normalized_image, expected_image))

    def test_center_crop(self):
        image = np.random.randint(0, 256, (3, 224, 224))
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; cat > /tmp/repro.py <<'EOF'
import numpy as np
from transformers import MaskFormerImageProcessor, OneFormerImageProcessor
from transformers.image_transforms import resize
seg = np.random.randint(0, 2, (512, 512))
print(np.unique(resize(seg[None], (256, 256), resample=0)))
p = MaskFormerImageProcessor(do_reduce_labels=False)
img = np.random.randint(0, 255, (3, 512, 512))
out = p([img], segmentation_maps=[seg], instance_id_to_semantic_id={0: 3, 1: 4}, return_tensors="pt")
print(out["class_labels"])
f = np.random.rand(3, 64, 64)
r = resize(f, (32, 32))
print(r.dtype, r.min(), r.max())
EOF
cp /tmp/repro.py repro_tmp.py; ../bin/envrun 'python repro_tmp.py' 2>&1 | tail -5
```

tool result:

```
(eval):1: operation not permitted: /tmp/repro.py
cp: /tmp/repro.py: No such file or directory
python: can't open file '/testbed/repro_tmp.py': [Errno 2] No such file or directory
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; cat > repro_tmp.py <<'EOF'
import numpy as np
from transformers import MaskFormerImageProcessor, OneFormerImageProcessor
from transformers.image_transforms import resize
seg = np.random.randint(0, 2, (512, 512))
print(np.unique(resize(seg[None], (256, 256), resample=0)))
p = MaskFormerImageProcessor(do_reduce_labels=False)
img = np.random.randint(0, 255, (3, 512, 512))
out = p([img], segmentation_maps=[seg], instance_id_to_semantic_id={0: 3, 1: 4}, return_tensors="pt")
print(out["class_labels"])
f = np.random.rand(3, 64, 64)
r = resize(f, (32, 32))
print(r.dtype, r.min(), r.max())
EOF
../bin/envrun 'python repro_tmp.py' 2>&1 | tail -5
```

tool result:

```
    return convert_segmentation_map_to_binary_masks(
  File "/testbed/src/transformers/models/maskformer/image_processing_maskformer.py", line 291, in convert_segmentation_map_to_binary_masks
    class_id = instance_id_to_semantic_id[label + 1 if reduce_labels else label]
KeyError: np.uint8(255)
```

**thinking:**

```
I've confirmed the bug: `to_pil_image` wrongly treats an integer 0/1 map as a float image in [0,1] and scales it by 255. I'll fix this by preventing integer-valued images from being rescaled, while having `resize` undo the rescale for float images.


```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; python3 - <<'EOF'
p = "src/transformers/image_transforms.py"
s = open(p).read()
old = """    # PIL.Image can only store uint8 values, so we rescale the image to be between 0 and 255 if needed.
    if do_rescale is None:
        if np.all(0 <= image) and np.all(image <= 1):
            do_rescale = True
        elif np.allclose(image, image.astype(int)):
            do_rescale = False
        else:
            raise ValueError(
                "The image to be converted to a PIL image contains values outside the range [0, 1], "
                f"got [{image.min()}, {image.max()}] which cannot be converted to uint8."
            )

"""
new = """    # PIL.Image can only store uint8 values so we rescale the image to be between 0 and 255 if needed.
    do_rescale = _rescale_for_pil_conversion(image) if do_rescale is None else do_rescale

"""
assert old in s
s = s.replace(old, new)
old2 = """def to_pil_image(
"""
new2 = '''def _rescale_for_pil_conversion(image):
    """
    Detects whether or not the image needs to be rescaled before being converted to a PIL image.

    The assumption is that if the image is of type `np.float` and all values are between 0 and 1, it needs to be
    rescaled.
    """
    if image.dtype == np.uint8:
        do_rescale = False
    elif np.allclose(image, image.astype(int)):
        if np.all(0 <= image) and np.all(image <= 255):
            do_rescale = False
        else:
            raise ValueError(
                "The image to be converted to a PIL image contains values outside the range [0, 255], "
                f"got [{image.min()}, {image.max()}] which cannot be converted to uint8."
            )
    elif np.all(0 <= image) and np.all(image <= 1):
        do_rescale = True
    else:
        raise ValueError(
            "The image to be converted to a PIL image contains values outside the range [0, 1], "
            f"got [{image.min()}, {image.max()}] which cannot be converted to uint8."
        )
    return do_rescale


def to_pil_image(
'''
s = s.replace(old2, new2, 1)
old3 = """    if not isinstance(image, PIL.Image.Image):
        image = to_pil_image(image)
    height, width = size"""
new3 = """    do_rescale = False
    if not isinstance(image, PIL.Image.Image):
        do_rescale = _rescale_for_pil_conversion(image)
        image = to_pil_image(image, do_rescale=do_rescale)
    height, width = size"""
assert old3 in s
s = s.replace(old3, new3)
old4 = """            resized_image, data_format, input_channel_dim=ChannelDimension.LAST
        )
    return resized_image"""
new4 = """            resized_image, data_format, input_channel_dim=ChannelDimension.LAST
        )
        # If an image was rescaled to be in the range [0, 255] before converting to a PIL image, then we need to
        # rescale it back to the original range.
        resized_image = rescale(resized_image, 1 / 255) if do_rescale else resized_image
    return resized_image"""
assert old4 in s
s = s.replace(old4, new4)
open(p, "w").write(s)
EOF
../bin/envrun 'python repro_tmp.py' 2>&1 | tail -5
```

tool result:

```
    constant_values = _expand_for_data_format(constant_values)
  File "/testbed/src/transformers/image_transforms.py", line 701, in _expand_for_data_format
    raise ValueError(f"Unsupported format: {values}")
ValueError: Unsupported format: None
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; ../bin/envrun 'python repro_tmp.py' 2>&1 | tail -25; git stash -q; ../bin/envrun 'python -c "
import numpy as np
from transformers import MaskFormerImageProcessor
p = MaskFormerImageProcessor(do_reduce_labels=False)
seg = np.random.randint(0, 3, (512, 512))
out = p([np.random.randint(0, 255, (3, 512, 512))], segmentation_maps=[seg], instance_id_to_semantic_id={0: 3, 1: 4, 2:5}, return_tensors=\"pt\")
print(out[\"class_labels\"])
"' 2>&1 | tail -3; git stash pop -q
```

tool result:

```
[0 1]
Traceback (most recent call last):
  File "/testbed/repro_tmp.py", line 8, in <module>
    out = p([img], segmentation_maps=[seg], instance_id_to_semantic_id={0: 3, 1: 4}, return_tensors="pt")
  File "/testbed/src/transformers/models/maskformer/image_processing_maskformer.py", line 565, in __call__
    return self.preprocess(images, segmentation_maps=segmentation_maps, **kwargs)
  File "/testbed/src/transformers/models/maskformer/image_processing_maskformer.py", line 751, in preprocess
    encoded_inputs = self.encode_inputs(
  File "/testbed/src/transformers/models/maskformer/image_processing_maskformer.py", line 902, in encode_inputs
    masks = [
  File "/testbed/src/transformers/models/maskformer/image_processing_maskformer.py", line 903, in <listcomp>
    self._pad_image(image=mask, output_size=pad_size, constant_values=ignore_index) for mask in masks
  File "/testbed/src/transformers/models/maskformer/image_processing_maskformer.py", line 773, in _pad_image
    padded_image = pad(
  File "/testbed/src/transformers/image_transforms.py", line 713, in pad
    constant_values = _expand_for_data_format(constant_values)
  File "/testbed/src/transformers/image_transforms.py", line 701, in _expand_for_data_format
    raise ValueError(f"Unsupported format: {values}")
ValueError: Unsupported format: None

    raise ValueError(f"Unsupported format: {values}")
ValueError: Unsupported format: None
```

**thinking:**

```
The resize fix worked, but now there's a separate pre-existing bug in `pad` with `constant_values=None`. I'll trace how `ignore_index` flows into the padding logic.


```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; grep -n "ignore_index" src/transformers/models/maskformer/image_processing_maskformer.py src/transformers/models/oneformer/image_processing_oneformer.py src/transformers/models/mask2former/image_processing_mask2former.py | grep -v '^\s*#'
```

tool result:

```
src/transformers/models/maskformer/image_processing_maskformer.py:266:    ignore_index: Optional[int] = None,
src/transformers/models/maskformer/image_processing_maskformer.py:269:    if reduce_labels and ignore_index is None:
src/transformers/models/maskformer/image_processing_maskformer.py:270:        raise ValueError("If `reduce_labels` is True, `ignore_index` must be provided.")
src/transformers/models/maskformer/image_processing_maskformer.py:273:        segmentation_map = np.where(segmentation_map == 0, ignore_index, segmentation_map - 1)
src/transformers/models/maskformer/image_processing_maskformer.py:279:    if ignore_index is not None:
src/transformers/models/maskformer/image_processing_maskformer.py:280:        all_labels = all_labels[all_labels != ignore_index]
src/transformers/models/maskformer/image_processing_maskformer.py:375:        ignore_index (`int`, *optional*):
src/transformers/models/maskformer/image_processing_maskformer.py:377:            denoted with 0 (background) will be replaced with `ignore_index`.
src/transformers/models/maskformer/image_processing_maskformer.py:381:            The background label will be replaced by `ignore_index`.
src/transformers/models/maskformer/image_processing_maskformer.py:398:        ignore_index: Optional[int] = None,
src/transformers/models/maskformer/image_processing_maskformer.py:441:        self.ignore_index = ignore_index
src/transformers/models/maskformer/image_processing_maskformer.py:551:        ignore_index: Optional[int] = None,
src/transformers/models/maskformer/image_processing_maskformer.py:556:        ignore_index = ignore_index if ignore_index is not None else self.ignore_index
src/transformers/models/maskformer/image_processing_maskformer.py:560:            ignore_index=ignore_index,
src/transformers/models/maskformer/image_processing_maskformer.py:666:        ignore_index: Optional[int] = None,
src/transformers/models/maskformer/image_processing_maskformer.py:698:        ignore_index = ignore_index if ignore_index is not None else self.ignore_index
src/transformers/models/maskformer/image_processing_maskformer.py:752:            images, segmentation_maps, instance_id_to_semantic_id, ignore_index, do_reduce_labels, return_tensors
src/transformers/models/maskformer/image_processing_maskformer.py:822:        ignore_index: Optional[int] = None,
src/transformers/models/maskformer/image_processing_maskformer.py:878:        ignore_index = self.ignore_index if ignore_index is None else ignore_index
src/transformers/models/maskformer/image_processing_maskformer.py:897:                    segmentation_map, instance_id, ignore_index=ignore_index, reduce_labels=reduce_labels
src/transformers/models/maskformer/image_processing_maskformer.py:903:                    self._pad_image(image=mask, output_size=pad_size, constant_values=ignore_index) for mask in masks
src/transformers/models/oneformer/image_processing_oneformer.py:263:    ignore_index: Optional[int] = None,
src/transformers/models/oneformer/image_processing_oneformer.py:266:    if reduce_labels and ignore_index is None:
src/transformers/models/oneformer/image_processing_oneformer.py:267:        raise ValueError("If `reduce_labels` is True, `ignore_index` must be provided.")
src/transformers/models/oneformer/image_processing_oneformer.py:270:        segmentation_map = np.where(segmentation_map == 0, ignore_index, segmentation_map - 1)
src/transformers/models/oneformer/image_processing_oneformer.py:276:    if ignore_index is not None:
src/transformers/models/oneformer/image_processing_oneformer.py:277:        all_labels = all_labels[all_labels != ignore_index]
src/transformers/models/oneformer/image_processing_oneformer.py:375:        ignore_index (`int`, *optional*):
src/transformers/models/oneformer/image_processing_oneformer.py:377:            denoted with 0 (background) will be replaced with `ignore_index`.
src/transformers/models/oneformer/image_processing_oneformer.py:381:            The background label will be replaced by `ignore_index`.
src/transformers/models/oneformer/image_processing_oneformer.py:403:        ignore_index: Optional[int] = None,
src/transformers/models/oneformer/image_processing_oneformer.py:435:        self.ignore_index = ignore_index
src/transformers/models/oneformer/image_processing_oneformer.py:510:        ignore_index: Optional[int] = None,
src/transformers/models/oneformer/image_processing_oneformer.py:515:        ignore_index = ignore_index if ignore_index is not None else self.ignore_index
src/transformers/models/oneformer/image_processing_oneformer.py:519:            ignore_index=ignore_index,
src/transformers/models/oneformer/image_processing_oneformer.py:620:        ignore_index: Optional[int] = None,
src/transformers/models/oneformer/image_processing_oneformer.py:657:        ignore_index = ignore_index if ignore_index is not None else self.ignore_index
src/transformers/models/oneformer/image_processing_oneformer.py:713:            ignore_index,
src/transformers/models/oneformer/image_processing_oneformer.py:883:        ignore_index: Optional[int] = None,
src/transformers/models/oneformer/image_processing_oneformer.py:945:        ignore_index = self.ignore_index if ignore_index is None else ignore_index
src/transformers/models/oneformer/image_processing_oneformer.py:963:                    segmentation_map, instance_id, ignore_index=ignore_index, reduce_labels=reduce_labels
src/transformers/models/oneformer/image_processing_oneformer.py:990:                    self._pad_image(image=mask, output_size=pad_size, constant_values=ignore_index) for mask in masks
src/transformers/models/mask2former/image_processing_mask2former.py:262:    ignore_index: Optional[int] = None,
src/transformers/models/mask2former/image_processing_mask2former.py:265:    if reduce_labels and ignore_index is None:
src/transformers/models/mask2former/image_processing_mask2former.py:266:        raise ValueError("If `reduce_labels` is True, `ignore_index` must be pr
[... 2530 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; grep -n "ignore_index\|randint(0, 2\|binary" tests/models/{maskformer,mask2former,oneformer}/test_image_processing*.py | head -30
```

tool result:

```
tests/models/maskformer/test_image_processing_maskformer.py:34:        from transformers.models.maskformer.image_processing_maskformer import binary_mask_to_rle
tests/models/maskformer/test_image_processing_maskformer.py:56:        ignore_index=255,
tests/models/maskformer/test_image_processing_maskformer.py:77:        self.ignore_index = ignore_index
tests/models/maskformer/test_image_processing_maskformer.py:89:            "ignore_index": self.ignore_index,
tests/models/maskformer/test_image_processing_maskformer.py:151:        self.assertTrue(hasattr(image_processing, "ignore_index"))
tests/models/maskformer/test_image_processing_maskformer.py:391:        image_processing = MaskFormerImageProcessor(reduce_labels=True, ignore_index=255, size=(512, 512))
tests/models/maskformer/test_image_processing_maskformer.py:434:        image_processing = MaskFormerImageProcessor(reduce_labels=True, ignore_index=255, size=(512, 512))
tests/models/maskformer/test_image_processing_maskformer.py:479:            # 0 is the "ignore" label, for which we don't need to make binary masks
tests/models/maskformer/test_image_processing_maskformer.py:491:        image_processing = MaskFormerImageProcessor(ignore_index=0, do_resize=False)
tests/models/maskformer/test_image_processing_maskformer.py:524:    def test_binary_mask_to_rle(self):
tests/models/maskformer/test_image_processing_maskformer.py:525:        fake_binary_mask = np.zeros((20, 50))
tests/models/maskformer/test_image_processing_maskformer.py:526:        fake_binary_mask[0, 20:] = 1
tests/models/maskformer/test_image_processing_maskformer.py:527:        fake_binary_mask[1, :15] = 1
tests/models/maskformer/test_image_processing_maskformer.py:528:        fake_binary_mask[5, :10] = 1
tests/models/maskformer/test_image_processing_maskformer.py:530:        rle = binary_mask_to_rle(fake_binary_mask)
tests/models/maskformer/test_image_processing_maskformer.py:593:            outputs, threshold=0, return_binary_maps=True
tests/models/mask2former/test_image_processing_mask2former.py:34:        from transformers.models.mask2former.image_processing_mask2former import binary_mask_to_rle
tests/models/mask2former/test_image_processing_mask2former.py:56:        ignore_index=255,
tests/models/mask2former/test_image_processing_mask2former.py:77:        self.ignore_index = ignore_index
tests/models/mask2former/test_image_processing_mask2former.py:89:            "ignore_index": self.ignore_index,
tests/models/mask2former/test_image_processing_mask2former.py:151:        self.assertTrue(hasattr(image_processing, "ignore_index"))
tests/models/mask2former/test_image_processing_mask2former.py:391:        image_processing = Mask2FormerImageProcessor(reduce_labels=True, ignore_index=255, size=(512, 512))
tests/models/mask2former/test_image_processing_mask2former.py:434:        image_processing = Mask2FormerImageProcessor(reduce_labels=True, ignore_index=255, size=(512, 512))
tests/models/mask2former/test_image_processing_mask2former.py:479:            # 0 is the "ignore" label, for which we don't need to make binary masks
tests/models/mask2former/test_image_processing_mask2former.py:491:        image_processing = Mask2FormerImageProcessor(ignore_index=0, do_resize=False)
tests/models/mask2former/test_image_processing_mask2former.py:524:    def test_binary_mask_to_rle(self):
tests/models/mask2former/test_image_processing_mask2former.py:525:        fake_binary_mask = np.zeros((20, 50))
tests/models/mask2former/test_image_processing_mask2former.py:526:        fake_binary_mask[0, 20:] = 1
tests/models/mask2former/test_image_processing_mask2former.py:527:        fake_binary_mask[1, :15] = 1
tests/models/mask2former/test_image_processing_mask2former.py:528:        fake_binary_mask[5, :10] = 1
```

**thinking:**

```
That padding failure is a separate, unrelated issue since real configs use `ignore_index=255`. I'll rerun the repro for both MaskFormer and OneFormer with that value set.


```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; cat > repro_tmp.py <<'EOF'
import numpy as np, torch
from transformers import MaskFormerImageProcessor, OneFormerImageProcessor
from transformers.image_transforms import resize, to_pil_image
seg = np.random.randint(0, 2, (512, 512))
img = np.random.randint(0, 255, (3, 512, 512))
p = MaskFormerImageProcessor(ignore_index=255)
out = p([img], segmentation_maps=[seg], instance_id_to_semantic_id={0: 3, 1: 4}, return_tensors="pt")
print("maskformer", out["class_labels"], out["mask_labels"][0].unique())
p = OneFormerImageProcessor(ignore_index=255, do_reduce_labels=True, num_text=10,
    metadata={str(i): f"c{i}" for i in range(10)}, class_info_file=None, repo_path=None)
seg_t = torch.randint(0, 2, (512, 512), dtype=torch.long)
out = p([img], ["panoptic"], segmentation_maps=[seg_t], instance_id_to_semantic_id={1: 4}, return_tensors="pt")
print("oneformer", out["class_labels"])
f = np.random.rand(3, 64, 64)
r = resize(f, (32, 32)); print("float", r.dtype, r.min(), r.max())
print("uint8 0/1", np.unique(np.asarray(to_pil_image(np.random.randint(0,2,(4,5,3)).astype(np.uint8)))))
EOF
../bin/envrun 'python repro_tmp.py' 2>&1 | tail -8
```

tool result:

```
  File "/testbed/src/transformers/models/oneformer/image_processing_oneformer.py", line 325, in prepare_metadata
    with open(hf_hub_download(repo_path, class_info_file, repo_type="dataset"), "r") as f:
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/utils/_validators.py", line 106, in _inner_fn
    validate_repo_id(arg_value)
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/utils/_validators.py", line 151, in validate_repo_id
    raise HFValidationError(f"Repo id must be a string, not {type(repo_id)}: '{repo_id}'.")
huggingface_hub.errors.HFValidationError: Repo id must be a string, not <class 'NoneType'>: 'None'.
```

**assistant:** OneFormer tries to download class metadata from the Hub, and the container has no network access. I'll check how its tests build the processor offline.

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; grep -n "metadata\|class_info\|repo_path" tests/models/oneformer/test_image_processing_oneformer.py | head; grep -n "def __init__" -A20 src/transformers/models/oneformer/image_processing_oneformer.py | grep -n "metadata\|class_info\|repo"
```

tool result:

```
41:def prepare_metadata(class_info_file, repo_path="shi-labs/oneformer_demo"):
42:    with open(hf_hub_download(repo_path, class_info_file, repo_type="dataset"), "r") as f:
43:        class_info = json.load(f)
44:    metadata = {}
47:    for key, info in class_info.items():
48:        metadata[key] = info["name"]
52:    metadata["thing_ids"] = thing_ids
53:    metadata["class_names"] = class_names
54:    return metadata
73:        repo_path="shi-labs/oneformer_demo",
13:405-        repo_path: str = "shi-labs/oneformer_demo",
14:406-        class_info_file: str = None,
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; sed -n 425,450p src/transformers/models/oneformer/image_processing_oneformer.py
```

tool result:

```
        super().__init__(**kwargs)
        self.do_resize = do_resize
        self.size = size
        self.resample = resample
        self.do_rescale = do_rescale
        self.rescale_factor = rescale_factor
        self.do_normalize = do_normalize
        self.image_mean = image_mean if image_mean is not None else IMAGENET_DEFAULT_MEAN
        self.image_std = image_std if image_std is not None else IMAGENET_DEFAULT_STD
        self.ignore_index = ignore_index
        self.do_reduce_labels = do_reduce_labels
        self.class_info_file = class_info_file
        self.repo_path = repo_path
        self.metadata = prepare_metadata(repo_path, class_info_file)
        self.num_text = num_text

    def resize(
        self,
        image: np.ndarray,
        size: Dict[str, int],
        resample: PILImageResampling = PILImageResampling.BILINEAR,
        data_format=None,
        **kwargs,
    ) -> np.ndarray:
        """
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; python3 - <<'EOF'
p="repro_tmp.py"; s=open(p).read()
s=s.replace("from transformers.image_transforms", "import transformers.models.oneformer.image_processing_oneformer as m\nm.prepare_metadata = lambda *a: {str(i): f'c{i}' for i in range(10)} | {'thing_ids': list(range(10)), 'class_names': [f'c{i}' for i in range(10)]}\nfrom transformers.image_transforms",1)
s=s.replace(",\n    metadata={str(i): f\"c{i}\" for i in range(10)}, class_info_file=None, repo_path=None)", ")")
open(p,"w").write(s)
EOF
../bin/envrun 'python repro_tmp.py' 2>&1 | grep -v Warn | tail -8
```

tool result:

```
maskformer [tensor([3, 4])] tensor([0., 1.])
oneformer [tensor([3])]
float float32 0.21176471 0.78431374
uint8 0/1 [0 1]
```

**thinking:**

```
Both processors now work correctly—MaskFormer returns classes [3, 4] with binary mask values, OneFormer returns class [3], and float images stay in [0, 1] after resize. Next I'll run the closest existing test suites.


```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; rm repro_tmp.py; ../bin/envrun 'HF_HUB_OFFLINE=1 python -m pytest -q -x tests/test_image_transforms.py tests/models/maskformer/test_image_processing_maskformer.py tests/models/mask2former/test_image_processing_mask2former.py tests/models/oneformer/test_image_processing_oneformer.py tests/models/vit/test_image_processing_vit.py tests/models/clip/test_image_processing_clip.py tests/models/segformer/test_image_processing_segformer.py 2>&1 | tail -15'
```

tool result:

```
E   AttributeError: 'MaskFormerImageProcessingTester' object has no attribute '_testMethodName'
=============================== warnings summary ===============================
src/transformers/models/maskformer/modeling_maskformer.py:1244
  /testbed/src/transformers/models/maskformer/modeling_maskformer.py:1244: DeprecationWarning: invalid escape sequence '\e'
    """

src/transformers/modeling_utils.py:1740
  /testbed/src/transformers/modeling_utils.py:1740: DeprecationWarning: invalid escape sequence '\d'
    reg = re.compile("(.*?)-\d{5}-of-\d{5}")

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
ERROR tests/models/maskformer/test_image_processing_maskformer.py::MaskFormerImageProcessingTester
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
2 warnings, 1 error in 1.09s
```

**assistant:** That error is a pytest collection quirk: pytest is trying to collect a helper class whose name starts with "Test". I'll rerun without `-x` and look at the real failures.

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; ../bin/envrun 'HF_HUB_OFFLINE=1 python -m pytest -q tests/test_image_transforms.py tests/models/maskformer/test_image_processing_maskformer.py tests/models/mask2former/test_image_processing_mask2former.py tests/models/oneformer/test_image_processing_oneformer.py tests/models/vit/test_image_processing_vit.py tests/models/clip/test_image_processing_clip.py tests/models/segformer/test_image_processing_segformer.py 2>&1 | grep -E "FAILED|ERROR|passed|failed"'
```

tool result:

```
==================================== ERRORS ====================================
_ ERROR collecting tests/models/maskformer/test_image_processing_maskformer.py _
_ ERROR collecting tests/models/mask2former/test_image_processing_mask2former.py _
__ ERROR collecting tests/models/oneformer/test_image_processing_oneformer.py __
________ ERROR collecting tests/models/vit/test_image_processing_vit.py ________
_______ ERROR collecting tests/models/clip/test_image_processing_clip.py _______
__ ERROR collecting tests/models/segformer/test_image_processing_segformer.py __
ERROR tests/models/maskformer/test_image_processing_maskformer.py::MaskFormerImageProcessingTester
ERROR tests/models/mask2former/test_image_processing_mask2former.py::Mask2FormerImageProcessingTester
ERROR tests/models/oneformer/test_image_processing_oneformer.py::OneFormerImageProcessorTester
ERROR tests/models/vit/test_image_processing_vit.py::ViTImageProcessingTester
ERROR tests/models/clip/test_image_processing_clip.py::CLIPImageProcessingTester
ERROR tests/models/segformer/test_image_processing_segformer.py::SegformerImageProcessingTester
```

**assistant:** The collection errors come from the container's pytest version, not from the code. I'll select the actual test classes directly.

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; ../bin/envrun 'HF_HUB_OFFLINE=1 python -m pytest -q tests/test_image_transforms.py tests/models/maskformer/test_image_processing_maskformer.py::MaskFormerImageProcessingTest tests/models/mask2former/test_image_processing_mask2former.py::Mask2FormerImageProcessingTest tests/models/oneformer/test_image_processing_oneformer.py::OneFormerImageProcessingTest tests/models/vit/test_image_processing_vit.py::ViTImageProcessingTest tests/models/clip/test_image_processing_clip.py::CLIPImageProcessingTest tests/models/segformer/test_image_processing_segformer.py::SegformerImageProcessingTest 2>&1 | grep -E "^(FAILED|ERROR)|passed|failed" | cut -c1-200'
```

tool result:

```
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
        """Raise an appropriate error when the HEAD call failed and we cannot locate a local file."""
                raise ValueError("Force download failed due to the above error.") from head_call_error
FAILED tests/models/maskformer/test_image_processing_maskformer.py::MaskFormerImageProcessingTest::test_integration_instance_segmentation
FAILED tests/models/maskformer/test_image_processing_maskformer.py::MaskFormerImageProcessingTest::test_integration_panoptic_segmentation
FAILED tests/models/maskformer/test_image_processing_maskformer.py::MaskFormerImageProcessingTest::test_integration_semantic_segmentation
FAILED tests/models/mask2former/test_image_processing_mask2former.py::Mask2FormerImageProcessingTest::test_integration_instance_segmentation
FAILED tests/models/mask2former/test_image_processing_mask2former.py::Mask2FormerImageProcessingTest::test_integration_panoptic_segmentation
FAILED tests/models/mask2former/test_image_processing_mask2former.py::Mask2FormerImageProcessingTest::test_integration_semantic_segmentation
FAILED tests/models/oneformer/test_image_processing_oneformer.py::OneFormerImageProcessingTest::test_batch_feature
FAILED tests/models/oneformer/test_image_processing_oneformer.py::OneFormerImageProcessingTest::test_binary_mask_to_rle
FAILED tests/models/oneformer/test_image_processing_oneformer.py::OneFormerImageProcessingTest::test_call_numpy
FAILED tests/models/oneformer/test_image_processing_oneformer.py::OneFormerImageProcessingTest::test_call_pil
FAILED tests/models/oneformer/test_image_processing_oneformer.py::OneFormerImageProcessingTest::test_call_pytorch
FAILED tests/models/oneformer/test_image_processing_oneformer.py::OneFormerImageProcessingTest::test_call_with_segmentation_maps
FAILED tests/models/oneformer/test_image_processing_oneformer.py::OneFormerImageProcessingTest::test_cast_dtype_device
FAILED tests/models/oneformer/test_image_processing_oneformer.py::OneFormerImageProcessingTest::test_equivalence_pad_and_create_pixel_mask
FAILED tests/models/oneformer/test_image_processing_oneformer.py::OneFormerImageProcessingTest::test_imag
[... 1243 more characters not shown]
```

**assistant:** 94 tests pass and 24 fail, and the output points to failed Hub downloads. To confirm none of the failures come from my change, I'll run the same suite on the original code and compare.

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; T='tests/test_image_transforms.py tests/models/maskformer/test_image_processing_maskformer.py::MaskFormerImageProcessingTest tests/models/mask2former/test_image_processing_mask2former.py::Mask2FormerImageProcessingTest tests/models/oneformer/test_image_processing_oneformer.py::OneFormerImageProcessingTest tests/models/vit/test_image_processing_vit.py::ViTImageProcessingTest tests/models/clip/test_image_processing_clip.py::CLIPImageProcessingTest tests/models/segformer/test_image_processing_segformer.py::SegformerImageProcessingTest'; ../bin/envrun "HF_HUB_OFFLINE=1 python -m pytest -q $T 2>&1 | grep -E '^FAILED' | sort" > ../after.txt; git stash -q; ../bin/envrun "HF_HUB_OFFLINE=1 python -m pytest -q $T 2>&1 | grep -E '^FAILED|passed' | sort" > ../before.txt; git stash pop -q; diff ../before.txt ../after.txt; rm ../before.txt ../after.txt; git status --short
```

tool result:

```
1d0
< 24 failed, 94 passed, 2 skipped, 11 warnings in 3.48s
 M src/transformers/image_transforms.py
?? Dockerfile
```

**assistant:** The original code fails the same 24 tests, all because they need to download files from the Hub. My change adds no new failures. (The untracked `Dockerfile` is not mine; I left it alone.)

**tool call: Bash**

```bash
cd /work/huggingface__transformers-22158/repo; git diff
```

tool result:

```
diff --git a/src/transformers/image_transforms.py b/src/transformers/image_transforms.py
index 16016d970..369ddc8d4 100644
--- a/src/transformers/image_transforms.py
+++ b/src/transformers/image_transforms.py
@@ -118,6 +118,33 @@ def rescale(
     return rescaled_image
 
 
+def _rescale_for_pil_conversion(image):
+    """
+    Detects whether or not the image needs to be rescaled before being converted to a PIL image.
+
+    The assumption is that if the image is of type `np.float` and all values are between 0 and 1, it needs to be
+    rescaled.
+    """
+    if image.dtype == np.uint8:
+        do_rescale = False
+    elif np.allclose(image, image.astype(int)):
+        if np.all(0 <= image) and np.all(image <= 255):
+            do_rescale = False
+        else:
+            raise ValueError(
+                "The image to be converted to a PIL image contains values outside the range [0, 255], "
+                f"got [{image.min()}, {image.max()}] which cannot be converted to uint8."
+            )
+    elif np.all(0 <= image) and np.all(image <= 1):
+        do_rescale = True
+    else:
+        raise ValueError(
+            "The image to be converted to a PIL image contains values outside the range [0, 1], "
+            f"got [{image.min()}, {image.max()}] which cannot be converted to uint8."
+        )
+    return do_rescale
+
+
 def to_pil_image(
     image: Union[np.ndarray, "PIL.Image.Image", "torch.Tensor", "tf.Tensor", "jnp.ndarray"],
     do_rescale: Optional[bool] = None,
@@ -156,17 +183,8 @@ def to_pil_image(
     # If there is a single channel, we squeeze it, as otherwise PIL can't handle it.
     image = np.squeeze(image, axis=-1) if image.shape[-1] == 1 else image
 
-    # PIL.Image can only store uint8 values, so we rescale the image to be between 0 and 255 if needed.
-    if do_rescale is None:
-        if np.all(0 <= image) and np.all(image <= 1):
-            do_rescale = True
-        elif np.allclose(image, image.astype(int)):
-            do_rescale = False
-        else:
-            raise ValueError(
-                "The image to be converted to a PIL image contains values outside the range [0, 1], "
-                f"got [{image.min()}, {image.max()}] which cannot be converted to uint8."
-            )
+    # PIL.Image can only store uint8 values so we rescale the image to be between 0 and 255 if needed.
+    do_rescale = _rescale_for_pil_conversion(image) if do_rescale is None else do_rescale
 
     if do_rescale:
         image = rescale(image, 255)
@@ -283,8 +301,10 @@ def resize(
 
     # To maintain backwards compatibility with the resizing done in previous image feature extractors, we use
     # the pillow library to resize the image and then convert back to numpy
+    do_rescale = False
     if not isinstance(image, PIL.Image.Image):
-        image = to_pil_image(image)
+        do_rescale = _rescale_for_pil_conversion(image)
+        image = to_pil_image(image, do_rescale=do_rescale)
     height, width = size
     # PIL images are in the format (width, height)
     resized_image = image.resize((width, height), resample=resample, reducing_gap=reducing_gap)
@@ -298,6 +318,9 @@ def resize(
         resized_image = to_channel_dimension_format(
             resized_image, data_format, input_channel_dim=ChannelDimension.LAST
         )
+        # If an image was rescaled to be in the range [0, 255] before converting to a PIL image, then we need to
+        # rescale it back to the original range.
+        resized_image = rescale(resized_image, 1 / 255) if do_rescale else resized_image
     return resized_image
```

**assistant:** A segmentation map containing only 0s and 1s now comes through `resize` unchanged, so the `KeyError: 255` is gone for MaskFormer, Mask2Former and OneFormer. The fix is in `src/transformers/image_transforms.py`, the shared helper all three use.

**Cause:** before converting an array to a PIL image, `to_pil_image` guessed whether to multiply it by 255. It checked "all values in [0, 1]" first, so an integer map of 0s and 1s was treated like a float image and scaled up, turning every 1 into 255.

**Fix:**
- A new helper, `_rescale_for_pil_conversion`, decides about scaling in this order:
  - `uint8` arrays are never scaled.
  - Arrays holding whole numbers are never scaled; they must be in [0, 255] or it raises a `ValueError`.
  - Only non-integer float arrays in [0, 1] are scaled by 255.
  - Anything else raises a `ValueError`, as before.
- `to_pil_image` uses this helper when `do_rescale` isn't given.
- `resize` records whether it scaled the image, and if so divides the result by 255 afterwards. A float image in [0, 1] therefore stays in [0, 1].

**Behaviour change:** before, resizing a float image in [0, 1] returned `uint8` values from 0 to 255. Now it returns `float32` values in [0, 1].

**Verification:**
- I reproduced the `KeyError: 255` first. After the fix, a random 0/1 map gives class labels `[3, 4]` and masks with values {0, 1} on MaskFormer. On OneFormer, the issue's setup (`do_reduce_labels=True`, `{1: 4}`) gives `[3]`.
- I ran the image-transform tests and the image-processor tests for MaskFormer, Mask2Former, OneFormer, ViT, CLIP and SegFormer: 94 passed and 24 failed. The original code gives exactly the same 24 failures; they all need to download files from the Hub, which the container can't reach. So nothing new breaks, but those 24 tests (including the segmentation integration tests) weren't actually exercised.
- My test script is deleted.

**Separate problem, not fixed:** with `ignore_index=None` (the MaskFormer default), passing segmentation maps fails during padding with `ValueError: Unsupported format: None`. This also happens on the original code with any segmentation map, so it isn't part of this issue. Setting `ignore_index` (for example 255, as the tests do) avoids it.

_session end: success, turns 20, is_error False_

## Container commands (task container, no network; broker log)

- `rc=2` 0.18 s: python repro_tmp.py
- `rc=1` 2.41 s: python repro_tmp.py
- `rc=1` 2.26 s: python repro_tmp.py
- `rc=1` 2.48 s: python repro_tmp.py
- `rc=1` 2.33 s: python -c " import numpy as np from transformers import MaskFormerImageProcessor p = MaskFormerImageProcessor(do_reduce_labels=False) seg = np.random.randint(0, 3, (512, 512)) out = p([np.random.randint(0, 255, (3, 512, 512))], segmentation_maps=[seg], instance_id_to_semantic_id={0: 3, 1: 4, 2:5}, return_tensors=\"pt\") print(out[\"class_labels\"]) "
- `rc=1` 2.39 s: python repro_tmp.py
- `rc=0` 2.38 s: python repro_tmp.py
- `rc=0` 3.49 s: HF_HUB_OFFLINE=1 python -m pytest -q -x tests/test_image_transforms.py tests/models/maskformer/test_image_processing_maskformer.py tests/models/mask2former/test_image_processing_mask2former.py tests/models/oneformer/test_image_processing_oneformer.py tests/models/vit/test_image_processing_vit.py tests/models/clip/test_image_processing_clip.py tests/models/segformer/test_image_processing_segformer.py 2>&1 | tail -15
- `rc=0` 3.52 s: HF_HUB_OFFLINE=1 python -m pytest -q tests/test_image_transforms.py tests/models/maskformer/test_image_processing_maskformer.py tests/models/mask2former/test_image_processing_mask2former.py tests/models/oneformer/test_image_processing_oneformer.py tests/models/vit/test_image_processing_vit.py tests/models/clip/test_image_processing_clip.py tests/models/segformer/test_image_processing_segformer.py 2>&1 | grep -E "FAILED|ERROR|passed|failed"
- `rc=0` 5.56 s: HF_HUB_OFFLINE=1 python -m pytest -q tests/test_image_transforms.py tests/models/maskformer/test_image_processing_maskformer.py::MaskFormerImageProcessingTest tests/models/mask2former/test_image_processing_mask2former.py::Mask2FormerImageProcessingTest tests/models/oneformer/test_image_processing_oneformer.py::OneFormerImageProcessingTest tests/models/vit/test_image_processing_vit.py::ViTImageProcessingTest tests/models/clip/test_image_processing_clip.py::CLIPImageProcessingTest tests/models/segformer/test_image_processing_segformer.py::SegformerImageProcessingTest 2>&1 | grep -E "^(FAILED|ERR
- `rc=0` 6.05 s: HF_HUB_OFFLINE=1 python -m pytest -q tests/test_image_transforms.py tests/models/maskformer/test_image_processing_maskformer.py::MaskFormerImageProcessingTest tests/models/mask2former/test_image_processing_mask2former.py::Mask2FormerImageProcessingTest tests/models/oneformer/test_image_processing_oneformer.py::OneFormerImageProcessingTest tests/models/vit/test_image_processing_vit.py::ViTImageProcessingTest tests/models/clip/test_image_processing_clip.py::CLIPImageProcessingTest tests/models/segformer/test_image_processing_segformer.py::SegformerImageProcessingTest 2>&1 | grep -E '^FAILED' | s
- `rc=0` 5.96 s: HF_HUB_OFFLINE=1 python -m pytest -q tests/test_image_transforms.py tests/models/maskformer/test_image_processing_maskformer.py::MaskFormerImageProcessingTest tests/models/mask2former/test_image_processing_mask2former.py::Mask2FormerImageProcessingTest tests/models/oneformer/test_image_processing_oneformer.py::OneFormerImageProcessingTest tests/models/vit/test_image_processing_vit.py::ViTImageProcessingTest tests/models/clip/test_image_processing_clip.py::CLIPImageProcessingTest tests/models/segformer/test_image_processing_segformer.py::SegformerImageProcessingTest 2>&1 | grep -E '^FAILED|pass
