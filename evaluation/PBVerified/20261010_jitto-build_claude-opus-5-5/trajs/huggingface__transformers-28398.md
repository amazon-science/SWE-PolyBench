# Instance: huggingface__transformers-28398

- Final resolved (evaluator, logs/huggingface__transformers-28398_result.json): True
- Run state: DONE
- One attempt. Duration 72.1 s, turns 9, actor cost $0.26151840000000004, container commands 4
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/huggingface__transformers-28398/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-28398/repo. Consider the following issue description:

<issue_description>
OneFormerImageProcessor does not support passing local config file, always tries to download from repo
### System Info

- `transformers` version: 4.29.0.dev0
- Platform: Linux-5.19.0-41-generic-x86_64-with-glibc2.35
- Python version: 3.10.10
- Huggingface_hub version: 0.14.1
- Safetensors version: 0.3.1
- PyTorch version (GPU?): 2.0.0+cu117 (True)
- Tensorflow version (GPU?): 2.11.1 (False)
- Flax version (CPU?/GPU?/TPU?): 0.5.3 (cpu)
- Jax version: 0.3.6
- JaxLib version: 0.3.5
- Using GPU in script?: <fill in>
- Using distributed or parallel set-up in script?: <fill in>

### Who can help?

@amyeroberts

this forum post I put up seems like a bug: https://discuss.huggingface.co/t/how-to-load-local-config-json-for-oneformerimageprocessor-without-invoking-huggingfacehub-downloader/38372

The OneFormerImageProcessor should accept local config files without trying to download them from a repo_path

https://github.com/huggingface/transformers/blob/v4.28.1/src/transformers/models/oneformer/image_processing_oneformer.py#L323

### Information

- [X] The official example scripts
- [X] My own modified scripts

### Tasks

- [X] An officially supported task in the `examples` folder (such as GLUE/SQuAD, ...)
- [X] My own task or dataset (give details below)

### Reproduction

```
from transformers import OneFormerProcessor
config_path = "/local/config/path"
OneFormerProcessor.from_pretrained(config_path, ignore_mismatched_sizes=True)ignore_mismatched_sizes=True)
```

### Expected behavior

the processor gets initialized and doesn't error with 

```
            + f"Repository Not Found for url: {response.url}."
            + "\nPlease make sure you specified the correct `repo_id` and"
            " `repo_type`.\nIf you are trying to access a private or gated repo,"
            " make sure you are authenticated."
```

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-28398/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-28398/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-28398/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-28398/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/huggingface__transformers-28398/repo; grep -n "def load_metadata\|hf_hub_download\|repo_path\|class_info_file" src/transformers/models/oneformer/image_processing_oneformer.py | head -50
```

tool result:

```
22:from huggingface_hub import hf_hub_download
334:def prepare_metadata(repo_path, class_info_file):
335:    with open(hf_hub_download(repo_path, class_info_file, repo_type="dataset"), "r") as f:
389:        repo_path (`str`, defaults to `shi-labs/oneformer_demo`, *optional*, defaults to `"shi-labs/oneformer_demo"`):
391:        class_info_file (`str`, *optional*):
392:            JSON file containing class information for the dataset. It is stored inside on the `repo_path` dataset
412:        repo_path: str = "shi-labs/oneformer_demo",
413:        class_info_file: str = None,
444:        self.class_info_file = class_info_file
445:        self.repo_path = repo_path
446:        self.metadata = prepare_metadata(repo_path, class_info_file)
1214:            if "ade20k" in self.class_info_file and not is_demo and "instance" in task_type:
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-28398/repo; sed -n 15,40p src/transformers/models/oneformer/image_processing_oneformer.py; sed -n 330,450p src/transformers/models/oneformer/image_processing_oneformer.py; grep -n "metadata\|repo_path\|class_info" tests/models/oneformer/test_image_processing_oneformer.py tests/models/oneformer/test_processor_oneformer.py | head -40
```

tool result:

```
"""Image processor class for OneFormer."""

import json
import warnings
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple, Union

