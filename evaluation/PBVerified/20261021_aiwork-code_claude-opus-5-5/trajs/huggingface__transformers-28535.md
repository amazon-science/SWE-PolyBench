# Instance: huggingface__transformers-28535
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
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
````

## Operational trajectory

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "cat src/transformers/models/esm/tokenization_esm.py"
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
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "src/transformers/models/esm/tokenization_esm.py"
  ],
  "command_sha256": [
   "268760a295c50a00a49c7b0c098b9b9b1359cf8f7fcf3f988dbab07bebd4aec1"
  ]
 },
 "_agent_context_projection": {
  "schema_version": "agent.exec_tool_result_receipt_preview.v1",
  "content_status": "partial_preview",
  "context_view_limit_bytes": 16384,
  "receipt": {
   "result_id": "tr_f5a77081019246d1893b0b7ae6554e81",
   "total_bytes": 6786,
   "total_lines": 162,
   "omitted_bytes": 1329,
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "artifact": {
   "result_id": "tr_f5a77081019246d1893b0b7ae6554e81",
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "content_preview": "{\"tool_outcome\":{\"schema_version\":1,\"tool_name\":\"exec\",\"status\":\"success\",\"exit_code\":0,\"retr\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=6689; total_bytes=6875; context_view_limit=512 bytes; context_view_strategy=head_tail_compact; guidance=preview_not_failure_outcome_neutral]...\n256\":[\"268760a295c50a00a49c7b0c098b9b9b1359cf8f7fcf3f988dbab07bebd4aec1\"]},\"duration_ms\":301}",
  "stdout": {
   "total_bytes": 6197,
   "total_lines": 162,
   "omitted_bytes": 1329,
   "preview": "# coding=utf-8\n# Copyright 2022 Meta and The HuggingFace Inc. team. All rights reserved.\n#\n# Licensed under the Apache License, Version 2.0 (the \"License\");\n# you may not use this file except in compliance with the License.\n# You may obtain a copy of the License at\n#\n#     http://www.apache.org/licenses/LICENSE-2.0\n#\n# Unless required by applicable law or agreed to in writing, software\n# distributed under the License is distributed on an \"AS IS\" BASIS,\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n# See the License for the specific language governing permissions and\n# limitations under the License.\n\"\"\"Tokenization classes for ESM.\"\"\"\nimport os\nfrom typing import List, Optional, Union\n\nfrom ...tokenization_utils import PreTrainedTokenizer\nfrom ...tokenization_utils_base import AddedToken\nfrom ...utils import logging\n\n\nlogger = logging.get_logger(__name__)\n\nVOCAB_FILES_NAMES = {\"vocab_file\": \"vocab.txt\"}\n\nPRETRAINED_VOCAB_FILES_MAP = {\n    \"vocab_file\": {\n        \"facebook/esm2_t6_8M_UR50D\": \"https://huggingface.co/facebook/esm2_t6_8M_UR50D/resolve/main/vocab.txt\",\n        \"facebook/esm2_t12_35M_UR50D\": \"https://huggingface.co/facebook/esm2_t12_35M_UR50D/resolve/main/vocab.txt\",\n    },\n}\n\nPRETRAINED_POSITIONAL_EMBEDDINGS_SIZES = {\n    \"facebook/esm2_t6_8M_UR50D\": 1024,\n    \"facebook/esm2_t12_35M_UR50D\": 1024,\n}\n\n\ndef load_vocab_file(vocab_file):\n    with open(vocab_file, \"r\") as f:\n        lines = f.read().splitlines()\n        return [l.strip() for l in lines]\n\n\nclass EsmTokenizer(PreTrainedTokenizer):\n    \"\"\"\n    Constructs an ESM tokenizer.\n    \"\"\"\n\n    vocab_files_names = VOCAB_FILES_NAMES\n    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP\n    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES\n    model_input_names = [\"input_ids\", \"attention_mask\"]\n\n    def __init__(\n        self,\n        vocab_file,\n        unk_token=\"<unk>\",\n        cls_token=\"<cls>\",\n        pad_token=\"<pad>\",\n        mask_token=\"<mask>\",\n        eos_token=\"<eos>\",\n        **kwargs,\n    ):\n        self.all_tokens = load_vocab_file(vocab_file)\n        self._id_to_token = dict(enumerate(self.all_tokens))\n        self._token_to_id = {tok: ind for ind, tok in enumerate(self.all_tokens)}\n        super().__init__(\n            unk_token=unk_token,\n            cls_token=cls_token,\n            pad_token=pad_token,\n            mask_token=mask_token,\n            eos_token=eos_token,\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=1329; total_bytes=6197; context_view_limit=5461 bytes; context_view_strategy=head_tail_v2; preserved_ranges=0..2434,3763..6197; model_guidance=this tool result was delivered and the visible content is a bounded preview, not evidence by itself that the read or command failed; continuation_hint=use read/exec with explicit offset/limit or rerun the command with narrower filters to inspect the omitted range]...\ns None:\n            if self.eos_token_id is None:\n                return cls + token_ids_0\n            else:\n                return cls + token_ids_0 + sep\n        elif self.eos_token_id is None:\n            raise ValueError(\"Cannot tokenize multiple sequences when EOS token is not set!\")\n        return cls + token_ids_0 + sep + token_ids_1 + sep  # Multiple inputs always have an EOS token\n\n    def get_special_tokens_mask(\n        self, token_ids_0: List, token_ids_1: Optional[List] = None, already_has_special_tokens: bool = False\n    ) -> List[int]:\n        \"\"\"\n        Retrieves sequence ids from a token list that has no special tokens added. This method is called when adding\n        special tokens using the tokenizer `prepare_for_model` or `encode_plus` methods.\n\n        Args:\n            token_ids_0 (`List[int]`):\n                List of ids of the first sequence.\n            token_ids_1 (`List[int]`, *optional*):\n                List of ids of the second sequence.\n            already_has_special_tokens (`bool`, *optional*, defaults to `False`):\n                Whether or not the token list is already formatted with special tokens for the model.\n\n        Returns:\n            A list of integers in the range [0, 1]: 1 for a special token, 0 for a sequence token.\n        \"\"\"\n        if already_has_special_tokens:\n            if token_ids_1 is not None:\n                raise ValueError(\n                    \"You should not supply a second sequence if the provided sequence of \"\n                    \"ids is already formatted with special tokens for the model.\"\n                )\n\n            return [1 if token in self.all_special_ids else 0 for token in token_ids_0]\n        mask = [1] + ([0] * len(token_ids_0)) + [1]\n        if token_ids_1 is not None:\n            mask += [0] * len(token_ids_1) + [1]\n        return mask\n\n    def save_vocabulary(self, save_directory, filename_prefix):\n        vocab_file = os.path.join(save_directory, (filename_prefix + \"-\" if filename_prefix else \"\") + \"vocab.txt\")\n        with open(vocab_file, \"w\") as f:\n            f.write(\"\\n\".join(self.all_tokens))\n        return (vocab_file,)\n\n    @property\n    def vocab_size(self) -> int:\n        return self.get_vocab_size(with_added_tokens=False)\n\n    def _add_tokens(self, new_tokens: Union[List[str], List[AddedToken]], special_tokens: bool = False) -> int:\n        return super()._add_tokens(new_tokens, special_tokens=True)\n"
  }
 }
}
````

### Turn 2 — tool call call_0002 (exec)

````json
{
 "command": "sed -n 75,110p src/transformers/models/esm/tokenization_esm.py; grep -n \"def __len__\\|def get_vocab\\b\\|def get_vocab(\" -A8 src/transformers/tokenization_utils.py | head -40"
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
 "stdout": "            eos_token=eos_token,\n            **kwargs,\n        )\n\n        # TODO, all the tokens are added? But they are also part of the vocab... bit strange.\n        # none of them are special, but they all need special splitting.\n\n        self.unique_no_split_tokens = self.all_tokens\n        self._update_trie(self.unique_no_split_tokens)\n\n    def _convert_id_to_token(self, index: int) -> str:\n        return self._id_to_token.get(index, self.unk_token)\n\n    def _convert_token_to_id(self, token: str) -> int:\n        return self._token_to_id.get(token, self._token_to_id.get(self.unk_token))\n\n    def _tokenize(self, text, **kwargs):\n        return text.split()\n\n    def get_vocab_size(self, with_added_tokens=False):\n        return len(self._id_to_token)\n\n    def get_vocab(self):\n        return {token: i for i, token in enumerate(self.all_tokens)}\n\n    def token_to_id(self, token: str) -> int:\n        return self._token_to_id.get(token, self._token_to_id.get(self.unk_token))\n\n    def id_to_token(self, index: int) -> str:\n        return self._id_to_token.get(index, self.unk_token)\n\n    def build_inputs_with_special_tokens(\n        self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None\n    ) -> List[int]:\n        cls = [self.cls_token_id]\n        sep = [self.eos_token_id]  # No sep token in ESM vocabulary\n426:    def __len__(self):\n427-        \"\"\"\n428-        Size of the full vocabulary with the added tokens. Counts the `keys` and not the `values` because otherwise if\n429-        there is a hole in the vocab, we will add tokenizers at a wrong index.\n430-        \"\"\"\n431-        return len(set(self.get_vocab().keys()))\n432-\n433-    def _add_tokens(self, new_tokens: Union[List[str], List[AddedToken]], special_tokens: bool = False) -> int:\n434-        \"\"\"\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 112,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "src/transformers/models/esm/tokenization_esm.py",
   "src/transformers/tokenization_utils.py"
  ],
  "command_sha256": [
   "74a94b083ad50f3f48744b7d131f975d9c1c70b7af26391e09e92d3812e8f267"
  ]
 }
}
````

