# Instance: huggingface__transformers-15843

- Final resolved (evaluator, logs/huggingface__transformers-15843_result.json): False
- Run state: DONE
- One attempt. Duration 149.9 s, turns 14, actor cost $0.6174846, container commands 6
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/huggingface__transformers-15843/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-15843/repo. Consider the following issue description:

<issue_description>
Timestamps in AutomaticSpeechRecognitionPipeline not aligned in sample space
## Environment info
<!-- You can run the command `transformers-cli env` and copy-and-paste its output below.
     Don't forget to fill out the missing fields in that output! -->

- `transformers` version: 4.17.0.dev0
- Platform: Linux-5.10.98-1-MANJARO-x86_64-with-glibc2.33
- Python version: 3.9.8
- PyTorch version (GPU?): 1.10.2+cpu (False)
- Tensorflow version (GPU?): 2.8.0 (False)
- Flax version (CPU?/GPU?/TPU?): 0.4.0 (cpu)
- Jax version: 0.3.1
- JaxLib version: 0.3.0
- Using GPU in script?: No
- Using distributed or parallel set-up in script?: No

### Who can help
@Narsil
<!-- Your issue will be replied to more quickly if you can figure out the right person to tag with @
 If you know how to use git blame, that is the easiest way, otherwise, here is a rough guide of **who to tag**.
 Please tag fewer than 3 people.

Models:

- ALBERT, BERT, XLM, DeBERTa, DeBERTa-v2, ELECTRA, MobileBert, SqueezeBert: @LysandreJik
- T5, BART, Marian, Pegasus, EncoderDecoder: @patrickvonplaten
- Blenderbot, MBART: @patil-suraj
- Longformer, Reformer, TransfoXL, XLNet, FNet, BigBird: @patrickvonplaten
- FSMT: @stas00
- Funnel: @sgugger
- GPT-2, GPT: @patrickvonplaten, @LysandreJik
- RAG, DPR: @patrickvonplaten, @lhoestq
- TensorFlow: @Rocketknight1
- JAX/Flax: @patil-suraj
- TAPAS, LayoutLM, LayoutLMv2, LUKE, ViT, BEiT, DEiT, DETR, CANINE: @NielsRogge
- GPT-Neo, GPT-J, CLIP: @patil-suraj
- Wav2Vec2, HuBERT, SpeechEncoderDecoder, UniSpeech, UniSpeechSAT, SEW, SEW-D, Speech2Text: @patrickvonplaten, @anton-l

If the model isn't in the list, ping @LysandreJik who will redirect you to the correct contributor.

Library:

- Benchmarks: @patrickvonplaten
- Deepspeed: @stas00
- Ray/raytune: @richardliaw, @amogkam
- Text generation: @patrickvonplaten @narsil
- Tokenizers: @SaulLu
- Trainer: @sgugger
- Pipelines: @Narsil
- Speech: @patrickvonplaten, @anton-l
- Vision: @NielsRogge, @sgugger

Documentation: @sgugger

Model hub:

- for issues with a model, report at https://discuss.huggingface.co/ and tag the model's creator.

HF projects:

- datasets: [different repo](https://github.com/huggingface/datasets)
- rust tokenizers: [different repo](https://github.com/huggingface/tokenizers)

Examples:

- maintained examples (not research project or legacy): @sgugger, @patil-suraj

For research projetcs, please ping the contributor directly. For example, on the following projects:

- research_projects/bert-loses-patience: @JetRunner
- research_projects/distillation: @VictorSanh

 -->

## Issue

Generating timestamps in the `AutomaticSpeechRecognitionPipeline` does not match the timestamps generated from `Wav2Vec2CTCTokenizer.decode()`. The timestamps from the pipeline are exceeding the duration of the audio signal because of the strides.

## Expected behavior

Generating timestamps using the pipeline gives the following prediction IDs and offsets:

```python
pred_ids=array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 12, 14, 14,  0,  0,
        0, 22, 11,  0,  7,  4, 15, 16,  0,  0,  4, 17,  5,  7,  7,  4,  4,
       14, 14, 18, 18, 15,  4,  4,  0,  7,  5,  0,  0, 13,  0,  9,  0,  0,
        0,  8,  0, 11, 11,  0,  0,  0, 27,  4,  4,  0, 23,  0, 16,  0,  5,
        7,  7,  0, 25, 25,  0,  0, 22,  7,  7, 11,  0,  0,  0, 10, 10,  0,
        0,  8,  0,  5,  5,  0,  0, 19, 19,  0,  4,  4,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  6,  4,  4,  0, 25,  0,
       14, 14, 16,  0,  0,  0,  0, 10,  9,  9,  0,  0,  0,  0, 25,  0,  0,
        0,  0,  0, 26, 26, 16, 12, 12,  0,  0,  0, 19,  0,  5,  0,  8,  8,
        4,  4, 27,  0, 16,  0,  0,  4,  4,  0,  3,  3,  0,  0,  0,  0,  0,
        0,  0,  0,  4,  4, 17, 11, 11, 13,  0, 13, 11, 14, 16, 16,  0,  6,
        5,  6,  6,  4,  0,  5,  5, 16, 16,  0,  0,  7, 14,  0,  0,  4,  4,
       12,  5,  0,  0,  0, 26,  0, 13, 14,  0,  0,  0,  0, 23,  0,  0, 21,
       11, 11, 11,  0,  5,  5,  5,  7,  7,  0,  8,  0,  4,  4,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0, 12, 21, 11, 11, 11,  0,  4,  4,  0,  0, 12, 11, 11,  0,  0,  0,
        0,  0,  7,  7,  5,  5,  0,  0,  0,  0, 23,  0,  0,  8,  0,  0,  4,
        4,  0,  0,  0,  0, 12,  5,  0,  0,  4,  4, 10,  0,  0, 24, 14, 14,
        0,  7,  7,  0,  8,  8, 10, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0, 26,  0,  5,  0,  0,  0, 20,  0,  5,  0,
        0,  5,  5,  0,  0, 19, 16, 16,  0,  6,  6, 19,  0,  5,  6,  6,  4,
        4,  0, 14, 18, 18, 15,  4,  4,  0,  0, 25, 25,  0,  5,  4,  4, 19,
       16,  8,  8,  0,  8,  8,  4,  4,  0, 23, 23,  0, 14, 17, 17,  0,  0,
       17,  0,  5,  6,  6,  4,  4])
       
decoded['word_offsets']=[{'word': 'dofir', 'start_offset': 12, 'end_offset': 22}, {'word': 'hu', 'start_offset': 23, 'end_offset': 25}, {'word': 'mer', 'start_offset': 28, 'end_offset': 32
}, {'word': 'och', 'start_offset': 34, 'end_offset': 39}, {'word': 'relativ', 'start_offset': 42, 'end_offset': 60}, {'word': 'kuerzfristeg', 'start_offset': 63, 'end_offset': 94}, {'word'
: 'en', 'start_offset': 128, 'end_offset': 131}, {'word': 'zousazbudget', 'start_offset': 134, 'end_offset': 170}, {'word': 'vu', 'start_offset': 172, 'end_offset': 175}, {'word': '<unk>',
 'start_offset': 180, 'end_offset': 182}, {'word': 'milliounen', 'start_offset': 192, 'end_offset': 207}, {'word': 'euro', 'start_offset': 209, 'end_offset': 217}, {'word': 'deblokéiert', 
'start_offset': 221, 'end_offset': 249}, {'word': 'déi', 'start_offset': 273, 'end_offset': 278}, {'word': 'direkt', 'start_offset': 283, 'end_offset': 303}, {'word': 'de', 'start_offset': 311, 'end_offset': 313}, 
{'word': 'sportsbeweegungen', 'start_offset': 317, 'end_offset': 492}, {'word': 'och', 'start_offset': 495, 'end_offset': 499}, {'word': 'ze', 'start_offset': 503, 'end_offset': 507}, {'word': 'gutt', 'start_offset': 509, 'end_offset': 516}, 
{'word': 'kommen', 'start_offset': 519, 'end_offset': 532}]
```

However, the following is computed using `Wav2Vec2CTCTokenizer.decode()` and these offsets are expected:

```python
pred_ids=tensor([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 12, 14, 14,  0,  0,  0,
        22, 11,  0,  7,  4, 15, 16,  0,  0,  4, 17,  5,  7,  7,  4,  0, 14, 14,
        18, 18, 15,  4,  4,  0,  7,  5,  0,  0, 13,  0,  9,  0,  0,  0,  8,  0,
        11, 11,  0,  0,  0, 27,  4,  4,  0, 23,  0, 16,  0,  5,  7,  7,  0, 25,
        25,  0,  0, 22,  7,  7, 11,  0,  0,  0, 10, 10,  0,  0,  8,  0,  5,  5,
         0,  0, 19, 19,  0,  4,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  5,  0,  6,  4,  4,  0, 25,  0, 14, 14, 16,  0,  0,  0,  0, 10,
         9,  9,  0,  0,  0,  0, 25,  0,  0,  0,  0,  0, 26, 26, 16, 12, 12,  0,
         0,  0, 19,  0,  5,  0,  8,  8,  4,  4, 27,  0, 16,  0,  0,  4,  4,  0,
         3,  3,  0,  0,  0,  0,  0,  0,  0,  0,  4,  4, 17, 11, 11, 13,  0, 13,
        11, 14, 16, 16,  0,  6,  5,  6,  6,  4,  0,  5,  5, 16, 16,  0,  0,  7,
        14,  0,  0,  4,  4, 12,  5,  0,  0,  0, 26,  0, 13, 14,  0,  0,  0,  0,
        23,  0,  0, 21, 11, 11, 11,  0,  5,  5,  5,  7,  7,  0,  8,  0,  4,  4,
         0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0, 12, 21, 11, 11, 11,  0,  4,  4,  0,  0, 12, 11, 11,  0,  0,
         0,  0,  0,  7,  7,  5,  5,  0,  0,  0,  0, 23,  0,  0,  8,  0,  0,  4,
         4,  0,  0,  0,  0, 12,  5,  0,  0,  4,  4, 10,  0,  0, 24, 14, 14,  0,
         7,  7,  0,  8,  8, 10, 10,  0,  0,  0, 26,  5,  5,  0,  0,  0, 20,  5,
         0,  0,  0,  5,  0,  0, 19,  0, 16, 16,  6,  6, 19, 19,  5,  5,  6,  6,
         4,  0, 14,  0, 18, 15, 15,  4,  4,  0,  0, 25,  0, 16,  0,  4,  4, 19,
        16,  8,  0,  0,  8,  0,  4,  0,  0, 23,  0, 14,  0, 17,  0,  0,  0, 17,
         5,  5,  6,  6,  4,  4])
         
word_offsets=[{'word': 'dofir', 'start_offset': 12, 'end_offset': 22}, {'word': 'hu', 'start_offset': 23, 'end_offset': 25}, {'word': 'mer', 'start_offset': 28, 'end_offset': 32},  {'word': 'och', 'start_offset': 34, 'end_offset': 39}, {'word': 'relativ', 'start_offset': 42, 'end_offset': 60}, {'word': 'kuerzfristeg', 'start_offset': 63, 'end_offset': 94},  {'word': 'en', 'start_offset': 128, 'end_offset': 131}, {'word': 'zousazbudget', 'start_offset': 134, 'end_offset': 170},  {'word': 'vu', 'start_offset': 172, 'end_offset': 175}, {'word': '<unk>', 'start_offset': 180, 'end_offset': 182}, {'word': 'milliounen', 'start_offset': 192, 'end_offset': 207},  {'word': 'euro', 'start_offset': 209, 'end_offset': 217}, {'word': 'deblokéiert', 'start_offset': 221, 'end_offset': 249},  {'word': 'déi', 'start_offset': 273, 'end_offset': 278}, {'word': 'direkt', 'start_offset': 283, 'end_offset': 303},  {'word': 'de', 'start_offset': 311, 'end_offset': 313}, {'word': 'sportsbeweegungen', 'start_offset': 317, 'end_offset': 360}, {'word': 'och', 'start_offset': 362, 'end_offset': 367},  {'word': 'zu', 'start_offset': 371, 'end_offset': 374}, {'word': 'gutt', 'start_offset': 377, 'end_offset': 383},  {'word': 'kommen', 'start_offset': 387, 'end_offset': 400}]
```

## Potential Fix

A fix could be removing the strides instead of filling them with `first_letter` and `last_letter` in `apply_stride()`:

```python
def apply_stride(tokens, stride):

    input_n, left, right = rescale_stride(tokens, stride)[0]
    left_token = left
    right_token = input_n - right

    return tokens[:, left_token:right_token]
```

<!-- A clear and concise description of what you would expect to happen. -->


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-15843/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-15843/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-15843/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-15843/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cat src/transformers/pipelines/automatic_speech_recognition.py
```

tool result:

```
# Copyright 2021 The HuggingFace Team. All rights reserved.
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
from collections import defaultdict
from typing import TYPE_CHECKING, Dict, Optional, Union

import numpy as np

from ..file_utils import is_torch_available
from ..utils import logging
from .audio_utils import ffmpeg_read
from .base import ChunkPipeline


if TYPE_CHECKING:
    from ...feature_extraction_sequence_utils import SequenceFeatureExtractor

logger = logging.get_logger(__name__)

if is_torch_available():
    from ..models.auto.modeling_auto import MODEL_FOR_CTC_MAPPING, MODEL_FOR_SPEECH_SEQ_2_SEQ_MAPPING


def rescale_stride(tokens_or_logits, stride):
    """
    Rescales the stride values from audio space to tokens/logits space.

    (160_000, 16_000, 16_000) -> (2000, 200, 200) for instance.
    """
    # Shape is [B, SEQ] for tokens
    # [B, SEQ, V] for logits

    max_token_n = tokens_or_logits.shape[1]
    max_input_n = max(input_n for input_n, _, _ in stride)
    ratio = max_token_n / max_input_n
    new_strides = []
    for input_n, left, right in stride:
        token_n = int(round(input_n * ratio))
        left = int(round(left / input_n * token_n))
        right = int(round(right / input_n * token_n))
        new_stride = (token_n, left, right)
        new_strides.append(new_stride)

    return new_strides


def apply_stride(tokens, stride):
    new_stride = rescale_stride(tokens, stride)
    for i, (input_n, left, right) in enumerate(new_stride):
        left_token = left
        right_token = input_n - right
        # This is CTC to preseve decoding, we need to duplicate
        # next letter, and last letter

        first_letter = tokens[i, left_token]
        tokens[i, :left_token] = first_letter

        last_letter = tokens[i, right_token - 1]
        tokens[i, right_token:] = last_letter


def chunk_iter(inputs, feature_extractor, chunk_len, stride_left, stride_right):
    inputs_len = inputs.shape[0]
    step = chunk_len - stride_left - stride_right
    for i in range(0, inputs_len, step):
        # add start and end paddings to the chunk
        chunk = inputs[i : i + chunk_len]
        processed = feature_extractor(chunk, sampling_rate=feature_extractor.sampling_rate, return_tensors="pt")
        _stride_left = 0 if i == 0 else stride_left
        is_last = i + step >= inputs_len
        _stride_right = 0 if is_last else stride_right

        if chunk.shape[0] > _stride_left:
            yield {"is_last": is_last, "stride": (chunk.shape[0], _stride_left, _stride_right), **processed}


class AutomaticSpeechRecognitionPipeline(ChunkPipeline):
    """
    Pipeline that aims at extracting spoken text contained within some audio.

    The input can be either a raw waveform or a audio file. In case of the audio file, ffmpeg should be installed for
    to support multiple audio formats
    """

    def __init__(self, feature_extractor: Union["SequenceFeatureExtractor", str], *args, **kwargs):
        """
        Arguments:
            model ([`PreTrainedModel`] or [`TFPreTrainedModel`]):
                The model that will be used by the pipeline to make predictions. This needs to be a model inheriting
                from [`PreTrainedModel`] for PyTorch and [`TFPreTrainedModel`] for TensorFlow.
            tokenizer ([`PreTrainedTokenizer`]):
                The tokenizer that will be used by the pipeline to encode data for the model. This object inherits from
                [`PreTrainedTokenizer`].
            feature_extractor ([`SequenceFeatureExtractor`]):
                The feature extractor that will be used by the pipeline to encode waveform for the model.
            chunk_length_s (`float`, *optional*, defaults to 0):
                The input length for in each chunk. If `0` then chunking is disabled (default). Only available for CTC
                models.
            stride_length_s (`float`, *optional*, defaults to `chunk_length_s / 6`):
                The length of stride on the left and right of each chunk. Used only with `chunk_length_s > 0`. This
                enables the model to *see* more context and infer letters better than without this context but the
                pipeline discards the stride bits at the end to make the final reconstitution as perfect as possible.
            framework (`str`, *optional*):
                The framework to use, either `"pt"` for PyTorch or `"tf"` for TensorFlow. The specified framework must
                be installed.

                If no framework is specified, will default to the one currently installed. If no framework is specified
                and both frameworks are installed, will default to the framework of the `model`, or to PyTorch if no
                model is provided.
            device (`int`, *optional*, defaults to -1):
                Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the
                model on the associated CUDA device id.
        """

        super().__init__(*args, **kwargs)
        self.feature_extractor = feature_extractor

        if self.model.__class__ in MODEL_FOR_SPEECH_SEQ_2_SEQ_MAPPING.values():
            self.type = "seq2seq"
        elif (
            feature_extractor._processor_class
            and feature_extractor._processor_class.endswith("WithLM")
            and kwargs.get("decoder", None) is not None
        ):
            self.decoder = kwargs["decoder"]
            self.type = "ctc_with_lm"
  
[... 13732 more characters not shown]
```

**tool call: Bash**

```bash
grep -n "rescale_stride\|apply_stride\|stride\|import" tests/test_pipelines_automatic_speech_recognition.py | head -60
```

tool result:

```
grep: tests/test_pipelines_automatic_speech_recognition.py: No such file or directory
```

**tool call: Bash**

```bash
f=$(git ls-files | grep -i "automatic_speech" | grep test); echo $f; grep -n "rescale_stride\|apply_stride\|stride\|^from\|^import" $f | head -60
```

tool result:

```
tests/pipelines/test_pipelines_automatic_speech_recognition.py
15:import unittest
17:import numpy as np
18:import pytest
19:from datasets import load_dataset
21:from huggingface_hub import snapshot_download
22:from transformers import (
30:from transformers.pipelines import AutomaticSpeechRecognitionPipeline, pipeline
31:from transformers.pipelines.audio_utils import chunk_bytes_iter
32:from transformers.pipelines.automatic_speech_recognition import apply_stride, chunk_iter
33:from transformers.testing_utils import (
44:from .test_pipelines_common import ANY, PipelineTestCaseMeta
86:        audio = {"raw": audio, "stride": (0, 4000), "sampling_rate": speech_recognizer.feature_extractor.sampling_rate}
593:        self.assertEqual([o["stride"] for o in outs], [(100, 0, 0)])
597:        # two chunks no stride
600:        self.assertEqual([o["stride"] for o in outs], [(50, 0, 0), (50, 0, 0)])
607:        self.assertEqual([o["stride"] for o in outs], [(80, 0, 0), (20, 0, 0)])
612:    def test_chunk_iterator_stride(self):
621:        self.assertEqual([o["stride"] for o in outs], [(100, 0, 10), (30, 20, 0)])
627:        self.assertEqual([o["stride"] for o in outs], [(80, 0, 10), (50, 20, 0)])
633:        self.assertEqual([o["stride"] for o in outs], [(90, 0, 0), (30, 20, 0)])
642:        self.assertEqual([o["stride"] for o in outs], [(30, 0, 5), (30, 5, 5), (30, 5, 5), (30, 5, 5), (20, 5, 0)])
657:    def test_stride(self):
663:        output = speech_recognizer({"raw": waveform, "stride": (0, 0), "sampling_rate": 16_000})
667:        output = speech_recognizer({"raw": waveform, "stride": (5000, 5000), "sampling_rate": 16_000})
671:        output = speech_recognizer({"raw": waveform, "stride": (0, 9000), "sampling_rate": 16_000})
675:        output = speech_recognizer({"raw": waveform, "stride": (1000, 8000), "sampling_rate": 16_000})
681:    def test_apply_stride(self):
684:        # No stride
685:        apply_stride(tokens, [(100, 0, 0), (100, 0, 0)])
690:    def test_apply_stride_real_stride(self):
693:        apply_stride(tokens, [(100, 20, 0), (100, 0, 20)])
698:        apply_stride(tokens, [(100, 15, 0), (100, 0, 15)])
701:        # No stride rounded
703:        apply_stride(tokens, [(100, 5, 0), (100, 0, 5)])
706:    def test_apply_stride_with_padding(self):
709:        apply_stride(tokens, [(100, 20, 0), (60, 0, 20)])
737:        iter_ = iter(chunk_bytes_iter(bytes_iter(chunk_size=3, chunks=2), 10, stride=(0, 0)))
738:        self.assertEqual(next(iter_), {"raw": b"\x00\x01\x02\x03\x04\x05", "stride": (0, 0)})
743:        iter_ = iter(chunk_bytes_iter(bytes_iter(chunk_size=3, chunks=2), 3, stride=(0, 0)))
744:        self.assertEqual(next(iter_), {"raw": b"\x00\x01\x02", "stride": (0, 0)})
745:        self.assertEqual(next(iter_), {"raw": b"\x03\x04\x05", "stride": (0, 0)})
749:    def test_chunk_bytes_iter_stride(self):
750:        iter_ = iter(chunk_bytes_iter(bytes_iter(chunk_size=3, chunks=2), 3, stride=(1, 1)))
751:        self.assertEqual(next(iter_), {"raw": b"\x00\x01\x02", "stride": (0, 1)})
752:        self.assertEqual(next(iter_), {"raw": b"\x01\x02\x03", "stride": (1, 1)})
753:        self.assertEqual(next(iter_), {"raw": b"\x02\x03\x04", "stride": (1, 1)})
755:        self.assertEqual(next(iter_), {"raw": b"\x03\x04\x05", "stride": (1, 1)})
756:        self.assertEqual(next(iter_), {"raw": b"\x04\x05", "stride": (1, 0)})
760:    def test_chunk_bytes_iter_stride_stream(self):
761:        iter_ = iter(chunk_bytes_iter(bytes_iter(chunk_size=3, chunks=2), 5, stride=(1, 1), stream=True))
762:        self.assertEqual(next(iter_), {"raw": b"\x00\x01\x02", "stride": (0, 0), "partial": True})
763:        self.assertEqual(next(iter_), {"raw": b"\x00\x01\x02\x03\x04", "stride": (0, 1), "partial": False})
764:        self.assertEqual(next(iter_), {"raw": b"\x03\x04\x05", "stride": (1, 0), "partial": False})
768:        iter_ = iter(chunk_bytes_iter(bytes_iter(chunk_size=3, chunks=3), 5, stride=(1, 1), stream=True))
769:        self.assertEqual(next(iter_), {"raw": b"\x00\x01\x02", "stride": (0, 0), "partial": True})
770:        self.assertEqual(next(iter_), {"raw": b"\x00\x01\x02\x03\x04", "stride": (0, 1), "partial": False})
771:        self.assertEqual(next(iter_), {"raw": b"\x03\x04\x05\x06\x07", "stride": (1, 1), "partial": False})
772:        self.assertEqual(next(iter_), {"raw": b"\x06\x07\x08", "stride": (1, 0), "partial": False})
776:        iter_ = iter(chunk_bytes_iter(bytes_iter(chunk_size=3, chunks=3), 10, stride=(1, 1), stream=True))
777:        self.assertEqual(next(iter_), {"raw": b"\x00\x01\x02", "stride": (0, 0), "partial": True})
```

**tool call: Bash**

```bash
cd tests/pipelines; sed -n 650,720p test_pipelines_automatic_speech_recognition.py; grep -n "return_timestamps\|chunk_length_s" test_pipelines_automatic_speech_recognition.py; git log --oneline -2
```

tool result:

```
        self.assertEqual(nested_simplify(input_values[:, 40:70]), nested_simplify(outs[2]["input_values"]))
        # (65, 85)
        self.assertEqual(nested_simplify(input_values[:, 60:90]), nested_simplify(outs[3]["input_values"]))
        # (85, 100)
        self.assertEqual(nested_simplify(input_values[:, 80:100]), nested_simplify(outs[4]["input_values"]))

    @require_torch
    def test_stride(self):
        speech_recognizer = pipeline(
            task="automatic-speech-recognition",
            model="hf-internal-testing/tiny-random-wav2vec2",
        )
        waveform = np.tile(np.arange(1000, dtype=np.float32), 10)
        output = speech_recognizer({"raw": waveform, "stride": (0, 0), "sampling_rate": 16_000})
        self.assertEqual(output, {"text": "OB XB  B EB BB  B EB B OB X"})

        # 0 effective ids Just take the middle one
        output = speech_recognizer({"raw": waveform, "stride": (5000, 5000), "sampling_rate": 16_000})
        self.assertEqual(output, {"text": "B"})

        # Only 1 arange.
        output = speech_recognizer({"raw": waveform, "stride": (0, 9000), "sampling_rate": 16_000})
        self.assertEqual(output, {"text": "O"})

        # 2nd arange
        output = speech_recognizer({"raw": waveform, "stride": (1000, 8000), "sampling_rate": 16_000})
        self.assertEqual(output, {"text": "B XB"})


@require_torch
class ApplyStrideTest(unittest.TestCase):
    def test_apply_stride(self):
        tokens = torch.arange(10).long().reshape((2, 5))

        # No stride
        apply_stride(tokens, [(100, 0, 0), (100, 0, 0)])

        expected = torch.arange(10).long().reshape((2, 5))
        self.assertEqual(expected.tolist(), tokens.tolist())

    def test_apply_stride_real_stride(self):
        # Stride aligned
        tokens = torch.arange(10).long().reshape((2, 5))
        apply_stride(tokens, [(100, 20, 0), (100, 0, 20)])
        self.assertEqual([[1, 1, 2, 3, 4], [5, 6, 7, 8, 8]], tokens.tolist())

        # Stride rounded
        tokens = torch.arange(10).long().reshape((2, 5))
        apply_stride(tokens, [(100, 15, 0), (100, 0, 15)])
        self.assertEqual([[1, 1, 2, 3, 4], [5, 6, 7, 8, 8]], tokens.tolist())

        # No stride rounded
        tokens = torch.arange(10).long().reshape((2, 5))
        apply_stride(tokens, [(100, 5, 0), (100, 0, 5)])
        self.assertEqual([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]], tokens.tolist())

    def test_apply_stride_with_padding(self):
        # Stride aligned
        tokens = torch.arange(10).long().reshape((2, 5))
        apply_stride(tokens, [(100, 20, 0), (60, 0, 20)])
        self.assertEqual([[1, 1, 2, 3, 4], [5, 6, 6, 6, 6]], tokens.tolist())


def require_ffmpeg(test_case):
    """
    Decorator marking a test that requires FFmpeg.

    These tests are skipped when FFmpeg isn't installed.

    """
    import subprocess
99:            outputs = speech_recognizer(audio, return_timestamps="char")
110:            outputs = speech_recognizer(audio, return_timestamps="word")
121:            # Non CTC models cannot use return_timestamps
123:                outputs = speech_recognizer(audio, return_timestamps="char")
345:            chunk_length_s=10.0,
358:    def test_return_timestamps_ctc_fast(self):
368:        output = speech_recognizer(audio, return_timestamps="char")
387:        output = speech_recognizer(audio, return_timestamps="word")
405:            chunk_length_s=10.0,
487:            chunk_length_s=10.0,
498:        output = speech_recognizer(audio, return_timestamps="char")
549:        output = speech_recognizer(audio, return_timestamps="word")
574:            chunk_length_s=10.0,
84eaa6acf Add TFConvNextModel (#15750)
0b5bf6abe Framework split model report (#15825)
```

**tool call: Bash**

```bash
cd tests/pipelines; sed -n 330,420p test_pipelines_automatic_speech_recognition.py; sed -n 480,600p test_pipelines_automatic_speech_recognition.py
```

tool result:

```
(eval):cd:1: no such file or directory: tests/pipelines
            tokenizer=AutoTokenizer.from_pretrained("patrickvonplaten/wav2vec2-2-bart-base"),
            framework="pt",
        )

        ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation").sort("id")
        filename = ds[40]["file"]

        output = speech_recognizer(filename)
        self.assertEqual(output, {"text": "a man said to the universe sir i exist"})

    @require_torch
    def test_chunking_fast(self):
        speech_recognizer = pipeline(
            task="automatic-speech-recognition",
            model="hf-internal-testing/tiny-random-wav2vec2",
            chunk_length_s=10.0,
        )

        ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation").sort("id")
        audio = ds[40]["audio"]["array"]

        n_repeats = 2
        audio_tiled = np.tile(audio, n_repeats)
        output = speech_recognizer([audio_tiled], batch_size=2)
        self.assertEqual(output, [{"text": ANY(str)}])
        self.assertEqual(output[0]["text"][:6], "ZBT ZC")

    @require_torch
    def test_return_timestamps_ctc_fast(self):
        speech_recognizer = pipeline(
            task="automatic-speech-recognition",
            model="hf-internal-testing/tiny-random-wav2vec2",
        )

        ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation").sort("id")
        # Take short audio to keep the test readable
        audio = ds[40]["audio"]["array"][:800]

        output = speech_recognizer(audio, return_timestamps="char")
        self.assertEqual(
            output,
            {
                "text": "ZBT ZX G",
                "chunks": [
                    {"text": " ", "timestamp": (0.0, 0.012)},
                    {"text": "Z", "timestamp": (0.012, 0.016)},
                    {"text": "B", "timestamp": (0.016, 0.02)},
                    {"text": "T", "timestamp": (0.02, 0.024)},
                    {"text": " ", "timestamp": (0.024, 0.028)},
                    {"text": "Z", "timestamp": (0.028, 0.032)},
                    {"text": "X", "timestamp": (0.032, 0.036)},
                    {"text": " ", "timestamp": (0.036, 0.04)},
                    {"text": "G", "timestamp": (0.04, 0.044)},
                ],
            },
        )

        output = speech_recognizer(audio, return_timestamps="word")
        self.assertEqual(
            output,
            {
                "text": "ZBT ZX G",
                "chunks": [
                    {"text": "ZBT", "timestamp": (0.012, 0.024)},
                    {"text": "ZX", "timestamp": (0.028, 0.036)},
                    {"text": "G", "timestamp": (0.04, 0.044)},
                ],
            },
        )

    @require_torch
    @require_pyctcdecode
    def test_chunking_fast_with_lm(self):
        speech_recognizer = pipeline(
            model="hf-internal-testing/processor_with_lm",
            chunk_length_s=10.0,
        )

        ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation").sort("id")
        audio = ds[40]["audio"]["array"]

        n_repeats = 2
        audio_tiled = np.tile(audio, n_repeats)
        # Batch_size = 1
        output1 = speech_recognizer([audio_tiled], batch_size=1)
        self.assertEqual(output1, [{"text": ANY(str)}])
        self.assertEqual(output1[0]["text"][:6], "<s> <s")

        # batch_size = 2
        output2 = speech_recognizer([audio_tiled], batch_size=2)
        self.assertEqual(output2, [{"text": ANY(str)}])
        feature_extractor = AutoFeatureExtractor.from_pretrained("facebook/wav2vec2-base-960h")
        speech_recognizer = pipeline(
            task="automatic-speech-recognition",
            model=model,
            tokenizer=tokenizer,
            feature_extractor=feature_extractor,
            framework="pt",
            chunk_length_s=10.0,
        )

        ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation").sort("id")
        audio = ds[40]["audio"]["array"]

        n_repeats = 10
        audio_tiled = np.tile(audio, n_repeats)
        output = speech_recognizer([audio_tiled], batch_size=2)
        self.assertEqual(output, [{"text": ("A MAN SAID TO THE UNIVERSE SIR I EXIST " * n_repeats).strip()}])

        output = speech_recognizer(audio, return_timestamps="char")
        self.assertEqual(audio.shape, (74_400,))
        self.assertEqual(speech_recognizer.feature_extractor.sampling_rate, 16_000)
        # The audio is 74_400 / 16_000 = 4.65s long.
        self.assertEqual(
            output,
            {
                "text": "A MAN SAID TO THE UNIVERSE SIR I EXIST",
                "chunks": [
                    {"text": "A", "timestamp": (0.6, 0.62)},
                    {"text": " ", "timestamp": (0.62, 0.66)},
                    {"text": "M", "timestamp": (0.68, 0.7)},
                    {"text": "A", "timestamp": (0.78, 0.8)},
                    {"text": "N", "timestamp": (0.84, 0.86)},
                    {"text": " ", "timestamp": (0.92, 0.98)},
                    {"text": "S", "timestamp": (1.06, 1.08)},
                    {"text": "A", "timestamp": (1.14, 1.16)},
                    {"text": "I", "timestamp": (1.16, 1.18)},
                    {"text": "D", "timestamp": (1.2, 1.24)},
                    {"text": " ", "timestamp": (1.24, 1.28)},
                    {"text": "T", "timestamp": (1.28, 1.32)},
                    {"text": "O", "timestamp": (1.34, 1.36)},
                    {"text": " ", "timestamp": (1.38, 1.42)},
                    {"text": "T", "timestamp": (1.42, 1.44)},
                    {"text": "H", "timestamp": (1.44, 1.46)},
                    {"text": "E", "timestamp": (1.46, 1.5)},
                    {"text": " ", "timestamp": (1.5, 1.56)},
                    {"text": "U", "timestamp": (1.58, 1.62)},
                    {"text": "N", "timestamp": (1.64, 1.68)},
      
[... 3494 more characters not shown]
```

**thinking:**

```
I found that `apply_stride` duplicates first/last letters into stride regions, causing offsets to overrun the audio length since the full token sequence is concatenated per chunk. I'll fix this by trimming stride regions in `postprocess` (matching how `ctc_with_lm` already handles logits), but first I'll check if the tests can run offline.


```

**tool call: Bash**

```bash
/work/huggingface__transformers-15843/bin/envrun 'HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m pytest tests/pipelines/test_pipelines_automatic_speech_recognition.py -x -q 2>&1 | tail -15'
```

tool result:

```
    imports = re.findall("^\s*import\s+(\S+)\s*$", content, flags=re.MULTILINE)

src/transformers/dynamic_module_utils.py:121
  /testbed/src/transformers/dynamic_module_utils.py:121: DeprecationWarning: invalid escape sequence '\s'
    imports += re.findall("^\s*from\s+(\S+)\s+import", content, flags=re.MULTILINE)

<frozen importlib._bootstrap>:241
  <frozen importlib._bootstrap>:241: DeprecationWarning: builtin type SwigPyPacked has no __module__ attribute

<frozen importlib._bootstrap>:241
  <frozen importlib._bootstrap>:241: DeprecationWarning: builtin type SwigPyObject has no __module__ attribute

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
3 passed, 30 skipped, 6 warnings in 1.69s
sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
```

**tool call: Bash**

```bash
/work/huggingface__transformers-15843/bin/envrun 'python -m pytest tests/pipelines/test_pipelines_automatic_speech_recognition.py -q -rs 2>&1 | grep -i skip | head; ls ~/.cache/huggingface 2>&1'
```

tool result:

```
Exit code 2
SKIPPED [1] tests/pipelines/test_pipelines_automatic_speech_recognition.py:586: test is pipeline test
SKIPPED [1] tests/pipelines/test_pipelines_automatic_speech_recognition.py:611: test is pipeline test
SKIPPED [1] tests/pipelines/test_pipelines_automatic_speech_recognition.py:475: test is pipeline test
SKIPPED [1] tests/pipelines/test_pipelines_automatic_speech_recognition.py:340: test is pipeline test
SKIPPED [1] tests/pipelines/test_pipelines_automatic_speech_recognition.py:400: test is pipeline test
SKIPPED [1] tests/pipelines/test_pipelines_automatic_speech_recognition.py:568: test is pipeline test
SKIPPED [1] tests/pipelines/test_pipelines_automatic_speech_recognition.py:160: test is pipeline test
SKIPPED [3] tests/pipelines/test_pipelines_common.py:142: test is pipeline test
SKIPPED [1] tests/pipelines/test_pipelines_automatic_speech_recognition.py:125: test is pipeline test
SKIPPED [1] tests/pipelines/test_pipelines_automatic_speech_recognition.py:357: test is pipeline test
ls: cannot access '/root/.cache/huggingface': No such file or directory
```

**assistant:** No models are cached and the container has no network, so the pipeline tests can't run here. I'll reproduce with a small, randomly initialized local Wav2Vec2 model instead. Now the fix:

**tool call: Bash**

```bash
cd /work/huggingface__transformers-15843/repo && python3 - <<'EOF'
p = "src/transformers/pipelines/automatic_speech_recognition.py"
s = open(p).read()
old_fwd = s[s.index('        elif self.type == "ctc_with_lm":\n            stride = model_inputs.pop'):s.index('        else:\n            logger.warning("This is an unknown class')]
new_fwd = '''        elif self.type in {"ctc", "ctc_with_lm"}:
            stride = model_inputs.pop("stride", None)
            # Consume values so we can let extra information flow freely through
            # the pipeline (important for `partial` in microphone)
            input_values = model_inputs.pop("input_values")
            attention_mask = model_inputs.pop("attention_mask", None)
            outputs = self.model(input_values=input_values, attention_mask=attention_mask)
            logits = outputs.logits

            if self.type == "ctc_with_lm":
                out = {"logits": logits}
            else:
                out = {"tokens": logits.argmax(dim=-1)}
            if stride is not None:
                # Send stride to `postprocess`.
                # it needs to be handled there where
                # the pieces are to be concatenated.
                if isinstance(stride, tuple):
                    out["stride"] = rescale_stride(logits, [stride])[0]
                else:
                    out["stride"] = rescale_stride(logits, stride)
'''
s = s.replace(old_fwd, new_fwd)

old_pp = s[s.index('        if self.type == "ctc_with_lm":\n            final_logits'):s.index('            if return_timestamps:\n')]
new_pp = '''        final_items = []
        key = "logits" if self.type == "ctc_with_lm" else "tokens"
        for outputs in model_outputs:
            items = outputs[key].numpy()
            stride = outputs.pop("stride", None)
            if stride is not None:
                total_n, left, right = stride
                # Total_n might be < logits.shape[1]
                # because of padding, that's why
                # we need to reconstruct this information
                # This won't work with left padding (which doesn't exist right now)
                right_n = total_n - right
                items = items[:, left:right_n]
            final_items.append(items)
        items = np.concatenate(final_items, axis=1)
        items = items.squeeze(0)
        if self.type == "ctc_with_lm":
            if decoder_kwargs is None:
                decoder_kwargs = {}
            text = self.decoder.decode_beams(items, **decoder_kwargs)[0][0]
        else:
            skip_special_tokens = self.type != "ctc"
            text = self.tokenizer.decode(items, skip_special_tokens=skip_special_tokens)

'''
s = s.replace(old_pp, new_pp)
s = s.replace('''                    decoded = self.tokenizer.decode(
                        tokens, skip_special_tokens=skip_special_tokens, output_char_offsets=True''', '''                    decoded = self.tokenizer.decode(
                        items, skip_special_tokens=skip_special_tokens, output_char_offsets=True''')
s = s.replace('''                    decoded = self.tokenizer.decode(
                        tokens, skip_special_tokens=skip_special_tokens, output_word_offsets=True''', '''                    decoded = self.tokenizer.decode(
                        items, skip_special_tokens=skip_special_tokens, output_word_offsets=True''')
open(p, "w").write(s)
EOF
git diff
```

tool result:

```
diff --git a/src/transformers/pipelines/automatic_speech_recognition.py b/src/transformers/pipelines/automatic_speech_recognition.py
index 3552a23ce..847afa9b5 100644
--- a/src/transformers/pipelines/automatic_speech_recognition.py
+++ b/src/transformers/pipelines/automatic_speech_recognition.py
@@ -300,13 +300,19 @@ class AutomaticSpeechRecognitionPipeline(ChunkPipeline):
                 attention_mask=attention_mask,
             )
             out = {"tokens": tokens}
-        elif self.type == "ctc_with_lm":
+        elif self.type in {"ctc", "ctc_with_lm"}:
             stride = model_inputs.pop("stride", None)
+            # Consume values so we can let extra information flow freely through
+            # the pipeline (important for `partial` in microphone)
             input_values = model_inputs.pop("input_values")
             attention_mask = model_inputs.pop("attention_mask", None)
             outputs = self.model(input_values=input_values, attention_mask=attention_mask)
             logits = outputs.logits
-            out = {"logits": logits}
+
+            if self.type == "ctc_with_lm":
+                out = {"logits": logits}
+            else:
+                out = {"tokens": logits.argmax(dim=-1)}
             if stride is not None:
                 # Send stride to `postprocess`.
                 # it needs to be handled there where
@@ -315,20 +321,6 @@ class AutomaticSpeechRecognitionPipeline(ChunkPipeline):
                     out["stride"] = rescale_stride(logits, [stride])[0]
                 else:
                     out["stride"] = rescale_stride(logits, stride)
-        elif self.type == "ctc":
-            stride = model_inputs.pop("stride", None)
-            # Consume values so we can let extra information flow freely through
-            # the pipeline (important for `partial` in microphone)
-            input_values = model_inputs.pop("input_values")
-            attention_mask = model_inputs.pop("attention_mask", None)
-            outputs = self.model(input_values=input_values, attention_mask=attention_mask)
-            tokens = outputs.logits.argmax(dim=-1)
-            if stride is not None:
-                if isinstance(stride, tuple):
-                    stride = [stride]
-
-                apply_stride(tokens, stride)
-            out = {"tokens": tokens}
         else:
             logger.warning("This is an unknown class, treating it as CTC.")
             outputs = self.model(**model_inputs)
@@ -345,39 +337,38 @@ class AutomaticSpeechRecognitionPipeline(ChunkPipeline):
         if return_timestamps and self.type != "ctc":
             raise ValueError("We cannot return_timestamps yet on non-ctc models !")
 
+        final_items = []
+        key = "logits" if self.type == "ctc_with_lm" else "tokens"
+        for outputs in model_outputs:
+            items = outputs[key].numpy()
+            stride = outputs.pop("stride", None)
+            if stride is not None:
+                total_n, left, right = stride
+                # Total_n might be < logits.shape[1]
+                # because of padding, that's why
+                # we need to reconstruct this information
+                # This won't work with left padding (which doesn't exist right now)
+                right_n = total_n - right
+                items = items[:, left:right_n]
+            final_items.append(items)
+        items = np.concatenate(final_items, axis=1)
+        items = items.squeeze(0)
         if self.type == "ctc_with_lm":
-            final_logits = []
-            for outputs in model_outputs:
-                logits = outputs["logits"].numpy()
-                stride = outputs.pop("stride", None)
-                if stride is not None:
-                    total_n, left, right = stride
-                    # Total_n might be < logits.shape[1]
-                    # because of padding, that's why
-                    # we need to reconstruct this information
-                    # This won't work with left padding (which doesn't exist right now)
-                    right_n = total_n - right
-                    logits = logits[:, left:right_n]
-                final_logits.append(logits)
             if decoder_kwargs is None:
                 decoder_kwargs = {}
-            logits = np.concatenate(final_logits, axis=1)
-            logits = logits.squeeze(0)
-            text = self.decoder.decode_beams(logits, **decoder_kwargs)[0][0]
+            text = self.decoder.decode_beams(items, **decoder_kwargs)[0][0]
         else:
             skip_special_tokens = self.type != "ctc"
-            tokens = np.concatenate([outputs["tokens"].numpy() for outputs in model_outputs], axis=-1)
-            tokens = tokens.squeeze(0)
-            text = self.tokenizer.decode(tokens, skip_special_tokens=skip_special_tokens)
+            text = self.tokenizer.decode(items, skip_special_tokens=skip_special_tokens)
 
             if return_timestamps:
                 if return_timestamps == "char":
                     decoded = self.tokenizer.decode(
-                        tokens, skip_special_tokens=skip_special_tokens, output_char_offsets=True
+                        items, skip_special_tokens=skip_special_tokens, output_char_offsets=True
                     )
                 elif return_timestamps == "word":
                     decoded = self.tokenizer.decode(
-                        tokens, skip_special_tokens=skip_special_tokens, output_word_offsets=True
+                        items, skip_special_tokens=skip_special_tokens, output_word_offsets=True
                     )
                 chunks = []
                 for item in decoded[f"{return_timestamps}_offsets"]:
```

**thinking:**

```
I'll run a reproduction using a small randomly initialized Wav2Vec2 model with a local tokenizer, checking that chunked timestamps don't exceed the audio duration and that chunked tokens match the unchunked output once strides are dropped.


```

**tool call: Bash**

```bash
mkdir -p /tmp/x; cat > /work/huggingface__transformers-15843/repo/repro_asr.py <<'EOF'
import json, tempfile, os
import numpy as np, torch
from transformers import Wav2Vec2Config, Wav2Vec2ForCTC, Wav2Vec2CTCTokenizer, Wav2Vec2FeatureExtractor, pipeline

torch.manual_seed(0)
d = tempfile.mkdtemp()
vocab = {"<pad>": 0, "<s>": 1, "</s>": 2, "<unk>": 3, "|": 4, **{c: i + 5 for i, c in enumerate("ABCDEFGH")}}
json.dump(vocab, open(os.path.join(d, "vocab.json"), "w"))
tok = Wav2Vec2CTCTokenizer(os.path.join(d, "vocab.json"))
fe = Wav2Vec2FeatureExtractor(do_normalize=True, return_attention_mask=False)
cfg = Wav2Vec2Config(vocab_size=len(vocab), hidden_size=16, num_hidden_layers=1, num_attention_heads=2,
                     intermediate_size=20, conv_dim=(8, 8, 8, 8, 8, 8, 8), num_conv_pos_embeddings=16, num_conv_pos_embedding_groups=2)
model = Wav2Vec2ForCTC(cfg).eval()
asr = pipeline("automatic-speech-recognition", model=model, tokenizer=tok, feature_extractor=fe)

audio = np.random.RandomState(0).randn(16000 * 5).astype(np.float32)
duration = len(audio) / 16000
out = asr(audio, chunk_length_s=1.0, return_timestamps="char")
last = out["chunks"][-1]["timestamp"][1] if out["chunks"] else 0
print("duration", duration, "last char end", last)
assert last <= duration, "timestamps exceed audio duration"

# Stride alignment: chunk with tiny stride vs no chunking -> same token count
full = asr(audio, return_timestamps="char")
print("chunks (chunked/unchunked):", len(out["chunks"]), len(full["chunks"]))

# explicit stride edge cases
w = np.tile(np.arange(1000, dtype=np.float32), 10)
for s in [(0, 0), (5000, 5000), (0, 9000), (1000, 8000)]:
    print(s, repr(asr({"raw": w, "stride": s, "sampling_rate": 16000})["text"]))
EOF
/work/huggingface__transformers-15843/bin/envrun 'python repro_asr.py 2>&1 | grep -v Warn | tail; git stash -q; echo ---BEFORE---; python repro_asr.py 2>&1 | tail -8; git stash pop -q; git status --short'
```

tool result:

```
mkdir: /tmp/x: Operation not permitted
    outputs = self.postprocess(all_outputs, **postprocess_params)
  File "/testbed/src/transformers/pipelines/automatic_speech_recognition.py", line 362, in postprocess
    text = self.tokenizer.decode(items, skip_special_tokens=skip_special_tokens)
  File "/testbed/src/transformers/models/wav2vec2/tokenization_wav2vec2.py", line 575, in decode
    return self._decode(
  File "/testbed/src/transformers/models/wav2vec2/tokenization_wav2vec2.py", line 380, in _decode
    string_output = self.convert_tokens_to_string(
  File "/testbed/src/transformers/models/wav2vec2/tokenization_wav2vec2.py", line 263, in convert_tokens_to_string
    chars, char_repetitions = zip(*((token, len(list(group_iter))) for token, group_iter in groupby(tokens)))
ValueError: not enough values to unpack (expected 2, got 0)
---BEFORE---
/usr/local/lib/python3.10/site-packages/torch/nn/utils/weight_norm.py:143: FutureWarning: `torch.nn.utils.weight_norm` is deprecated in favor of `torch.nn.utils.parametrizations.weight_norm`.
  WeightNorm.apply(module, name, dim)
[W1009 04:39:23.570392916 NNPACK.cpp:61] Could not initialize NNPACK! Reason: Unsupported hardware.
duration 5.0 last char end 7.18
Traceback (most recent call last):
  File "/testbed/repro_asr.py", line 21, in <module>
    assert last <= duration, "timestamps exceed audio duration"
AssertionError: timestamps exceed audio duration
 M src/transformers/pipelines/automatic_speech_recognition.py
?? Dockerfile
?? repro_asr.py
```

**assistant:** I've reproduced the bug on the original code: 5 s of audio produced timestamps that end at 7.18 s. With my change, one case now crashes because the slice is empty. Let me see which input causes it:

**tool call: Bash**

```bash
/work/huggingface__transformers-15843/bin/envrun 'python repro_asr.py 2>&1 | grep -v Warn | grep -v "^ "| head'
```

tool result:

```
2026-10-09 04:39:30.860103: I external/local_xla/xla/tsl/cuda/cudart_stub.cc:31] Could not find cuda drivers on your machine, GPU will not be used.
2026-10-09 04:39:31.164370: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
[W1009 04:39:33.178796046 NNPACK.cpp:61] Could not initialize NNPACK! Reason: Unsupported hardware.
duration 5.0 last char end 4.94
chunks (chunked/unchunked): 195 203
(0, 0) 'F F FE FEFEFEF F F'
Traceback (most recent call last):
ValueError: not enough values to unpack (expected 2, got 0)
```

**thinking:**

```
Timestamps are now correctly ending at 4.94s instead of 7.18s. The remaining crash is an edge case in `test_stride` where an empty token slice breaks decoding, so I'll add a fallback to keep the middle item of the first chunk when every stride slice is empty.


```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/huggingface__transformers-15843/repo/src/transformers/pipelines/automatic_speech_recognition.py",
 "old_string": "        final_items = []\n        key = \"logits\" if self.type == \"ctc_with_lm\" else \"tokens\"\n        for outputs in model_outputs:\n            items = outputs[key].numpy()\n            stride = outputs.pop(\"stride\", None)\n            if stride is not None:\n                total_n, left, right = stride\n                # Total_n might be < logits.shape[1]\n                # because of padding, that's why\n                # we need to reconstruct this information\n                # This won't work with left padding (which doesn't exist right now)\n                right_n = total_n - right\n                items = items[:, left:right_n]\n            final_items.append(items)\n        items = np.concatenate(final_items, axis=1)",
 "new_string": "        final_items = []\n        middle_item = None\n        key = \"logits\" if self.type == \"ctc_with_lm\" else \"tokens\"\n        for outputs in model_outputs:\n            items = outputs[key].numpy()\n            stride = outputs.pop(\"stride\", None)\n            if stride is not None:\n                total_n, left, right = stride\n                if middle_item is None:\n                    middle_item = items[:, total_n // 2 : total_n // 2 + 1]\n                # Total_n might be < logits.shape[1]\n                # because of padding, that's why\n                # we need to reconstruct this information\n                # This won't work with left padding (which doesn't exist right now)\n                right_n = total_n - right\n                items = items[:, left:right_n]\n            final_items.append(items)\n        items = np.concatenate(final_items, axis=1)\n        if items.shape[1] == 0 and middle_item is not None:\n            # The strides cover the whole input, keep only the middle item\n            items = middle_item"
}
```

tool result:

```
The file /work/huggingface__transformers-15843/repo/src/transformers/pipelines/automatic_speech_recognition.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
/work/huggingface__transformers-15843/bin/envrun 'python repro_asr.py 2>&1 | tail -6'
```

tool result:

```
duration 5.0 last char end 4.94
chunks (chunked/unchunked): 195 203
(0, 0) 'F F FE FEFEFEF F F'
(5000, 5000) 'F'
(0, 9000) 'F F'
(1000, 8000) 'F F'
```

**assistant:** Everything works now. Next I'll run the existing tests and the style checks, then delete the repro script. `apply_stride` stays because the tests still import it.

**tool call: Bash**

```bash
rm repro_asr.py; /work/huggingface__transformers-15843/bin/envrun 'python -m pytest tests/pipelines/test_pipelines_automatic_speech_recognition.py -q 2>&1 | tail -2; black --check src/transformers/pipelines/automatic_speech_recognition.py; flake8 src/transformers/pipelines/automatic_speech_recognition.py; git status --short'
```

tool result:

```
3 passed, 30 skipped, 6 warnings in 1.64s
sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
All done! ✨ 🍰 ✨
1 file would be left unchanged.
 M src/transformers/pipelines/automatic_speech_recognition.py
?? Dockerfile
```

**assistant:** I fixed the timestamp bug. With chunking on, the pipeline's timestamps now stay inside the audio's duration and line up with what `Wav2Vec2CTCTokenizer.decode()` returns.

**Cause:** in `apply_stride`, the plain CTC path filled each chunk's stride regions with copies of the first and last letters, then joined every chunk's full token sequence. The overlapping stride frames were counted more than once, which pushed the offsets past the end of the audio.

**Fix** (all in `src/transformers/pipelines/automatic_speech_recognition.py`):
- **Forward pass:** plain CTC now shares the code path `ctc_with_lm` already used. It keeps the argmax tokens and passes the rescaled stride on to `postprocess`, instead of filling the stride regions in place.
- **Postprocess:** both CTC types now cut the stride regions off each chunk before joining. Text, char offsets and word offsets are then computed on the trimmed tokens, so the frame indices match real sample positions.
- **Edge case:** if the stride covers the whole input (e.g. stride `(5000, 5000)` on 10,000 samples), the slice would be empty and the tokenizer crashes on an empty sequence. In that case it now keeps the middle item, which is what the existing `test_stride` expects ("Just take the middle one").
- **Kept `apply_stride`:** the pipeline no longer calls it, but I left it in place because the tests still import it.

**Verification:** no models are cached and the container has no network, so I tested with a small, randomly initialized Wav2Vec2 model and a local tokenizer:
- **Before:** 5.0 s of audio with `chunk_length_s=1.0` gave timestamps ending at 7.18 s.
- **After:** the last timestamp ends at 4.94 s.
- **Explicit strides:** `(0,0)`, `(5000,5000)`, `(0,9000)` and `(1000,8000)` all decode without errors.

The existing test file passes 3 tests and skips 30. The skipped ones are the pipeline tests, which need to download models, so the exact expected strings for the hub models (such as `"B"` in `test_stride`) are untested here. `black` and `flake8` pass on the changed file, and I deleted the repro script. The untracked `Dockerfile` in the repo isn't mine, so I left it.

_session end: success, turns 14, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 9.55 s: HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m pytest tests/pipelines/test_pipelines_automatic_speech_recognition.py -x -q 2>&1 | tail -15
- `rc=2` 8.08 s: python -m pytest tests/pipelines/test_pipelines_automatic_speech_recognition.py -q -rs 2>&1 | grep -i skip | head; ls ~/.cache/huggingface 2>&1
- `rc=0` 13.57 s: python repro_asr.py 2>&1 | grep -v Warn | tail; git stash -q; echo ---BEFORE---; python repro_asr.py 2>&1 | tail -8; git stash pop -q; git status --short
- `rc=0` 6.48 s: python repro_asr.py 2>&1 | grep -v Warn | grep -v "^ "| head
- `rc=0` 6.79 s: python repro_asr.py 2>&1 | tail -6
- `rc=0` 9.57 s: python -m pytest tests/pipelines/test_pipelines_automatic_speech_recognition.py -q 2>&1 | tail -2; black --check src/transformers/pipelines/automatic_speech_recognition.py; flake8 src/transformers/pipelines/automatic_speech_recognition.py; git status --short