import numpy as np
from huggingface_hub import hf_hub_download

from ...image_processing_utils import BaseImageProcessor, BatchFeature, get_size_dict
from ...image_transforms import (
    PaddingMode,
    get_resize_output_image_size,
    pad,
    rescale,
    resize,
    to_channel_dimension_format,
)
from ...image_utils import (
    ChannelDimension,
    ImageInput,
    PILImageResampling,
    get_image_size,
    infer_channel_dimension_format,
    is_scaled_image,
    make_list_of_images,
    )
    return output_size


def prepare_metadata(repo_path, class_info_file):
    with open(hf_hub_download(repo_path, class_info_file, repo_type="dataset"), "r") as f:
        class_info = json.load(f)
    metadata = {}
    class_names = []
    thing_ids = []
    for key, info in class_info.items():
        metadata[key] = info["name"]
        class_names.append(info["name"])
        if info["isthing"]:
            thing_ids.append(int(key))
    metadata["thing_ids"] = thing_ids
    metadata["class_names"] = class_names
    return metadata


class OneFormerImageProcessor(BaseImageProcessor):
    r"""
    Constructs a OneFormer image processor. The image processor can be used to prepare image(s), task input(s) and
    optional text inputs and targets for the model.

    This image processor inherits from [`BaseImageProcessor`] which contains most of the main methods. Users should
    refer to this superclass for more information regarding those methods.

    Args:
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the input to a certain `size`.
        size (`int`, *optional*, defaults to 800):
            Resize the input to the given size. Only has an effect if `do_resize` is set to `True`. If size is a
            sequence like `(width, height)`, output size will be matched to this. If size is an int, smaller edge of
            the image will be matched to this number. i.e, if `height > width`, then image will be rescaled to `(size *
            height / width, size)`.
        resample (`int`, *optional*, defaults to `Resampling.BILINEAR`):
            An optional resampling filter. This can be one of `PIL.Image.Resampling.NEAREST`,
            `PIL.Image.Resampling.BOX`, `PIL.Image.Resampling.BILINEAR`, `PIL.Image.Resampling.HAMMING`,
            `PIL.Image.Resampling.BICUBIC` or `PIL.Image.Resampling.LANCZOS`. Only has an effect if `do_resize` is set
            to `True`.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Whether to rescale the input to a certain `scale`.
        rescale_factor (`float`, *optional*, defaults to `1/ 255`):
            Rescale the input by the given factor. Only has an effect if `do_rescale` is set to `True`.
        do_normalize (`bool`, *optional*, defaults to `True`):
            Whether or not to normalize the input with mean and standard deviation.
        image_mean (`int`, *optional*, defaults to `[0.485, 0.456, 0.406]`):
            The sequence of means for each channel, to be used when normalizing images. Defaults to the ImageNet mean.
        image_std (`int`, *optional*, defaults to `[0.229, 0.224, 0.225]`):
            The sequence of standard deviations for each channel, to be used when normalizing images. Defaults to the
            ImageNet std.
        ignore_index (`int`, *optional*):
            Label to be assigned to background pixels in segmentation maps. If provided, segmentation map pixels
            denoted with 0 (background) will be replaced with `ignore_index`.
        do_reduce_labels (`bool`, *optional*, defaults to `False`):
            Whether or not to decrement all label values of segmentation maps by 1. Usually used for datasets where 0
            is used for background, and background itself is not included in all classes of a dataset (e.g. ADE20k).
            The background label will be replaced by `ignore_index`.
        repo_path (`str`, defaults to `shi-labs/oneformer_demo`, *optional*, defaults to `"shi-labs/oneformer_demo"`):
            Dataset repository on huggingface hub containing the JSON file with class information for the dataset.
        class_info_file (`str`, *optional*):
            JSON file containing class information for the dataset. It is stored inside on the `repo_path` dataset
            repository.
        num_text (`int`, *optional*):
            Number of text entries in the text input list.
    """

    model_input_names = ["pixel_values", "pixel_mask", "task_inputs"]

    def __init__(
        self,
        do_resize: bool = True,
        size: Dict[str, int] = None,
        resample: PILImageResampling = PILImageResampling.BILINEAR,
        do_rescale: bool = True,
        rescale_factor: float = 1 / 255,
        do_normalize: bool = True,
        image_mean: Union[float, List[float]] = None,
        image_std: Union[float, List[float]] = None,
        ignore_index: Optional[int] = None,
        do_reduce_labels: bool = False,
        repo_path: str = "shi-labs/oneformer_demo",
        class_info_file: str = None,
        num_text: Optional[int] = None,
        **kwargs,
    ):
        if "max_size" in kwargs:
            self._max_size = kwargs.pop("max_size")
        else:
            self._max_size = 1333

        size = size if size is not None else {"shortest_edge": 800, "longest_edge": self._max_size}
        size = get_size_dict(size, max_size=self._max_size, default_to_square=False)

        if "reduce_labels" in kwargs:
            warnings.warn(
                "The `reduce_labels` argument is deprecated and will be removed in v4.27. "
                "Please use `do_reduce_labels` instead.",
                FutureWarning,
            )
            do_reduce_labels = kwargs.pop("reduce_labels")

        super().__init__(**kwargs)
        self.do_resize = do_resize
        se
