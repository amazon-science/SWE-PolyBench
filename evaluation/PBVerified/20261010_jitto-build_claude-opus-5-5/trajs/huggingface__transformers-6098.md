# Instance: huggingface__transformers-6098

- Final resolved (evaluator, logs/huggingface__transformers-6098_result.json): True
- Run state: DONE
- One attempt. Duration 53.8 s, turns 8, actor cost $0.1885868, container commands 3
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/huggingface__transformers-6098/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-6098/repo. Consider the following issue description:

<issue_description>
mBART: incorrect <mask> token id
# 🐛 Bug

## Information

Model I am using: mBART

## To reproduce

```
from transformers import MBartTokenizer
tokenizer = MBartTokenizer.from_pretrained('facebook/mbart-large-cc25')
print(tokenizer.convert_tokens_to_ids(['<mask>', 'ar_AR']))
```
The output for the above code is `[250001, 250001]`  - two different special tokens are mapped to the same id.

## Expected behavior

As far as I can tell, `<mask>` token should be mapped to id 250026.

I've checked [fairseq implementation](https://github.com/pytorch/fairseq/blob/master/fairseq/tasks/multilingual_denoising.py) and it seems that `<mask>` token is added after all the language codes, so it should be the last token in the vocab.

Currently, when I try to use mBART to denoise text with `<mask>` tokens, it mostly just ignores them, but if I replace mask ids with 250026, the model actually generates new text in place of `<mask>` tokens:

```
from transformers import MBartTokenizer, BartForConditionalGeneration

tokenizer = MBartTokenizer.from_pretrained('facebook/mbart-large-cc25')
model = BartForConditionalGeneration.from_pretrained('facebook/mbart-large-cc25')

text = 'I highly recommend <mask> - it is one of the best <mask> ever read!'
inputs = tokenizer.prepare_translation_batch([text], src_lang='en_XX')

outputs = model.generate(inputs['input_ids'], decoder_start_token_id=tokenizer.lang_code_to_id['en_XX'], 
                         num_beams=5)
print(tokenizer.batch_decode(outputs)[0])
```

The output is:
```
en_XX<s> highly recommend - it is one of the best ever read!
```
Replacing mask ids:

```
where = (inputs['input_ids'] == 250001)
inputs['input_ids'][where] = 250026

outputs = model.generate(inputs['input_ids'], decoder_start_token_id=tokenizer.lang_code_to_id['en_XX'], 
                         num_beams=5)
print(tokenizer.batch_decode(outputs)[0])
```

The output is:
```
en_XX<s> highly recommend this book - it is one of the best books I have ever read!
```

