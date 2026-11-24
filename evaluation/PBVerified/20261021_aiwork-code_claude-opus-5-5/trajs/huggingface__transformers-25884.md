# Instance: huggingface__transformers-25884
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: False

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
OSError: /home/datascience/huggingface does not appear to have a file named preprocessor_config.json. Checkout 'https://huggingface.co//home/datascience/huggingface/None' for available files.
### System Info

import transformers
transformers.__version__

'4.31.0'

### Who can help?

_No response_

### Information

- [ ] The official example scripts
- [ ] My own modified scripts

### Tasks

- [ ] An officially supported task in the `examples` folder (such as GLUE/SQuAD, ...)
- [ ] My own task or dataset (give details below)

### Reproduction
![image](https://github.com/huggingface/transformers/assets/25996703/6e26deb4-237b-473a-8874-164a4d134ea8)

```python
segmenter = pipeline(task="image-segmentation", model="facebook/detr-resnet-50-panoptic", revision="fc15262")
segmenter.save_pretrained("./huggingface")


from transformers import pipeline
task = 'image-segmentation'
model_dir="./huggingface"
model = pipeline(task, model = model_dir)

OSError: /home/datascience/huggingface does not appear to have a file named preprocessor_config.json. Checkout 'https://huggingface.co//home/datascience/huggingface/None' for available files.
```

### Expected behavior

no bug
````

## Operational trajectory

### Turn 1 — thinking

````text
I suspect the pipeline's save_pretrained method doesn't handle the image_processor attribute. I want to check how Pipeline.save_pretrained is implemented in base.py.
````

### Turn 1 — tool call call_0001 (rg)

````json
{
 "pattern": "def save_pretrained",
 "path": "src/transformers/pipelines/base.py",
 "context_after": 40
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "def save_pretrained",
 "search_path": "/testbed/src/transformers/pipelines/base.py",
 "matches": [
  {
   "path": "base.py",
   "line_number": 831,
   "line": "    def save_pretrained(self, save_directory: str, safe_serialization: bool = False):",
   "context_after": [
    "        \"\"\"",
    "        Save the pipeline's model and tokenizer.",
    "",
    "        Args:",
    "            save_directory (`str`):",
    "                A path to the directory where to saved. It will be created if it doesn't exist.",
    "            safe_serialization (`str`):",
    "                Whether to save the model using `safetensors` or the traditional way for PyTorch or Tensorflow",
    "        \"\"\"",
    "        if os.path.isfile(save_directory):",
    "            logger.error(f\"Provided path ({save_directory}) should be a directory, not a file\")",
    "            return",
    "        os.makedirs(save_directory, exist_ok=True)",
    "",
    "        if hasattr(self, \"_registered_impl\"):",
    "            # Add info to the config",
    "            pipeline_info = self._registered_impl.copy()",
    "            custom_pipelines = {}",
    "            for task, info in pipeline_info.items():",
    "                if info[\"impl\"] != self.__class__:"
   ]
  }
 ],
 "stats": {
  "files_searched": 1,
  "files_with_matches": 1,
  "matches_found": 1,
  "matches_returned": 1,
  "denied_skips": 0,
  "duration_ms": 4,
  "timing": {
   "walk_ms": 0,
   "search_ms": 4,
   "collect_ms": 0,
   "total_ms": 4
  }
 },
 "truncated": false
}
````

### Turn 2 — tool call call_0002 (read)

````json
{
 "file_path": "src/transformers/pipelines/base.py",
 "offset": 750,
 "limit": 130
}
````

Result:

````text
{
 "type": "file",
 "path": "src/transformers/pipelines/base.py",
 "full_read": false,
 "output": "src/transformers/pipelines/base.py\n\n750:     default_input_names = None\n751: \n752:     def __init__(\n753:         self,\n754:         model: Union[\"PreTrainedModel\", \"TFPreTrainedModel\"],\n755:         tokenizer: Optional[PreTrainedTokenizer] = None,\n756:         feature_extractor: Optional[PreTrainedFeatureExtractor] = None,\n757:         image_processor: Optional[BaseImageProcessor] = None,\n758:         modelcard: Optional[ModelCard] = None,\n759:         framework: Optional[str] = None,\n760:         task: str = \"\",\n761:         args_parser: ArgumentHandler = None,\n762:         device: Union[int, \"torch.device\"] = None,\n763:         torch_dtype: Optional[Union[str, \"torch.dtype\"]] = None,\n764:         binary_output: bool = False,\n765:         **kwargs,\n766:     ):\n767:         if framework is None:\n768:             framework, model = infer_framework_load_model(model, config=model.config)\n769: \n770:         self.task = task\n771:         self.model = model\n772:         self.tokenizer = tokenizer\n773:         self.feature_extractor = feature_extractor\n774:         self.image_processor = image_processor\n775:         self.modelcard = modelcard\n776:         self.framework = framework\n777: \n778:         # `accelerate` device map\n779:         hf_device_map = getattr(self.model, \"hf_device_map\", None)\n780: \n781:         if hf_device_map is not None and device is not None:\n782:             raise ValueError(\n783:                 \"The model has been loaded with `accelerate` and therefore cannot be moved to a specific device. Please \"\n784:                 \"discard the `device` argument when creating your pipeline object.\"\n785:             )\n786: \n787:         # We shouldn't call `model.to()` for models loaded with accelerate\n788:         if self.framework == \"pt\" and device is not None and not (isinstance(device, int) and device < 0):\n789:             self.model.to(device)\n790: \n791:         if device is None:\n792:             if hf_device_map is not None:\n793:                 # Take the first device used by `accelerate`.\n794:                 device = next(iter(hf_device_map.values()))\n795:             else:\n796:                 device = -1\n797: \n798:         if is_torch_available() and self.framework == \"pt\":\n799:             if isinstance(device, torch.device):\n800:                 self.device = device\n801:             elif isinstance(device, str):\n802:                 self.device = torch.device(device)\n803:             elif device < 0:\n804:                 self.device = torch.device(\"cpu\")\n805:             else:\n806:                 self.device = torch.device(f\"cuda:{device}\")\n807:         else:\n808:             self.device = device if device is not None else -1\n809:         self.torch_dtype = torch_dtype\n810:         self.binary_output = binary_output\n811: \n812:         # Update config and generation_config with task specific parameters\n813:         task_specific_params = self.model.config.task_specific_params\n814:         if task_specific_params is not None and task in task_specific_params:\n815:             self.model.config.update(task_specific_params.get(task))\n816:             if self.model.can_generate():\n817:                 self.model.generation_config.update(**task_specific_params.get(task))\n818: \n819:         self.call_count = 0\n820:         self._batch_size = kwargs.pop(\"batch_size\", None)\n821:         self._num_workers = kwargs.pop(\"num_workers\", None)\n822:         self._preprocess_params, self._forward_params, self._postprocess_params = self._sanitize_parameters(**kwargs)\n823: \n824:         if self.image_processor is None and self.feature_extractor is not None:\n825:             if isinstance(self.feature_extractor, BaseImageProcessor):\n826:                 # Backward compatible change, if users called\n827:                 # ImageSegmentationPipeline(.., feature_extractor=MyFeatureExtractor())\n828:                 # then we should keep working\n829:                 self.image_processor = self.feature_extractor\n830: \n831:     def save_pretrained(self, save_directory: str, safe_serialization: bool = False):\n832:         \"\"\"\n833:         Save the pipeline's model and tokenizer.\n834: \n835:         Args:\n836:             save_directory (`str`):\n837:                 A path to the directory where to saved. It will be created if it doesn't exist.\n838:             safe_serialization (`str`):\n839:                 Whether to save the model using `safetensors` or the traditional way for PyTorch or Tensorflow\n840:         \"\"\"\n841:         if os.path.isfile(save_directory):\n842:             logger.error(f\"Provided path ({save_directory}) should be a directory, not a file\")\n843:             return\n844:         os.makedirs(save_directory, exist_ok=True)\n845: \n846:         if hasattr(self, \"_registered_impl\"):\n847:             # Add info to the config\n848:             pipeline_info = self._registered_impl.copy()\n849:             custom_pipelines = {}\n850:             for task, info in pipeline_info.items():\n851:                 if info[\"impl\"] != self.__class__:\n852:                     continue\n853: \n854:                 info = info.copy()\n855:                 module_name = info[\"impl\"].__module__\n856:                 last_module = module_name.split(\".\")[-1]\n857:                 # Change classes into their names/full names\n858:                 info[\"impl\"] = f\"{last_module}.{info['impl'].__name__}\"\n859:                 info[\"pt\"] = tuple(c.__name__ for c in info[\"pt\"])\n860:                 info[\"tf\"] = tuple(c.__name__ for c in info[\"tf\"])\n861: \n862:                 custom_pipelines[task] = info\n863:             self.model.config.custom_pipelines = custom_pipelines\n864:             # Save the pipeline custom code\n865:             custom_object_save(self, save_directory)\n866: \n867:         self.model.save_pretrained(save_directory, safe_serialization=safe_serialization)\n868: \n869:         if self.tokenizer is not None:\n870:             self.tokenizer.save_pretrained(save_directory)\n871: \n872:         if self.feature_extractor is not None:\n873:             self.feature_extractor.save_pretrained(save_directory)\n874: \n875:         if self.modelcard is not None:\n876:             self.modelcard.save_pretrained(save_directory)\n877: \n878:     def transform(self, X):\n879:         \"\"\"\n\n(Returned 130 lines starting at 750; total 1244; output truncated — call read again with a higher offset or limit to continue)",
 "offset": 750,
 "limit": 130,
 "lines_returned": 130,
 "total_lines": 1244,
 "observed_lines": 1244,
 "total_lines_lower_bound": 1244,
 "total_lines_exact": true,
 "truncated": true,
 "next_offset": 880,
 "window_bytes_limit": 102400,
 "size_bytes": 51938
}
````

### Turn 3 — tool call call_0003 (edit)

````json
{
 "file_path": "src/transformers/pipelines/base.py",
 "old_string": "            self.feature_extractor.save_pretrained(save_directory)\n\n        if self.modelcard",
 "new_string": "            self.feature_extractor.save_pretrained(save_directory)\n\n        if self.image_processor is not None:\n            self.image_processor.save_pretrained(save_directory)\n\n        if self.modelcard"
}
````

Result:

````text
{
 "path": "src/transformers/pipelines/base.py",
 "edited": true,
 "replacements": 1,
 "total_file_lines": 1247,
 "total_file_size_bytes": 52049,
 "diff": "+         if self.image_processor is not None:\n+             self.image_processor.save_pretrained(save_directory)\n+ ",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "edit",
    "paths": [
     "src/transformers/pipelines/base.py"
    ]
   }
  ]
 },
 "file_change": {
  "kind": "diff",
  "operation": "update",
  "path": "src/transformers/pipelines/base.py",
  "patch": "+         if self.image_processor is not None:\n+             self.image_processor.save_pretrained(save_directory)\n+ ",
  "additions": 3,
  "deletions": 0,
  "truncated": false,
  "omitted_lines": 0
 }
}
````