[... 4924 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-28398/repo; grep -rn "load_metadata\|image_processing_oneformer import\|tmpdirname\|TemporaryDirectory" tests/models/oneformer/ | head; grep -rn "RepositoryNotFoundError" src/transformers/utils/hub.py | head -3
```

tool result:

```
tests/models/oneformer/test_processor_oneformer.py:37:        from transformers.models.oneformer.image_processing_oneformer import binary_mask_to_rle
tests/models/oneformer/test_processor_oneformer.py:404:        with tempfile.TemporaryDirectory() as tmpdirname:
tests/models/oneformer/test_processor_oneformer.py:405:            feat_extract_first.save_pretrained(tmpdirname)
tests/models/oneformer/test_processor_oneformer.py:406:            check_json_file_has_correct_format(os.path.join(tmpdirname, "preprocessor_config.json"))
tests/models/oneformer/test_processor_oneformer.py:407:            feat_extract_second = self.feature_extraction_class.from_pretrained(tmpdirname)
tests/models/oneformer/test_image_processing_oneformer.py:34:        from transformers.models.oneformer.image_processing_oneformer import binary_mask_to_rle
src/transformers/utils/hub.py:51:    RepositoryNotFoundError,
src/transformers/utils/hub.py:403:    except RepositoryNotFoundError as e:
src/transformers/utils/hub.py:623:    except RepositoryNotFoundError as e:
```

**assistant:** Reproducing first: a local repo_path dir with a class info file.

**tool call: Bash**

```bash
cd /work/huggingface__transformers-28398/repo; cat > repro.py <<'EOF'
import json, os, tempfile
from transformers import OneFormerImageProcessor
info = {"0": {"isthing": 0, "name": "foo"}, "1": {"isthing": 1, "name": "bar"}}
with tempfile.TemporaryDirectory() as d:
    with open(os.path.join(d, "info.json"), "w") as f:
        json.dump(info, f)
    p = OneFormerImageProcessor(repo_path=d, class_info_file="info.json")
    print(p.metadata)
    # absolute path, no repo
    p = OneFormerImageProcessor(repo_path=None, class_info_file=os.path.join(d, "info.json"))
    print(p.metadata)
    p.save_pretrained(d)
    print(OneFormerImageProcessor.from_pretrained(d).metadata)
EOF
../bin/envrun 'HF_HUB_OFFLINE=1 python repro.py 2>&1 | tail -3'
```

tool result:

```
  File "/usr/local/lib/python3.10/site-packages/huggingface_hub/utils/_validators.py", line 154, in validate_repo_id
    raise HFValidationError(
huggingface_hub.errors.HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/tmp/tmpsd0mj_zo'. Use `repo_type` argument if needed.
```

**assistant:** Now the fix: load the class-info file locally when it exists, otherwise fall back to the Hub.

**tool call: Bash**

```bash
cd /work/huggingface__transformers-28398/repo; python3 - <<'EOF'
p = "src/transformers/models/oneformer/image_processing_oneformer.py"
s = open(p).read()
s = s.replace('''import json
import warnings
''', '''import json
import os
import warnings
''', 1)
s = s.replace('''from huggingface_hub import hf_hub_download
''', '''from huggingface_hub import hf_hub_download
from huggingface_hub.utils import RepositoryNotFoundError
''', 1)
s = s.replace('''def prepare_metadata(repo_path, class_info_file):
    with open(hf_hub_download(repo_path, class_info_file, repo_type="dataset"), "r") as f:
        class_info = json.load(f)
    metadata = {}''', '''def load_metadata(repo_id, class_info_file):
    fname = os.path.join("" if repo_id is None else repo_id, class_info_file)

    if not os.path.exists(fname) or not os.path.isfile(fname):
        if repo_id is None:
            raise ValueError(f"Could not file {fname} locally. repo_id must be defined if loading from the hub")
        # We try downloading from a dataset by default for backward compatibility
        try:
            fname = hf_hub_download(repo_id, class_info_file, repo_type="dataset")
        except RepositoryNotFoundError:
            fname = hf_hub_download(repo_id, class_info_file)

    with open(fname, "r") as f:
        class_info = json.load(f)

    return class_info


def prepare_metadata(class_info):
    metadata = {}''', 1)
s = s.replace('''        repo_path (`str`, defaults to `shi-labs/oneformer_demo`, *optional*, defaults to `"shi-labs/oneformer_demo"`):
            Dataset repository on huggingface hub containing the JSON file with class information for the dataset.
        class_info_file (`str`, *optional*):
            JSON file containing class information for the dataset. It is stored inside on the `repo_path` dataset
            repository.''', '''        repo_path (`str`, *optional*, defaults to `"shi-labs/oneformer_demo"`):
            Path to hub repo or local directory containing the JSON file with class information for the dataset.
            If unset, will look for `class_info_file` in the current working directory.
        class_info_file (`str`, *optional*):
            JSON file containing class information for the dataset. See `shi-labs/oneformer_demo/cityscapes_panoptic.json` for an example.''', 1)
s = s.replace('''        repo_path: str = "shi-labs/oneformer_demo",''', '''        repo_path: Optional[str] = "shi-labs/oneformer_demo",''', 1)
s = s.replace('''self.metadata = prepare_metadata(repo_path, class_info_file)''', '''self.metadata = prepare_metadata(load_metadata(repo_path, class_info_file))''', 1)
open(p, "w").write(s)
EOF
git diff --stat; ../bin/envrun 'HF_HUB_OFFLINE=1 python repro.py 2>&1 | tail -3'
```

tool result:

```
 .../models/oneformer/image_processing_oneformer.py | 34 +++++++++++++++++-----
 1 file changed, 26 insertions(+), 8 deletions(-)
{'0': 'foo', '1': 'bar', 'thing_ids': [1], 'class_names': ['foo', 'bar']}
{'0': 'foo', '1': 'bar', 'thing_ids': [1], 'class_names': ['foo', 'bar']}
{'0': 'foo', '1': 'bar', 'thing_ids': [1], 'class_names': ['foo', 'bar']}
```

**assistant:** Works. Let me tidy the docstring/typo and run the existing tests.

**tool call: Bash**

```bash
cd /work/huggingface__transformers-28398/repo; f=src/transformers/models/oneformer/image_processing_oneformer.py
sed -i '' 's/Could not file {fname} locally/Could not find {fname} locally/' $f
python3 - <<'EOF'
p = "src/transformers/models/oneformer/image_processing_oneformer.py"
s = open(p).read()
s = s.replace('''            JSON file containing class information for the dataset. See `shi-labs/oneformer_demo/cityscapes_panoptic.json` for an example.''', '''            JSON file containing class information for the dataset. See `shi-labs/oneformer_demo/cityscapes_panoptic.json`
            for an example.''')
open(p, "w").write(s)
EOF
rm repro.py
../bin/envrun 'ruff check src/transformers/models/oneformer/ && ruff format --check src/transformers/models/oneformer/; python -m pytest -q tests/models/oneformer/test_image_processing_oneformer.py tests/models/oneformer/test_processor_oneformer.py 2>&1 | tail -5'
```

tool result:

```
6 files left unchanged
FAILED tests/models/oneformer/test_processor_oneformer.py::OneFormerProcessingTest::test_integration_semantic_segmentation
FAILED tests/models/oneformer/test_processor_oneformer.py::OneFormerProcessingTest::test_post_process_instance_segmentation
FAILED tests/models/oneformer/test_processor_oneformer.py::OneFormerProcessingTest::test_post_process_panoptic_segmentation
FAILED tests/models/oneformer/test_processor_oneformer.py::OneFormerProcessingTest::test_post_process_semantic_segmentation
30 failed, 1 warning in 5.93s
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-28398/repo; ../bin/envrun 'python -m pytest -q tests/models/oneformer/test_image_processing_oneformer.py 2>&1 | grep -E "^E " | sort | uniq -c | head; git stash -q; python -m pytest -q tests/models/oneformer/test_image_processing_oneformer.py tests/models/oneformer/test_processor_oneformer.py 2>&1 | tail -1; git stash pop -q; git status --short'
```

tool result:

```
     15 E           huggingface_hub.errors.LocalEntryNotFoundError: An error happened while trying to locate the file on the Hub and we cannot find the requested files in the local cache. Please check your connection and try again or make sure your Internet connection is on.
      1 E           requests.exceptions.ConnectionError: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /datasets/shi-labs/oneformer_demo/resolve/main/ade20k_panoptic.json (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7fffbee34760>: Failed to resolve \'huggingface.co\' ([Errno -3] Temporary failure in name resolution)"))'), '(Request ID: 93e79de2-74ff-4575-a47d-a7f91697817b)')
      1 E           requests.exceptions.ConnectionError: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /datasets/shi-labs/oneformer_demo/resolve/main/ade20k_panoptic.json (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7fffbeee7c40>: Failed to resolve \'huggingface.co\' ([Errno -3] Temporary failure in name resolution)"))'), '(Request ID: 9caca33b-e597-4553-974c-ee8ecb058c31)')
      1 E           requests.exceptions.ConnectionError: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /datasets/shi-labs/oneformer_demo/resolve/main/ade20k_panoptic.json (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7fffbef5e4a0>: Failed to resolve \'huggingface.co\' ([Errno -3] Temporary failure in name resolution)"))'), '(Request ID: 4e3412a9-277e-4d5f-a5c3-b79a52a54965)')
      1 E           requests.exceptions.ConnectionError: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /datasets/shi-labs/oneformer_demo/resolve/main/ade20k_panoptic.json (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7fffbf00d330>: Failed to resolve \'huggingface.co\' ([Errno -3] Temporary failure in name resolution)"))'), '(Request ID: 1d812de3-e3e0-41b7-8600-82666c8cdb1a)')
      1 E           requests.exceptions.ConnectionError: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /datasets/shi-labs/oneformer_demo/resolve/main/ade20k_panoptic.json (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7fffbf0269e0>: Failed to resolve \'huggingface.co\' ([Errno -3] Temporary failure in name resolution)"))'), '(Request ID: b2b2a5fa-4a30-465d-9a9d-d98e9f47f97b)')
      1 E           requests.exceptions.ConnectionError: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /datasets/shi-labs/oneformer_demo/resolve/main/ade20k_panoptic.json (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7fffbf058310>: Failed to resolve \'huggingface.co\' ([Errno -3] Temporary failure in name resolution)"))'), '(Request ID: 506ca6d8-9103-4696-b337-b27d9ca984ad)')
      1 E           requests.exceptions.ConnectionError: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /datasets/shi-labs/oneformer_demo/resolve/main/ade20k_panoptic.json (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7fffbf0a50f0>: Failed to resolve \'huggingface.co\' ([Errno -3] Temporary failure in name resolution)"))'), '(Request ID: 0be1a797-629b-410f-baeb-59912a952686)')
      1 E           requests.exceptions.ConnectionError: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /datasets/shi-labs/oneformer_demo/resolve/main/ade20k_panoptic.json (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7fffbf15ad70>: Failed to resolve \'huggingface.co\' ([Errno -3] Temporary failure in name resolution)"))'), '(Request ID: 855f2c2b-42a2-413d-970f-d16401be96d8)')
      1 E           requests.exceptions.ConnectionError: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /datasets/shi-labs/oneformer_demo/resolve/main/ade20k_panoptic.json (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7fffbf1811b0>: Failed to resolve \'huggingface.co\' ([Errno -3] Temporary failure in name resolution)"))'), '(Request ID: 773c385b-f57a-4044-bf83-1c62b35a1e94)')
