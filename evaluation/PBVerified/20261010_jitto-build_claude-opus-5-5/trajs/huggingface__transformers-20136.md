# Instance: huggingface__transformers-20136

- Final resolved (evaluator, logs/huggingface__transformers-20136_result.json): True
- Run state: DONE
- One attempt. Duration 280.8 s, turns 22, actor cost $1.1823176, container commands 6
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/huggingface__transformers-20136/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-20136/repo. Consider the following issue description:

<issue_description>
Add image-guided object detection support to OWL-ViT
Hi,

The [OWL-ViT](https://huggingface.co/docs/transformers/model_doc/owlvit) model is an open-vocabulary model that can be used for both zero-shot text-guided (supported) and one-shot image-guided (not supported) object detection. 

It'd be great to add support for one-shot object detection to `OwlViTForObjectDetection` such that users can query images with an image of the target object instead of using text queries - e.g. using an image of a butterfly to search for all butterfly instances in the target image. See an example below.

<img width="989" alt="Screenshot 2022-08-24 at 17 16 28" src="https://user-images.githubusercontent.com/8944735/186441941-7278676e-aecb-4c7d-b1d5-df4fb444becb.png">

To do this, we would just need to compute and use the `OwlViTModel` (alias to CLIP) embeddings of the query images instead of the text query embeddings within `OwlViTForObjectDetection.forward()`, which would take the target image + either text queries or  image queries as input. Similarly, `OwlViTProcessor` would be updated to preprocess sets of (image, text) and (image, query_image).

@sgugger @NielsRogge @amyeroberts @LysandreJik what do you think about this? Would this be something we would like to support?

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-20136/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-20136/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-20136/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-20136/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/huggingface__transformers-20136/repo; ls src/transformers/models/owlvit/; wc -l src/transformers/models/owlvit/*.py; git log --oneline -2; grep -n "image_guided\|query_image\|query_pixel" -r tests/models/owlvit src/transformers/models/owlvit docs/source/en/model_doc/owlvit.mdx src/transformers/pipelines | head -60
```

tool result:

```
__init__.py
configuration_owlvit.py
convert_owlvit_original_flax_to_hf.py
feature_extraction_owlvit.py
modeling_owlvit.py
processing_owlvit.py
     102 src/transformers/models/owlvit/__init__.py
     395 src/transformers/models/owlvit/configuration_owlvit.py
     407 src/transformers/models/owlvit/convert_owlvit_original_flax_to_hf.py
     221 src/transformers/models/owlvit/feature_extraction_owlvit.py
    1403 src/transformers/models/owlvit/modeling_owlvit.py
     167 src/transformers/models/owlvit/processing_owlvit.py
    2695 total
fda125638 Downgrade log warning -> info (#20202)
36b063ed4 Update README.md (#20188)
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; ls tests/models/owlvit; grep -n "def test\|query\|image_guided\|post_process" tests/models/owlvit/*.py | head -80
```

tool result:

```
__init__.py
test_feature_extraction_owlvit.py
test_modeling_owlvit.py
test_processor_owlvit.py
tests/models/owlvit/test_feature_extraction_owlvit.py:95:    def test_feat_extract_properties(self):
tests/models/owlvit/test_feature_extraction_owlvit.py:106:    def test_call_pil(self):
tests/models/owlvit/test_feature_extraction_owlvit.py:139:    def test_call_numpy(self):
tests/models/owlvit/test_feature_extraction_owlvit.py:171:    def test_call_pytorch(self):
tests/models/owlvit/test_modeling_owlvit.py:151:    def test_config(self):
tests/models/owlvit/test_modeling_owlvit.py:155:    def test_inputs_embeds(self):
tests/models/owlvit/test_modeling_owlvit.py:158:    def test_model_common_attributes(self):
tests/models/owlvit/test_modeling_owlvit.py:167:    def test_forward_signature(self):
tests/models/owlvit/test_modeling_owlvit.py:179:    def test_model(self):
tests/models/owlvit/test_modeling_owlvit.py:184:    def test_training(self):
tests/models/owlvit/test_modeling_owlvit.py:188:    def test_training_gradient_checkpointing(self):
tests/models/owlvit/test_modeling_owlvit.py:192:    def test_save_load_fast_init_from_base(self):
tests/models/owlvit/test_modeling_owlvit.py:196:    def test_save_load_fast_init_to_base(self):
tests/models/owlvit/test_modeling_owlvit.py:200:    def test_model_from_pretrained(self):
tests/models/owlvit/test_modeling_owlvit.py:307:    def test_config(self):
tests/models/owlvit/test_modeling_owlvit.py:310:    def test_model(self):
tests/models/owlvit/test_modeling_owlvit.py:315:    def test_training(self):
tests/models/owlvit/test_modeling_owlvit.py:319:    def test_training_gradient_checkpointing(self):
tests/models/owlvit/test_modeling_owlvit.py:323:    def test_inputs_embeds(self):
tests/models/owlvit/test_modeling_owlvit.py:327:    def test_save_load_fast_init_from_base(self):
tests/models/owlvit/test_modeling_owlvit.py:331:    def test_save_load_fast_init_to_base(self):
tests/models/owlvit/test_modeling_owlvit.py:335:    def test_model_from_pretrained(self):
tests/models/owlvit/test_modeling_owlvit.py:410:    def test_model(self):
tests/models/owlvit/test_modeling_owlvit.py:415:    def test_hidden_states_output(self):
tests/models/owlvit/test_modeling_owlvit.py:419:    def test_inputs_embeds(self):
tests/models/owlvit/test_modeling_owlvit.py:423:    def test_retain_grad_hidden_states_attentions(self):
tests/models/owlvit/test_modeling_owlvit.py:427:    def test_model_common_attributes(self):
tests/models/owlvit/test_modeling_owlvit.py:431:    def test_initialization(self):
tests/models/owlvit/test_modeling_owlvit.py:501:    def test_load_vision_text_config(self):
tests/models/owlvit/test_modeling_owlvit.py:517:    def test_model_from_pretrained(self):
tests/models/owlvit/test_modeling_owlvit.py:593:    def test_model(self):
tests/models/owlvit/test_modeling_owlvit.py:598:    def test_hidden_states_output(self):
tests/models/owlvit/test_modeling_owlvit.py:602:    def test_inputs_embeds(self):
tests/models/owlvit/test_modeling_owlvit.py:606:    def test_retain_grad_hidden_states_attentions(self):
tests/models/owlvit/test_modeling_owlvit.py:610:    def test_model_common_attributes(self):
tests/models/owlvit/test_modeling_owlvit.py:614:    def test_initialization(self):
tests/models/owlvit/test_modeling_owlvit.py:618:    def test_forward_signature(self):
tests/models/owlvit/test_modeling_owlvit.py:622:    def test_save_load_fast_init_from_base(self):
tests/models/owlvit/test_modeling_owlvit.py:626:    def test_training(self):
tests/models/owlvit/test_modeling_owlvit.py:630:    def test_training_gradient_checkpointing(self):
tests/models/owlvit/test_modeling_owlvit.py:680:    def test_model_outputs_equivalence(self):
tests/models/owlvit/test_modeling_owlvit.py:727:    def test_model_from_pretrained(self):
tests/models/owlvit/test_modeling_owlvit.py:744:    def test_inference(self):
tests/models/owlvit/test_modeling_owlvit.py:775:    def test_inference_object_detection(self):
tests/models/owlvit/test_processor_owlvit.py:91:    def test_save_load_pretrained_default(self):
tests/models/owlvit/test_processor_owlvit.py:115:    def test_save_load_pretrained_additional_features(self):
tests/models/owlvit/test_processor_owlvit.py:132:    def test_feature_extractor(self):
tests/models/owlvit/test_processor_owlvit.py:146:    def test_tokenizer(self):
tests/models/owlvit/test_processor_owlvit.py:161:    def test_processor(self):
tests/models/owlvit/test_processor_owlvit.py:178:    def test_processor_with_text_list(self):
tests/models/owlvit/test_processor_owlvit.py:193:    def test_processor_with_nested_text_list(self):
tests/models/owlvit/test_processor_owlvit.py:211:    def test_processor_case(self):
tests/models/owlvit/test_processor_owlvit.py:230:    def test_tokenizer_decode(self):
tests/models/owlvit/test_processor_owlvit.py:243:    def test_model_input_names(self):
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; sed -n 1,140p src/transformers/models/owlvit/modeling_owlvit.py; grep -n "^class \|def \|^OWLVIT" src/transformers/models/owlvit/modeling_owlvit.py
```

tool result:

```
# coding=utf-8
# Copyright 2022 Google AI and The HuggingFace Team. All rights reserved.
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
""" PyTorch OWL-ViT model."""


import warnings
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple, Union

import numpy as np
import torch
import torch.utils.checkpoint
from torch import nn

from ...activations import ACT2FN
from ...modeling_outputs import BaseModelOutput, BaseModelOutputWithPooling
from ...modeling_utils import PreTrainedModel
from ...utils import (
    ModelOutput,
    add_start_docstrings,
    add_start_docstrings_to_model_forward,
    logging,
    replace_return_docstrings,
)
from .configuration_owlvit import OwlViTConfig, OwlViTTextConfig, OwlViTVisionConfig


logger = logging.get_logger(__name__)

_CHECKPOINT_FOR_DOC = "google/owlvit-base-patch32"

# See all OwlViT models at https://huggingface.co/models?filter=owlvit
OWLVIT_PRETRAINED_MODEL_ARCHIVE_LIST = [
    "google/owlvit-base-patch32",
    "google/owlvit-base-patch16",
    "google/owlvit-large-patch14",
]


# Copied from transformers.models.bart.modeling_bart._expand_mask
def _expand_mask(mask: torch.Tensor, dtype: torch.dtype, tgt_len: Optional[int] = None):
    """
    Expands attention_mask from `[bsz, seq_len]` to `[bsz, 1, tgt_seq_len, src_seq_len]`.
    """
    bsz, src_len = mask.size()
    tgt_len = tgt_len if tgt_len is not None else src_len

    expanded_mask = mask[:, None, None, :].expand(bsz, 1, tgt_len, src_len).to(dtype)

    inverted_mask = 1.0 - expanded_mask

    return inverted_mask.masked_fill(inverted_mask.to(torch.bool), torch.finfo(dtype).min)


# Copied from transformers.models.clip.modeling_clip.contrastive_loss with clip->owlvit
def contrastive_loss(logits: torch.Tensor) -> torch.Tensor:
    return nn.functional.cross_entropy(logits, torch.arange(len(logits), device=logits.device))


# Copied from transformers.models.clip.modeling_clip.clip_loss with clip->owlvit
def owlvit_loss(similarity: torch.Tensor) -> torch.Tensor:
    caption_loss = contrastive_loss(similarity)
    image_loss = contrastive_loss(similarity.t())
    return (caption_loss + image_loss) / 2.0


@dataclass
class OwlViTOutput(ModelOutput):
    """
    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `return_loss` is `True`):
            Contrastive loss for image-text similarity.
        logits_per_image (`torch.FloatTensor` of shape `(image_batch_size, text_batch_size)`):
            The scaled dot product scores between `image_embeds` and `text_embeds`. This represents the image-text
            similarity scores.
        logits_per_text (`torch.FloatTensor` of shape `(text_batch_size, image_batch_size)`):
            The scaled dot product scores between `text_embeds` and `image_embeds`. This represents the text-image
            similarity scores.
        text_embeds (`torch.FloatTensor` of shape `(batch_size * num_max_text_queries, output_dim`):
            The text embeddings obtained by applying the projection layer to the pooled output of [`OwlViTTextModel`].
        image_embeds (`torch.FloatTensor` of shape `(batch_size, output_dim`):
            The image embeddings obtained by applying the projection layer to the pooled output of
            [`OwlViTVisionModel`].
        text_model_output (Tuple[`BaseModelOutputWithPooling`]):
            The output of the [`OwlViTTextModel`].
        vision_model_output (`BaseModelOutputWithPooling`):
            The output of the [`OwlViTVisionModel`].
    """

    loss: Optional[torch.FloatTensor] = None
    logits_per_image: torch.FloatTensor = None
    logits_per_text: torch.FloatTensor = None
    text_embeds: torch.FloatTensor = None
    image_embeds: torch.FloatTensor = None
    text_model_output: BaseModelOutputWithPooling = None
    vision_model_output: BaseModelOutputWithPooling = None

    def to_tuple(self) -> Tuple[Any]:
        return tuple(
            self[k] if k not in ["text_model_output", "vision_model_output"] else getattr(self, k).to_tuple()
            for k in self.keys()
        )


@dataclass
class OwlViTObjectDetectionOutput(ModelOutput):
    """
    Output type of [`OwlViTForObjectDetection`].

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` are provided)):
            Total loss as a linear combination of a negative log-likehood (cross-entropy) for class prediction and a
            bounding box loss. The latter is defined as a linear combination of the L1 loss and the generalized
            scale-invariant IoU loss.
        loss_dict (`Dict`, *optional*):
            A dictionary containing the individual losses. Useful for logging.
        logits (`torch.FloatTensor` of shape `(batch_size, num_patches, num_queries)`):
            Classification logits (including no-object) for all queries.
        pred_boxes (`torch.FloatTensor` of shape `(batch_size, num_patches, 4)`):
            Normalized boxes coordinates for all queries, represented as (center_x, center_y, width, height). These
            values are normalized in [0, 1], relative to the size of each individual image in the batch (disregarding
            possible padding). You can use [`~OwlViTFeatureExtractor.post_process`] to retrieve the unnormalized
            bounding boxes.
        text_embeds (`torch.FloatTensor` of shape `(batch_size, num_max_text_queries, output_dim`):
            The text embeddings obtained by applying the projection layer
[... 3584 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; sed -n 520,600p src/transformers/models/owlvit/modeling_owlvit.py; sed -n 1020,1403p src/transformers/models/owlvit/modeling_owlvit.py
```

tool result:

````
        return_dict (`bool`, *optional*):
            Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
"""

OWLVIT_OBJECT_DETECTION_INPUTS_DOCSTRING = r"""
    Args:
        pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`):
            Pixel values.
        input_ids (`torch.LongTensor` of shape `(batch_size * num_max_text_queries, sequence_length)`):
            Indices of input sequence tokens in the vocabulary. Indices can be obtained using [`CLIPTokenizer`]. See
            [`PreTrainedTokenizer.encode`] and [`PreTrainedTokenizer.__call__`] for details. [What are input
            IDs?](../glossary#input-ids)
        attention_mask (`torch.Tensor` of shape `(batch_size, num_max_text_queries, sequence_length)`, *optional*):
            Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:
            - 1 for tokens that are **not masked**,
            - 0 for tokens that are **masked**.
            [What are attention masks?](../glossary#attention-mask)
"""


class OwlViTEncoder(nn.Module):
    """
    Transformer encoder consisting of `config.num_hidden_layers` self attention layers. Each layer is a
    [`OwlViTEncoderLayer`].

    Args:
        config: OwlViTConfig
    """

    def __init__(self, config: OwlViTConfig):
        super().__init__()
        self.layers = nn.ModuleList([OwlViTEncoderLayer(config) for _ in range(config.num_hidden_layers)])
        self.gradient_checkpointing = False

    def forward(
        self,
        inputs_embeds,
        attention_mask: Optional[torch.Tensor] = None,
        causal_attention_mask: Optional[torch.Tensor] = None,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
        return_dict: Optional[bool] = None,
    ) -> Union[Tuple, BaseModelOutput]:
        r"""
        Args:
            inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`).
            attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:
                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.
                [What are attention masks?](../glossary#attention-mask)
            causal_attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Causal mask for the text model. Mask values selected in `[0, 1]`:
                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.
                [What are attention masks?](../glossary#attention-mask)
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """
        output_attentions = output_attentions if output_attentions is not None else self.config.output_attentions
        output_hidden_states = (
            output_hidden_states if output_hidden_states is not None else self.config.output_hidden_states
        )
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        encoder_states = () if output_hidden_states else None
        all_attentions = () if output_attentions else None

        hidden_states = inputs_embeds
        for encoder_layer in self.layers:
            if output_hidden_states:
                encoder_states = encoder_states + (hidden_states,)
            if self.gradient_checkpointing and self.training:

                def create_custom_forward(module):
        >>> from transformers import OwlViTProcessor, OwlViTModel

        >>> model = OwlViTModel.from_pretrained("google/owlvit-base-patch32")
        >>> processor = OwlViTProcessor.from_pretrained("google/owlvit-base-patch32")
        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)
        >>> inputs = processor(text=[["a photo of a cat", "a photo of a dog"]], images=image, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
        >>> probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities
        ```"""
        # Use OWL-ViT model's config for some fields (if specified) instead of those of vision & text components.
        output_attentions = output_attentions if output_attentions is not None else self.config.output_attentions
        output_hidden_states = (
            output_hidden_states if output_hidden_states is not None else self.config.output_hidden_states
        )
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        vision_outputs = self.vision_model(
            pixel_values=pixel_values,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )

        # Get embeddings for all text queries in all batch samples
        text_outputs = self.text_model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )

        text_embeds = text_outputs[1]
        text_embeds = self.text_projection(text
[... 14200 more characters not shown]
````

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; sed -n 520,800p tests/models/owlvit/test_modeling_owlvit.py
```

tool result:

```
            self.assertIsNotNone(model)


class OwlViTForObjectDetectionTester:
    def __init__(self, parent, is_training=True):
        self.parent = parent
        self.text_model_tester = OwlViTTextModelTester(parent)
        self.vision_model_tester = OwlViTVisionModelTester(parent)
        self.is_training = is_training
        self.text_config = self.text_model_tester.get_config().to_dict()
        self.vision_config = self.vision_model_tester.get_config().to_dict()

    def prepare_config_and_inputs(self):
        text_config, input_ids, attention_mask = self.text_model_tester.prepare_config_and_inputs()
        vision_config, pixel_values = self.vision_model_tester.prepare_config_and_inputs()
        config = self.get_config()
        return config, pixel_values, input_ids, attention_mask

    def get_config(self):
        return OwlViTConfig.from_text_vision_configs(self.text_config, self.vision_config, projection_dim=64)

    def create_and_check_model(self, config, pixel_values, input_ids, attention_mask):
        model = OwlViTForObjectDetection(config).to(torch_device).eval()
        with torch.no_grad():
            result = model(
                pixel_values=pixel_values,
                input_ids=input_ids,
                attention_mask=attention_mask,
                return_dict=True,
            )

        pred_boxes_size = (
            self.vision_model_tester.batch_size,
            (self.vision_model_tester.image_size // self.vision_model_tester.patch_size) ** 2,
            4,
        )
        pred_logits_size = (
            self.vision_model_tester.batch_size,
            (self.vision_model_tester.image_size // self.vision_model_tester.patch_size) ** 2,
            4,
        )
        pred_class_embeds_size = (
            self.vision_model_tester.batch_size,
            (self.vision_model_tester.image_size // self.vision_model_tester.patch_size) ** 2,
            self.text_model_tester.hidden_size,
        )
        self.parent.assertEqual(result.pred_boxes.shape, pred_boxes_size)
        self.parent.assertEqual(result.logits.shape, pred_logits_size)
        self.parent.assertEqual(result.class_embeds.shape, pred_class_embeds_size)

    def prepare_config_and_inputs_for_common(self):
        config_and_inputs = self.prepare_config_and_inputs()
        config, pixel_values, input_ids, attention_mask = config_and_inputs
        inputs_dict = {
            "pixel_values": pixel_values,
            "input_ids": input_ids,
            "attention_mask": attention_mask,
        }
        return config, inputs_dict


@require_torch
class OwlViTForObjectDetectionTest(ModelTesterMixin, unittest.TestCase):
    all_model_classes = (OwlViTForObjectDetection,) if is_torch_available() else ()
    fx_compatible = False
    test_head_masking = False
    test_pruning = False
    test_resize_embeddings = False
    test_attention_outputs = False

    def setUp(self):
        self.model_tester = OwlViTForObjectDetectionTester(self)

    def test_model(self):
        config_and_inputs = self.model_tester.prepare_config_and_inputs()
        self.model_tester.create_and_check_model(*config_and_inputs)

    @unittest.skip(reason="Hidden_states is tested in individual model tests")
    def test_hidden_states_output(self):
        pass

    @unittest.skip(reason="Inputs_embeds is tested in individual model tests")
    def test_inputs_embeds(self):
        pass

    @unittest.skip(reason="Retain_grad is tested in individual model tests")
    def test_retain_grad_hidden_states_attentions(self):
        pass

    @unittest.skip(reason="OwlViTModel does not have input/output embeddings")
    def test_model_common_attributes(self):
        pass

    @unittest.skip(reason="Test_initialization is tested in individual model tests")
    def test_initialization(self):
        pass

    @unittest.skip(reason="Test_forward_signature is tested in individual model tests")
    def test_forward_signature(self):
        pass

    @unittest.skip(reason="Test_save_load_fast_init_from_base is tested in individual model tests")
    def test_save_load_fast_init_from_base(self):
        pass

    @unittest.skip(reason="OWL-ViT does not support training yet")
    def test_training(self):
        pass

    @unittest.skip(reason="OWL-ViT does not support training yet")
    def test_training_gradient_checkpointing(self):
        pass

    def _create_and_check_torchscript(self, config, inputs_dict):
        if not self.test_torchscript:
            return

        configs_no_init = _config_zero_init(config)  # To be sure we have no Nan
        configs_no_init.torchscript = True
        configs_no_init.return_dict = False
        for model_class in self.all_model_classes:
            model = model_class(config=configs_no_init).to(torch_device)
            model.eval()

            try:
                input_ids = inputs_dict["input_ids"]
                pixel_values = inputs_dict["pixel_values"]  # OWLVIT needs pixel_values
                traced_model = torch.jit.trace(model, (input_ids, pixel_values))
            except RuntimeError:
                self.fail("Couldn't trace module.")

            with tempfile.TemporaryDirectory() as tmp_dir_name:
                pt_file_name = os.path.join(tmp_dir_name, "traced_model.pt")

                try:
                    torch.jit.save(traced_model, pt_file_name)
                except Exception:
                    self.fail("Couldn't save module.")

                try:
                    loaded_model = torch.jit.load(pt_file_name)
                except Exception:
                    self.fail("Couldn't load module.")

            loaded_model = loaded_model.to(torch_device)
            loaded_model.eval()

            model_state_dict = model.state_dict()
            loaded_model_state_dict = loaded_model.state_dict()

            self.assertEqual(set(model_state_dict.keys()), set(loaded_model_state_dict.keys()))

            models_equal = True
            fo
[... 5383 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; sed -n 15,110p src/transformers/models/owlvit/feature_extraction_owlvit.py; sed -n 15,167p src/transformers/models/owlvit/processing_owlvit.py
```

tool result:

```
"""Feature extractor class for OwlViT."""

from typing import List, Optional, Union

import numpy as np
from PIL import Image

from transformers.image_utils import PILImageResampling

from ...feature_extraction_utils import BatchFeature, FeatureExtractionMixin
from ...image_utils import ImageFeatureExtractionMixin, is_torch_tensor
from ...utils import TensorType, is_torch_available, logging


if is_torch_available():
    import torch

logger = logging.get_logger(__name__)


def center_to_corners_format(x):
    """
    Converts a PyTorch tensor of bounding boxes of center format (center_x, center_y, width, height) to corners format
    (left, top, right, bottom).
    """
    x_center, y_center, width, height = x.unbind(-1)
    boxes = [(x_center - 0.5 * width), (y_center - 0.5 * height), (x_center + 0.5 * width), (y_center + 0.5 * height)]
    return torch.stack(boxes, dim=-1)


class OwlViTFeatureExtractor(FeatureExtractionMixin, ImageFeatureExtractionMixin):
    r"""
    Constructs an OWL-ViT feature extractor.

    This feature extractor inherits from [`FeatureExtractionMixin`] which contains most of the main methods. Users
    should refer to this superclass for more information regarding those methods.

    Args:
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the shorter edge of the input to a certain `size`.
        size (`int` or `Tuple[int, int]`, *optional*, defaults to (768, 768)):
            The size to use for resizing the image. Only has an effect if `do_resize` is set to `True`. If `size` is a
            sequence like (h, w), output size will be matched to this. If `size` is an int, then image will be resized
            to (size, size).
        resample (`int`, *optional*, defaults to `PILImageResampling.BICUBIC`):
            An optional resampling filter. This can be one of `PILImageResampling.NEAREST`, `PILImageResampling.BOX`,
            `PILImageResampling.BILINEAR`, `PILImageResampling.HAMMING`, `PILImageResampling.BICUBIC` or
            `PILImageResampling.LANCZOS`. Only has an effect if `do_resize` is set to `True`.
        do_center_crop (`bool`, *optional*, defaults to `False`):
            Whether to crop the input at the center. If the input size is smaller than `crop_size` along any edge, the
            image is padded with 0's and then center cropped.
        crop_size (`int`, *optional*, defaults to 768):
        do_normalize (`bool`, *optional*, defaults to `True`):
            Whether or not to normalize the input with `image_mean` and `image_std`. Desired output size when applying
            center-cropping. Only has an effect if `do_center_crop` is set to `True`.
        image_mean (`List[int]`, *optional*, defaults to `[0.48145466, 0.4578275, 0.40821073]`):
            The sequence of means for each channel, to be used when normalizing images.
        image_std (`List[int]`, *optional*, defaults to `[0.26862954, 0.26130258, 0.27577711]`):
            The sequence of standard deviations for each channel, to be used when normalizing images.
    """

    model_input_names = ["pixel_values"]

    def __init__(
        self,
        do_resize=True,
        size=(768, 768),
        resample=PILImageResampling.BICUBIC,
        crop_size=768,
        do_center_crop=False,
        do_normalize=True,
        image_mean=None,
        image_std=None,
        **kwargs
    ):
        # Early versions of the OWL-ViT config on the hub had "rescale" as a flag. This clashes with the
        # vision feature extractor method `rescale` as it would be set as an attribute during the super().__init__
        # call. This is for backwards compatibility.
        if "rescale" in kwargs:
            rescale_val = kwargs.pop("rescale")
            kwargs["do_rescale"] = rescale_val

        super().__init__(**kwargs)
        self.size = size
        self.resample = resample
        self.crop_size = crop_size
        self.do_resize = do_resize
        self.do_center_crop = do_center_crop
        self.do_normalize = do_normalize
        self.image_mean = image_mean if image_mean is not None else [0.48145466, 0.4578275, 0.40821073]
        self.image_std = image_std if image_std is not None else [0.26862954, 0.26130258, 0.27577711]

    def post_process(self, outputs, target_sizes):
        """
        Converts the output of [`OwlViTForObjectDetection`] into the format expected by the COCO api.

"""
Image/Text processor class for OWL-ViT
"""
from typing import List

import numpy as np

from transformers import is_flax_available, is_tf_available, is_torch_available

from ...processing_utils import ProcessorMixin
from ...tokenization_utils_base import BatchEncoding


class OwlViTProcessor(ProcessorMixin):
    r"""
    Constructs an OWL-ViT processor which wraps [`OwlViTFeatureExtractor`] and [`CLIPTokenizer`]/[`CLIPTokenizerFast`]
    into a single processor that interits both the feature extractor and tokenizer functionalities. See the
    [`~OwlViTProcessor.__call__`] and [`~OwlViTProcessor.decode`] for more information.

    Args:
        feature_extractor ([`OwlViTFeatureExtractor`]):
            The feature extractor is a required input.
        tokenizer ([`CLIPTokenizer`, `CLIPTokenizerFast`]):
            The tokenizer is a required input.
    """
    feature_extractor_class = "OwlViTFeatureExtractor"
    tokenizer_class = ("CLIPTokenizer", "CLIPTokenizerFast")

    def __init__(self, feature_extractor, tokenizer):
        super().__init__(feature_extractor, tokenizer)

    def __call__(self, text=None, images=None, padding="max_length", return_tensors="np", **kwargs):
        """
        Main method to prepare for the model one or several text(s) and image(s). This method forwards the `text` and
        `kwargs` arguments to CLIPTokenizerFast's [`~CLIPTokenizerFast.__call__`] if `text` is not `None` to encode:
        the text. To prepare the image(s), this method forwards the `images` and `kwrags` arguments to
        CLIPFeatur
[... 6200 more characters not shown]
```

**thinking:**

```
Confirmed the OWL-ViT processor doesn't support `query_images` and the model lacks an image-query path. I'll verify this further, then add support across the processor, model, and feature extractor's post-processing.


```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; ../bin/envrun 'python -c "
from transformers import OwlViTForObjectDetection
print(hasattr(OwlViTForObjectDetection, \"image_guided_detection\"))
import inspect; from transformers import OwlViTProcessor; print(inspect.signature(OwlViTProcessor.__call__))
"' 2>&1 | tail -3
```

tool result:

```
False
(self, text=None, images=None, padding='max_length', return_tensors='np', **kwargs)
```

**assistant:** Confirmed. Now the processor:

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; python3 - <<'EOF'
p='src/transformers/models/owlvit/processing_owlvit.py'
s=open(p).read()
s=s.replace('''    def __call__(self, text=None, images=None, padding="max_length", return_tensors="np", **kwargs):
        """
        Main method to prepare for the model one or several text(s) and image(s). This method forwards the `text` and''','''    def __call__(self, text=None, images=None, query_images=None, padding="max_length", return_tensors="np", **kwargs):
        """
        Main method to prepare for the model one or several text(s), query image(s) and image(s). This method forwards
        the `text` and''')
s=s.replace('''                number of channels, H and W are image height and width.
            return_tensors''','''                number of channels, H and W are image height and width.
            query_images (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `List[PIL.Image.Image]`, `List[np.ndarray]`,
            `List[torch.Tensor]`):
                The query image or batch of query images to be prepared for image-guided object detection. Each query
                image is used to search for similar objects in the corresponding target image (`images`). Each image
                can be a PIL image, NumPy array or PyTorch tensor.
            return_tensors''')
s=s.replace('''            - **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.
        """

        if text is None and images is None:
            raise ValueError("You have to specify at least one text or image. Both cannot be none.")
''','''            - **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.
            - **query_pixel_values** -- Pixel values of the query images to be fed to a model. Returned when
              `query_images` is not `None`.
        """

        if text is None and query_images is None and images is None:
            raise ValueError(
                "You have to specify at least one text or query image or image. All three cannot be none."
            )
        if text is not None and query_images is not None:
            raise ValueError("You have to specify either text or query_images, not both.")
''')
s=s.replace('''            encoding["attention_mask"] = attention_mask

        if images is not None:
            image_features = self.feature_extractor(images, return_tensors=return_tensors, **kwargs)

        if text is not None and images is not None:
            encoding["pixel_values"] = image_features.pixel_values
            return encoding
        elif text is not None:
            return encoding
''','''            encoding["attention_mask"] = attention_mask

        if query_images is not None:
            encoding = BatchEncoding()
            query_pixel_values = self.feature_extractor(
                query_images, return_tensors=return_tensors, **kwargs
            ).pixel_values
            encoding["query_pixel_values"] = query_pixel_values

        if images is not None:
            image_features = self.feature_extractor(images, return_tensors=return_tensors, **kwargs)

        if (text is not None or query_images is not None) and images is not None:
            encoding["pixel_values"] = image_features.pixel_values
            return encoding
        elif text is not None or query_images is not None:
            return encoding
''')
s=s.replace('''        return self.feature_extractor.post_process(*args, **kwargs)
''','''        return self.feature_extractor.post_process(*args, **kwargs)

    def post_process_image_guided_detection(self, *args, **kwargs):
        """
        This method forwards all its arguments to [`OwlViTFeatureExtractor.post_process_image_guided_detection`].
        Please refer to the docstring of this method for more information.
        """
        return self.feature_extractor.post_process_image_guided_detection(*args, **kwargs)
''')
open(p,'w').write(s)
EOF
git diff --stat
```

tool result:

```
 .../models/owlvit/processing_owlvit.py             | 38 ++++++++++++++++++----
 1 file changed, 32 insertions(+), 6 deletions(-)
```

**assistant:** Next, the feature extractor's post-processing.

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; sed -n 108,150p src/transformers/models/owlvit/feature_extraction_owlvit.py
```

tool result:

```
        """
        Converts the output of [`OwlViTForObjectDetection`] into the format expected by the COCO api.

        Args:
            outputs ([`OwlViTObjectDetectionOutput`]):
                Raw outputs of the model.
            target_sizes (`torch.Tensor` of shape `(batch_size, 2)`):
                Tensor containing the size (h, w) of each image of the batch. For evaluation, this must be the original
                image size (before any data augmentation). For visualization, this should be the image size after data
                augment, but before padding.
        Returns:
            `List[Dict]`: A list of dictionaries, each dictionary containing the scores, labels and boxes for an image
            in the batch as predicted by the model.
        """
        logits, boxes = outputs.logits, outputs.pred_boxes

        if len(logits) != len(target_sizes):
            raise ValueError("Make sure that you pass in as many target sizes as the batch dimension of the logits")
        if target_sizes.shape[1] != 2:
            raise ValueError("Each element of target_sizes must contain the size (h, w) of each image of the batch")

        probs = torch.max(logits, dim=-1)
        scores = torch.sigmoid(probs.values)
        labels = probs.indices

        # Convert to [x0, y0, x1, y1] format
        boxes = center_to_corners_format(boxes)

        # Convert from relative [0, 1] to absolute [0, height] coordinates
        img_h, img_w = target_sizes.unbind(1)
        scale_fct = torch.stack([img_w, img_h, img_w, img_h], dim=1)
        boxes = boxes * scale_fct[:, None, :]

        results = [{"scores": s, "labels": l, "boxes": b} for s, l, b in zip(scores, labels, boxes)]

        return results

    def __call__(
        self,
        images: Union[
            Image.Image, np.ndarray, "torch.Tensor", List[Image.Image], List[np.ndarray], List["torch.Tensor"]  # noqa
        ],
        return_tensors: Optional[Union[str, TensorType]] = None,
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; python3 - <<'EOF'
p='src/transformers/models/owlvit/feature_extraction_owlvit.py'
s=open(p).read()
s=s.replace('''    return torch.stack(boxes, dim=-1)

''','''    return torch.stack(boxes, dim=-1)


# Copied from transformers.models.detr.modeling_detr._upcast
def _upcast(t):
    # Protects from numerical overflows in multiplications by upcasting to the equivalent higher type
    if t.is_floating_point():
        return t if t.dtype in (torch.float32, torch.float64) else t.float()
    else:
        return t if t.dtype in (torch.int32, torch.int64) else t.int()


def box_area(boxes):
    """
    Computes the area of a set of bounding boxes, which are specified by its (x1, y1, x2, y2) coordinates.

    Args:
        boxes (`torch.FloatTensor` of shape `(number_of_boxes, 4)`):
            Boxes for which the area will be computed. They are expected to be in (x1, y1, x2, y2) format with `0 <= x1
            < x2` and `0 <= y1 < y2`.
    Returns:
        `torch.FloatTensor`: a tensor containing the area for each box.
    """
    boxes = _upcast(boxes)
    return (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])


def box_iou(boxes1, boxes2):
    area1 = box_area(boxes1)
    area2 = box_area(boxes2)

    left_top = torch.max(boxes1[:, None, :2], boxes2[:, :2])  # [N,M,2]
    right_bottom = torch.min(boxes1[:, None, 2:], boxes2[:, 2:])  # [N,M,2]

    width_height = (right_bottom - left_top).clamp(min=0)  # [N,M,2]
    inter = width_height[:, :, 0] * width_height[:, :, 1]  # [N,M]

    union = area1[:, None] + area2 - inter

    iou = inter / union
    return iou, union

''',1)
s=s.replace('''        results = [{"scores": s, "labels": l, "boxes": b} for s, l, b in zip(scores, labels, boxes)]

        return results
''','''        results = [{"scores": s, "labels": l, "boxes": b} for s, l, b in zip(scores, labels, boxes)]

        return results

    def post_process_image_guided_detection(self, outputs, threshold=0.6, nms_threshold=0.3, target_sizes=None):
        """
        Converts the output of [`OwlViTForObjectDetection.image_guided_detection`] into the format expected by the COCO
        api.

        Args:
            outputs ([`OwlViTImageGuidedObjectDetectionOutput`]):
                Raw outputs of the model.
            threshold (`float`, *optional*, defaults to 0.6):
                Minimum confidence threshold to use to filter out predicted boxes.
            nms_threshold (`float`, *optional*, defaults to 0.3):
                IoU threshold for non-maximum suppression of overlapping boxes.
            target_sizes (`torch.Tensor`, *optional*):
                Tensor of shape (batch_size, 2) where each entry is the (height, width) of the corresponding image in
                the batch. If set, predicted normalized bounding boxes are rescaled to the target sizes. If left to
                None, predictions will not be unnormalized.

        Returns:
            `List[Dict]`: A list of dictionaries, each dictionary containing the scores, labels and boxes for an image
            in the batch as predicted by the model. All labels are set to None as
            `OwlViTForObjectDetection.image_guided_detection` perform one-shot object detection.
        """
        logits, target_boxes = outputs.logits, outputs.target_pred_boxes

        if target_sizes is not None:
            if len(logits) != len(target_sizes):
                raise ValueError(
                    "Make sure that you pass in as many target sizes as the batch dimension of the logits"
                )
            if target_sizes.shape[1] != 2:
                raise ValueError(
                    "Each element of target_sizes must contain the size (h, w) of each image of the batch"
                )

        probs = torch.max(logits, dim=-1)
        scores = torch.sigmoid(probs.values)

        # Convert to [x0, y0, x1, y1] format
        target_boxes = center_to_corners_format(target_boxes)

        # Apply non-maximum suppression (NMS)
        if nms_threshold < 1.0:
            for idx in range(target_boxes.shape[0]):
                for i in torch.argsort(-scores[idx]):
                    if not scores[idx][i]:
                        continue

                    ious = box_iou(target_boxes[idx][i, :].unsqueeze(0), target_boxes[idx])[0][0]
                    ious[i] = -1.0  # Mask self-IoU.
                    scores[idx][ious > nms_threshold] = 0.0

        # Convert from relative [0, 1] to absolute [0, height] coordinates
        if target_sizes is not None:
            img_h, img_w = target_sizes.unbind(1)
            scale_fct = torch.stack([img_w, img_h, img_w, img_h], dim=1).to(target_boxes.device)
            target_boxes = target_boxes * scale_fct[:, None, :]

        results = []
        for idx in range(target_boxes.shape[0]):
            query_scores = scores[idx]
            query_alphas = torch.zeros_like(query_scores)

            if query_scores.nonzero().numel():
                # Scale box alpha such that the best box has alpha 1.0 and the worst box has alpha 0.1.
                max_score = torch.max(query_scores) + 1e-6
                query_alphas = (query_scores - (max_score * 0.1)) / (max_score * 0.9)
                query_alphas[query_alphas < threshold] = 0.0
                query_alphas = torch.clip(query_alphas, 0.0, 1.0)

            mask = query_alphas > 0
            results.append({"scores": query_alphas[mask], "labels": None, "boxes": target_boxes[idx][mask]})

        return results
''')
open(p,'w').write(s)
EOF
```

tool result:

```
(Bash completed with no output)
```

**assistant:** Now the model. First the box utilities and the new output class:

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; sed -n 140,162p src/transformers/models/owlvit/modeling_owlvit.py
```

tool result:

```
            image embeddings for each patch.
        class_embeds (`torch.FloatTensor` of shape `(batch_size, num_patches, hidden_size)`):
            Class embeddings of all image patches. OWL-ViT represents images as a set of image patches where the total
            number of patches is (image_size / patch_size)**2.
        text_model_last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`)):
            Last hidden states extracted from the [`OwlViTTextModel`].
        vision_model_last_hidden_state (`torch.FloatTensor` of shape `(batch_size, num_patches + 1, hidden_size)`)):
            Last hidden states extracted from the [`OwlViTVisionModel`]. OWL-ViT represents images as a set of image
            patches where the total number of patches is (image_size / patch_size)**2.
    """

    loss: Optional[torch.FloatTensor] = None
    loss_dict: Optional[Dict] = None
    logits: torch.FloatTensor = None
    pred_boxes: torch.FloatTensor = None
    text_embeds: torch.FloatTensor = None
    image_embeds: torch.FloatTensor = None
    class_embeds: torch.FloatTensor = None
    text_model_last_hidden_state: Optional[torch.FloatTensor] = None
    vision_model_last_hidden_state: Optional[torch.FloatTensor] = None


class OwlViTVisionEmbeddings(nn.Module):
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; python3 - <<'EOF'
p='src/transformers/models/owlvit/modeling_owlvit.py'
s=open(p).read()
s=s.replace('''    return (caption_loss + image_loss) / 2.0

''','''    return (caption_loss + image_loss) / 2.0


# Copied from transformers.models.owlvit.feature_extraction_owlvit.center_to_corners_format
def center_to_corners_format(x):
    """
    Converts a PyTorch tensor of bounding boxes of center format (center_x, center_y, width, height) to corners format
    (left, top, right, bottom).
    """
    x_center, y_center, width, height = x.unbind(-1)
    boxes = [(x_center - 0.5 * width), (y_center - 0.5 * height), (x_center + 0.5 * width), (y_center + 0.5 * height)]
    return torch.stack(boxes, dim=-1)


# Copied from transformers.models.detr.modeling_detr._upcast
def _upcast(t):
    # Protects from numerical overflows in multiplications by upcasting to the equivalent higher type
    if t.is_floating_point():
        return t if t.dtype in (torch.float32, torch.float64) else t.float()
    else:
        return t if t.dtype in (torch.int32, torch.int64) else t.int()


# Copied from transformers.models.detr.modeling_detr.box_area
def box_area(boxes):
    """
    Computes the area of a set of bounding boxes, which are specified by its (x1, y1, x2, y2) coordinates.

    Args:
        boxes (`torch.FloatTensor` of shape `(number_of_boxes, 4)`):
            Boxes for which the area will be computed. They are expected to be in (x1, y1, x2, y2) format with `0 <= x1
            < x2` and `0 <= y1 < y2`.

    Returns:
        `torch.FloatTensor`: a tensor containing the area for each box.
    """
    boxes = _upcast(boxes)
    return (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])


# Copied from transformers.models.detr.modeling_detr.box_iou
def box_iou(boxes1, boxes2):
    area1 = box_area(boxes1)
    area2 = box_area(boxes2)

    left_top = torch.max(boxes1[:, None, :2], boxes2[:, :2])  # [N,M,2]
    right_bottom = torch.min(boxes1[:, None, 2:], boxes2[:, 2:])  # [N,M,2]

    width_height = (right_bottom - left_top).clamp(min=0)  # [N,M,2]
    inter = width_height[:, :, 0] * width_height[:, :, 1]  # [N,M]

    union = area1[:, None] + area2 - inter

    iou = inter / union
    return iou, union


# Copied from transformers.models.detr.modeling_detr.generalized_box_iou
def generalized_box_iou(boxes1, boxes2):
    """
    Generalized IoU from https://giou.stanford.edu/. The boxes should be in [x0, y0, x1, y1] (corner) format.

    Returns:
        `torch.FloatTensor`: a [N, M] pairwise matrix, where N = len(boxes1) and M = len(boxes2)
    """
    # degenerate boxes gives inf / nan results
    # so do an early check
    if not (boxes1[:, 2:] >= boxes1[:, :2]).all():
        raise ValueError(f"boxes1 must be in [x0, y0, x1, y1] (corner) format, but got {boxes1}")
    if not (boxes2[:, 2:] >= boxes2[:, :2]).all():
        raise ValueError(f"boxes2 must be in [x0, y0, x1, y1] (corner) format, but got {boxes2}")
    iou, union = box_iou(boxes1, boxes2)

    top_left = torch.min(boxes1[:, None, :2], boxes2[:, :2])
    bottom_right = torch.max(boxes1[:, None, 2:], boxes2[:, 2:])

    width_height = (bottom_right - top_left).clamp(min=0)  # [N,M,2]
    area = width_height[:, :, 0] * width_height[:, :, 1]

    return iou - (area - union) / area

''',1)
s=s.replace('''    text_model_last_hidden_state: Optional[torch.FloatTensor] = None
    vision_model_last_hidden_state: Optional[torch.FloatTensor] = None

''','''    text_model_last_hidden_state: Optional[torch.FloatTensor] = None
    vision_model_last_hidden_state: Optional[torch.FloatTensor] = None


@dataclass
class OwlViTImageGuidedObjectDetectionOutput(ModelOutput):
    """
    Output type of [`OwlViTForObjectDetection.image_guided_detection`].

    Args:
        logits (`torch.FloatTensor` of shape `(batch_size, num_patches, num_queries)`):
            Classification logits (including no-object) for all queries.
        target_pred_boxes (`torch.FloatTensor` of shape `(batch_size, num_patches, 4)`):
            Normalized boxes coordinates for all queries, represented as (center_x, center_y, width, height). These
            values are normalized in [0, 1], relative to the size of each individual target image in the batch
            (disregarding possible padding). You can use
            [`~OwlViTFeatureExtractor.post_process_image_guided_detection`] to retrieve the unnormalized bounding
            boxes.
        query_pred_boxes (`torch.FloatTensor` of shape `(batch_size, num_patches, 4)`):
            Normalized boxes coordinates for all queries, represented as (center_x, center_y, width, height). These
            values are normalized in [0, 1], relative to the size of each individual query image in the batch
            (disregarding possible padding).
        image_embeds (`torch.FloatTensor` of shape `(batch_size, patch_size, patch_size, output_dim`):
            Pooled output of [`OwlViTVisionModel`] for the target images. OWL-ViT represents images as a set of image
            patches and computes image embeddings for each patch.
        query_image_embeds (`torch.FloatTensor` of shape `(batch_size, patch_size, patch_size, output_dim`):
            Pooled output of [`OwlViTVisionModel`] for the query images. OWL-ViT represents images as a set of image
            patches and computes image embeddings for each patch.
        class_embeds (`torch.FloatTensor` of shape `(batch_size, num_patches, hidden_size)`):
            Class embeddings of all image patches. OWL-ViT represents images as a set of image patches where the total
            number of patches is (image_size / patch_size)**2.
        vision_model_output (`BaseModelOutputWithPooling`):
            The output of the [`OwlViTVisionModel`] for the target images.
    """

    logits: torch.FloatTensor = None
    image_embeds: torch.FloatTensor = None
    query_image_embeds: torch.FloatTensor = None
    target_pred_boxes: torch.FloatTensor = None
    query_pred_boxes: torch.FloatTensor = None
    class_embeds: torch.FloatTensor = None
    vision_model_output: BaseModelOutputWithPooling = None

    def to_tuple(self) -> Tuple[Any]:
        return tuple(self[k] if k != "vision_model_output" else getattr(self, k).to_tuple() for k in self.keys())

''',1)
open(p,'w').write(s)
EOF
```

tool result:

```
(Bash completed with no output)
```

**assistant:** Now the class head (allow no queries), plus the new `image_embedder`, `embed_image_query`, and `image_guided_detection` methods:

**tool call: Bash**

````bash
cd /work/huggingface__transformers-20136/repo; python3 - <<'EOF'
p='src/transformers/models/owlvit/modeling_owlvit.py'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
rep('''        self.dense0 = nn.Linear(query_dim, out_dim)
        self.logit_shift''','''        self.out_dim = out_dim
        self.dense0 = nn.Linear(query_dim, out_dim)
        self.logit_shift''')
rep('''        query_embeds: torch.FloatTensor,
        query_mask: torch.Tensor,
    ) -> Tuple[torch.FloatTensor]:

        image_class_embeds = self.dense0(image_embeds)
''','''        query_embeds: Optional[torch.FloatTensor],
        query_mask: Optional[torch.Tensor],
    ) -> Tuple[torch.FloatTensor]:

        image_class_embeds = self.dense0(image_embeds)
        if query_embeds is None:
            batch_size, num_patches = image_class_embeds.shape[:2]
            pred_logits = torch.zeros(
                (batch_size, num_patches, self.out_dim), dtype=image_class_embeds.dtype, device=image_class_embeds.device
            )
            return (pred_logits, image_class_embeds)
''')
rep('''            [What are attention masks?](../glossary#attention-mask)
"""


class OwlViTEncoder(''','''            [What are attention masks?](../glossary#attention-mask)
"""

OWLVIT_IMAGE_GUIDED_OBJECT_DETECTION_INPUTS_DOCSTRING = r"""
    Args:
        pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`):
            Pixel values of target images.
        query_pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`):
            Pixel values of query images to detect. Pass in one query image per target image.
        output_attentions (`bool`, *optional*):
            Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
            tensors for more detail.
        output_hidden_states (`bool`, *optional*):
            Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
            more detail.
        return_dict (`bool`, *optional*):
            Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
"""


class OwlViTEncoder(''')
rep('''        query_embeds: torch.FloatTensor,
        query_mask: torch.Tensor,
    ) -> Tuple[torch.FloatTensor]:
        """
        Args:
            image_feats:
                Features extracted from the `image_text_embedder`.
            query_embeds:
                Text query embeddings.
            query_mask:
                Must be provided with query_embeddings. A mask indicating which query embeddings are valid.
        """''','''        query_embeds: Optional[torch.FloatTensor] = None,
        query_mask: Optional[torch.Tensor] = None,
    ) -> Tuple[torch.FloatTensor]:
        """
        Args:
            image_feats:
                Features extracted from the `image_text_embedder` or `image_embedder` methods.
            query_embeds:
                Text or image query embeddings.
            query_mask:
                A mask indicating which query embeddings are valid.
        """''')
rep('''    def image_text_embedder(
        self,
        input_ids: torch.Tensor,
        pixel_values: torch.FloatTensor,
        attention_mask: torch.Tensor,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
    ) -> Tuple[torch.FloatTensor]:

        # Encode text and image
        outputs = self.owlvit(
            pixel_values=pixel_values,
            input_ids=input_ids,
            attention_mask=attention_mask,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=True,
        )

        # Resize class token
        last_hidden_state = outputs.vision_model_output[0]
        image_embeds = self.owlvit.vision_model.post_layernorm(last_hidden_state)
''','''    def _vision_feature_map(self, last_hidden_state: torch.FloatTensor) -> torch.FloatTensor:
        # Merges the patch embeddings with the class token and reshapes them into a spatial feature map
        image_embeds = self.owlvit.vision_model.post_layernorm(last_hidden_state)
''')
rep('''        image_embeds = image_embeds.reshape(new_size)
        text_embeds = outputs.text_embeds
''','''        return image_embeds.reshape(new_size)

    def image_text_embedder(
        self,
        input_ids: torch.Tensor,
        pixel_values: torch.FloatTensor,
        attention_mask: torch.Tensor,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
    ) -> Tuple[torch.FloatTensor]:

        # Encode text and image
        outputs = self.owlvit(
            pixel_values=pixel_values,
            input_ids=input_ids,
            attention_mask=attention_mask,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=True,
        )

        # Compute the [batch_size, num_patches, num_patches, hidden_size] feature map
        image_embeds = self._vision_feature_map(outputs.vision_model_output[0])
        text_embeds = outputs.text_embeds
''')
rep('''        return (text_embeds, image_embeds, text_model_last_hidden_state, vision_model_last_hidden_state)
''','''        return (text_embeds, image_embeds, text_model_last_hidden_state, vision_model_last_hidden_state)

    def image_embedder(
        self,
        pixel_values: torch.FloatTensor,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
    ) -> Tuple[torch.FloatTensor]:
        # Encode images
        vision_outputs = self.owlvit.vision_model(
            pixel_values=pixel_values,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=True,
        )

        # Compute the [batch_size, num_patches, num_patches, hidden_size] feature map
        image_embeds = self._vision_feature_map(vision_outputs[0])

        return (image_embeds, vision_outputs)

    def embed_image_query(
        self, query_image_features: torch.FloatTensor, query_feature_map: torch.FloatTensor
    ) -> Tuple[torch.FloatTensor]:
        """
        Selects, for each query image, the class embedding of the predicted box that best represents the query object.

        Args:
            query_image_features:
                Flattened features of the query images, of shape `(batch_size, num_patches, hidden_size)`.
            query_feature_map:
                A spatial re-arrangement of `query_image_features`, returned by the `image_embedder` method.
        Returns:
            A tuple of the query embeddings of shape `(batch_size, 1, hidden_size)`, the indices of the selected boxes
            of shape `(batch_size,)` and the boxes predicted on the query images.
        """
        _, class_embeds = self.class_predictor(query_image_features)
        pred_boxes = self.box_predictor(query_image_features, query_feature_map)
        pred_boxes_as_corners = center_to_corners_format(pred_boxes)

        # The query object is assumed to cover the whole query image
        query_box = torch.tensor([[0.0, 0.0, 1.0, 1.0]], dtype=pred_boxes.dtype, device=pred_boxes.device)

        # Loop over query images
        best_class_embeds = []
        best_box_indices = []
        for i in range(query_image_features.shape[0]):
            ious = box_iou(query_box, pred_boxes_as_corners[i])[0][0]

            # If there are no overlapping boxes, fall back to generalized IoU
            if torch.all(ious == 0.0):
                ious = generalized_box_iou(query_box, pred_boxes_as_corners[i])[0]

            # Use an adaptive threshold to include all boxes within 80% of the best IoU
            max_iou = torch.max(ious)
            iou_threshold = max_iou - 0.2 * torch.abs(max_iou)
            selected_inds = torch.nonzero(ious >= iou_threshold).squeeze(1)

            # Among the selected boxes, pick the one that is the most dissimilar to the mean embedding
            selected_embeddings = class_embeds[i][selected_inds]
            mean_embeds = torch.mean(class_embeds[i], dim=0)
            mean_sim = torch.einsum("d,id->i", mean_embeds, selected_embeddings)
            best_box_ind = selected_inds[torch.argmin(mean_sim)]

            best_class_embeds.append(class_embeds[i][best_box_ind])
            best_box_indices.append(best_box_ind)

        query_embeds = torch.stack(best_class_embeds).unsqueeze(1)
        box_indices = torch.stack(best_box_indices)

        return query_embeds, box_indices, pred_boxes

    @add_start_docstrings_to_model_forward(OWLVIT_IMAGE_GUIDED_OBJECT_DETECTION_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=OwlViTImageGuidedObjectDetectionOutput, config_class=OwlViTConfig)
    def image_guided_detection(
        self,
        pixel_values: torch.FloatTensor,
        query_pixel_values: torch.FloatTensor,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
        return_dict: Optional[bool] = None,
    ) -> OwlViTImageGuidedObjectDetectionOutput:
        r"""
        Returns:

        Examples:
        ```python
        >>> import requests
        >>> from PIL import Image
        >>> import torch
        >>> from transformers import OwlViTProcessor, OwlViTForObjectDetection

        >>> processor = OwlViTProcessor.from_pretrained("google/owlvit-base-patch16")
        >>> model = OwlViTForObjectDetection.from_pretrained("google/owlvit-base-patch16")
        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)
        >>> query_url = "http://images.cocodataset.org/val2017/000000001675.jpg"
        >>> query_image = Image.open(requests.get(query_url, stream=True).raw)
        >>> inputs = processor(images=image, query_images=query_image, return_tensors="pt")
        >>> with torch.no_grad():
        ...     outputs = model.image_guided_detection(**inputs)
        >>> # Target image sizes (height, width) to rescale box predictions [batch_size, 2]
        >>> target_sizes = torch.Tensor([image.size[::-1]])
        >>> # Convert outputs (bounding boxes and class logits) to COCO API
        >>> results = processor.post_process_image_guided_detection(
        ...     outputs=outputs, threshold=0.6, nms_threshold=0.3, target_sizes=target_sizes
        ... )
        >>> i = 0  # Retrieve predictions for the first image
        >>> boxes, scores = results[i]["boxes"], results[i]["scores"]
        >>> for box, score in zip(boxes, scores):
        ...     box = [round(i, 2) for i in box.tolist()]
        ...     print(f"Detected similar object with confidence {round(score.item(), 3)} at location {box}")
        ```"""
        output_attentions = output_attentions if output_attentions is not None else self.config.output_attentions
        output_hidden_states = (
            output_hidden_states if output_hidden_states is not None else self.config.output_hidden_states
        )
        return_dict = return_dict if return_dict is not None else self.config.return_dict

        if pixel_values.shape[0] != query_pixel_values.shape[0]:
            raise ValueError(
                "Make sure to pass in one query image per target image, got"
                f" {query_pixel_values.shape[0]} query images and {pixel_values.shape[0]} target images."
            )

        # Compute feature maps for the input and query images
        query_feature_map = self.image_embedder(pixel_values=query_pixel_values)[0]
        feature_map, vision_outputs = self.image_embedder(
            pixel_values=pixel_values,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
        )

        batch_size, num_patches, num_patches, hidden_dim = feature_map.shape
        image_feats = torch.reshape(feature_map, (batch_size, num_patches * num_patches, hidden_dim))

        batch_size, num_patches, num_patches, hidden_dim = query_feature_map.shape
        query_image_feats = torch.reshape(query_feature_map, (batch_size, num_patches * num_patches, hidden_dim))

        # Get top class embedding for each query image in batch [batch_size, 1, hidden_dim]
        query_embeds, _, query_pred_boxes = self.embed_image_query(query_image_feats, query_feature_map)

        # Predict object classes [batch_size, num_patches, 1]
        (pred_logits, class_embeds) = self.class_predictor(image_feats=image_feats, query_embeds=query_embeds)

        # Predict object boxes
        target_pred_boxes = self.box_predictor(image_feats, feature_map)

        if not return_dict:
            output = (
                pred_logits,
                feature_map,
                query_feature_map,
                target_pred_boxes,
                query_pred_boxes,
                class_embeds,
                vision_outputs.to_tuple(),
            )
            output = tuple(x for x in output if x is not None)
            return output

        return OwlViTImageGuidedObjectDetectionOutput(
            logits=pred_logits,
            image_embeds=feature_map,
            query_image_embeds=query_feature_map,
            target_pred_boxes=target_pred_boxes,
            query_pred_boxes=query_pred_boxes,
            class_embeds=class_embeds,
            vision_model_output=vision_outputs,
        )
''')
open(p,'w').write(s)
EOF
sed -n '/def _vision_feature_map/,/def image_text_embedder/p' src/transformers/models/owlvit/modeling_owlvit.py
````

tool result:

```
    def _vision_feature_map(self, last_hidden_state: torch.FloatTensor) -> torch.FloatTensor:
        # Merges the patch embeddings with the class token and reshapes them into a spatial feature map
        image_embeds = self.owlvit.vision_model.post_layernorm(last_hidden_state)
        new_size = tuple(np.array(image_embeds.shape) - np.array((0, 1, 0)))
        class_token_out = torch.broadcast_to(image_embeds[:, :1, :], new_size)

        # Merge image embedding with class tokens
        image_embeds = image_embeds[:, 1:, :] * class_token_out
        image_embeds = self.layer_norm(image_embeds)

        # Resize to [batch_size, num_patches, num_patches, hidden_size]
        new_size = (
            image_embeds.shape[0],
            int(np.sqrt(image_embeds.shape[1])),
            int(np.sqrt(image_embeds.shape[1])),
            image_embeds.shape[-1],
        )
        return image_embeds.reshape(new_size)

    def image_text_embedder(
```

**assistant:** The model changes are in. Next I'll run an end-to-end check with a tiny randomly initialized model and the processor, covering both the dict and tuple outputs and the post-processing:

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; cat > repro_owlvit.py <<'EOF'
import numpy as np, torch
from PIL import Image
from transformers import OwlViTConfig, OwlViTForObjectDetection, OwlViTFeatureExtractor, OwlViTProcessor, CLIPTokenizer

text_cfg = dict(vocab_size=99, hidden_size=32, intermediate_size=37, num_hidden_layers=2, num_attention_heads=4, max_position_embeddings=16)
vis_cfg = dict(hidden_size=32, intermediate_size=37, num_hidden_layers=2, num_attention_heads=4, image_size=32, patch_size=8)
config = OwlViTConfig.from_text_vision_configs(text_cfg, vis_cfg, projection_dim=64)
model = OwlViTForObjectDetection(config).eval()

fe = OwlViTFeatureExtractor(size=32, crop_size=32)
imgs = [Image.fromarray(np.random.randint(0, 255, (40, 50, 3), dtype=np.uint8)) for _ in range(2)]
q = [Image.fromarray(np.random.randint(0, 255, (30, 30, 3), dtype=np.uint8)) for _ in range(2)]

class DummyProc(OwlViTProcessor):
    def __init__(self, fe):
        self.feature_extractor = fe
proc = DummyProc(fe)
inputs = proc(images=imgs, query_images=q, return_tensors="pt")
print(list(inputs.keys()), inputs.query_pixel_values.shape)
print(list(proc(images=imgs, query_images=q).keys()))
try:
    proc()
except ValueError as e:
    print("ok raises:", e)

with torch.no_grad():
    out = model.image_guided_detection(**inputs)
    tup = model.image_guided_detection(**inputs, return_dict=False)
print(out.logits.shape, out.target_pred_boxes.shape, out.query_pred_boxes.shape, out.class_embeds.shape,
      out.image_embeds.shape, out.query_image_embeds.shape)
for a, b in zip(tup[:6], out.to_tuple()[:6]):
    assert torch.allclose(a, b)
res = proc.post_process_image_guided_detection(out, threshold=0.0, nms_threshold=0.3, target_sizes=torch.Tensor([[40, 50], [40, 50]]))
print([(r["scores"].shape, r["boxes"].shape) for r in res])
res = proc.post_process_image_guided_detection(out)
print(len(res))
EOF
../bin/envrun 'python repro_owlvit.py' 2>&1 | tail -12
```

tool result:

```
['query_pixel_values', 'pixel_values'] torch.Size([2, 3, 32, 32])
['query_pixel_values', 'pixel_values']
ok raises: You have to specify at least one text or query image or image. All three cannot be none.
torch.Size([2, 16, 1]) torch.Size([2, 16, 4]) torch.Size([2, 16, 4]) torch.Size([2, 16, 32]) torch.Size([2, 4, 4, 32]) torch.Size([2, 4, 4, 32])
[(torch.Size([16]), torch.Size([16, 4])), (torch.Size([16]), torch.Size([16, 4]))]
2
```

**thinking:**

```
The repro confirms expected behavior: the processor outputs query_pixel_values and pixel_values, image_guided_detection returns consistent dict/tuple outputs, and post-processing yields one result per image. Next I'll update the docs and run the existing tests plus consistency checks.


```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; grep -n "members\|autodoc\|post_process" docs/source/en/model_doc/owlvit.mdx
```

tool result:

```
49:>>> results = processor.post_process(outputs=outputs, target_sizes=target_sizes)
68:[[autodoc]] OwlViTConfig
73:[[autodoc]] OwlViTTextConfig
77:[[autodoc]] OwlViTVisionConfig
81:[[autodoc]] OwlViTFeatureExtractor
86:[[autodoc]] OwlViTProcessor
90:[[autodoc]] OwlViTModel
97:[[autodoc]] OwlViTTextModel
102:[[autodoc]] OwlViTVisionModel
107:[[autodoc]] OwlViTForObjectDetection
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; sed -n 18,30p docs/source/en/model_doc/owlvit.mdx; sed -n 78,112p docs/source/en/model_doc/owlvit.mdx
```

tool result:

````
The abstract from the paper is the following:

*Combining simple architectures with large-scale pre-training has led to massive improvements in image classification. For object detection, pre-training and scaling approaches are less well established, especially in the long-tailed and open-vocabulary setting, where training data is relatively scarce. In this paper, we propose a strong recipe for transferring image-text models to open-vocabulary object detection. We use a standard Vision Transformer architecture with minimal modifications, contrastive image-text pre-training, and end-to-end detection fine-tuning. Our analysis of the scaling properties of this setup shows that increasing image-level pre-training and model size yield consistent improvements on the downstream detection task. We provide the adaptation strategies and regularizations needed to attain very strong performance on zero-shot text-conditioned and one-shot image-conditioned object detection. Code and models are available on GitHub.*

## Usage

OWL-ViT is a zero-shot text-conditioned object detection model. OWL-ViT uses [CLIP](clip) as its multi-modal backbone, with a ViT-like Transformer to get visual features and a causal language model to get the text features. To use CLIP for detection, OWL-ViT removes the final token pooling layer of the vision model and attaches a lightweight classification and box head to each transformer output token. Open-vocabulary classification is enabled by replacing the fixed classification layer weights with the class-name embeddings obtained from the text model. The authors first train CLIP from scratch and fine-tune it end-to-end with the classification and box heads on standard detection datasets using a bipartite matching loss. One or multiple text queries per image can be used to perform zero-shot text-conditioned object detection. 

[`OwlViTFeatureExtractor`] can be used to resize (or rescale) and normalize images for the model and [`CLIPTokenizer`] is used to encode the text. [`OwlViTProcessor`] wraps [`OwlViTFeatureExtractor`] and [`CLIPTokenizer`] into a single instance to both encode the text and prepare the images. The following example shows how to perform object detection using [`OwlViTProcessor`] and [`OwlViTForObjectDetection`].


```python

## OwlViTFeatureExtractor

[[autodoc]] OwlViTFeatureExtractor
    - __call__

## OwlViTProcessor

[[autodoc]] OwlViTProcessor

## OwlViTModel

[[autodoc]] OwlViTModel
    - forward
    - get_text_features
    - get_image_features

## OwlViTTextModel

[[autodoc]] OwlViTTextModel
    - forward

## OwlViTVisionModel

[[autodoc]] OwlViTVisionModel
    - forward

## OwlViTForObjectDetection

[[autodoc]] OwlViTForObjectDetection
    - forward
````

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; python3 - <<'EOF'
p='docs/source/en/model_doc/owlvit.mdx'
s=open(p).read()
s=s.replace("""One or multiple text queries per image can be used to perform zero-shot text-conditioned object detection. 
""","""One or multiple text queries per image can be used to perform zero-shot text-conditioned object detection. Alternatively, a query image can be passed in place of text queries to perform one-shot image-guided object detection with [`OwlViTForObjectDetection.image_guided_detection`]. 
""")
s=s.replace("""[[autodoc]] OwlViTFeatureExtractor
    - __call__
""","""[[autodoc]] OwlViTFeatureExtractor
    - __call__
    - post_process
    - post_process_image_guided_detection
""")
s=s.replace("""[[autodoc]] OwlViTForObjectDetection
    - forward""","""[[autodoc]] OwlViTForObjectDetection
    - forward
    - image_guided_detection""")
open(p,'w').write(s)
EOF
git diff --stat docs; rm repro_owlvit.py
../bin/envrun 'python utils/check_copies.py; python utils/check_repo.py 2>&1 | tail -3; black --check src/transformers/models/owlvit; flake8 src/transformers/models/owlvit; python -m pytest tests/models/owlvit -q -x 2>&1 | tail -3'
```

tool result:

```
 docs/source/en/model_doc/owlvit.mdx | 5 ++++-
 1 file changed, 4 insertions(+), 1 deletion(-)
    raise RuntimeError(
RuntimeError: Failed to import transformers.models.rag.modeling_rag because of the following error (look up to see its traceback):
module 'pyarrow' has no attribute 'PyExtensionType'
would reformat src/transformers/models/owlvit/modeling_owlvit.py

Oh no! 💥 💔 💥
1 file would be reformatted, 5 files would be left unchanged.
bash: line 1: flake8: command not found
ERROR tests/models/owlvit/test_feature_extraction_owlvit.py::OwlViTFeatureExtractionTester
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
1 error in 0.33s
```

**thinking:**

```
check_copies passes, but check_repo fails due to an unrelated pyarrow import error. I'll now review the black diff and the test-collection error, first checking if it also occurs on the original code.


```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; ../bin/envrun 'black --diff -q src/transformers/models/owlvit/modeling_owlvit.py; python -m pytest tests/models/owlvit -q 2>&1 | tail -5; git stash -q; python -m pytest tests/models/owlvit -q 2>&1 | tail -2; git stash pop -q; git status --short'
```

tool result:

```
--- src/transformers/models/owlvit/modeling_owlvit.py	2026-10-08 21:15:04.474622 +0000
+++ src/transformers/models/owlvit/modeling_owlvit.py	2026-10-08 21:15:55.535299 +0000
@@ -1272,11 +1272,13 @@
 
         image_class_embeds = self.dense0(image_embeds)
         if query_embeds is None:
             batch_size, num_patches = image_class_embeds.shape[:2]
             pred_logits = torch.zeros(
-                (batch_size, num_patches, self.out_dim), dtype=image_class_embeds.dtype, device=image_class_embeds.device
+                (batch_size, num_patches, self.out_dim),
+                dtype=image_class_embeds.dtype,
+                device=image_class_embeds.device,
             )
             return (pred_logits, image_class_embeds)
 
         # Normalize image and text features
         image_class_embeds /= torch.linalg.norm(image_class_embeds, dim=-1, keepdim=True) + 1e-6
-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
ERROR tests/models/owlvit/test_feature_extraction_owlvit.py::OwlViTFeatureExtractionTester
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.74s
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.84s
 M docs/source/en/model_doc/owlvit.mdx
 M src/transformers/models/owlvit/feature_extraction_owlvit.py
 M src/transformers/models/owlvit/modeling_owlvit.py
 M src/transformers/models/owlvit/processing_owlvit.py
?? Dockerfile
```

**thinking:**

```
The collection error exists in the original code too, so it's a pre-existing environment issue, not something I introduced. I'll apply black's formatting, then run the test files separately to avoid the collection error blocking the run.


```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; ../bin/envrun 'black -q src/transformers/models/owlvit; python -m pytest tests/models/owlvit/test_modeling_owlvit.py tests/models/owlvit/test_processor_owlvit.py -q 2>&1 | tail -3; python -m pytest tests/models/owlvit/test_feature_extraction_owlvit.py -q 2>&1 | grep -m3 Error'
```

tool result:

```
FAILED tests/models/owlvit/test_processor_owlvit.py::OwlViTProcessorTest::test_processor_with_nested_text_list
FAILED tests/models/owlvit/test_processor_owlvit.py::OwlViTProcessorTest::test_processor_with_text_list
3 failed, 125 passed, 81 skipped, 13 warnings in 18.73s
E   AttributeError: 'OwlViTFeatureExtractionTester' object has no attribute '_testMethodName'
```

**assistant:** Three processor tests fail. I'll check whether they fail on the original code too:

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; ../bin/envrun 'python -m pytest tests/models/owlvit/test_processor_owlvit.py -q 2>&1 | grep -E "^E |FAILED" | head -8; git stash -q; python -m pytest tests/models/owlvit/test_processor_owlvit.py -q 2>&1 | tail -4; git stash pop -q'
```

tool result:

```
E               huggingface_hub.utils._errors.LocalEntryNotFoundError: Cannot find the requested files in the disk cache and outgoing traffic has been disabled. To enable hf.co look-ups and downloads online, set 'local_files_only' to False.
E           OSError: We couldn't connect to 'https://huggingface.co' to load this file, couldn't find it in the cached files and it looks like google/owlvit-base-patch32 is not the path to a directory containing a file named preprocessor_config.json.
E           Checkout your internet connection or see how to run the library in offline mode at 'https://huggingface.co/docs/transformers/installation#offline-mode'.
E               huggingface_hub.utils._errors.LocalEntryNotFoundError: Cannot find the requested files in the disk cache and outgoing traffic has been disabled. To enable hf.co look-ups and downloads online, set 'local_files_only' to False.
E           OSError: We couldn't connect to 'https://huggingface.co' to load this file, couldn't find it in the cached files and it looks like google/owlvit-base-patch32 is not the path to a directory containing a file named preprocessor_config.json.
E           Checkout your internet connection or see how to run the library in offline mode at 'https://huggingface.co/docs/transformers/installation#offline-mode'.
E               huggingface_hub.utils._errors.LocalEntryNotFoundError: Cannot find the requested files in the disk cache and outgoing traffic has been disabled. To enable hf.co look-ups and downloads online, set 'local_files_only' to False.
E           OSError: We couldn't connect to 'https://huggingface.co' to load this file, couldn't find it in the cached files and it looks like google/owlvit-base-patch32 is not the path to a directory containing a file named preprocessor_config.json.
FAILED tests/models/owlvit/test_processor_owlvit.py::OwlViTProcessorTest::test_processor_case
FAILED tests/models/owlvit/test_processor_owlvit.py::OwlViTProcessorTest::test_processor_with_nested_text_list
FAILED tests/models/owlvit/test_processor_owlvit.py::OwlViTProcessorTest::test_processor_with_text_list
3 failed, 7 passed, 1 warning in 0.55s
```

**thinking:**

```
Those 3 failures are pre-existing, caused by lack of network access to download google/owlvit-base-patch32, not by my changes. I'll take one more look at the processor diff.


```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-20136/repo; git diff src/transformers/models/owlvit/processing_owlvit.py | sed -n 1,200p | grep '^[+-]' | head -60; git diff --stat
```

tool result:

```
--- a/src/transformers/models/owlvit/processing_owlvit.py
+++ b/src/transformers/models/owlvit/processing_owlvit.py
-    def __call__(self, text=None, images=None, padding="max_length", return_tensors="np", **kwargs):
+    def __call__(self, text=None, images=None, query_images=None, padding="max_length", return_tensors="np", **kwargs):
-        Main method to prepare for the model one or several text(s) and image(s). This method forwards the `text` and
+        Main method to prepare for the model one or several text(s), query image(s) and image(s). This method forwards
+        the `text` and
+            query_images (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `List[PIL.Image.Image]`, `List[np.ndarray]`,
+            `List[torch.Tensor]`):
+                The query image or batch of query images to be prepared for image-guided object detection. Each query
+                image is used to search for similar objects in the corresponding target image (`images`). Each image
+                can be a PIL image, NumPy array or PyTorch tensor.
+            - **query_pixel_values** -- Pixel values of the query images to be fed to a model. Returned when
+              `query_images` is not `None`.
-        if text is None and images is None:
-            raise ValueError("You have to specify at least one text or image. Both cannot be none.")
+        if text is None and query_images is None and images is None:
+            raise ValueError(
+                "You have to specify at least one text or query image or image. All three cannot be none."
+            )
+        if text is not None and query_images is not None:
+            raise ValueError("You have to specify either text or query_images, not both.")
+        if query_images is not None:
+            encoding = BatchEncoding()
+            query_pixel_values = self.feature_extractor(
+                query_images, return_tensors=return_tensors, **kwargs
+            ).pixel_values
+            encoding["query_pixel_values"] = query_pixel_values
+
-        if text is not None and images is not None:
+        if (text is not None or query_images is not None) and images is not None:
-        elif text is not None:
+        elif text is not None or query_images is not None:
+    def post_process_image_guided_detection(self, *args, **kwargs):
+        """
+        This method forwards all its arguments to [`OwlViTFeatureExtractor.post_process_image_guided_detection`].
+        Please refer to the docstring of this method for more information.
+        """
+        return self.feature_extractor.post_process_image_guided_detection(*args, **kwargs)
+
 docs/source/en/model_doc/owlvit.mdx                |   5 +-
 .../models/owlvit/feature_extraction_owlvit.py     | 114 +++++++
 src/transformers/models/owlvit/modeling_owlvit.py  | 369 +++++++++++++++++++--
 .../models/owlvit/processing_owlvit.py             |  38 ++-
 4 files changed, 494 insertions(+), 32 deletions(-)
```

**assistant:** OWL-ViT can now do one-shot, image-guided detection: you pass an image of the object you're looking for instead of text queries. On a tiny randomly initialized model, the processor and `image_guided_detection` give the expected output shapes and post-processing returns one result per image. I couldn't run it with the real pretrained weights because the container has no network access.

```python
inputs = processor(images=image, query_images=query_image, return_tensors="pt")
outputs = model.image_guided_detection(**inputs)
results = processor.post_process_image_guided_detection(outputs, threshold=0.6, nms_threshold=0.3, target_sizes=target_sizes)
```

**Changes, all in `src/transformers/models/owlvit/`:**

- **Processor (`processing_owlvit.py`):** `__call__` accepts a new `query_images` argument and returns `query_pixel_values` alongside `pixel_values`. It raises an error if no input is given, or if both `text` and `query_images` are given. There's also a new `post_process_image_guided_detection` method that passes through to the feature extractor.
- **Model (`modeling_owlvit.py`):**
  - New `OwlViTForObjectDetection.image_guided_detection(pixel_values, query_pixel_values, ...)`, which returns a new `OwlViTImageGuidedObjectDetectionOutput`.
  - To build the query from the query image, it predicts boxes on that image and keeps those within 80% of the best overlap with the whole image. Of those, it uses the embedding that differs most from the image's average as the query. This follows the original OWL-ViT method.
  - The class prediction head now works without queries.
  - Box-overlap helpers were copied from DETR.
  - The image-embedding code is shared between text and image queries, so the existing text-query `forward` behaves the same.
- **Feature extractor (`feature_extraction_owlvit.py`):** new `post_process_image_guided_detection`, which applies a score threshold and removes overlapping duplicate boxes. It always returns one result per image, with an empty result when nothing passes the threshold. `target_sizes` is optional, and `labels` is `None` because there's only one query.
- **Docs:** `owlvit.mdx` now mentions image-guided detection and lists the new methods.

**Tests:** the modeling and processor tests give 125 passed, 81 skipped and 3 failed. The 3 failures try to download `google/owlvit-base-patch32`, which needs network access, and they fail the same way on the original code. `check_copies` and `black` pass. Two problems also happen without my changes:

- `test_feature_extraction_owlvit.py` won't load: pytest tries to collect a helper class as a test.
- `utils/check_repo.py` crashes on a `pyarrow` import error.

I deleted my reproduction script. There's an untracked `Dockerfile` at the repo root that I didn't create, so I left it alone.

_session end: success, turns 22, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 3.36 s: python -c " from transformers import OwlViTForObjectDetection print(hasattr(OwlViTForObjectDetection, \"image_guided_detection\")) import inspect; from transformers import OwlViTProcessor; print(inspect.signature(OwlViTProcessor.__call__)) "
- `rc=0` 2.95 s: python repro_owlvit.py
- `rc=0` 18.28 s: python utils/check_copies.py; python utils/check_repo.py 2>&1 | tail -3; black --check src/transformers/models/owlvit; flake8 src/transformers/models/owlvit; python -m pytest tests/models/owlvit -q -x 2>&1 | tail -3
- `rc=0` 8.09 s: black --diff -q src/transformers/models/owlvit/modeling_owlvit.py; python -m pytest tests/models/owlvit -q 2>&1 | tail -5; git stash -q; python -m pytest tests/models/owlvit -q 2>&1 | tail -2; git stash pop -q; git status --short
- `rc=0` 24.56 s: black -q src/transformers/models/owlvit; python -m pytest tests/models/owlvit/test_modeling_owlvit.py tests/models/owlvit/test_processor_owlvit.py -q 2>&1 | tail -3; python -m pytest tests/models/owlvit/test_feature_extraction_owlvit.py -q 2>&1 | grep -m3 Error
- `rc=0` 6.33 s: python -m pytest tests/models/owlvit/test_processor_owlvit.py -q 2>&1 | grep -E "^E |FAILED" | head -8; git stash -q; python -m pytest tests/models/owlvit/test_processor_owlvit.py -q 2>&1 | tail -4; git stash pop -q
