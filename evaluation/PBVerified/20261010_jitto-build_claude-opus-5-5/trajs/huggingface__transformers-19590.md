# Instance: huggingface__transformers-19590

- Final resolved (evaluator, logs/huggingface__transformers-19590_result.json): True
- Run state: DONE
- One attempt. Duration 78.5 s, turns 8, actor cost $0.2382566, container commands 4
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/huggingface__transformers-19590/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-19590/repo. Consider the following issue description:

<issue_description>
Allow TFBertTokenizer to use Tensorflow text BertTokenizer (and not FastBertTokenizer) to make it servable by TF Serving
### Feature request

I would like to serve a bundle of Tokenizer + Model on TF Serving, but can't do it because TF Serving still have no support for TF FastBertTokenizer annd FastBertNormalize operations (https://github.com/tensorflow/serving/issues/2064).

It would be good if we could let [TFBertTokenizer ](https://github.com/huggingface/transformers/blob/4ed0fa3676ad8900eaa982a6c5c2ad6b75c8ea46/src/transformers/models/bert/tokenization_bert_tf.py) give the user an option not to use Tensorflow FastBertTokenizer when creating a TFBertTokenizer, so that it is servable on TFServing. 

It would consist of moving (or creating an option to change) this

https://github.com/huggingface/transformers/blob/4ed0fa3676ad8900eaa982a6c5c2ad6b75c8ea46/src/transformers/models/bert/tokenization_bert_tf.py#L67-L69

To this:
```python
# to avoid naming collision with transformers BertTokenizer
from tensorflow_text import BertTokenizer as TFBertTokenizerLayer

lookup_table = tf.lookup.StaticVocabularyTable(
    tf.lookup.KeyValueTensorInitializer(
        keys=vocab_list,
        key_dtype=tf.string,
        values=tf.range(
            tf.size(vocab_list, out_type=tf.int64), dtype=tf.int64),
            value_dtype=tf.int64
        ),
        num_oov_buckets=1
)
        
self.tf_tokenizer = TFBertTokenizerLayer(
    lookup_table, token_out_type=tf.int64, lower_case=do_lower_case
)
```

### Motivation

I would like to serve a bundle of Tokenizer + Model on TF Serving, but can't do it because TF Serving still have no support for TF FastBertTokenizer annd FastBertNormalize operations (https://github.com/tensorflow/serving/issues/2064).

As this lib is much faster to solve this kind of thing than TF Serving, I thought it was worth it trying to solve it from here. 

### Your contribution

I can definitely submit a PR with that if you approve the idea. 

EDIT: I've created https://github.com/huggingface/transformers/pull/19590 to showcase the idea. 

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-19590/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-19590/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-19590/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-19590/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cat src/transformers/models/bert/tokenization_bert_tf.py && grep -n "use_fast\|TFBertTokenizer(" tests/models/bert/test_tokenization_bert_tf.py
```

tool result:

````
import os
from typing import List, Union

import tensorflow as tf

from tensorflow_text import FastBertTokenizer, ShrinkLongestTrimmer, case_fold_utf8, combine_segments, pad_model_inputs

from .tokenization_bert import BertTokenizer


class TFBertTokenizer(tf.keras.layers.Layer):
    """
    This is an in-graph tokenizer for BERT. It should be initialized similarly to other tokenizers, using the
    `from_pretrained()` method. It can also be initialized with the `from_tokenizer()` method, which imports settings
    from an existing standard tokenizer object.

    In-graph tokenizers, unlike other Hugging Face tokenizers, are actually Keras layers and are designed to be run
    when the model is called, rather than during preprocessing. As a result, they have somewhat more limited options
    than standard tokenizer classes. They are most useful when you want to create an end-to-end model that goes
    straight from `tf.string` inputs to outputs.

    Args:
        vocab_list (`list`):
            List containing the vocabulary.
        do_lower_case (`bool`, *optional*, defaults to `True`):
            Whether or not to lowercase the input when tokenizing.
        cls_token_id (`str`, *optional*, defaults to `"[CLS]"`):
            The classifier token which is used when doing sequence classification (classification of the whole sequence
            instead of per-token classification). It is the first token of the sequence when built with special tokens.
        sep_token_id (`str`, *optional*, defaults to `"[SEP]"`):
            The separator token, which is used when building a sequence from multiple sequences, e.g. two sequences for
            sequence classification or for a text and a question for question answering. It is also used as the last
            token of a sequence built with special tokens.
        pad_token_id (`str`, *optional*, defaults to `"[PAD]"`):
            The token used for padding, for example when batching sequences of different lengths.
        padding (`str`, defaults to `"longest"`):
            The type of padding to use. Can be either `"longest"`, to pad only up to the longest sample in the batch,
            or `"max_length", to pad all inputs to the maximum length supported by the tokenizer.
        truncation (`bool`, *optional*, defaults to `True`):
            Whether to truncate the sequence to the maximum length.
        max_length (`int`, *optional*, defaults to `512`):
            The maximum length of the sequence, used for padding (if `padding` is "max_length") and/or truncation (if
            `truncation` is `True`).
        pad_to_multiple_of (`int`, *optional*, defaults to `None`):
            If set, the sequence will be padded to a multiple of this value.
        return_token_type_ids (`bool`, *optional*, defaults to `True`):
            Whether to return token_type_ids.
        return_attention_mask (`bool`, *optional*, defaults to `True`):
            Whether to return the attention_mask.
    """

    def __init__(
        self,
        vocab_list: List,
        do_lower_case: bool,
        cls_token_id: int = None,
        sep_token_id: int = None,
        pad_token_id: int = None,
        padding: str = "longest",
        truncation: bool = True,
        max_length: int = 512,
        pad_to_multiple_of: int = None,
        return_token_type_ids: bool = True,
        return_attention_mask: bool = True,
    ):
        super().__init__()
        self.tf_tokenizer = FastBertTokenizer(
            vocab_list, token_out_type=tf.int64, lower_case_nfd_strip_accents=do_lower_case
        )
        self.vocab_list = vocab_list
        self.do_lower_case = do_lower_case
        self.cls_token_id = cls_token_id or vocab_list.index("[CLS]")
        self.sep_token_id = sep_token_id or vocab_list.index("[SEP]")
        self.pad_token_id = pad_token_id or vocab_list.index("[PAD]")
        self.paired_trimmer = ShrinkLongestTrimmer(max_length - 3, axis=1)  # Allow room for special tokens
        self.max_length = max_length
        self.padding = padding
        self.truncation = truncation
        self.pad_to_multiple_of = pad_to_multiple_of
        self.return_token_type_ids = return_token_type_ids
        self.return_attention_mask = return_attention_mask

    @classmethod
    def from_tokenizer(cls, tokenizer: "PreTrainedTokenizerBase", **kwargs):  # noqa: F821
        """
        Initialize a `TFBertTokenizer` from an existing `Tokenizer`.

        Args:
            tokenizer (`PreTrainedTokenizerBase`):
                The tokenizer to use to initialize the `TFBertTokenizer`.

        Examples:

        ```python
        from transformers import AutoTokenizer, TFBertTokenizer

        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        tf_tokenizer = TFBertTokenizer.from_tokenizer(tokenizer)
        ```
        """
        vocab = tokenizer.get_vocab()
        vocab = sorted([(wordpiece, idx) for wordpiece, idx in vocab.items()], key=lambda x: x[1])
        vocab_list = [entry[0] for entry in vocab]
        return cls(
            vocab_list=vocab_list,
            do_lower_case=tokenizer.do_lower_case,
            cls_token_id=tokenizer.cls_token_id,
            sep_token_id=tokenizer.sep_token_id,
            pad_token_id=tokenizer.pad_token_id,
            **kwargs,
        )

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], *init_inputs, **kwargs):
        """
        Instantiate a `TFBertTokenizer` from a pre-trained tokenizer.

        Args:
            pretrained_model_name_or_path (`str` or `os.PathLike`):
                The name or path to the pre-trained tokenizer.

        Examples:

        ```python
        from transformers import TFBertTokenizer

        tf_tokenizer = TFBertTokenizer.from_pretrained("bert-base-uncased")
        ```
        """
        try:
            tokenizer = BertTokenizer.from_pretrained(pretrained_model_name_or_path, *init_inputs,
[... 4106 more characters not shown]
````

**tool call: Bash**

```bash
cat tests/models/bert/test_tokenization_bert_tf.py | head -80
```

tool result:

```
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from transformers import AutoConfig, TFAutoModel, is_tensorflow_text_available, is_tf_available
from transformers.models.bert.tokenization_bert import BertTokenizer
from transformers.testing_utils import require_tensorflow_text, slow


if is_tensorflow_text_available():
    from transformers.models.bert import TFBertTokenizer

if is_tf_available():
    import tensorflow as tf


TOKENIZER_CHECKPOINTS = ["bert-base-uncased", "bert-base-cased"]
TINY_MODEL_CHECKPOINT = "hf-internal-testing/tiny-bert-tf-only"

if is_tf_available():

    class ModelToSave(tf.keras.Model):
        def __init__(self, tokenizer):
            super().__init__()
            self.tokenizer = tokenizer
            config = AutoConfig.from_pretrained(TINY_MODEL_CHECKPOINT)
            self.bert = TFAutoModel.from_config(config)

        def call(self, inputs):
            tokenized = self.tokenizer(inputs)
            out = self.bert(**tokenized)
            return out["pooler_output"]


@require_tensorflow_text
class BertTokenizationTest(unittest.TestCase):
    # The TF tokenizers are usually going to be used as pretrained tokenizers from existing model checkpoints,
    # so that's what we focus on here.

    def setUp(self):
        super().setUp()

        self.tokenizers = [BertTokenizer.from_pretrained(checkpoint) for checkpoint in TOKENIZER_CHECKPOINTS]
        self.tf_tokenizers = [TFBertTokenizer.from_pretrained(checkpoint) for checkpoint in TOKENIZER_CHECKPOINTS]
        self.test_sentences = [
            "This is a straightforward English test sentence.",
            "This one has some weird characters\rto\nsee\r\nif  those\u00E9break things.",
            "Now we're going to add some Chinese: 一 二 三 一二三",
            "And some much more rare Chinese: 齉 堃 齉堃",
            "Je vais aussi écrire en français pour tester les accents",
            "Classical Irish also has some unusual characters, so in they go: Gaelaċ, ꝼ",
        ]
        self.paired_sentences = list(zip(self.test_sentences, self.test_sentences[::-1]))

    def test_output_equivalence(self):
        for tokenizer, tf_tokenizer in zip(self.tokenizers, self.tf_tokenizers):
            for test_inputs in (self.test_sentences, self.paired_sentences):
                python_outputs = tokenizer(test_inputs, return_tensors="tf", padding="longest")
                tf_outputs = tf_tokenizer(test_inputs)

                for key in python_outputs.keys():
                    self.assertTrue(tf.reduce_all(python_outputs[key].shape == tf_outputs[key].shape))
                    self.assertTrue(tf.reduce_all(tf.cast(python_outputs[key], tf.int64) == tf_outputs[key]))

    @slow
    def test_different_pairing_styles(self):
        for tf_tokenizer in self.tf_tokenizers:
            merged_outputs = tf_tokenizer(self.paired_sentences)
            separated_outputs = tf_tokenizer(
                text=[sentence[0] for sentence in self.paired_sentences],
                text_pair=[sentence[1] for sentence in self.paired_sentences],
            )
            for key in merged_outputs.keys():
                self.assertTrue(tf.reduce_all(tf.cast(merged_outputs[key], tf.int64) == separated_outputs[key]))

    @slow
    def test_graph_mode(self):
        for tf_tokenizer in self.tf_tokenizers:
            compiled_tokenizer = tf.function(tf_tokenizer)
            for test_inputs in (self.test_sentences, self.paired_sentences):
```

**tool call: Bash**

```bash
python3 - <<'EOF'
p='src/transformers/models/bert/tokenization_bert_tf.py'
s=open(p).read()
s=s.replace("""from tensorflow_text import FastBertTokenizer,""","""from tensorflow_text import BertTokenizer as BertTokenizerLayer
from tensorflow_text import FastBertTokenizer,""")
s=s.replace("""            Whether to return the attention_mask.
    \"\"\"""","""            Whether to return the attention_mask.
        use_fast_bert_tokenizer (`bool`, *optional*, defaults to `True`):
            If set to false will use standard TF Text BertTokenizer, making it servable by TF Serving.
    \"\"\"""")