30 failed, 1 warning in 5.51s
 M src/transformers/models/oneformer/image_processing_oneformer.py
?? Dockerfile
```

**thinking:**

```
The OneFormer test failures are all due to lack of network access for downloading from the Hub, which happens regardless of my change—confirming these failures are unrelated to the fix. The untracked Dockerfile is also just part of the environment, not something I added.


```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-28398/repo; git diff
```

tool result:

```
diff --git a/src/transformers/models/oneformer/image_processing_oneformer.py b/src/transformers/models/oneformer/image_processing_oneformer.py
index c42001a96..9162e6b6f 100644
--- a/src/transformers/models/oneformer/image_processing_oneformer.py
+++ b/src/transformers/models/oneformer/image_processing_oneformer.py
@@ -15,11 +15,13 @@
 """Image processor class for OneFormer."""
 
 import json
+import os
 import warnings
 from typing import Any, Dict, Iterable, List, Optional, Set, Tuple, Union
 
 import numpy as np
 from huggingface_hub import hf_hub_download
+from huggingface_hub.utils import RepositoryNotFoundError
 
 from ...image_processing_utils import BaseImageProcessor, BatchFeature, get_size_dict
 from ...image_transforms import (
@@ -331,9 +333,25 @@ def get_oneformer_resize_output_image_size(
     return output_size
 
 
-def prepare_metadata(repo_path, class_info_file):
-    with open(hf_hub_download(repo_path, class_info_file, repo_type="dataset"), "r") as f:
+def load_metadata(repo_id, class_info_file):
+    fname = os.path.join("" if repo_id is None else repo_id, class_info_file)
+
+    if not os.path.exists(fname) or not os.path.isfile(fname):
+        if repo_id is None:
+            raise ValueError(f"Could not find {fname} locally. repo_id must be defined if loading from the hub")
+        # We try downloading from a dataset by default for backward compatibility
+        try:
+            fname = hf_hub_download(repo_id, class_info_file, repo_type="dataset")
+        except RepositoryNotFoundError:
+            fname = hf_hub_download(repo_id, class_info_file)
+
+    with open(fname, "r") as f:
         class_info = json.load(f)
+
+    return class_info
+
+
+def prepare_metadata(class_info):
     metadata = {}
     class_names = []
     thing_ids = []
@@ -386,11 +404,12 @@ class OneFormerImageProcessor(BaseImageProcessor):
             Whether or not to decrement all label values of segmentation maps by 1. Usually used for datasets where 0
             is used for background, and background itself is not included in all classes of a dataset (e.g. ADE20k).
             The background label will be replaced by `ignore_index`.
-        repo_path (`str`, defaults to `shi-labs/oneformer_demo`, *optional*, defaults to `"shi-labs/oneformer_demo"`):
-            Dataset repository on huggingface hub containing the JSON file with class information for the dataset.
+        repo_path (`str`, *optional*, defaults to `"shi-labs/oneformer_demo"`):
+            Path to hub repo or local directory containing the JSON file with class information for the dataset.
+            If unset, will look for `class_info_file` in the current working directory.
         class_info_file (`str`, *optional*):
-            JSON file containing class information for the dataset. It is stored inside on the `repo_path` dataset
-            repository.
+            JSON file containing class information for the dataset. See `shi-labs/oneformer_demo/cityscapes_panoptic.json`
+            for an example.
         num_text (`int`, *optional*):
             Number of text entries in the text input list.
     """
@@ -409,7 +428,7 @@ class OneFormerImageProcessor(BaseImageProcessor):
         image_std: Union[float, List[float]] = None,
         ignore_index: Optional[int] = None,
         do_reduce_labels: bool = False,
-        repo_path: str = "shi-labs/oneformer_demo",
+        repo_path: Optional[str] = "shi-labs/oneformer_demo",
         class_info_file: str = None,
         num_text: Optional[int] = None,
         **kwargs,
@@ -443,7 +462,7 @@ class OneFormerImageProcessor(BaseImageProcessor):
         self.do_reduce_labels = do_reduce_labels
         self.class_info_file = class_info_file
         self.repo_path = repo_path
-        self.metadata = prepare_metadata(repo_path, class_info_file)
+        self.metadata = prepare_metadata(load_metadata(repo_path, class_info_file))
         self.num_text = num_text
 
     def resize(
```