(In both cases, the model also skips the first input token when generating output, as discussed in #5755.)

I've also noticed that fairseq is using [language code tokens](https://github.com/pytorch/fairseq/blob/108bb2560b1ec01524ba723bc7c69186875afa0a/fairseq/tasks/multilingual_denoising.py#L62) of the form `[en_XX]` rather than just `en_XX`, which can lead to different tokenization if words like  `en_XX` appear in the text, but that's a rather contrived case.


## Environment info
<!-- You can run the command `transformers-cli env` and copy-and-paste its output below.
     Don't forget to fill out the missing fields in that output! -->
     
- `transformers` version: 3.0.2


@sshleifer


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-6098/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-6098/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-6098/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-6098/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cat src/transformers/tokenization_bart.py && sed -n 1,200p src/transformers/tokenization_xlm_roberta.py | grep -n "fairseq\|mask\|def \|offset" 
```

tool result:

````
# coding=utf-8
# Copyright 2020 The Facebook AI Research Team Authors and The HuggingFace Inc. team.
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

import logging
from typing import List, Optional

from .tokenization_roberta import RobertaTokenizer, RobertaTokenizerFast
from .tokenization_utils import BatchEncoding
from .tokenization_xlm_roberta import XLMRobertaTokenizer


logger = logging.getLogger(__name__)


# vocab and merges same as roberta
vocab_url = "https://s3.amazonaws.com/models.huggingface.co/bert/roberta-large-vocab.json"
merges_url = "https://s3.amazonaws.com/models.huggingface.co/bert/roberta-large-merges.txt"
_all_bart_models = [
    "facebook/bart-base",
    "facebook/bart-large",
    "facebook/bart-large-mnli",
    "facebook/bart-large-cnn",
    "facebook/bart-large-xsum",
    "yjernite/bart_eli5",
]


class BartTokenizer(RobertaTokenizer):
    # merges and vocab same as Roberta
    max_model_input_sizes = {m: 1024 for m in _all_bart_models}
    pretrained_vocab_files_map = {
        "vocab_file": {m: vocab_url for m in _all_bart_models},
        "merges_file": {m: merges_url for m in _all_bart_models},
    }


class BartTokenizerFast(RobertaTokenizerFast):
    # merges and vocab same as Roberta
    max_model_input_sizes = {m: 1024 for m in _all_bart_models}
    pretrained_vocab_files_map = {
        "vocab_file": {m: vocab_url for m in _all_bart_models},
        "merges_file": {m: merges_url for m in _all_bart_models},
    }


_all_mbart_models = ["facebook/mbart-large-en-ro", "facebook/mbart-large-cc25"]
SPM_URL = "https://s3.amazonaws.com/models.huggingface.co/bert/facebook/mbart-large-en-ro/sentence.bpe.model"

FAIRSEQ_LANGUAGE_CODES = [
    "ar_AR",
    "cs_CZ",
    "de_DE",
    "en_XX",
    "es_XX",
    "et_EE",
    "fi_FI",
    "fr_XX",
    "gu_IN",
    "hi_IN",
    "it_IT",
    "ja_XX",
    "kk_KZ",
    "ko_KR",
    "lt_LT",
    "lv_LV",
    "my_MM",
    "ne_NP",
    "nl_XX",
    "ro_RO",
    "ru_RU",
    "si_LK",
    "tr_TR",
    "vi_VN",
    "zh_CN",
]


class MBartTokenizer(XLMRobertaTokenizer):
    """
    This inherits from XLMRobertaTokenizer. ``prepare_translation_batch`` should be used to encode inputs.
    Other tokenizer methods like ``encode`` do not work properly.
    The tokenization method is ``<tokens> <eos> <language code>`` for source language documents, and
    ``<language code> <tokens> <eos>``` for target language documents.

    Examples::

        >>> from transformers import MBartTokenizer
        >>> tokenizer = MBartTokenizer.from_pretrained('facebook/mbart-large-en-ro')
        >>> example_english_phrase = " UN Chief Says There Is No Military Solution in Syria"
        >>> expected_translation_romanian = "Şeful ONU declară că nu există o soluţie militară în Siria"
        >>> batch: dict = tokenizer.prepare_translation_batch(
        ...     example_english_phrase, src_lang="en_XX", tgt_lang="ro_RO", tgt_texts=expected_translation_romanian
        ... )

    """

    vocab_files_names = {"vocab_file": "sentencepiece.bpe.model"}
    max_model_input_sizes = {m: 1024 for m in _all_mbart_models}
    pretrained_vocab_files_map = {"vocab_file": {m: SPM_URL for m in _all_mbart_models}}

    prefix_tokens: List[int] = []
    suffix_tokens: List[int] = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sp_model_size = len(self.sp_model)
        self.lang_code_to_id = {
            code: self.sp_model_size + i + self.fairseq_offset for i, code in enumerate(FAIRSEQ_LANGUAGE_CODES)
        }
        self.id_to_lang_code = {v: k for k, v in self.lang_code_to_id.items()}
        self.cur_lang_code = self.lang_code_to_id["en_XX"]

        self.fairseq_tokens_to_ids.update(self.lang_code_to_id)
        self.fairseq_ids_to_tokens = {v: k for k, v in self.fairseq_tokens_to_ids.items()}
        self._additional_special_tokens = list(self.lang_code_to_id.keys())
        self.set_src_lang_special_tokens(kwargs.get("src_lang", "en_XX"))

    def build_inputs_with_special_tokens(
        self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None
    ) -> List[int]:
        """
        Build model inputs from a sequence or a pair of sequence for sequence classification tasks
        by concatenating and adding special tokens. The special tokens depend on calling set_lang.
        An MBART sequence has the following format, where ``X`` represents the sequence:
        - ``input_ids`` (for encoder) ``X [eos, src_lang_code]``
        - ``decoder_input_ids``: (for decoder) ``[tgt_lang_code] X [eos]``
        BOS is never used.
        Pairs of sequences are not the expected use case, but they will be handled without a separator.

        Args:
            token_ids_0 (:obj:`List[int]`):
                List of IDs to which the special tokens will be added
            token_ids_1 (:obj:`List[int]`, `optional`, defaults to :obj:`None`):
                Optional second list of IDs for sequence pairs.

        Returns:
            :obj:`List[int]`: list of `input IDs <../glossary.html#input-ids>`__ with the appropriate special tokens.
        """
        if token_ids_1 is None:
            return self.prefix_tokens + token_ids_0 + self.suffix_tokens
        # We don't expect to process pairs, but leave the pair logic for API consistency
        return self.prefix_tokens + token_ids_0 + token_ids_1 + self.suffix_tokens

    def get_special_tokens_mask(
        self, token_ids_0: List[int], token_ids_1: Optional[List[i
[... 5599 more characters not shown]
````

**tool call: Bash**

```bash
grep -n "vocab_size" -A3 src/transformers/tokenization_xlm_roberta.py; grep -n "mask\|250\|vocab_size\|len(" tests/test_tokenization_mbart.py | head -40
```

tool result:

```
261:    def vocab_size(self):
262-        return len(self.sp_model) + self.fairseq_offset + 1  # Add the <mask> token
263-
264-    def get_vocab(self):
265:        vocab = {self.convert_ids_to_tokens(i): i for i in range(self.vocab_size)}
266-        vocab.update(self.added_tokens_encoder)
267-        return vocab
268-
10:EN_CODE = 250004
11:RO_CODE = 250020
121:        self.assertEqual(self.tokenizer.fairseq_tokens_to_ids["ar_AR"], 250001)
122:        self.assertEqual(self.tokenizer.fairseq_tokens_to_ids["en_EN"], 250004)
123:        self.assertEqual(self.tokenizer.fairseq_tokens_to_ids["ro_RO"], 250020)
127:            self.src_text, tgt_texts=self.tgt_text, max_length=len(self.expected_src_tokens),
132:        self.assertEqual((2, 14), batch.attention_mask.shape)
173:        self.assertEqual(len(ids), desired_max_length)
```

**tool call: Bash**

```bash
sed -n 100,130p tests/test_tokenization_mbart.py
```

tool result:

```
@require_torch
class MBartEnroIntegrationTest(unittest.TestCase):
    checkpoint_name = "facebook/mbart-large-en-ro"
    src_text = [
        " UN Chief Says There Is No Military Solution in Syria",
        """ Secretary-General Ban Ki-moon says his response to Russia's stepped up military support for Syria is that "there is no military solution" to the nearly five-year conflict and more weapons will only worsen the violence and misery for millions of people.""",
    ]
    tgt_text = [
        "Şeful ONU declară că nu există o soluţie militară în Siria",
        'Secretarul General Ban Ki-moon declară că răspunsul său la intensificarea sprijinului militar al Rusiei pentru Siria este că "nu există o soluţie militară" la conflictul de aproape cinci ani şi că noi arme nu vor face decât să înrăutăţească violenţele şi mizeria pentru milioane de oameni.',
    ]
    expected_src_tokens = [8274, 127873, 25916, 7, 8622, 2071, 438, 67485, 53, 187895, 23, 51712, 2, EN_CODE]

    @classmethod
    def setUpClass(cls):
        cls.tokenizer: MBartTokenizer = AutoTokenizer.from_pretrained(cls.checkpoint_name)
        cls.pad_token_id = 1
        return cls

    def check_language_codes(self):
        self.assertEqual(self.tokenizer.fairseq_tokens_to_ids["ar_AR"], 250001)
        self.assertEqual(self.tokenizer.fairseq_tokens_to_ids["en_EN"], 250004)
        self.assertEqual(self.tokenizer.fairseq_tokens_to_ids["ro_RO"], 250020)

    def test_enro_tokenizer_prepare_translation_batch(self):
        batch = self.tokenizer.prepare_translation_batch(
            self.src_text, tgt_texts=self.tgt_text, max_length=len(self.expected_src_tokens),
        )
        self.assertIsInstance(batch, BatchEncoding)
