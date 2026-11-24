# Instance: huggingface__transformers-6098
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
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
````

## Operational trajectory

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "cat src/transformers/tokenization_bart.py | sed -n 80,200p; grep -n \"mask\\|fairseq_offset\\|def vocab_size\" src/transformers/tokenization_xlm_roberta.py"
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
   "src/transformers/tokenization_bart.py",
   "src/transformers/tokenization_xlm_roberta.py"
  ],
  "command_sha256": [
   "1fc91cdc4c4b7f0ad94852f1024eea66f4b4fdb3b8d491116acbc34e6419eae9"
  ]
 },
 "_agent_context_projection": {
  "schema_version": "agent.exec_tool_result_receipt_preview.v1",
  "content_status": "partial_preview",
  "context_view_limit_bytes": 16384,
  "receipt": {
   "result_id": "tr_12be2042f81645aa8ea8b822b0eb3c5e",
   "total_bytes": 7323,
   "total_lines": 134,
   "omitted_bytes": 1533,
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "artifact": {
   "result_id": "tr_12be2042f81645aa8ea8b822b0eb3c5e",
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "content_preview": "{\"tool_outcome\":{\"schema_version\":1,\"tool_name\":\"exec\",\"status\":\"success\",\"exit_code\":0,\"retr\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=6951; total_bytes=7137; context_view_limit=512 bytes; context_view_strategy=head_tail_compact; guidance=preview_not_failure_outcome_neutral]...\n.py\"],\"command_sha256\":[\"1fc91cdc4c4b7f0ad94852f1024eea66f4b4fdb3b8d491116acbc34e6419eae9\"]}}",
  "stdout": {
   "total_bytes": 6401,
   "total_lines": 134,
   "omitted_bytes": 1533,
   "preview": "    \"nl_XX\",\n    \"ro_RO\",\n    \"ru_RU\",\n    \"si_LK\",\n    \"tr_TR\",\n    \"vi_VN\",\n    \"zh_CN\",\n]\n\n\nclass MBartTokenizer(XLMRobertaTokenizer):\n    \"\"\"\n    This inherits from XLMRobertaTokenizer. ``prepare_translation_batch`` should be used to encode inputs.\n    Other tokenizer methods like ``encode`` do not work properly.\n    The tokenization method is ``<tokens> <eos> <language code>`` for source language documents, and\n    ``<language code> <tokens> <eos>``` for target language documents.\n\n    Examples::\n\n        >>> from transformers import MBartTokenizer\n        >>> tokenizer = MBartTokenizer.from_pretrained('facebook/mbart-large-en-ro')\n        >>> example_english_phrase = \" UN Chief Says There Is No Military Solution in Syria\"\n        >>> expected_translation_romanian = \"Şeful ONU declară că nu există o soluţie militară în Siria\"\n        >>> batch: dict = tokenizer.prepare_translation_batch(\n        ...     example_english_phrase, src_lang=\"en_XX\", tgt_lang=\"ro_RO\", tgt_texts=expected_translation_romanian\n        ... )\n\n    \"\"\"\n\n    vocab_files_names = {\"vocab_file\": \"sentencepiece.bpe.model\"}\n    max_model_input_sizes = {m: 1024 for m in _all_mbart_models}\n    pretrained_vocab_files_map = {\"vocab_file\": {m: SPM_URL for m in _all_mbart_models}}\n\n    prefix_tokens: List[int] = []\n    suffix_tokens: List[int] = []\n\n    def __init__(self, *args, **kwargs):\n        super().__init__(*args, **kwargs)\n\n        self.sp_model_size = len(self.sp_model)\n        self.lang_code_to_id = {\n            code: self.sp_model_size + i + self.fairseq_offset for i, code in enumerate(FAIRSEQ_LANGUAGE_CODES)\n        }\n        self.id_to_lang_code = {v: k for k, v in self.lang_code_to_id.items()}\n        self.cur_lang_code = self.lang_code_to_id[\"en_XX\"]\n\n        self.fairseq_tokens_to_ids.update(self.lang_code_to_id)\n        self.fairseq_ids_to_tokens = {v: k for k, v in self.fairseq_tokens_to_ids.items()}\n        self._additional_special_tokens = list(self.lang_code_to_id.keys())\n        self.set_src_lang_special_tokens(kwargs.get(\"src_lang\", \"en_XX\"))\n\n    def build_inputs_with_special_tokens(\n        self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None\n    ) -> List[int]:\n        \"\"\"\n        Build model inputs from a sequence or a pair of sequence for sequence classification tasks\n        by concatenating and adding special tokens. The special tokens depend on calling set_lang.\n        A\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=1533; total_bytes=6401; context_view_limit=5461 bytes; context_view_strategy=head_tail_v2; preserved_ranges=0..2434,3967..6401; model_guidance=this tool result was delivered and the visible content is a bounded preview, not evidence by itself that the read or command failed; continuation_hint=use read/exec with explicit offset/limit or rerun the command with narrower filters to inspect the omitted range]...\nids_1 (:obj:`List[int]`, `optional`, defaults to :obj:`None`):\n                Optional second list of IDs for sequence pairs.\n            already_has_special_tokens (:obj:`bool`, `optional`, defaults to :obj:`False`):\n                Set to True if the token list is already formatted with special tokens for the model\n\n        Returns:\n            :obj:`List[int]`: A list of integers in the range [0, 1]: 1 for a special token, 0 for a sequence token.\n        \"\"\"\n\n        if already_has_special_tokens:\n            if token_ids_1 is not None:\n                raise ValueError(\n                    \"You should not supply a second sequence if the provided sequence of \"\n                    \"ids is already formated with special tokens for the model.\"\n                )\n            return list(map(lambda x: 1 if x in [self.sep_token_id, self.cls_token_id] else 0, token_ids_0))\n        prefix_ones = [1] * len(self.prefix_tokens)\n        suffix_ones = [1] * len(self.suffix_tokens)\n        if token_ids_1 is None:\n            return prefix_ones + ([0] * len(token_ids_0)) + suffix_ones\n        return prefix_ones + ([0] * len(token_ids_0)) + ([0] * len(token_ids_1)) + suffix_ones\n\n    def prepare_translation_batch(\n        self,\n        src_texts: List[str],\n        src_lang: str = \"en_XX\",\n        tgt_texts: Optional[List[str]] = None,\n        tgt_lang: str = \"ro_RO\",\n        max_length: Optional[int] = None,\n        max_target_length: Optional[int] = None,\n        padding: str = \"longest\",\n        return_tensors: str = \"pt\",\n        **kwargs,\n    ) -> BatchEncoding:\n92:        mask_token (:obj:`string`, `optional`, defaults to \"<mask>\"):\n93:            The token used for masking values. This is the token used when training this model with masked language\n106:    model_input_names = [\"attention_mask\"]\n117:        mask_token=\"<mask>\",\n127:            mask_token=mask_token,\n154:        self.fairseq_offset = 1\n156:        self.fairseq_tokens_to_ids[\"<mask>\"] = len(self.sp_model) + self.fairseq_offset\n204:    def get_special_tokens_mask(\n239:        Creates a mask from the two sequences passed to be used in a sequence-pair classification task.\n261:    def vocab_size(self):\n262:        return len(self.sp_model) + self.fairseq_offset + 1  # Add the <mask> token\n279:        return spm_id + self.fairseq_offset if spm_id else self.unk_token_id\n285:        return self.sp_model.IdToPiece(index - self.fairseq_offset)\n"
  }
 }
}
````

### Turn 2 — thinking

````text
I need to fix the mask token id calculation to properly account for the sp_model length, lang_code_to_id length, and offset combined, matching the upstream fix for MBart's tokenizer initialization.
````

### Turn 2 — tool call call_0002 (exec)

````json
{
 "command": "grep -n \"vocab_size\\|get_vocab\" src/transformers/tokenization_bart.py src/transformers/tokenization_xlm_roberta.py"
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
 "stdout": "src/transformers/tokenization_xlm_roberta.py:261:    def vocab_size(self):\nsrc/transformers/tokenization_xlm_roberta.py:264:    def get_vocab(self):\nsrc/transformers/tokenization_xlm_roberta.py:265:        vocab = {self.convert_ids_to_tokens(i): i for i in range(self.vocab_size)}\n",
 "device_targets": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "src/transformers/tokenization_bart.py",
   "src/transformers/tokenization_xlm_roberta.py"
  ],
  "command_sha256": [
   "184cfc2dcf4cbc3ca32955a792611085c171dcdffd0b4620d063e8efcb1d98ae"
  ]
 },
 "duration_ms": 57
}
````