**assistant:** `OneFormerImageProcessor` (and so `OneFormerProcessor.from_pretrained`) can now read the class-info JSON from a local folder, and only goes to the Hub when the file isn't found locally.

**The cause:** `prepare_metadata` in `src/transformers/models/oneformer/image_processing_oneformer.py` always called `hf_hub_download(repo_path, class_info_file, repo_type="dataset")`. A local path was treated as a Hub repo name, which raised a "Repo id must be in the form…" error.

**The fix:** all changes are in that one file.
- **New `load_metadata(repo_id, class_info_file)`:** it builds `os.path.join(repo_id or "", class_info_file)`.
  - If that file exists locally, it opens it directly.
  - If not, it downloads from the Hub. It tries a dataset repo first, as before, and falls back to a model repo if no dataset repo is found.
  - If `repo_path` is `None` and the file doesn't exist locally, it raises a clear `ValueError`.
- **`prepare_metadata(class_info)`:** now only turns the loaded dict into the metadata.
- **`repo_path`:** its type is now `Optional[str]`, and the docstring explains that it can be a Hub repo or a local directory.

**Testing:** before the fix, a reproduction script running offline (`HF_HUB_OFFLINE=1`) failed with the error above. After the fix, all three cases it covers return the right metadata:
- a local directory as `repo_path`
- `repo_path=None` with a full file path as `class_info_file`
- `save_pretrained` and then `from_pretrained` from a local folder