```

**tool call: Bash**

```bash
ls ~/.cache/torch/transformers 2>/dev/null | head; /work/huggingface__transformers-6098/bin/envrun 'ls ~/.cache/torch/transformers 2>/dev/null | head; ls tests/fixtures'
```

tool result:

```
dummy-config.json
empty.txt
input.txt
sample_text.txt
spiece.model
test_sentencepiece.model
tests_samples
```

**assistant:** Now apply the fix: place `<mask>` after all language codes and make `vocab_size` account for them.

**tool call: Bash**

```bash
python3 - <<'EOF'
p='src/transformers/tokenization_bart.py'
s=open(p).read()
s=s.replace('''        self.cur_lang_code = self.lang_code_to_id["en_XX"]

        self.fairseq_tokens_to_ids.update(self.lang_code_to_id)''','''        self.cur_lang_code = self.lang_code_to_id["en_XX"]
        self.fairseq_tokens_to_ids["<mask>"] = len(self.sp_model) + len(self.lang_code_to_id) + self.fairseq_offset

        self.fairseq_tokens_to_ids.update(self.lang_code_to_id)''')
s=s.replace('''        self.set_src_lang_special_tokens(kwargs.get("src_lang", "en_XX"))

    def build_inputs''','''        self.set_src_lang_special_tokens(kwargs.get("src_lang", "en_XX"))

    @property
    def vocab_size(self):
        return len(self.sp_model) + len(self.lang_code_to_id) + self.fairseq_offset + 1  # Plus 1 for the mask token

    def build_inputs''')