### Turn 3 — thinking

````text
I should fix get_vocab to merge in the added tokens encoder alongside the base vocab, and recall how the upstream ESM tokenizer actually builds its vocab by enumerating all_tokens—that might be the simpler correct approach to mirror.
````

### Turn 3 — tool call call_0003 (exec)

````json
{
 "command": "python - <<'EOF'\nimport re\np='src/transformers/models/esm/tokenization_esm.py'\ns=open(p).read()\ns=s.replace(\"\"\"    def get_vocab(self):\n        return {token: i for i, token in enumerate(self.all_tokens)}\n\"\"\",\"\"\"    def get_vocab(self):\n        base_vocab = {token: i for i, token in enumerate(self.all_tokens)}\n        base_vocab.update(self.added_tokens_encoder)\n        return base_vocab\n\"\"\")\ns=s.replace(\"\"\"\n    def _add_tokens(self, new_tokens: Union[List[str], List[AddedToken]], special_tokens: bool = False) -> int:\n        return super()._add_tokens(new_tokens, special_tokens=True)\n\"\"\",\"\")\nopen(p,'w').write(s)\nEOF\ngrep -n \"AddedToken\\|Union\" src/transformers/models/esm/tokenization_esm.py"
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
 "stdout": "17:from typing import List, Optional, Union\n20:from ...tokenization_utils_base import AddedToken\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 169,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "src/transformers/models/esm/tokenization_esm.py"
  ],
  "command_sha256": [
   "bcc4c0c335a87c99d1e4dfc9397054e490c407c8e690185abf8b69c728d071e4"
  ]
 }
}
````