### Turn 4 — thinking

````text
Since network access is likely unavailable, I'm considering a minimal offline smoke test instead—building a tiny randomly initialized ViT model with a ViTImageProcessor, running it through an image-classification pipeline, then saving and reloading it to verify everything works.
````

### Turn 5 — assistant text

Now a quick smoke test with a locally built tiny model (no network needed):

### Turn 5 — tool call call_0004 (exec)

````json
{
 "command": "cd /tmp && timeout 300 python -c \"\nimport tempfile, os\nfrom transformers import ViTConfig, ViTForImageClassification, ViTImageProcessor, pipeline\nm = ViTForImageClassification(ViTConfig(image_size=32, patch_size=8, hidden_size=32, num_hidden_layers=1, num_attention_heads=2, intermediate_size=37))\np = pipeline('image-classification', model=m, image_processor=ViTImageProcessor(size={'height':32,'width':32}))\nd = tempfile.mkdtemp()\np.save_pretrained(d)\nprint(sorted(os.listdir(d)))\np2 = pipeline('image-classification', model=d)\nprint(type(p2.image_processor).__name__)\n\" 2>&1 | tail -5"
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
 "stdout": "  torch.utils._pytree._register_pytree_node(\n/testbed/src/transformers/modeling_utils.py:488: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.\n  return torch.load(checkpoint_file, map_location=map_location)\n['config.json', 'preprocessor_config.json', 'pytorch_model.bin']\nViTImageProcessor\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 10556,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/tmp"
  ],
  "command_sha256": [
   "7634f4955439c68fcf354448e648bd8be5dda708a70050e40f1082024795efe7"
  ]
 }
}
````