s=s.replace("""        return_attention_mask: bool = True,
    ):
        super().__init__()
        self.tf_tokenizer = FastBertTokenizer(
            vocab_list, token_out_type=tf.int64, lower_case_nfd_strip_accents=do_lower_case
        )
""","""        return_attention_mask: bool = True,
        use_fast_bert_tokenizer: bool = True,
    ):
        super().__init__()
        if use_fast_bert_tokenizer:
            self.tf_tokenizer = FastBertTokenizer(
                vocab_list, token_out_type=tf.int64, lower_case_nfd_strip_accents=do_lower_case
            )
        else:
            lookup_table = tf.lookup.StaticVocabularyTable(
                tf.lookup.KeyValueTensorInitializer(
                    keys=vocab_list,
                    key_dtype=tf.string,
                    values=tf.range(tf.size(vocab_list, out_type=tf.int64), dtype=tf.int64),
                    value_dtype=tf.int64,
                ),
                num_oov_buckets=1,
            )
            self.tf_tokenizer = BertTokenizerLayer(lookup_table, token_out_type=tf.int64, lower_case=do_lower_case)
""")
s=s.replace("""        self.return_attention_mask = return_attention_mask
""","""        self.return_attention_mask = return_attention_mask
        self.use_fast_bert_tokenizer = use_fast_bert_tokenizer
""",1)
s=s.replace("""            texts = case_fold_utf8(texts)
        return self.tf_tokenizer.tokenize(texts)""","""            texts = case_fold_utf8(texts)
        tokens = self.tf_tokenizer.tokenize(texts)
        # The standard BertTokenizer returns a [batch, words, wordpieces] tensor, so merge the last two dims
        return tokens.merge_dims(1, -1)""")