### Turn 4 — assistant text

Remove now-unused imports, then test.

### Turn 4 — tool call call_0004 (exec)

````json
{
 "command": "sed -i 's/^from typing import List, Optional, Union$/from typing import List, Optional/; /^from ...tokenization_utils_base import AddedToken$/d' src/transformers/models/esm/tokenization_esm.py\npython - <<'EOF'\nimport tempfile,os\nfrom transformers import EsmTokenizer\nd=tempfile.mkdtemp(); f=os.path.join(d,'vocab.txt')\nopen(f,'w').write(\"\\n\".join([\"<cls>\",\"<pad>\",\"<eos>\",\"<unk>\",\"L\",\"A\",\"G\",\"V\",\"<mask>\"]))\nt=EsmTokenizer(f); print(len(t))\nprint(t.add_tokens(['J'],special_tokens=False), len(t), t.all_special_tokens, t.added_tokens_decoder[len(t)-1])\nprint(t.add_tokens(['<z>'],special_tokens=True), len(t), t.all_special_tokens)\nprint(t.encode(\"L J A <z>\"), t.tokenize(\"LJA\"))\nEOF\npython -m pytest tests/models/esm/test_tokenization_esm.py -q 2>&1 | tail -3"
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
 "stdout": "9\n1 10 ['<eos>', '<unk>', '<pad>', '<cls>', '<mask>'] J\n1 11 ['<eos>', '<unk>', '<pad>', '<cls>', '<mask>', '<z>']\n[0, 4, 9, 5, 10, 2] ['L', 'J', 'A']\n-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html\n5 passed, 3 warnings in 1.07s\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 12072,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "write",
    "paths": [
     "src/transformers/models/esm/tokenization_esm.py"
    ]
   }
  ],
  "reads": [],
  "command_sha256": [
   "9ebfd1f434dd5c6a2b87d75a9a91243177652a50063fecf20639d3716cd5160e"
  ]
 }
}
````