### Turn 6 — assistant text

I fixed the bug: `Pipeline.save_pretrained` now saves the pipeline's image processor, so a saved image pipeline can be loaded again from its directory.

**Cause:** in `src/transformers/pipelines/base.py`, `save_pretrained` saved the model, tokenizer, feature extractor and model card, but not `self.image_processor`. Image pipelines like `image-segmentation` use only an image processor, so `preprocessor_config.json` was never written and loading the folder failed with the error in the report.

**Fix:** I added this to `save_pretrained`:
```python
if self.image_processor is not None:
    self.image_processor.save_pretrained(save_directory)
```

**Check:** I couldn't run the exact example from the report, so I used a tiny ViT image-classification pipeline built locally. After `save_pretrained`, the folder contained `config.json`, `preprocessor_config.json` and `pytorch_model.bin`. Loading it with `pipeline('image-classification', model=dir)` worked and returned a `ViTImageProcessor`. I didn't run the repo's test suite.

### Turn 7 — assistant text

I fixed it: `Pipeline.save_pretrained` now saves the image processor, so a saved image pipeline can be loaded back from its directory.

The cause was in `src/transformers/pipelines/base.py`. `save_pretrained` saved the model, tokenizer, feature extractor and model card, but never the image processor. Newer image pipelines like image segmentation keep their preprocessor in `self.image_processor`, so `preprocessor_config.json` was never written. Reloading from the directory then failed with the error in the report.