s=s.replace("""            "pad_token_id": self.pad_token_id,
        }""","""            "pad_token_id": self.pad_token_id,
            "use_fast_bert_tokenizer": self.use_fast_bert_tokenizer,
        }""")
open(p,'w').write(s)
EOF
git diff --stat
```

tool result:

```
 .../models/bert/tokenization_bert_tf.py            | 28 ++++++++++++++++++----
 1 file changed, 24 insertions(+), 4 deletions(-)
```

**assistant:** Now let me check both modes, comparing against the Python tokenizer (if the vocab is cached offline).

**tool call: Bash**

```bash
cat > /tmp/t.py <<'EOF'
import tensorflow as tf
from transformers import BertTokenizer
from transformers.models.bert import TFBertTokenizer
sents=["This is a straightforward English test sentence.","weird\rto\nsee\r\nif  thoseébreak things.","Chinese: 一 二 三 一二三 齉堃","Gaelaċ, ꝼ français écrire"]
pairs=list(zip(sents,sents[::-1]))
for ck in ["bert-base-uncased","bert-base-cased"]:
    try: tok=BertTokenizer.from_pretrained(ck)
    except Exception as e: print("skip",ck,e); continue
    for fast in (True,False):
        tft=TFBertTokenizer.from_pretrained(ck,use_fast_bert_tokenizer=fast)
        for inp in (sents,pairs):
            py=tok(inp,return_tensors="tf",padding="longest"); o=tft(inp); og=tf.function(tft)(tf.constant(inp))
            for k in py: assert py[k].shape==o[k].shape and bool(tf.reduce_all(tf.cast(py[k],tf.int64)==o[k])) and bool(tf.reduce_all(o[k]==og[k])),(ck,fast,k)
        print(ck,fast,"ok", tft.get_config()["use_fast_bert_tokenizer"])