open(p,'w').write(s)
EOF
git diff --stat
```

tool result:

```
 src/transformers/tokenization_bart.py | 5 +++++
 1 file changed, 5 insertions(+)
```

**assistant:** The real checkpoint can't be downloaded (no network), so I'll check with the local sentencepiece fixture.

**tool call: Bash**

```bash
/work/huggingface__transformers-6098/bin/envrun 'python -c "
from transformers import MBartTokenizer
t = MBartTokenizer(\"tests/fixtures/test_sentencepiece.model\")
n=len(t.sp_model); print(n, t.vocab_size)
print(t.convert_tokens_to_ids([\"<mask>\",\"ar_AR\",\"zh_CN\"]), t.mask_token_id)
print(t.convert_ids_to_tokens([n+1, n+25, n+26]))
v=t.get_vocab(); print(len(v), v[\"<mask>\"], len(set(v.values())))
" && python -m pytest -q tests/test_tokenization_mbart.py tests/test_tokenization_xlm_roberta.py 2>&1 | tail -3'
```

tool result:

```
2026-10-09 19:19:46.168194: I tensorflow/tsl/cuda/cudart_stub.cc:28] Could not find cuda drivers on your machine, GPU will not be used.
2026-10-09 19:19:46.417864: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2026-10-09 19:19:47.094546: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
1000 1027
[1026, 1001, 1025] 1026
['ar_AR', 'zh_CN', '<mask>']
1027 1026 1027
ERROR tests/test_tokenization_mbart.py::MBartEnroIntegrationTest::test_enro_tokenizer_truncation
ERROR tests/test_tokenization_mbart.py::MBartEnroIntegrationTest::test_max_target_length
62 passed, 8 skipped, 4 warnings, 5 errors in 6.79s
```

**tool call: Bash**

```bash
/work/huggingface__transformers-6098/bin/envrun 'python -m pytest -q tests/test_tokenization_mbart.py 2>&1 | grep -iE "^E .*(Error|connection)" | sort | uniq -c | head; git stash -q; python -c "
from transformers import MBartTokenizer
t = MBartTokenizer(\"tests/fixtures/test_sentencepiece.model\")
print(\"before:\", t.convert_tokens_to_ids([\"<mask>\",\"ar_AR\"]))
" 2>&1 | tail -1; git stash pop -q; git status --short'
```

tool result:

```
      5 E               OSError
      5 E           OSError: Can't load config for 'facebook/mbart-large-en-ro'. Make sure that:
before: [1001, 1001]
 M src/transformers/tokenization_bart.py
?? Dockerfile
```

**assistant:** I fixed the tokenizer so `<mask>` no longer shares an id with `ar_AR`; it now gets its own id after all 25 language codes. I checked this with the small local test vocabulary, not the real checkpoint, because the container has no network access to download `facebook/mbart-large-cc25`.

**Cause:** `MBartTokenizer` inherits from `XLMRobertaTokenizer`, which puts `<mask>` at `len(sp_model) + fairseq_offset`. mBART then put its language codes starting at that same position, so `ar_AR` took the mask's id. Fairseq adds `<mask>` after all the language codes.

**Fix** (`src/transformers/tokenization_bart.py`, `MBartTokenizer`):
- In `__init__`, `<mask>` is now set to `len(sp_model) + len(lang_code_to_id) + fairseq_offset`. For mbart-large-cc25 that is 250000 + 25 + 1 = **250026**, as the issue expects.
- I added a `vocab_size` property that counts the language codes and the mask. Without it, the inherited version stops before the language codes, so `get_vocab()` would leave out `<mask>` and most of the codes.

**Checks** (using `tests/fixtures/test_sentencepiece.model`, 1000 pieces):
- Before: `convert_tokens_to_ids(['<mask>', 'ar_AR'])` gave `[1001, 1001]`.
- After: it gives `[1026, 1001]`, and `mask_token_id` is 1026.
- Converting ids back to tokens works: 1001 → `ar_AR`, 1025 → `zh_CN`, 1026 → `<mask>`.
- `vocab_size` and `len(get_vocab())` are both 1027, with no duplicate ids.
- `tests/test_tokenization_mbart.py` and `tests/test_tokenization_xlm_roberta.py`: 62 passed, 8 skipped, 5 errors. All 5 errors are `OSError: Can't load config for 'facebook/mbart-large-en-ro'`: those integration tests need to download the model, so they couldn't run here.

I left alone the issue's side note about fairseq writing language codes as `[en_XX]`, since that's a separate tokenization question. I didn't create any extra files. There is an untracked `Dockerfile` in the repo that I didn't create, and I left it as it was.

_session end: success, turns 8, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.15 s: ls ~/.cache/torch/transformers 2>/dev/null | head; ls tests/fixtures
- `rc=0` 13.1 s: python -c " from transformers import MBartTokenizer t = MBartTokenizer(\"tests/fixtures/test_sentencepiece.model\") n=len(t.sp_model); print(n, t.vocab_size) print(t.convert_tokens_to_ids([\"<mask>\",\"ar_AR\",\"zh_CN\"]), t.mask_token_id) print(t.convert_ids_to_tokens([n+1, n+25, n+26])) v=t.get_vocab(); print(len(v), v[\"<mask>\"], len(set(v.values()))) " && python -m pytest -q tests/test_tokenization_mbart.py tests/test_tokenization_xlm_roberta.py 2>&1 | tail -3
- `rc=0` 11.94 s: python -m pytest -q tests/test_tokenization_mbart.py 2>&1 | grep -iE "^E .*(Error|connection)" | sort | uniq -c | head; git stash -q; python -c " from transformers import MBartTokenizer t = MBartTokenizer(\"tests/fixtures/test_sentencepiece.model\") print(\"before:\", t.convert_tokens_to_ids([\"<mask>\",\"ar_AR\"])) " 2>&1 | tail -1; git stash pop -q; git status --short