### Turn 3 — tool call call_0003 (edit)

````json
{
 "file_path": "src/transformers/tokenization_bart.py",
 "old_string": "        self.cur_lang_code = self.lang_code_to_id[\"en_XX\"]\n\n        self.fairseq_tokens_to_ids.update(self.lang_code_to_id)",
 "new_string": "        self.cur_lang_code = self.lang_code_to_id[\"en_XX\"]\n        self.fairseq_tokens_to_ids[\"<mask>\"] = len(self.sp_model) + len(self.lang_code_to_id) + self.fairseq_offset\n\n        self.fairseq_tokens_to_ids.update(self.lang_code_to_id)"
}
````

Result:

````text
{
 "path": "src/transformers/tokenization_bart.py",
 "edited": true,
 "replacements": 1,
 "total_file_lines": 258,
 "total_file_size_bytes": 10605,
 "diff": "+         self.fairseq_tokens_to_ids[\"<mask>\"] = len(self.sp_model) + len(self.lang_code_to_id) + self.fairseq_offset",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "edit",
    "paths": [
     "src/transformers/tokenization_bart.py"
    ]
   }
  ]
 },
 "file_change": {
  "kind": "diff",
  "operation": "update",
  "path": "src/transformers/tokenization_bart.py",
  "patch": "+         self.fairseq_tokens_to_ids[\"<mask>\"] = len(self.sp_model) + len(self.lang_code_to_id) + self.fairseq_offset",
  "additions": 1,
  "deletions": 0,
  "truncated": false,
  "omitted_lines": 0
 }
}
````