I then deleted the script. `ruff check` and `ruff format --check` are clean.

**Existing tests not confirmed:** I couldn't confirm the existing OneFormer tests pass. All 30 fail in this sandbox because they download `shi-labs/oneformer_demo` from the Hub and there's no network. They fail the same way without my change, so the failures aren't caused by it, but the Hub download path still needs a run with network access to confirm.

_session end: success, turns 9, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 2.56 s: HF_HUB_OFFLINE=1 python repro.py 2>&1 | tail -3
- `rc=0` 2.48 s: HF_HUB_OFFLINE=1 python repro.py 2>&1 | tail -3
- `rc=0` 8.86 s: ruff check src/transformers/models/oneformer/ && ruff format --check src/transformers/models/oneformer/; python -m pytest -q tests/models/oneformer/test_image_processing_oneformer.py tests/models/oneformer/test_processor_oneformer.py 2>&1 | tail -5
- `rc=0` 14.19 s: python -m pytest -q tests/models/oneformer/test_image_processing_oneformer.py 2>&1 | grep -E "^E " | sort | uniq -c | head; git stash -q; python -m pytest -q tests/models/oneformer/test_image_processing_oneformer.py tests/models/oneformer/test_processor_oneformer.py 2>&1 | tail -1; git stash pop -q; git status --short