EOF
cp /tmp/t.py ./_t.py; /work/huggingface__transformers-19590/bin/envrun 'HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python _t.py 2>&1 | grep -v Warning | tail -15'
```

tool result:

```
(eval):1: operation not permitted: /tmp/t.py
cp: /tmp/t.py: No such file or directory
python: can't open file '/testbed/_t.py': [Errno 2] No such file or directory
```

**tool call: Bash**

```bash
cat > _t.py <<'EOF'
import tensorflow as tf
from transformers import BertTokenizer
from transformers.models.bert import TFBertTokenizer
sents=["This is a straightforward English test sentence.","weird\rto\nsee\r\nif  thoseébreak things.","Chinese: 一 二 三 一二三 齉堃","Gaelaċ, ꝼ français écrire"]
pairs=list(zip(sents,sents[::-1]))
for ck in ["bert-base-uncased","bert-base-cased"]:
    try: tok=BertTokenizer.from_pretrained(ck)
    except Exception as e: print("skip",ck,e); continue
    for fast in (True,False):
        tft=TFBertTokenizer.from_pretrained(ck,use_fast_bert_tokenizer=fast)
        for inp in (sents,pairs):
            py=tok(inp,return_tensors="tf",padding="longest"); o=tft(inp); og=tf.function(tft)(tf.constant(inp))
            for k in py: assert py[k].shape==o[k].shape and bool(tf.reduce_all(tf.cast(py[k],tf.int64)==o[k])) and bool(tf.reduce_all(o[k]==og[k])),(ck,fast,k)
        print(ck,fast,"ok", tft.get_config()["use_fast_bert_tokenizer"])