### Turn 4 — thinking

````text
I should add a vocab_size property that sums the sentencepiece model size, language codes, and fairseq offset plus one for the mask token, making sure get_vocab reflects the full vocabulary. I need to double-check that lang_code_to_id already exists by the time this property might get called during initialization.
````

### Turn 4 — tool call call_0004 (edit)

````json
{
 "file_path": "src/transformers/tokenization_bart.py",
 "old_string": "        self.set_src_lang_special_tokens(kwargs.get(\"src_lang\", \"en_XX\"))\n",
 "new_string": "        self.set_src_lang_special_tokens(kwargs.get(\"src_lang\", \"en_XX\"))\n\n    @property\n    def vocab_size(self):\n        return len(self.sp_model) + len(self.lang_code_to_id) + self.fairseq_offset + 1  # Plus 1 for the mask token\n"
}
````

Result:

````text
{
 "path": "src/transformers/tokenization_bart.py",
 "edited": true,
 "replacements": 1,
 "total_file_lines": 262,
 "total_file_size_bytes": 10763,
 "diff": "+     @property\n+     def vocab_size(self):\n+         return len(self.sp_model) + len(self.lang_code_to_id) + self.fairseq_offset + 1  # Plus 1 for the mask token\n+ ",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "edit",
    "paths": [
     "src/transformers/tokenization_bart.py"
    ]
   }
  ]
 },
 "file_change": {
  "kind": "diff",
  "operation": "update",
  "path": "src/transformers/tokenization_bart.py",
  "patch": "+     @property\n+     def vocab_size(self):\n+         return len(self.sp_model) + len(self.lang_code_to_id) + self.fairseq_offset + 1  # Plus 1 for the mask token\n+ ",
  "additions": 4,
  "deletions": 0,
  "truncated": false,
  "omitted_lines": 0
 }
}
````