### Turn 5 — assistant text

I fixed the ESM tokenizer bug in `src/transformers/models/esm/tokenization_esm.py`. `add_tokens(['J'], special_tokens=False)` now adds `J` as a normal token, and `len(tokenizer)` goes up by one, so `model.resize_token_embeddings(len(tokenizer))` will grow the embedding layer.

There were two causes:
- **Tokens forced to special:** `EsmTokenizer` overrode `_add_tokens` to always pass `special_tokens=True`, ignoring what you asked for. I removed that override so the base class handles `special_tokens` normally. I also removed the imports this left unused.
- **Length not changing:** `get_vocab()` only returned the original vocabulary file's tokens, and `len(tokenizer)` is computed from `get_vocab()`. It now includes the added tokens too.

I tested it with a small vocabulary file I made up, not the real `facebook/esm2_t6_8M_UR50D` vocabulary, and didn't run an actual model resize:
- The length went from 9 to 10 after adding `J` as a normal token, and `J` was not in `all_special_tokens`.
- Adding `<z>` with `special_tokens=True` still made it a special token, and the length went to 11.
- Encoding text containing `J` gave it its new id, and `"LJA"` still splits into `['L', 'J', 'A']`.
- The existing ESM tokenizer tests pass (`tests/models/esm/test_tokenization_esm.py`, 5 passed).

### Turn 6 — assistant text

I fixed the ESM tokenizer so new tokens added with `special_tokens=False` stay normal tokens, and `len(tokenizer)` now goes up after they're added. That means `model.resize_token_embeddings(len(tokenizer))` will now grow the embedding layer.

There were two causes, both in `src/transformers/models/esm/tokenization_esm.py`:

1. **Tokens always marked special:** `EsmTokenizer` overrode `_add_tokens` and always passed `special_tokens=True`, ignoring the caller's setting. I removed that override, along with the `Union` and `AddedToken` imports that were only used by it.
2. **Length not changing:** `get_vocab()` only returned the tokens from `vocab.txt`, so added tokens weren't counted by `__len__`. It now includes the added tokens as well.

I checked it with a small vocabulary that has 9 tokens:
- Adding `J` with `special_tokens=False` raised the length from 9 to 10, and `J` did not appear in `all_special_tokens`.
- Adding `<z>` with `special_tokens=True` raised the length to 11, and `<z>` did appear in `all_special_tokens`.
- Encoding and tokenizing text containing `J` gave it its own ID (`"LJA"` → `['L', 'J', 'A']`).
- The existing ESM tokenizer tests pass (`tests/models/esm/test_tokenization_esm.py`: 5 passed).

I didn't test with the real `facebook/esm2_t6_8M_UR50D` download or run the model's `resize_token_embeddings` step.

## Final answer

I fixed the ESM tokenizer so new tokens added with `special_tokens=False` stay normal tokens, and `len(tokenizer)` now goes up after they're added. That means `model.resize_token_embeddings(len(tokenizer))` will now grow the embedding layer.

There were two causes, both in `src/transformers/models/esm/tokenization_esm.py`:

1. **Tokens always marked special:** `EsmTokenizer` overrode `_add_tokens` and always passed `special_tokens=True`, ignoring the caller's setting. I removed that override, along with the `Union` and `AddedToken` imports that were only used by it.
2. **Length not changing:** `get_vocab()` only returned the tokens from `vocab.txt`, so added tokens weren't counted by `__len__`. It now includes the added tokens as well.

I checked it with a small vocabulary that has 9 tokens:
- Adding `J` with `special_tokens=False` raised the length from 9 to 10, and `J` did not appear in `all_special_tokens`.
- Adding `<z>` with `special_tokens=True` raised the length to 11, and `<z>` did appear in `all_special_tokens`.
- Encoding and tokenizing text containing `J` gave it its own ID (`"LJA"` → `['L', 'J', 'A']`).
- The existing ESM tokenizer tests pass (`tests/models/esm/test_tokenization_esm.py`: 5 passed).

I didn't test with the real `facebook/esm2_t6_8M_UR50D` download or run the model's `resize_token_embeddings` step.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 102125 | 2494 | 92645 | 9464 | 104619 |
