# Instance: huggingface__transformers-28535

- Final resolved (evaluator, logs/huggingface__transformers-28535_result.json): True
- Run state: DONE
- One attempt. Duration 40.3 s, turns 7, actor cost $0.1699194, container commands 3
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/huggingface__transformers-28535/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-28535/repo. Consider the following issue description:

<issue_description>
Issue with Adding New Tokens to ESM2 Model Tokenizer
Hello

I am encountering an issue while working with the ESM2 models (`facebook/esm2_t6_8M_UR50D`). Specifically, when I try to add new tokens to the tokenizer, they are automatically classified as special tokens, even though I am specifying `special_tokens=False`.

Here is the code snippet I am using:

```python
model_checkpoint = "facebook/esm2_t6_8M_UR50D"
model = AutoModelForMaskedLM.from_pretrained(model_checkpoint)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
num_added_toks = tokenizer.add_tokens(['J'], special_tokens=False)
print("We have added", num_added_toks, "tokens")
model.resize_token_embeddings(len(tokenizer))
```

After executing this code, the new token ('J') is added as a special token, which is not the intended behavior. This behavior is different compared to when I use similar code with BERT models, where new tokens are added as expected without being automatically marked as special.

The vocab output is below:
```python
<bound method EsmTokenizer.get_vocab of EsmTokenizer(name_or_path=‘facebook/esm2_t6_8M_UR50D’, vocab_size=33, model_max_length=1024, is_fast=False, padding_side=‘right’, truncation_side=‘right’, special_tokens={‘eos_token’: ‘’, ‘unk_token’: ‘’, ‘pad_token’: ‘’, ‘cls_token’: ‘’, ‘mask_token’: ‘’, ‘additional_special_tokens’: [‘J’]}, clean_up_tokenization_spaces=True), added_tokens_decoder={
0: AddedToken(“”, rstrip=False, lstrip=False, single_word=False, normalized=False, special=True),
1: AddedToken(“”, rstrip=False, lstrip=False, single_word=False, normalized=False, special=True),
2: AddedToken(“”, rstrip=False, lstrip=False, single_word=False, normalized=False, special=True),
3: AddedToken(“”, rstrip=False, lstrip=False, single_word=False, normalized=False, special=True),
32: AddedToken(“”, rstrip=False, lstrip=False, single_word=False, normalized=False, special=True),
33: AddedToken(“J”, rstrip=False, lstrip=False, single_word=False, normalized=False, special=True),
}>
```
My main problem is that I noticed the **length of the tokenizer** does not change after adding the new token and therefore the above code does not extend the embeddings layer as expected.

I'm seeking guidance or a workaround for this issue. Is this a known issue with the ESM2 tokenizer, or am I missing something in my implementation?

Any help or insight into this matter would be greatly appreciated.

Thank you!


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-28535/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-28535/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-28535/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-28535/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cat src/transformers/models/esm/tokenization_esm.py
```

tool result:

```
# coding=utf-8
# Copyright 2022 Meta and The HuggingFace Inc. team. All rights reserved.
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
"""Tokenization classes for ESM."""
import os
from typing import List, Optional, Union

from ...tokenization_utils import PreTrainedTokenizer
from ...tokenization_utils_base import AddedToken
from ...utils import logging


logger = logging.get_logger(__name__)

VOCAB_FILES_NAMES = {"vocab_file": "vocab.txt"}

PRETRAINED_VOCAB_FILES_MAP = {
    "vocab_file": {
        "facebook/esm2_t6_8M_UR50D": "https://huggingface.co/facebook/esm2_t6_8M_UR50D/resolve/main/vocab.txt",
        "facebook/esm2_t12_35M_UR50D": "https://huggingface.co/facebook/esm2_t12_35M_UR50D/resolve/main/vocab.txt",
    },
}

PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES = {
    "facebook/esm2_t6_8M_UR50D": 1024,
    "facebook/esm2_t12_35M_UR50D": 1024,
}