### Turn 5 — tool call call_0005 (exec)

````json
{
 "command": "ls tests | grep -i mbart; python -m pytest tests/test_tokenization_mbart.py -q 2>&1 | tail -5; python -c \"\nfrom transformers import MBartTokenizer\nt=MBartTokenizer('tests/fixtures/test_sentencepiece.model')\nprint(t.convert_tokens_to_ids(['<mask>','ar_AR','zh_CN']), t.vocab_size, len(t.get_vocab()), t.convert_ids_to_tokens([t.mask_token_id]))\""
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
 "stdout": "test_modeling_mbart.py\ntest_tokenization_mbart.py\nERROR tests/test_tokenization_mbart.py::MBartEnroIntegrationTest::test_enro_tokenizer_decode_ignores_language_codes\nERROR tests/test_tokenization_mbart.py::MBartEnroIntegrationTest::test_enro_tokenizer_prepare_translation_batch\nERROR tests/test_tokenization_mbart.py::MBartEnroIntegrationTest::test_enro_tokenizer_truncation\nERROR tests/test_tokenization_mbart.py::MBartEnroIntegrationTest::test_max_target_length\n31 passed, 3 skipped, 3 warnings, 5 errors in 7.53s\n[1026, 1001, 1025] 1027 1027 ['<mask>']\n",
 "stderr": "2026-10-17 06:21:40.788750: I tensorflow/core/util/port.cc:110] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.\n2026-10-17 06:21:40.791316: I tensorflow/tsl/cuda/cudart_stub.cc:28] Could not find cuda drivers on your machine, GPU will not be used.\n2026-10-17 06:21:40.845642: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.\nTo enable the following instructions: AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.\n2026-10-17 06:21:41.806814: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT\n",
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "guidance": "stderr contains error-like diagnostics while the final exit code is 0. Inspect stderr before treating this command as successful; shell control flow may have masked a failed subcommand.",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "tests"
  ],
  "command_sha256": [
   "5d499e8adba252bfed39ef8f4b0540920dc3b694316d660e85e00a8cf51ebc61"
  ]
 },
 "device_targets": [],
 "duration_ms": 15178
}
````

### Turn 6 — thinking

````text
These errors are likely from integration tests that need network access, so let me check quickly.
````

### Turn 6 — tool call call_0006 (exec)

````json
{
 "command": "python -m pytest tests/test_tokenization_mbart.py -q -k test_max_target_length 2>&1 | grep -iE \"Error|connection\" | head -5; git stash -q; python -m pytest tests/test_tokenization_mbart.py -q 2>&1 | tail -1; git stash pop -q; git diff --stat"
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
 "stdout": "==================================== ERRORS ====================================\n______ ERROR at setup of MBartEnroIntegrationTest.test_max_target_length _______\n>               raise EnvironmentError\nE               OSError\nsrc/transformers/configuration_utils.py:330: OSError\n31 passed, 3 skipped, 2 warnings, 5 errors in 8.10s\n src/transformers/tokenization_bart.py | 5 +++++\n 1 file changed, 5 insertions(+)\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 17590,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [],
  "command_sha256": [
   "4098b060962bb581eb62f67aa0ac607bede7b316cd0e8b96c75c06777be83773"
  ]
 }
}
````

### Turn 7 — assistant text

I fixed it: in `MBartTokenizer`, `<mask>` now gets its own id after all the language codes, so it no longer shares an id with `ar_AR`. For `facebook/mbart-large-cc25` that id should be 250026, as the issue expected. I worked that number out from the formula; I didn't check it against the real checkpoint because downloading it failed here.