EOF
/work/huggingface__transformers-19590/bin/envrun 'HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python _t.py 2>&1 | grep -v Warning | tail -15'
```

tool result:

```
  warnings.warn(
2026-10-09 00:05:00.305981: I tensorflow_text/core/kernels/fast_bert_normalizer_model_builder.cc:210] CharacterSet built (lower_case_nfd_strip_accents=1). Trie data size (int32): 35072. Normalized string pool size (byte): 111208
2026-10-09 00:05:00.309948: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory
2026-10-09 00:05:00.310099: W tensorflow/compiler/xla/stream_executor/cuda/cuda_driver.cc:265] failed call to cuInit: UNKNOWN ERROR (303)
2026-10-09 00:05:00.310280: I tensorflow/compiler/xla/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (ba9f199c73a4): /proc/driver/nvidia/version does not exist
2026-10-09 00:05:00.316043: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
WARNING:tensorflow:From /usr/local/lib/python3.10/site-packages/tensorflow/python/autograph/pyct/static_analysis/liveness.py:83: Analyzer.lamba_check (from tensorflow.python.autograph.pyct.static_analysis.liveness) is deprecated and will be removed after 2023-09-23.
Instructions for updating:
Lambda fuctions will be no more assumed to be used in the statement where they are used, or at least in the same block. https://github.com/tensorflow/tensorflow/issues/56089
bert-base-uncased True ok True
bert-base-uncased False ok False
2026-10-09 00:05:05.779964: I tensorflow_text/core/kernels/fast_bert_normalizer_model_builder.cc:210] CharacterSet built (lower_case_nfd_strip_accents=0). Trie data size (int32): 512. Normalized string pool size (byte): 1
bert-base-cased True ok True
bert-base-cased False ok False
```

**assistant:** Both modes match the Python tokenizer, in eager and graph mode. Now the existing test suite:

**tool call: Bash**

```bash
rm _t.py; /work/huggingface__transformers-19590/bin/envrun 'HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 RUN_SLOW=1 python -m pytest -q tests/models/bert/test_tokenization_bert_tf.py 2>&1 | tail -5; git status --short'
```

tool result:

```
-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED tests/models/bert/test_tokenization_bert_tf.py::BertTokenizationTest::test_saved_model
1 failed, 3 passed, 5 warnings in 6.38s
 M src/transformers/models/bert/tokenization_bert_tf.py
