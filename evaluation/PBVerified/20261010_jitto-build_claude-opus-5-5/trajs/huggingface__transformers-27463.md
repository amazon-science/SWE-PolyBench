# Instance: huggingface__transformers-27463

- Final resolved (evaluator, logs/huggingface__transformers-27463_result.json): True
- Run state: DONE
- One attempt. Duration 167.0 s, turns 12, actor cost $0.5881050000000001, container commands 3
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/huggingface__transformers-27463/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-27463/repo. Consider the following issue description:

<issue_description>
Add how to preprocess mask for finetuning with SAM
### Feature request

The [SAM image processor](https://github.com/huggingface/transformers/blob/main/src/transformers/models/sam/image_processing_sam.py) takes images as input and resizes them so that the longest edge is 1024 (using default values). This is the size expect as input fo the SAM model. 
For inference, this works fine as only the images need resizing but for fine-tuning as per [this tutorial](https://github.com/NielsRogge/Transformers-Tutorials/blob/master/SAM/Fine_tune_SAM_(segment_anything)_on_a_custom_dataset.ipynb), you need to resize both your images and your masks as the SAM model produces `pred_masks` with size 256x256. If I don't resize my masks I get `ground truth has different shape (torch.Size([2, 1, 768, 1024])) from input (torch.Size([2, 1, 256, 256]))` when trying to calculate loss.

To fix this, I've currently written a resize and pad function into my code:

```
from PIL import Image

def resize_mask(image):
    longest_edge = 256
    
    # get new size
    w, h = image.size
    scale = longest_edge * 1.0 / max(h, w)
    new_h, new_w = h * scale, w * scale
    new_h = int(new_h + 0.5)
    new_w = int(new_w + 0.5)

    resized_image = image.resize((new_w, new_h), resample=Image.Resampling.BILINEAR)
    return resized_image

def pad_mask(image):
    pad_height = 256 - image.height
    pad_width = 256 - image.width

    padding = ((0, pad_height), (0, pad_width))
    padded_image = np.pad(image, padding, mode="constant")
    return padded_image

def process_mask(image):
    resized_mask = resize_mask(image)
    padded_mask = pad_mask(resized_mask)
    return padded_mask
```

and then have added this to my definition of SAMDataset:

```
class SAMDataset(Dataset):
    def __init__(self, dataset, processor, transform = None):
        self.dataset = dataset
        self.processor = processor
        self.transform = transform

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        item = self.dataset[idx]
        
        if self.transform:
            image = self.transform(item["pixel_values"])
        else:
            image = item["pixel_values"]
        
        # get bounding box prompt
        padded_mask = process_mask(item["label"])
        prompt = get_bounding_box(padded_mask)

        # prepare image and prompt for the model
        inputs = self.processor(image, input_boxes=[[prompt]], return_tensors="pt")

        # remove batch dimension which the processor adds by default
        inputs = {k:v.squeeze(0) for k,v in inputs.items()}

        # add ground truth segmentation
        inputs["ground_truth_mask"] = padded_mask

        return inputs
```

This seems to work fine. 

What I think would be good is to allow input of masks in the SAM image processor. For example, the [Segformer image processor](https://github.com/huggingface/transformers/blob/v4.35.0/src/transformers/models/segformer/image_processing_segformer.py#L305) takes images and masks as inputs and resizes both to the size expected by the Segformer model. 

I have also seen there is a 'post_process_mask' method in the SAM image processor but I am unsure how to implement this in the tutorial I'm following. If you think this is a better way vs. what I am suggesting then please could you explain where I would add this in the code from the tutorial notebook.

### Motivation

Easier fine tuning of SAM model.

### Your contribution

I could try write a PR for this and/or make a PR to update the [notebook](https://github.com/NielsRogge/Transformers-Tutorials/blob/master/SAM/Fine_tune_SAM_(segment_anything)_on_a_custom_dataset.ipynb) instead .

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-27463/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-27463/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-27463/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-27463/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
wc -l src/transformers/models/sam/image_processing_sam.py && sed -n 1,520p src/transformers/models/sam/image_processing_sam.py && grep -n "mask_size\|mask_pad\|segmentation_maps\|reshaped_input" tests/models/sam/test_image_processing_sam.py tests/models/sam/test_processor_sam.py src/transformers/models/sam/processing_sam.py
```

tool result:

```
Exit code 2
    1298 src/transformers/models/sam/image_processing_sam.py
# coding=utf-8
# Copyright 2023 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Image processor class for SAM."""
import math
from copy import deepcopy
from itertools import product
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np

from ...image_processing_utils import BaseImageProcessor, BatchFeature, get_size_dict
from ...image_transforms import convert_to_rgb, pad, resize, to_channel_dimension_format
from ...image_utils import (
    IMAGENET_DEFAULT_MEAN,
    IMAGENET_DEFAULT_STD,
    ChannelDimension,
    ImageInput,
    PILImageResampling,
    get_image_size,
    infer_channel_dimension_format,
    is_scaled_image,
    make_list_of_images,
    to_numpy_array,
    valid_images,
)
from ...utils import (
    TensorType,
    is_tf_available,
    is_torch_available,
    is_torchvision_available,
    logging,
    requires_backends,
)


if is_torch_available():
    import torch
    import torch.nn.functional as F

if is_torchvision_available():
    from torchvision.ops.boxes import batched_nms

if is_tf_available():
    import tensorflow as tf
    from tensorflow.experimental import numpy as tnp

    from ...tf_utils import flatten, shape_list

logger = logging.get_logger(__name__)


class SamImageProcessor(BaseImageProcessor):
    r"""
    Constructs a SAM image processor.

    Args:
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the image's (height, width) dimensions to the specified `size`. Can be overridden by the
            `do_resize` parameter in the `preprocess` method.
        size (`dict`, *optional*, defaults to `{"longest_edge": 1024}`):
            Size of the output image after resizing. Resizes the longest edge of the image to match
            `size["longest_edge"]` while maintaining the aspect ratio. Can be overridden by the `size` parameter in the
            `preprocess` method.
        resample (`PILImageResampling`, *optional*, defaults to `Resampling.BILINEAR`):
            Resampling filter to use if resizing the image. Can be overridden by the `resample` parameter in the
            `preprocess` method.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Wwhether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the
            `do_rescale` parameter in the `preprocess` method.
        rescale_factor (`int` or `float`, *optional*, defaults to `1/255`):
            Scale factor to use if rescaling the image. Only has an effect if `do_rescale` is set to `True`. Can be
            overridden by the `rescale_factor` parameter in the `preprocess` method.
        do_normalize (`bool`, *optional*, defaults to `True`):
            Whether to normalize the image. Can be overridden by the `do_normalize` parameter in the `preprocess`
            method. Can be overridden by the `do_normalize` parameter in the `preprocess` method.
        image_mean (`float` or `List[float]`, *optional*, defaults to `IMAGENET_DEFAULT_MEAN`):
            Mean to use if normalizing the image. This is a float or list of floats the length of the number of
            channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method. Can be
            overridden by the `image_mean` parameter in the `preprocess` method.
        image_std (`float` or `List[float]`, *optional*, defaults to `IMAGENET_DEFAULT_STD`):
            Standard deviation to use if normalizing the image. This is a float or list of floats the length of the
            number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method.
            Can be overridden by the `image_std` parameter in the `preprocess` method.
        do_pad (`bool`, *optional*, defaults to `True`):
            Whether to pad the image to the specified `pad_size`. Can be overridden by the `do_pad` parameter in the
            `preprocess` method.
        pad_size (`dict`, *optional*, defaults to `{"height": 1024, "width": 1024}`):
            Size of the output image after padding. Can be overridden by the `pad_size` parameter in the `preprocess`
            method.
        do_convert_rgb (`bool`, *optional*, defaults to `True`):
            Whether to convert the image to RGB.
    """

    model_input_names = ["pixel_values"]

    def __init__(
        self,
       

... [18220 characters truncated] ...

binarize the masks.
            pad_size (`int`, *optional*, defaults to `self.pad_size`):
                The target size the images were padded to before being passed to the model. If None, the target size is
                assumed to be the processor's `pad_size`.
        Returns:
            (`torch.Tensor`): Batched masks in batch_size, num_channels, height, width) format, where (height, width)
            is given by original_size.
        """
        requires_backends(self, ["torch"])
        pad_size = self.pad_size if pad_size is None else pad_size
        target_image_size = (pad_size["height"], pad_size["width"])
        if isinstance(original_sizes, (torch.Tensor, np.ndarray)):
            original_sizes = original_sizes.tolist()
        if isinstance(reshaped_input_sizes, (torch.Tensor, np.ndarray)):
            reshaped_input_sizes = reshaped_input_sizes.tolist()
        output_masks = []
        for i, original_size in enumerate(o
[... 4040 more characters not shown]
```

**tool call: Bash**

```bash
sed -n 100,420p src/transformers/models/sam/image_processing_sam.py; sed -n 1,100p tests/models/sam/test_processor_sam.py; ls tests/models/sam
```

tool result:

```
            Size of the output image after padding. Can be overridden by the `pad_size` parameter in the `preprocess`
            method.
        do_convert_rgb (`bool`, *optional*, defaults to `True`):
            Whether to convert the image to RGB.
    """

    model_input_names = ["pixel_values"]

    def __init__(
        self,
        do_resize: bool = True,
        size: Dict[str, int] = None,
        resample: PILImageResampling = PILImageResampling.BILINEAR,
        do_rescale: bool = True,
        rescale_factor: Union[int, float] = 1 / 255,
        do_normalize: bool = True,
        image_mean: Optional[Union[float, List[float]]] = None,
        image_std: Optional[Union[float, List[float]]] = None,
        do_pad: bool = True,
        pad_size: int = None,
        do_convert_rgb: bool = True,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        size = size if size is not None else {"longest_edge": 1024}
        size = get_size_dict(max_size=size, default_to_square=False) if not isinstance(size, dict) else size

        pad_size = pad_size if pad_size is not None else {"height": 1024, "width": 1024}
        pad_size = get_size_dict(pad_size, default_to_square=True)

        self.do_resize = do_resize
        self.size = size
        self.resample = resample
        self.do_rescale = do_rescale
        self.rescale_factor = rescale_factor
        self.do_normalize = do_normalize
        self.image_mean = image_mean if image_mean is not None else IMAGENET_DEFAULT_MEAN
        self.image_std = image_std if image_std is not None else IMAGENET_DEFAULT_STD
        self.do_pad = do_pad
        self.pad_size = pad_size
        self.do_convert_rgb = do_convert_rgb

    def pad_image(
        self,
        image: np.ndarray,
        pad_size: Dict[str, int],
        data_format: Optional[Union[str, ChannelDimension]] = None,
        input_data_format: Optional[Union[str, ChannelDimension]] = None,
        **kwargs,
    ) -> np.ndarray:
        """
        Pad an image to `(pad_size["height"], pad_size["width"])` with zeros to the right and bottom.

        Args:
            image (`np.ndarray`):
                Image to pad.
            pad_size (`Dict[str, int]`):
                Size of the output image after padding.
            data_format (`str` or `ChannelDimension`, *optional*):
                The data format of the image. Can be either "channels_first" or "channels_last". If `None`, the
                `data_format` of the `image` will be used.
            input_data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the input image. If not provided, it will be inferred.
        """
        output_height, output_width = pad_size["height"], pad_size["width"]
        input_height, input_width = get_image_size(image, channel_dim=input_data_format)

        pad_width = output_width - input_width
        pad_height = output_height - input_height

        padded_image = pad(
            image,
            ((0, pad_height), (0, pad_width)),
            data_format=data_format,
            input_data_format=input_data_format,
            **kwargs,
        )
        return padded_image

    def _get_preprocess_shape(self, old_shape: Tuple[int, int], longest_edge: int):
        """
        Compute the output size given input size and target long side length.
        """
        oldh, oldw = old_shape
        scale = longest_edge * 1.0 / max(oldh, oldw)
        newh, neww = oldh * scale, oldw * scale
        newh = int(newh + 0.5)
        neww = int(neww + 0.5)
        return (newh, neww)

    def resize(
        self,
        image: np.ndarray,
        size: Dict[str, int],
        resample: PILImageResampling = PILImageResampling.BICUBIC,
        data_format: Optional[Union[str, ChannelDimension]] = None,
        input_data_format: Optional[Union[str, ChannelDimension]] = None,
        **kwargs,
    ) -> np.ndarray:
        """
        Resize an image to `(size["height"], size["width"])`.

        Args:
            image (`np.ndarray`):
                Image to resize.
            size (`Dict[str, int]`):
                Dictionary in the format `{"longest_edge": int}` specifying the size of the output image. The longest
                edge of the image will be resized to the specified size, while the other edge will be resized to
                maintain the aspect ratio.
            resample:
                `PILImageResampling` filter to use when resizing the image e.g. `PILImageResampling.BILINEAR`.
            data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format for the output image. If unset, the channel dimension format of the input
                image is used. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
            input_data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format for the input image. If unset, the channel dimension format is inferred
                from the input image. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.

        Returns:
            `np.ndarray`: The resized image.
        """
        size = get_size_dict(size)
        if "longest_edge" not in size:
            raise ValueError(f"The `size` dictionary must contain the key `longest_edge`. Got {size.keys()}")
        input_size = get_image_size(image, channel_dim=input_data_format)
        output_height, output_width = self._get_preprocess_shape(input_size, size["longest_edge"])
        return resize(
            image,
            size=(output_height, output_widt
[... 13618 more characters not shown]
```

**tool call: Bash**

```bash
sed -n 1,140p src/transformers/models/sam/processing_sam.py
```

tool result:

```
# coding=utf-8
# Copyright 2023 The HuggingFace Inc. team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Processor class for SAM.
"""
from copy import deepcopy
from typing import Optional, Union

import numpy as np

from ...processing_utils import ProcessorMixin
from ...tokenization_utils_base import BatchEncoding
from ...utils import TensorType, is_tf_available, is_torch_available


if is_torch_available():
    import torch

if is_tf_available():
    import tensorflow as tf


class SamProcessor(ProcessorMixin):
    r"""
    Constructs a SAM processor which wraps a SAM image processor and an 2D points & Bounding boxes processor into a
    single processor.

    [`SamProcessor`] offers all the functionalities of [`SamImageProcessor`]. See the docstring of
    [`~SamImageProcessor.__call__`] for more information.

    Args:
        image_processor (`SamImageProcessor`):
            An instance of [`SamImageProcessor`]. The image processor is a required input.
    """

    attributes = ["image_processor"]
    image_processor_class = "SamImageProcessor"

    def __init__(self, image_processor):
        super().__init__(image_processor)
        self.current_processor = self.image_processor
        self.point_pad_value = -10
        self.target_size = self.image_processor.size["longest_edge"]

    def __call__(
        self,
        images=None,
        input_points=None,
        input_labels=None,
        input_boxes=None,
        return_tensors: Optional[Union[str, TensorType]] = None,
        **kwargs,
    ) -> BatchEncoding:
        """
        This method uses [`SamImageProcessor.__call__`] method to prepare image(s) for the model. It also prepares 2D
        points and bounding boxes for the model if they are provided.
        """
        encoding_image_processor = self.image_processor(
            images,
            return_tensors=return_tensors,
            **kwargs,
        )

        # pop arguments that are not used in the foward but used nevertheless
        original_sizes = encoding_image_processor["original_sizes"]

        if hasattr(original_sizes, "numpy"):  # Checks if Torch or TF tensor
            original_sizes = original_sizes.numpy()

        input_points, input_labels, input_boxes = self._check_and_preprocess_points(
            input_points=input_points,
            input_labels=input_labels,
            input_boxes=input_boxes,
        )

        encoding_image_processor = self._normalize_and_convert(
            encoding_image_processor,
            original_sizes,
            input_points=input_points,
            input_labels=input_labels,
            input_boxes=input_boxes,
            return_tensors=return_tensors,
        )

        return encoding_image_processor

    def _normalize_and_convert(
        self,
        encoding_image_processor,
        original_sizes,
        input_points=None,
        input_labels=None,
        input_boxes=None,
        return_tensors="pt",
    ):
        if input_points is not None:
            if len(original_sizes) != len(input_points):
                input_points = [
                    self._normalize_coordinates(self.target_size, point, original_sizes[0]) for point in input_points
                ]
            else:
                input_points = [
                    self._normalize_coordinates(self.target_size, point, original_size)
                    for point, original_size in zip(input_points, original_sizes)
                ]
            # check that all arrays have the same shape
            if not all(point.shape == input_points[0].shape for point in input_points):
                if input_labels is not None:
                    input_points, input_labels = self._pad_points_and_labels(input_points, input_labels)

            input_points = np.array(input_points)

        if input_labels is not None:
            input_labels = np.array(input_labels)

        if input_boxes is not None:
            if len(original_sizes) != len(input_boxes):
                input_boxes = [
                    self._normalize_coordinates(self.target_size, box, original_sizes[0], is_bounding_box=True)
                    for box in input_boxes
                ]
            else:
                input_boxes = [
                    self._normalize_coordinates(self.target_size, box, original_size, is_bounding_box=True)
                    for box, original_size in zip(input_boxes, original_sizes)
                ]
            input_boxes = np.array(input_boxes)
```

**assistant:** Now I'll refactor `preprocess` to support `segmentation_maps` (resized with nearest-neighbour to `mask_size`, longest edge 256, and padded to `mask_pad_size`, 256x256), returned as `labels`.

**tool call: Bash**

```bash
cd src/transformers/models/sam && python3 - <<'EOF'
p='image_processing_sam.py'
s=open(p).read()

# class docstring
s=s.replace('''        resample (`PILImageResampling`, *optional*, defaults to `Resampling.BILINEAR`):
            Resampling filter to use if resizing the image. Can be overridden by the `resample` parameter in the
            `preprocess` method.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Wwhether''','''        mask_size (`dict`, *optional*, defaults to `{"longest_edge": 256}`):
            Size of the output segmentation map after resizing. Resizes the longest edge of the image to match
            `size["longest_edge"]` while maintaining the aspect ratio. Can be overridden by the `mask_size` parameter
            in the `preprocess` method.
        resample (`PILImageResampling`, *optional*, defaults to `Resampling.BILINEAR`):
            Resampling filter to use if resizing the image. Can be overridden by the `resample` parameter in the
            `preprocess` method.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Wwhether''',1)
s=s.replace('''            Size of the output image after padding. Can be overridden by the `pad_size` parameter in the `preprocess`
            method.
        do_convert_rgb''','''            Size of the output image after padding. Can be overridden by the `pad_size` parameter in the `preprocess`
            method.
        mask_pad_size (`dict`, *optional*, defaults to `{"height": 256, "width": 256}`):
            Size of the output segmentation map after padding. Can be overridden by the `mask_pad_size` parameter in
            the `preprocess` method.
        do_convert_rgb''',1)

# __init__
s=s.replace('''        size: Dict[str, int] = None,
        resample: PILImageResampling = PILImageResampling.BILINEAR,
        do_rescale: bool = True,
        rescale_factor: Union[int, float] = 1 / 255,
        do_normalize: bool = True,
        image_mean: Optional[Union[float, List[float]]] = None,
        image_std: Optional[Union[float, List[float]]] = None,
        do_pad: bool = True,
        pad_size: int = None,
        do_convert_rgb: bool = True,''','''        size: Dict[str, int] = None,
        mask_size: Dict[str, int] = None,
        resample: PILImageResampling = PILImageResampling.BILINEAR,
        do_rescale: bool = True,
        rescale_factor: Union[int, float] = 1 / 255,
        do_normalize: bool = True,
        image_mean: Optional[Union[float, List[float]]] = None,
        image_std: Optional[Union[float, List[float]]] = None,
        do_pad: bool = True,
        pad_size: int = None,
        mask_pad_size: int = None,
        do_convert_rgb: bool = True,''',1)
s=s.replace('''        pad_size = get_size_dict(pad_size, default_to_square=True)

        self.do_resize = do_resize
        self.size = size
''','''        pad_size = get_size_dict(pad_size, default_to_square=True)

        mask_size = mask_size if mask_size is not None else {"longest_edge": 256}
        mask_size = (
            get_size_dict(max_size=mask_size, default_to_square=False)
            if not isinstance(mask_size, dict)
            else mask_size
        )

        mask_pad_size = mask_pad_size if mask_pad_size is not None else {"height": 256, "width": 256}
        mask_pad_size = get_size_dict(mask_pad_size, default_to_square=True)

        self.do_resize = do_resize
        self.size = size
        self.mask_size = mask_size
''',1)
s=s.replace('''        self.pad_size = pad_size
        self.do_convert_rgb''','''        self.pad_size = pad_size
        self.mask_pad_size = mask_pad_size
        self.do_convert_rgb''',1)

# preprocess body
start=s.index('    def preprocess(\n')
end=s.index('    def post_process_masks(\n')
new='''    def _preprocess(
        self,
        image: ImageInput,
        do_resize: bool,
        do_rescale: bool,
        do_normalize: bool,
        size: Optional[Dict[str, int]] = None,
        resample: PILImageResampling = None,
        rescale_factor: Optional[float] = None,
        image_mean: Optional[Union[float, List[float]]] = None,
        image_std: Optional[Union[float, List[float]]] = None,
        do_pad: Optional[bool] = None,
        pad_size: Optional[Dict[str, int]] = None,
        input_data_format: Optional[Union[str, ChannelDimension]] = None,
    ):
        if do_resize:
            image = self.resize(image=image, size=size, resample=resample, input_data_format=input_data_format)
        reshaped_input_size = get_image_size(image, channel_dim=input_data_format)

        if do_rescale:
            image = self.rescale(image=image, scale=rescale_factor, input_data_format=input_data_format)

        if do_normalize:
            image = self.normalize(image=image, mean=image_mean, std=image_std, input_data_format=input_data_format)

        if do_pad:
            image = self.pad_image(image=image, pad_size=pad_size, input_data_format=input_data_format)

        return image, reshaped_input_size

    def _preprocess_image(
        self,
        image: ImageInput,
        do_resize: Optional[bool] = None,
        size: Dict[str, int] = None,
        resample: PILImageResampling = None,
        do_rescale: bool = None,
        rescale_factor: Optional[float] = None,
        do_normalize: Optional[bool] = None,
        image_mean: Optional[Union[float, List[float]]] = None,
        image_std: Optional[Union[float, List[float]]] = None,
        do_pad: Optional[bool] = None,
        pad_size: Optional[Dict[str, int]] = None,
        do_convert_rgb: Optional[bool] = None,
        data_format: Optional[Union[str, ChannelDimension]] = None,
        input_data_format: Optional[Union[str, ChannelDimension]] = None,
    ) -> Tuple[np.ndarray, Tuple[int, int], Tuple[int, int]]:
        image = to_numpy_array(image)

        # PIL RGBA images are converted to RGB
        if do_convert_rgb:
            image = convert_to_rgb(image)

        # All transformations expect numpy arrays.
        image = to_numpy_array(image)

        if is_scaled_image(image) and do_rescale:
            logger.warning_once(
                "It looks like you are trying to rescale already rescaled images. If the input"
                " images have pixel values between 0 and 1, set `do_rescale=False` to avoid rescaling them again."
            )

        if input_data_format is None:
            input_data_format = infer_channel_dimension_format(image)

        original_size = get_image_size(image, channel_dim=input_data_format)

        image, reshaped_input_size = self._preprocess(
            image=image,
            do_resize=do_resize,
            size=size,
            resample=resample,
            do_rescale=do_rescale,
            rescale_factor=rescale_factor,
            do_normalize=do_normalize,
            image_mean=image_mean,
            image_std=image_std,
            do_pad=do_pad,
            pad_size=pad_size,
            input_data_format=input_data_format,
        )

        if data_format is not None:
            image = to_channel_dimension_format(image, data_format, input_channel_dim=input_data_format)

        return image, original_size, reshaped_input_size

    def _preprocess_mask(
        self,
        segmentation_map: ImageInput,
        do_resize: Optional[bool] = None,
        mask_size: Dict[str, int] = None,
        do_pad: Optional[bool] = None,
        mask_pad_size: Optional[Dict[str, int]] = None,
        input_data_format: Optional[Union[str, ChannelDimension]] = None,
    ) -> np.ndarray:
        segmentation_map = to_numpy_array(segmentation_map)

        # Add channel dimension if missing - needed for certain transformations
        if segmentation_map.ndim == 2:
            added_channel_dim = True
            segmentation_map = segmentation_map[None, ...]
            input_data_format = ChannelDimension.FIRST
        else:
            added_channel_dim = False
            if input_data_format is None:
                input_data_format = infer_channel_dimension_format(segmentation_map, num_channels=1)

        original_size = get_image_size(segmentation_map, channel_dim=input_data_format)

        segmentation_map, _ = self._preprocess(
            image=segmentation_map,
            do_resize=do_resize,
            size=mask_size,
            resample=PILImageResampling.NEAREST,
            do_rescale=False,
            do_normalize=False,
            do_pad=do_pad,
            pad_size=mask_pad_size,
            input_data_format=input_data_format,
        )

        # Remove extra channel dimension if added for processing
        if added_channel_dim:
            segmentation_map = segmentation_map.squeeze(0)
        segmentation_map = segmentation_map.astype(np.int64)

        return segmentation_map, original_size

    def preprocess(
        self,
        images: ImageInput,
        segmentation_maps: Optional[ImageInput] = None,
        do_resize: Optional[bool] = None,
        size: Optional[Dict[str, int]] = None,
        mask_size: Optional[Dict[str, int]] = None,
        resample: Optional["PILImageResampling"] = None,
        do_rescale: Optional[bool] = None,
        rescale_factor: Optional[Union[int, float]] = None,
        do_normalize: Optional[bool] = None,
        image_mean: Optional[Union[float, List[float]]] = None,
        image_std: Optional[Union[float, List[float]]] = None,
        do_pad: Optional[bool] = None,
        pad_size: Optional[Dict[str, int]] = None,
        mask_pad_size: Optional[Dict[str, int]] = None,
        do_convert_rgb: Optional[bool] = None,
        return_tensors: Optional[Union[str, TensorType]] = None,
        data_format: ChannelDimension = ChannelDimension.FIRST,
        input_data_format: Optional[Union[str, ChannelDimension]] = None,
        **kwargs,
    ):
        """
        Preprocess an image or batch of images.

        Args:
            images (`ImageInput`):
                Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
                passing in images with pixel values between 0 and 1, set `do_rescale=False`.
            segmentation_maps (`ImageInput`, *optional*):
                Segmentation map to preprocess.
            do_resize (`bool`, *optional*, defaults to `self.do_resize`):
                Whether to resize the image.
            size (`Dict[str, int]`, *optional*, defaults to `self.size`):
                Controls the size of the image after `resize`. The longest edge of the image is resized to
                `size["longest_edge"]` whilst preserving the aspect ratio.
            mask_size (`Dict[str, int]`, *optional*, defaults to `self.mask_size`):
                Controls the size of the segmentation map after `resize`. The longest edge of the image is resized to
                `size["longest_edge"]` whilst preserving the aspect ratio.
            resample (`PILImageResampling`, *optional*, defaults to `self.resample`):
                `PILImageResampling` filter to use when resizing the image e.g. `PILImageResampling.BILINEAR`.
            do_rescale (`bool`, *optional*, defaults to `self.do_rescale`):
                Whether to rescale the image pixel values by rescaling factor.
            rescale_factor (`int` or `float`, *optional*, defaults to `self.rescale_factor`):
                Rescale factor to apply to the image pixel values.
            do_normalize (`bool`, *optional*, defaults to `self.do_normalize`):
                Whether to normalize the image.
            image_mean (`float` or `List[float]`, *optional*, defaults to `self.image_mean`):
                Image mean to normalize the image by if `do_normalize` is set to `True`.
            image_std (`float` or `List[float]`, *optional*, defaults to `self.image_std`):
                Image standard deviation to normalize the image by if `do_normalize` is set to `True`.
            do_pad (`bool`, *optional*, defaults to `self.do_pad`):
                Whether to pad the image.
            pad_size (`Dict[str, int]`, *optional*, defaults to `self.pad_size`):
                Controls the size of the padding applied to the image. The image is padded to `pad_size["height"]` and
                `pad_size["width"]` if `do_pad` is set to `True`.
            mask_pad_size (`Dict[str, int]`, *optional*, defaults to `self.mask_pad_size`):
                Controls the size of the padding applied to the segmentation map. The image is padded to
                `mask_pad_size["height"]` and `mask_pad_size["width"]` if `do_pad` is set to `True`.
            do_convert_rgb (`bool`, *optional*, defaults to `self.do_convert_rgb`):
                Whether to convert the image to RGB.
            return_tensors (`str` or `TensorType`, *optional*):
                The type of tensors to return. Can be one of:
                    - Unset: Return a list of `np.ndarray`.
                    - `TensorType.TENSORFLOW` or `'tf'`: Return a batch of type `tf.Tensor`.
                    - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`.
                    - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.
                    - `TensorType.JAX` or `'jax'`: Return a batch of type `jax.numpy.ndarray`.
            data_format (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`):
                The channel dimension format for the output image. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
                - Unset: Use the channel dimension format of the input image.
            input_data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format for the input image. If unset, the channel dimension format is inferred
                from the input image. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
                - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.
        """
        do_resize = do_resize if do_resize is not None else self.do_resize
        size = size if size is not None else self.size
        size = get_size_dict(max_size=size, default_to_square=False) if not isinstance(size, dict) else size
        mask_size = mask_size if mask_size is not None else self.mask_size
        mask_size = (
            get_size_dict(max_size=mask_size, default_to_square=False)
            if not isinstance(mask_size, dict)
            else mask_size
        )
        resample = resample if resample is not None else self.resample
        do_rescale = do_rescale if do_rescale is not None else self.do_rescale
        rescale_factor = rescale_factor if rescale_factor is not None else self.rescale_factor
        do_normalize = do_normalize if do_normalize is not None else self.do_normalize
        image_mean = image_mean if image_mean is not None else self.image_mean
        image_std = image_std if image_std is not None else self.image_std
        do_pad = do_pad if do_pad is not None else self.do_pad
        pad_size = pad_size if pad_size is not None else self.pad_size
        pad_size = get_size_dict(pad_size, default_to_square=True)
        mask_pad_size = mask_pad_size if mask_pad_size is not None else self.mask_pad_size
        mask_pad_size = get_size_dict(mask_pad_size, default_to_square=True)
        do_convert_rgb = do_convert_rgb if do_convert_rgb is not None else self.do_convert_rgb

        images = make_list_of_images(images)

        if not valid_images(images):
            raise ValueError(
                "Invalid image type. Must be of type PIL.Image.Image, numpy.ndarray, "
                "torch.Tensor, tf.Tensor or jax.ndarray."
            )

        if segmentation_maps is not None:
            segmentation_maps = make_list_of_images(segmentation_maps, expected_ndims=2)

            if not valid_images(segmentation_maps):
                raise ValueError(
                    "Invalid segmentation map type. Must be of type PIL.Image.Image, numpy.ndarray, "
                    "torch.Tensor, tf.Tensor or jax.ndarray."
                )

            if len(segmentation_maps) != len(images):
                raise ValueError(
                    f"The number of segmentation maps ({len(segmentation_maps)}) must match the number of images "
                    f"({len(images)})."
                )

        if do_resize and (size is None or resample is None):
            raise ValueError("Size and resample must be specified if do_resize is True.")

        if do_resize and segmentation_maps is not None and mask_size is None:
            raise ValueError("Mask size must be specified if do_resize is True and segmentation maps are given.")

        if do_rescale and rescale_factor is None:
            raise ValueError("Rescale factor must be specified if do_rescale is True.")

        if do_normalize and (image_mean is None or image_std is None):
            raise ValueError("Image mean and std must be specified if do_normalize is True.")

        if do_pad and pad_size is None:
            raise ValueError("Pad size must be specified if do_pad is True.")

        if do_pad and segmentation_maps is not None and mask_pad_size is None:
            raise ValueError("Mask pad size must be specified if do_pad is True and segmentation maps are given.")

        images, original_sizes, reshaped_input_sizes = zip(
            *(
                self._preprocess_image(
                    image=img,
                    do_resize=do_resize,
                    size=size,
                    resample=resample,
                    do_rescale=do_rescale,
                    rescale_factor=rescale_factor,
                    do_normalize=do_normalize,
                    image_mean=image_mean,
                    image_std=image_std,
                    do_pad=do_pad,
                    pad_size=pad_size,
                    do_convert_rgb=do_convert_rgb,
                    data_format=data_format,
                    input_data_format=input_data_format,
                )
                for img in images
            )
        )

        data = {
            "pixel_values": images,
            "original_sizes": original_sizes,
            "reshaped_input_sizes": reshaped_input_sizes,
        }

        if segmentation_maps is not None:
            segmentation_maps, original_mask_sizes = zip(
                *(
                    self._preprocess_mask(
                        segmentation_map=mask,
                        do_resize=do_resize,
                        mask_size=mask_size,
                        do_pad=do_pad,
                        mask_pad_size=mask_pad_size,
                        input_data_format=input_data_format,
                    )
                    for mask in segmentation_maps
                )
            )

            # masks should start out the same size as input images
            assert all(
                original_im_size == original_mask_size
                for original_im_size, original_mask_size in zip(original_sizes, original_mask_sizes)
            ), "Segmentation maps should be the same size as input images."

            data["labels"] = segmentation_maps

        return BatchFeature(data=data, tensor_type=return_tensors)

'''
s=s[:start]+new+s[end:]
open(p,'w').write(s)
EOF
grep -n "def make_list_of_images" -A3 /dev/null ../../image_utils.py; grep -n "def infer_channel_dimension_format" -A4 ../../image_utils.py
```

tool result:

```
../../image_utils.py:129:def make_list_of_images(images, expected_ndims: int = 3) -> List[ImageInput]:
../../image_utils.py-130-    """
../../image_utils.py-131-    Ensure that the input is a list of images. If the input is a single image, it is converted to a list of length 1.
../../image_utils.py-132-    If the input is a batch of images, it is converted to a list of images.
177:def infer_channel_dimension_format(
178-    image: np.ndarray, num_channels: Optional[Union[int, Tuple[int, ...]]] = None
179-) -> ChannelDimension:
180-    """
181-    Infers the channel dimension format of `image`.
```

**assistant:** Let me fix a couple of things: drop the premature `to_numpy_array` (it would bypass RGB conversion of PIL images), replace the `assert` with a `ValueError`, and fix the return annotation.

**tool call: Bash**

```bash
cd src/transformers/models/sam && python3 - <<'EOF'
p='image_processing_sam.py'
s=open(p).read()
old='''    ) -> Tuple[np.ndarray, Tuple[int, int], Tuple[int, int]]:
        image = to_numpy_array(image)

        # PIL'''
assert old in s
s=s.replace(old,'''    ) -> Tuple[np.ndarray, Tuple[int, int], Tuple[int, int]]:
        # PIL''')
old='''        input_data_format: Optional[Union[str, ChannelDimension]] = None,
    ) -> np.ndarray:
        segmentation_map'''
assert old in s
s=s.replace(old,'''        input_data_format: Optional[Union[str, ChannelDimension]] = None,
    ) -> Tuple[np.ndarray, Tuple[int, int]]:
        segmentation_map''')
old='''            # masks should start out the same size as input images
            assert all(
                original_im_size == original_mask_size
                for original_im_size, original_mask_size in zip(original_sizes, original_mask_sizes)
            ), "Segmentation maps should be the same size as input images."
'''
assert old in s
s=s.replace(old,'''            # masks should start out the same size as input images
            if any(
                original_im_size != original_mask_size
                for original_im_size, original_mask_size in zip(original_sizes, original_mask_sizes)
            ):
                raise ValueError("Segmentation maps should be the same size as input images.")
''')
open(p,'w').write(s)

p='processing_sam.py'
s=open(p).read()
s=s.replace('''        images=None,
        input_points=None,''','''        images=None,
        segmentation_maps=None,
        input_points=None,''',1)
s=s.replace('''            images,
            return_tensors=return_tensors,''','''            images,
            segmentation_maps=segmentation_maps,
            return_tensors=return_tensors,''',1)
open(p,'w').write(s)
EOF
git diff processing_sam.py
```

tool result:

```
(eval):cd:1: no such file or directory: src/transformers/models/sam
```

**tool call: Bash**

```bash
pwd; git status --short
```

tool result:

```
/work/huggingface__transformers-27463/repo/src/transformers/models/sam
 M ../../../../setup.py
 M image_processing_sam.py
?? ../../../../Dockerfile
```

**assistant:** The shell is already in the `sam` directory; rerunning the script there. (`setup.py`/`Dockerfile` changes are not mine — I'll leave them alone.)

**tool call: Bash**

```bash
python3 - <<'EOF'
p='image_processing_sam.py'
s=open(p).read()
old='''    ) -> Tuple[np.ndarray, Tuple[int, int], Tuple[int, int]]:
        image = to_numpy_array(image)

        # PIL'''
assert old in s
s=s.replace(old,'''    ) -> Tuple[np.ndarray, Tuple[int, int], Tuple[int, int]]:
        # PIL''')
old='''        input_data_format: Optional[Union[str, ChannelDimension]] = None,
    ) -> np.ndarray:
        segmentation_map'''
assert old in s
s=s.replace(old,'''        input_data_format: Optional[Union[str, ChannelDimension]] = None,
    ) -> Tuple[np.ndarray, Tuple[int, int]]:
        segmentation_map''')
old='''            # masks should start out the same size as input images
            assert all(
                original_im_size == original_mask_size
                for original_im_size, original_mask_size in zip(original_sizes, original_mask_sizes)
            ), "Segmentation maps should be the same size as input images."
'''
assert old in s
s=s.replace(old,'''            # masks should start out the same size as input images
            if any(
                original_im_size != original_mask_size
                for original_im_size, original_mask_size in zip(original_sizes, original_mask_sizes)
            ):
                raise ValueError("Segmentation maps should be the same size as input images.")
''')
open(p,'w').write(s)

p='processing_sam.py'
s=open(p).read()
s=s.replace('''        images=None,
        input_points=None,''','''        images=None,
        segmentation_maps=None,
        input_points=None,''',1)
s=s.replace('''            images,
            return_tensors=return_tensors,''','''            images,
            segmentation_maps=segmentation_maps,
            return_tensors=return_tensors,''',1)
open(p,'w').write(s)
EOF
git diff processing_sam.py
```

tool result:

```
diff --git a/src/transformers/models/sam/processing_sam.py b/src/transformers/models/sam/processing_sam.py
index 7c632b215..ed89ebeb3 100644
--- a/src/transformers/models/sam/processing_sam.py
+++ b/src/transformers/models/sam/processing_sam.py
@@ -57,6 +57,7 @@ class SamProcessor(ProcessorMixin):
     def __call__(
         self,
         images=None,
+        segmentation_maps=None,
         input_points=None,
         input_labels=None,
         input_boxes=None,
@@ -69,6 +70,7 @@ class SamProcessor(ProcessorMixin):
         """
         encoding_image_processor = self.image_processor(
             images,
+            segmentation_maps=segmentation_maps,
             return_tensors=return_tensors,
             **kwargs,
         )
```

**assistant:** Now a reproduction/check script covering the issue's scenario and edge cases:

**tool call: Bash**

```bash
cd ../../../.. && cat > repro_sam_masks.py <<'EOF'
import numpy as np
from PIL import Image
from transformers import SamImageProcessor, SamProcessor

ip = SamImageProcessor()
proc = SamProcessor(ip)
img = Image.fromarray(np.random.randint(0, 255, (768, 1024, 3), dtype=np.uint8))
mask = Image.fromarray(np.random.randint(0, 2, (768, 1024), dtype=np.uint8))

out = proc(img, segmentation_maps=mask, input_boxes=[[[10, 10, 100, 100]]], return_tensors="pt")
print({k: tuple(v.shape) for k, v in out.items()}, out["labels"].dtype)
assert out["labels"].shape == (1, 256, 256)
assert out["labels"][0, 192:].sum() == 0  # padded rows
assert set(out["labels"].unique().tolist()) <= {0, 1}

# batch of numpy masks, channel-dim mask, and channels-last mask
imgs = [np.random.randint(0, 255, (30, 400, 3), dtype=np.uint8)] * 2
masks = [np.random.randint(0, 2, (30, 400), dtype=np.uint8)] * 2
o = ip(imgs, segmentation_maps=masks, return_tensors="np")
print(o["pixel_values"].shape, o["labels"].shape)
o = ip(imgs[0], segmentation_maps=masks[0][None], return_tensors="np")
print(o["labels"].shape)
o = ip(imgs[0], segmentation_maps=masks[0][..., None], return_tensors="np")
print(o["labels"].shape)

# no masks: unchanged behaviour
o = ip(imgs, return_tensors="np")
print(sorted(o.keys()), o["pixel_values"].shape)

try:
    ip(imgs[0], segmentation_maps=masks[0][:10])
except ValueError as e:
    print("ValueError:", e)
EOF
../bin/envrun 'python repro_sam_masks.py' 2>&1 | grep -v Warning
```

tool result:

```
2026-10-09 07:13:04.309138: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:9261] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2026-10-09 07:13:04.309756: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:607] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2026-10-09 07:13:04.335136: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1515] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
{'pixel_values': (1, 3, 1024, 1024), 'original_sizes': (1, 2), 'reshaped_input_sizes': (1, 2), 'labels': (1, 256, 256), 'input_boxes': (1, 1, 4)} torch.int64
(2, 3, 1024, 1024) (2, 256, 256)
(1, 256, 256)
Traceback (most recent call last):
  File "/testbed/repro_sam_masks.py", line 23, in <module>
    o = ip(imgs[0], segmentation_maps=masks[0][..., None], return_tensors="np")
  File "/testbed/src/transformers/image_processing_utils.py", line 552, in __call__
    return self.preprocess(images, **kwargs)
  File "/testbed/src/transformers/models/sam/image_processing_sam.py", line 507, in preprocess
    raise ValueError(
ValueError: The number of segmentation maps (30) must match the number of images (1).
```

**thinking:**

```
I confirmed the single unbatched (H, W, 1) mask gets read as a batch of 2D maps, consistent with how Segformer and other processors handle 3D input, with the length check catching it clearly. Now I'll test that same format passed as a list.


```

**tool call: Bash**

```bash
sed -i '' 's/segmentation_maps=masks\[0\]\[..., None\]/segmentation_maps=[masks[0][..., None]]/' repro_sam_masks.py && ../bin/envrun 'python repro_sam_masks.py' 2>&1 | grep -v "Warning\|cuda"
```

tool result:

```
{'pixel_values': (1, 3, 1024, 1024), 'original_sizes': (1, 2), 'reshaped_input_sizes': (1, 2), 'labels': (1, 256, 256), 'input_boxes': (1, 1, 4)} torch.int64
(2, 3, 1024, 1024) (2, 256, 256)
(1, 256, 256)
(1, 256, 256, 1)
['original_sizes', 'pixel_values', 'reshaped_input_sizes'] (2, 3, 1024, 1024)
ValueError: Segmentation maps should be the same size as input images.
```

**assistant:** All work. Now the existing SAM tests and repo consistency checks:

**tool call: Bash**

```bash
rm repro_sam_masks.py && ../bin/envrun 'python -m pytest tests/models/sam -q -x 2>&1 | tail -5; ruff check src/transformers/models/sam; ruff format --check src/transformers/models/sam; python utils/check_docstrings.py 2>&1 | tail -3'
```

tool result:

```
  /testbed/tests/test_modeling_common.py:463: FutureWarning: `torch.testing.assert_allclose()` is deprecated since 1.12 and will be removed in a future release. Please use `torch.testing.assert_close()` instead. You can find detailed upgrade instructions in https://github.com/pytorch/pytorch/issues/61844.
    torch.testing.assert_allclose(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
87 passed, 118 skipped, 6 warnings in 15.77s
7 files left unchanged
The following objects docstrings do not match their signature. Run `make fix-copies` to fix this.
- TFRegNetForImageClassification
- TFRegNetModel
```

**tool call: Bash**

```bash
git status --short
```

tool result:

```
 M setup.py
 M src/transformers/models/sam/image_processing_sam.py
 M src/transformers/models/sam/processing_sam.py
?? Dockerfile
```

**assistant:** The SAM image processor and `SamProcessor` now accept masks and resize them to the size the model's `pred_masks` come out at. You can drop the hand-written resize-and-pad code from the issue and write:

```python
inputs = processor(image, segmentation_maps=mask, input_boxes=[[prompt]], return_tensors="pt")
inputs["labels"]  # (1, 256, 256), int64 — same shape as pred_masks
```

**Changes**

- **`src/transformers/models/sam/image_processing_sam.py`**
  - `preprocess` takes a new `segmentation_maps` argument.
  - Two new settings, `mask_size` and `mask_pad_size`, can be set in `__init__` or per call. By default masks are resized so the longest edge is 256 and then padded to 256×256, which matches `pred_masks`.
  - Masks are resized with nearest-neighbour so labels stay as whole numbers (0/1 stays 0/1). They skip rescaling and normalisation and are returned as int64 under the `labels` key.
  - It raises a `ValueError` if the number of masks doesn't match the number of images, or if a mask isn't the same size as its image.
  - I split the per-image steps into small helpers so images and masks share the same resize and pad code. Calls without masks return exactly the same output as before.
- **`src/transformers/models/sam/processing_sam.py`**: `SamProcessor.__call__` takes `segmentation_maps` and passes it to the image processor.

`segmentation_maps` is the second parameter of `SamProcessor.__call__`, before `input_points`. Code that passes `input_points` by position (rather than `input_points=...`) would now break. Keyword calls are unaffected.

**Testing**

- A throwaway script (now deleted) covered:
  - the issue's case: a 768×1024 image and mask give `labels` of shape `(1, 256, 256)`, the padded rows are zero, and values stay 0/1;
  - batches of masks;
  - masks with an extra channel dimension;
  - no masks: same output as before;
  - a mask whose size doesn't match its image raises the error.
- `tests/models/sam`: 87 passed, 118 skipped.
- `ruff check` and `ruff format --check` are clean on the SAM folder.
- `utils/check_docstrings.py` reports two mismatches, both in TFRegNet, not in SAM.

**Limitations**

- A single 3D mask passed on its own, such as shape `(H, W, 1)`, is read as a batch of 2D masks and fails the count check with a clear error. Wrapping it in a list (`[mask]`) works. Segformer's processor treats this input the same way.
- Masks with label values above 255 won't survive the resize, because it goes through an 8-bit image conversion. Binary SAM masks are fine.

`git status` also shows a modified `setup.py` and an untracked `Dockerfile`. I didn't make those changes and left them alone.

_session end: success, turns 12, is_error False_

## Container commands (task container, no network; broker log)

- `rc=1` 7.34 s: python repro_sam_masks.py
- `rc=0` 6.23 s: python repro_sam_masks.py
- `rc=0` 48.77 s: python -m pytest tests/models/sam -q -x 2>&1 | tail -5; ruff check src/transformers/models/sam; ruff format --check src/transformers/models/sam; python utils/check_docstrings.py 2>&1 | tail -3