def load_vocab_file(vocab_file):
    with open(vocab_file, "r") as f:
        lines = f.read().splitlines()
        return [l.strip() for l in lines]


class EsmTokenizer(PreTrainedTokenizer):
    """
    Constructs an ESM tokenizer.
    """

    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    model_input_names = ["input_ids", "attention_mask"]

    def __init__(
        self,
        vocab_file,
        unk_token="<unk>",
        cls_token="<cls>",
        pad_token="<pad>",
        mask_token="<mask>",
        eos_token="<eos>",
        **kwargs,
    ):
        self.all_tokens = load_vocab_file(vocab_file)
        self._id_to_token = dict(enumerate(self.all_tokens))
        self._token_to_id = {tok: ind for ind, tok in enumerate(self.all_tokens)}
        super().__init__(
            unk_token=unk_token,
            cls_token=cls_token,
            pad_token=pad_token,
            mask_token=mask_token,
            eos_token=eos_token,
            **kwargs,
        )

        # TODO, all the tokens are added? But they are also part of the vocab... bit strange.
        # none of them are special, but they all need special splitting.

        self.unique_no_split_tokens = self.all_tokens
        self._update_trie(self.unique_no_split_tokens)

    def _convert_id_to_token(self, index: int) -> str:
        return self._id_to_token.get(index, self.unk_token)

    def _convert_token_to_id(self, token: str) -> int:
        return self._token_to_id.get(token, self._token_to_id.get(self.unk_token))

    def _tokenize(self, text, **kwargs):
        return text.split()

    def get_vocab_size(self, with_added_tokens=False):
        return len(self._id_to_token)

    def get_vocab(self):
        return {token: i for i, token in enumerate(self.all_tokens)}

    def token_to_id(self, token: str) -> int:
        return self._token_to_id.get(token, self._token_to_id.get(self.unk_token))

    def id_to_token(self, index: int) -> str:
        return self._id_to_token.get(index, self.unk_token)

    def build_inputs_with_special_tokens(
        self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None
    ) -> List[int]:
        cls = [self.cls_token_id]
        sep = [self.eos_token_id]  # No sep token in ESM vocabulary
        if token_ids_1 is None:
            if self.eos_token_id is None:
                return cls + token_ids_0
            else:
                return cls + token_ids_0 + sep
        elif self.eos_token_id is None:
            raise ValueError("Cannot tokenize multiple sequences when EOS token is not set!")
        return cls + token_ids_0 + sep + token_ids_1 + sep  # Multiple inputs always have an EOS token

    def get_special_tokens_mask(
        self, token_ids_0: List, token_ids_1: Optional[List] = None, already_has_special_tokens: bool = False
    ) -> List[int]:
        """
        Retrieves sequence ids from a token list that has no special tokens added. This method is called when adding
        special tokens using the tokenizer `prepare_for_model` or `encode_plus` methods.

        Args:
            token_ids_0 (`List[int]`):
                List of ids of the first sequence.
            token_ids_1 (`List[int]`, *optional*):
                List of ids of the second sequence.
            already_has_special_tokens (`bool`, *optional*, defaults to `False`):
                Whether or not the token list is already formatted with special tokens for the model.

        Returns:
            A list of integers in the range [0, 1]: 1 for a special token, 0 for a sequence token.
        """
        if already_has_special_tokens:
            if token_ids_1 is not None:
                raise ValueError(
                    "You should not supply a second sequence if the provided sequence of "
                    "ids is already formatted with special tokens for the model."
                )

            return [1 if token in self.all_special_ids else 0 for token in token_ids_0]
        mask = [1] + ([0] * len(token_ids_0)) + [1]
        if token_ids_1 is not None:
            mask += [0] * len(token_ids_1) + [1]
        return mask

    def save_vocabulary(self, save_directory, filename_prefix):
        vocab_file = os.path.join(save_directory, (filename_prefix + "-" if filename_prefix else "") + "vocab.txt")
        with open(vocab_file, "w") as f:
            f.write("\n".join(self.all_tokens))
        return (vocab_file,)

    @property
    def vocab_size(self) -> int:
        return self.get_vocab_size(with_adde
[... 196 more characters not shown]
```

**tool call: Bash**

```bash
grep -n "add_tokens\|special" -A3 tests/models/esm/test_tokenization_esm.py | head -60; ls ~/.cache 2>/dev/null
```

tool result:

```
Exit code 1
75:    def test_tokenize_special_tokens(self):
76:        """Test `tokenize` with special tokens."""
77-        tokenizers = self.get_tokenizers(fast=True)
78-        for tokenizer in tokenizers:
79-            with self.subTest(f"{tokenizer.__class__.__name__}"):
```

**assistant:** Let me reproduce with a local vocab file.

**tool call: Bash**

```bash
cat > repro_esm.py <<'EOF'
import tempfile, os
from transformers import EsmTokenizer
d = tempfile.mkdtemp()
vocab = ["<cls>","<pad>","<eos>","<unk>","L","A","G","V","S","E","R","T","I","D","P","K","Q","N","F","Y","M","H","W","C","X","B","U","Z","O",".","-","<null_1>","<mask>"]
open(os.path.join(d,"vocab.txt"),"w").write("\n".join(vocab))
tok = EsmTokenizer(os.path.join(d,"vocab.txt"))
print(len(tok))
n = tok.add_tokens(["J"], special_tokens=False)
print(n, len(tok), tok.all_special_tokens, tok.added_tokens_decoder[33])
print(tok.get_vocab().get("J"), tok.tokenize("LAJG"), tok("LAJG").input_ids)
tok.add_special_tokens({"additional_special_tokens": ["<new>"]})
print(len(tok), tok.all_special_tokens, tok.tokenize("L<new>A"))
tok.save_pretrained(d+"/out"); t2 = EsmTokenizer.from_pretrained(d+"/out")
print(len(t2), t2.tokenize("LAJG<new>"), t2("LAJG").input_ids)
EOF
../bin/envrun 'python repro_esm.py'
```

tool result:

```
33
1 33 ['<eos>', '<unk>', '<pad>', '<cls>', '<mask>', 'J'] J
None ['L', 'A', 'J', 'G'] [0, 4, 5, 33, 6, 2]
33 ['<eos>', '<unk>', '<pad>', '<cls>', '<mask>', '<new>'] ['L', '<new>', 'A']
33 ['L', 'A', 'J', 'G', '<new>'] [0, 4, 5, 3, 6, 2]
```

**thinking:**

```
Confirmed the bug: tokens are forced special, `len()` stays unchanged since `get_vocab()` ignores added tokens, and reloaded tokens map to `<unk>`. I'll now fix `get_vocab` and remove the `_add_tokens` override.


```

**tool call: Bash**

```bash
python3 - <<'EOF'
p='src/transformers/models/esm/tokenization_esm.py'
s=open(p).read()
s=s.replace('''    def get_vocab(self):
        return {token: i for i, token in enumerate(self.all_tokens)}
''','''    def get_vocab(self):
        base_vocab = {token: i for i, token in enumerate(self.all_tokens)}
        base_vocab.update(self.added_tokens_encoder)
        return base_vocab
''')
s=s.replace('''

    def _add_tokens(self, new_tokens: Union[List[str], List[AddedToken]], special_tokens: bool = False) -> int:
        return super()._add_tokens(new_tokens, special_tokens=True)''','')
s=s.replace("from typing import List, Optional, Union","from typing import List, Optional")
s=s.replace("from ...tokenization_utils_base import AddedToken\n","")
open(p,'w').write(s)
EOF
git diff --stat; ../bin/envrun 'python repro_esm.py'
```

tool result:

```
 setup.py                                        |  2 +-
 src/transformers/models/esm/tokenization_esm.py | 10 ++++------
 2 files changed, 5 insertions(+), 7 deletions(-)
33
1 34 ['<eos>', '<unk>', '<pad>', '<cls>', '<mask>'] J
33 ['L', 'A', 'J', 'G'] [0, 4, 5, 33, 6, 2]
35 ['<eos>', '<unk>', '<pad>', '<cls>', '<mask>', '<new>'] ['L', '<new>', 'A']
Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
35 ['L', 'A', 'J', 'G', '<new>'] [0, 4, 5, 33, 6, 2]
```

**assistant:** Everything works now. `setup.py` shows up in the diff, though, and I didn't touch it — let me check.

**tool call: Bash**

```bash
git diff setup.py
```

tool result:

```
diff --git a/setup.py b/setup.py
index 65b84fe93..60321c925 100644
--- a/setup.py
+++ b/setup.py
@@ -97,7 +97,7 @@ if stale_egg_info.exists():
 _deps = [
     "Pillow>=10.0.1,<=15.0",
     "accelerate>=0.21.0",
-    "av==9.2.0",  # Latest version of PyAV (10.0.0) has issues with audio stream.
+    "av==10.0.0",  # Latest version of PyAV (10.0.0) has issues with audio stream.
     "beautifulsoup4",
     "codecarbon==1.2.0",
     "cookiecutter==1.7.3",
```

**assistant:** That `setup.py` change came from the environment setup, not from me. I'll leave it alone. Now the ESM tests:

**tool call: Bash**

```bash
rm repro_esm.py; ../bin/envrun 'python -m pytest tests/models/esm/test_tokenization_esm.py -q 2>&1 | tail -5'
```

tool result:

```
  <frozen importlib._bootstrap>:241: DeprecationWarning: builtin type SwigPyObject has no __module__ attribute

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
5 passed, 3 warnings in 1.09s
sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
```

**assistant:** I fixed the ESM tokenizer so that `add_tokens(..., special_tokens=False)` adds an ordinary token and `len(tokenizer)` grows. That means `model.resize_token_embeddings(len(tokenizer))` now extends the embeddings as expected. The 5 existing ESM tokenizer tests pass.

**What was wrong**, in `src/transformers/models/esm/tokenization_esm.py`:
1. The tokenizer overrode `_add_tokens` and always passed `special_tokens=True`, so your `special_tokens=False` was ignored and every new token became special.
2. `get_vocab()` only returned the tokens from `vocab.txt`. The tokenizer's length is computed from `get_vocab()`, so added tokens never counted and the length stayed at 33.

**Changes:**
- Removed the `_add_tokens` override, so the standard behaviour applies.
- `get_vocab()` now includes added tokens as well as the base vocabulary.
- Removed the two imports that only the override used.

**Checked with a throwaway script** built on a local copy of the 33-token ESM2 vocab (no network here, so not the real checkpoint):
- **Before:** after `add_tokens(['J'], special_tokens=False)`, `len` stayed 33 and `J` was listed as a special token. After save and reload, `J` turned into `<unk>` (id 3).
- **After:** `len` becomes 34, `J` is a normal token with id 33, and `"LAJG"` encodes to `[0, 4, 5, 33, 6, 2]`. Adding a real special token with `add_special_tokens` still works and raises `len` to 35. After save and reload, everything is unchanged and `J` keeps id 33.

I deleted the script afterwards.

**Unrelated diff:** `git diff` also shows a change in `setup.py` (`av==9.2.0` → `av==10.0.0`) that I didn't make. It looks like it came from the environment setup, so I left it alone. You may want to keep it out of any commit.

_session end: success, turns 7, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 2.84 s: python repro_esm.py
- `rc=0` 2.67 s: python repro_esm.py
- `rc=0` 8.12 s: python -m pytest tests/models/esm/test_tokenization_esm.py -q 2>&1 | tail -5