?? Dockerfile
```

**tool call: Bash**

```bash
/work/huggingface__transformers-19590/bin/envrun 'HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 RUN_SLOW=1 python -m pytest -q tests/models/bert/test_tokenization_bert_tf.py -k saved_model 2>&1 | grep -E "Error|error" | tail -5; git stash -q; HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 RUN_SLOW=1 python -m pytest -q tests/models/bert/test_tokenization_bert_tf.py 2>&1 | tail -2; git stash pop -q; git status --short'
```

tool result:

```
            if not _raise_exceptions_for_missing_entries or not _raise_exceptions_for_connection_errors:
>           raise EnvironmentError(
E           OSError: We couldn't connect to 'https://huggingface.co' to load this file, couldn't find it in the cached files and it looks like hf-internal-testing/tiny-bert-tf-only is not the path to a directory containing a file named config.json.
src/transformers/utils/hub.py:443: OSError
2026-10-09 00:05:28.382805: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory
FAILED tests/models/bert/test_tokenization_bert_tf.py::BertTokenizationTest::test_saved_model
1 failed, 3 passed, 5 warnings in 6.61s
 M src/transformers/models/bert/tokenization_bert_tf.py
?? Dockerfile
```

**assistant:** I added the option. `TFBertTokenizer` now takes a `use_fast_bert_tokenizer` argument, which defaults to `True`. Set it to `False` and the tokenizer uses TF Text's standard `BertTokenizer` instead of `FastBertTokenizer`, which should let it run on TF Serving. I couldn't test on TF Serving itself; the reasoning is that this path avoids the fast operations it doesn't support.

All changes are in `src/transformers/models/bert/tokenization_bert_tf.py`:
- **The new argument:** when it's `False`, the tokenizer looks up the vocabulary in a table built as in your snippet and handles lowercasing with `lower_case=do_lower_case`. The default behaviour is unchanged. The argument can be passed through `from_pretrained(..., use_fast_bert_tokenizer=False)` and `from_tokenizer`, and it's documented in the class docstring.
- **Matching output shape:** the standard tokenizer returns tokens grouped by word as well as by sentence, so `unpaired_tokenize` now flattens that to one list of tokens per sentence. For the fast tokenizer this step changes nothing.
- **Saving the setting:** `get_config()` now includes `use_fast_bert_tokenizer`, so a saved tokenizer keeps the setting when it's reloaded.

**Testing:** I ran both settings on `bert-base-uncased` and `bert-base-cased`, using single sentences and sentence pairs with odd characters, Chinese text and accents. Every output (`input_ids`, `attention_mask`, `token_type_ids`) matched the Python `BertTokenizer` exactly, and running under `tf.function` gave the same results. I deleted that check script afterwards.

In `tests/models/bert/test_tokenization_bert_tf.py` (run with slow tests on), 3 tests pass and `test_saved_model` fails. It fails because it needs to download `hf-internal-testing/tiny-bert-tf-only` and the container has no network. It fails the same way without my change.

The untracked `Dockerfile` in the repo isn't mine, and I left it alone.

_session end: success, turns 8, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.19 s: HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python _t.py 2>&1 | grep -v Warning | tail -15
- `rc=0` 11.93 s: HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python _t.py 2>&1 | grep -v Warning | tail -15
- `rc=0` 10.7 s: HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 RUN_SLOW=1 python -m pytest -q tests/models/bert/test_tokenization_bert_tf.py 2>&1 | tail -5; git status --short
- `rc=0` 16.01 s: HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 RUN_SLOW=1 python -m pytest -q tests/models/bert/test_tokenization_bert_tf.py -k saved_model 2>&1 | grep -E "Error|error" | tail -5; git stash -q; HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 RUN_SLOW=1 python -m pytest -q tests/models/bert/test_tokenization_bert_tf.py 2>&1 | tail -2; git stash pop -q; git status --short