The fix adds these lines next to the existing feature-extractor save:

```python
if self.image_processor is not None:
    self.image_processor.save_pretrained(save_directory)
```

I checked it with a small, randomly initialized ViT image-classification pipeline built offline. After `save_pretrained`, the directory held `config.json`, `preprocessor_config.json` and `pytorch_model.bin`. Loading it with `pipeline('image-classification', model=dir)` worked and picked up the `ViTImageProcessor`.

I didn't re-run the exact `facebook/detr-resnet-50-panoptic` example from the report, because that needs to download the model. The repo's existing test suite wasn't run either.

## Final answer

I fixed it: `Pipeline.save_pretrained` now saves the image processor, so a saved image pipeline can be loaded back from its directory.

The cause was in `src/transformers/pipelines/base.py`. `save_pretrained` saved the model, tokenizer, feature extractor and model card, but never the image processor. Newer image pipelines like image segmentation keep their preprocessor in `self.image_processor`, so `preprocessor_config.json` was never written. Reloading from the directory then failed with the error in the report.

The fix adds these lines next to the existing feature-extractor save:

```python
if self.image_processor is not None:
    self.image_processor.save_pretrained(save_directory)
```

I checked it with a small, randomly initialized ViT image-classification pipeline built offline. After `save_pretrained`, the directory held `config.json`, `preprocessor_config.json` and `pytorch_model.bin`. Loading it with `pipeline('image-classification', model=dir)` worked and picked up the `ViTImageProcessor`.

I didn't re-run the exact `facebook/detr-resnet-50-panoptic` example from the report, because that needs to download the model. The repo's existing test suite wasn't run either.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 90843 | 1693 | 85218 | 5609 | 92536 |