The change is in `src/transformers/tokenization_bart.py`:

- **Mask id:** in `MBartTokenizer.__init__`, `<mask>` is now set to `len(sp_model) + len(lang_code_to_id) + fairseq_offset`. This matches fairseq, which adds the mask after the language codes. Before, the tokenizer reused XLM-R's mask id, which is the id of the first language code.
- **Vocab size:** I added a `vocab_size` override that counts the language codes as well as the mask. Without it, `get_vocab()` would leave out the new last id.

**Checks:**
- With the test sentencepiece model, `<mask>`, `ar_AR` and `zh_CN` map to 1026, 1001 and 1025. `vocab_size` is 1027, `len(get_vocab())` is 1027, and id 1026 decodes back to `<mask>`.
- `tests/test_tokenization_mbart.py`: 31 passed, 3 skipped, 5 errors. The 5 errors are integration tests that fail at setup with an `OSError` because they can't download the pretrained model. They fail the same way without my change.

### Turn 8 — assistant text

I fixed the `<mask>` id clash in `MBartTokenizer`. `<mask>` now gets its own id after all the language codes, as in fairseq. Before the fix, `<mask>` and `ar_AR` both got id 250001.

The change is in `src/transformers/tokenization_bart.py`, in two parts:
- **`<mask>` id:** in `__init__`, `<mask>` is now set to `len(sp_model) + len(lang_code_to_id) + fairseq_offset`. For `facebook/mbart-large-cc25` that works out to 250026, the value the issue expects.
- **`vocab_size`:** I added an override so the vocabulary size counts the language codes plus the mask token. Without it, `get_vocab()` and `vocab_size` would stop before the new `<mask>` id.

With the test sentencepiece model, `<mask>` now maps to 1026, after the last language code `zh_CN` (1025), and `ar_AR` stays at 1001. `vocab_size` and `len(get_vocab())` both equal 1027, and converting the mask id back gives `<mask>`. I didn't test against the real `facebook/mbart-large-cc25` vocabulary, so 250026 is calculated, not observed.

In `tests/test_tokenization_mbart.py`, 31 tests pass and 3 are skipped. The 5 errors happen at setup in `MBartEnroIntegrationTest` with an `OSError` when loading the pretrained model, which looks like no network access. The result is the same with and without my change.

I didn't change the language-code format the issue mentions (fairseq uses `[en_XX]`, this tokenizer uses `en_XX`).

## Final answer

I fixed the `<mask>` id clash in `MBartTokenizer`. `<mask>` now gets its own id after all the language codes, as in fairseq. Before the fix, `<mask>` and `ar_AR` both got id 250001.

The change is in `src/transformers/tokenization_bart.py`, in two parts:
- **`<mask>` id:** in `__init__`, `<mask>` is now set to `len(sp_model) + len(lang_code_to_id) + fairseq_offset`. For `facebook/mbart-large-cc25` that works out to 250026, the value the issue expects.
- **`vocab_size`:** I added an override so the vocabulary size counts the language codes plus the mask token. Without it, `get_vocab()` and `vocab_size` would stop before the new `<mask>` id.

With the test sentencepiece model, `<mask>` now maps to 1026, after the last language code `zh_CN` (1025), and `ar_AR` stays at 1001. `vocab_size` and `len(get_vocab())` both equal 1027, and converting the mask id back gives `<mask>`. I didn't test against the real `facebook/mbart-large-cc25` vocabulary, so 250026 is calculated, not observed.

In `tests/test_tokenization_mbart.py`, 31 tests pass and 3 are skipped. The 5 errors happen at setup in `MBartEnroIntegrationTest` with an `OSError` when loading the pretrained model, which looks like no network access. The result is the same with and without my change.

I didn't change the language-code format the issue mentions (fairseq uses `[en_XX]`, this tokenizer uses `en_XX`).

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 122650 | 2626 | 101294 | 21338 | 125276 |
