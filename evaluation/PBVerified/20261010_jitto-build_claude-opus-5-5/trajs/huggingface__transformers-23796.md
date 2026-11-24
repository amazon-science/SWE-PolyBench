# Instance: huggingface__transformers-23796

- Final resolved (evaluator, logs/huggingface__transformers-23796_result.json): True
- Run state: DONE
- One attempt. Duration 146.3 s, turns 8, actor cost $0.16953500000000002, container commands 6
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/huggingface__transformers-23796/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-23796/repo. Consider the following issue description:

<issue_description>
Whisper `get_prompt_ids` throws error when used with a 'FastTokenizer'
### System Info

- `transformers` version: 4.30.0.dev0
- Platform: macOS-13.0-arm64-arm-64bit
- Python version: 3.9.16
- Huggingface_hub version: 0.12.0
- Safetensors version: 0.2.8
- PyTorch version (GPU?): 1.13.1 (False)
- Tensorflow version (GPU?): not installed (NA)
- Flax version (CPU?/GPU?/TPU?): 0.5.3 (cpu)
- Jax version: 0.3.6
- JaxLib version: 0.3.5
- Using GPU in script?: No
- Using distributed or parallel set-up in script?: No

### Who can help?

@sanchit-gandhi @hollance 

### Information

- [ ] The official example scripts
- [X] My own modified scripts

### Tasks

- [ ] An officially supported task in the `examples` folder (such as GLUE/SQuAD, ...)
- [X] My own task or dataset (give details below)

### Reproduction

```py
from transformers import WhisperTokenizerFast, WhisperTokenizer, GPT2Tokenizer, GPT2TokenizerFast


slow_tokenizer = WhisperTokenizer.from_pretrained('openai/whisper-tiny')
prompt_ids = slow_tokenizer.get_prompt_ids("Hello, world!", return_tensors="pt")
print('Whisper slow tokenizer succeeded')

try:
    fast_tokenizer = WhisperTokenizerFast.from_pretrained('openai/whisper-tiny')
    prompt_ids = fast_tokenizer.get_prompt_ids("Hello, world!", return_tensors="pt")
except Exception as e:
    print('Whisper fast tokenizer failed - ', e)
    

# Alternatively, this slow-fast param difference can be seen when tokenizing with a
# pipeline or any model that has a slow tokenizer `prepare_for_tokenization` method 
# that checks `add_prefix_space` (GPT2 is old but there are ~20 models this applies to)
tokenizer = GPT2Tokenizer.from_pretrained('gpt2', use_fast=False)
prompt_ids = tokenizer("Hello, world!", add_prefix_space=True)["input_ids"]
print('GPT2 slow tokenizer succeeded')

try:
    tokenizer = GPT2TokenizerFast.from_pretrained('gpt2')
    prompt_ids = tokenizer("Hello, world!", add_prefix_space=True)["input_ids"]
except Exception as e:
    print('Whisper fast tokenizer failed - ', e)
```

### Expected behavior

Are the slow and fast tokenizers supposed to have the same arg options for tokenizing text? They diverge with the `add_prefix_space` argument; while the slow tokenizer accepts and applies it with the [prepare_for_tokenization](https://github.com/huggingface/transformers/blob/3416bba7c70c358ac17efd3be31e9090135969ab/src/transformers/tokenization_utils.py#L502) method that same model's fast tokenizer does not and throws an error. Given that this arg difference appears to be present across all models where `add_prefix_space` can be provided to the slow tokenizer (at a glance appears to be ~20) I'd imagine the answer is no, the arg options aren't supposed to be 1:1.

The fix for the Whisper tokenizer `get_prompt_ids` method is straightforward as we can just do `" " + text` directly in the method instead of `add_prefix_space=True`, but I wanted to bring up the above in case that argument is actually supposed to compatible across both slow and fast tokenizers in which case we would also want to address that.

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-23796/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-23796/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-23796/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-23796/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -n "add_prefix_space\|def get_prompt_ids" -A3 src/transformers/models/whisper/tokenization_whisper*.py
```

tool result:

```
src/transformers/models/whisper/tokenization_whisper.py:238:        add_prefix_space (`bool`, *optional*, defaults to `False`):
src/transformers/models/whisper/tokenization_whisper.py-239-            Whether or not to add an initial space to the input. This allows to treat the leading word just as any
src/transformers/models/whisper/tokenization_whisper.py-240-            other word.
src/transformers/models/whisper/tokenization_whisper.py-241-        language (`str`, *optional*):
--
src/transformers/models/whisper/tokenization_whisper.py:267:        add_prefix_space=False,
src/transformers/models/whisper/tokenization_whisper.py-268-        language=None,
src/transformers/models/whisper/tokenization_whisper.py-269-        task=None,
src/transformers/models/whisper/tokenization_whisper.py-270-        predict_timestamps=False,
--
src/transformers/models/whisper/tokenization_whisper.py:283:            add_prefix_space=add_prefix_space,
src/transformers/models/whisper/tokenization_whisper.py-284-            **kwargs,
src/transformers/models/whisper/tokenization_whisper.py-285-        )
src/transformers/models/whisper/tokenization_whisper.py-286-
--
src/transformers/models/whisper/tokenization_whisper.py:298:        self.add_prefix_space = add_prefix_space
src/transformers/models/whisper/tokenization_whisper.py-299-
src/transformers/models/whisper/tokenization_whisper.py-300-        if normalizer_file is not None:
src/transformers/models/whisper/tokenization_whisper.py-301-            with open(normalizer_file, encoding="utf-8") as vocab_handle:
--
src/transformers/models/whisper/tokenization_whisper.py:689:        add_prefix_space = kwargs.pop("add_prefix_space", self.add_prefix_space)
src/transformers/models/whisper/tokenization_whisper.py:690:        if is_split_into_words or add_prefix_space:
src/transformers/models/whisper/tokenization_whisper.py-691-            text = " " + text
src/transformers/models/whisper/tokenization_whisper.py-692-        return (text, kwargs)
src/transformers/models/whisper/tokenization_whisper.py-693-
--
src/transformers/models/whisper/tokenization_whisper.py:722:    def get_prompt_ids(self, text: str, return_tensors="np"):
src/transformers/models/whisper/tokenization_whisper.py-723-        """Converts prompt text to IDs that can be passed to [`~WhisperForConditionalGeneration.generate`]."""
src/transformers/models/whisper/tokenization_whisper.py:724:        batch_encoding = self("<|startofprev|>", text.strip(), add_prefix_space=True, add_special_tokens=False)
src/transformers/models/whisper/tokenization_whisper.py-725-
src/transformers/models/whisper/tokenization_whisper.py-726-        # Check for special tokens
src/transformers/models/whisper/tokenization_whisper.py-727-        prompt_text_ids = batch_encoding["input_ids"][1:]
--
src/transformers/models/whisper/tokenization_whisper_fast.py:112:        add_prefix_space (`bool`, *optional*, defaults to `False`):
src/transformers/models/whisper/tokenization_whisper_fast.py-113-            Whether or not to add an initial space to the input. This allows to treat the leading word just as any
src/transformers/models/whisper/tokenization_whisper_fast.py-114-            other word. (Whisper tokenizer detect beginning of words by the preceding space).
src/transformers/models/whisper/tokenization_whisper_fast.py-115-        trim_offsets (`bool`, *optional*, defaults to `True`):
--
src/transformers/models/whisper/tokenization_whisper_fast.py:143:        add_prefix_space=False,
src/transformers/models/whisper/tokenization_whisper_fast.py-144-        language=None,
src/transformers/models/whisper/tokenization_whisper_fast.py-145-        task=None,
src/transformers/models/whisper/tokenization_whisper_fast.py-146-        predict_timestamps=False,
--
src/transformers/models/whisper/tokenization_whisper_fast.py:156:            add_prefix_space=add_prefix_space,
src/transformers/models/whisper/tokenization_whisper_fast.py-157-            **kwargs,
src/transformers/models/whisper/tokenization_whisper_fast.py-158-        )
src/transformers/models/whisper/tokenization_whisper_fast.py-159-
--
src/transformers/models/whisper/tokenization_whisper_fast.py:163:        if pre_tok_state.get("add_prefix_space", add_prefix_space) != add_prefix_space:
src/transformers/models/whisper/tokenization_whisper_fast.py-164-            pre_tok_class = getattr(pre_tokenizers, pre_tok_state.pop("type"))
src/transformers/models/whisper/tokenization_whisper_fast.py:165:            pre_tok_state["add_prefix_space"] = add_prefix_space
src/transformers/models/whisper/tokenization_whisper_fast.py-166-            self.backend_tokenizer.pre_tokenizer = pre_tok_class(**pre_tok_state)
src/transformers/models/whisper/tokenization_whisper_fast.py-167-
src/transformers/models/whisper/tokenization_whisper_fast.py-168-        if normalizer_file is not None:
--
src/transformers/models/whisper/tokenization_whisper_fast.py:174:        self.add_prefix_space = add_prefix_space
src/transformers/models/whisper/tokenization_whisper_fast.py-175-
src/transformers/models/whisper/tokenization_whisper_fast.py-176-        self.language = language
src/transformers/models/whisper/tokenization_whisper_fast.py-177-        self.task = task
--
src/transformers/models/whisper/tokenization_whisper_fast.py:183:        assert self.add_prefix_space or not is_split_into_words, (
src/transformers/models/whisper/tokenization_whisper_fast.py:184:            f"You need to instantiate {self.__class__.__name__} with add_prefix_space=True "
src/transformers/models/whisper/tokenization_whisper_fast.py-185-            "to use it with pretokenized inputs."
src/transformers/models/whisper/tokenization_whisper_fast.py-186-        )
src/transformers/models/whisper/tokenization_whisper_fast.py-187-
--
src/transformers/models/whisper/tokenization_whisper_fast.py:194:        assert self.add_prefix_space or not is_split_into_words, (
src/transformers/models/whisper/tokenization_whisper_fast.py:195:          
[... 1110 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-23796; cat > testbed/repro_tmp.py <<'EOF'
from transformers import WhisperTokenizer, WhisperTokenizerFast
s = WhisperTokenizer.from_pretrained('openai/whisper-tiny')
print(s.get_prompt_ids("Hello, world!"))
print(s.get_prompt_ids("  Hello, world!  "))
f = WhisperTokenizerFast.from_pretrained('openai/whisper-tiny')
print(f.get_prompt_ids("Hello, world!"))
EOF
bin/envrun 'HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python repro_tmp.py 2>&1 | tail -5'
```

tool result:

```
  File "/testbed/src/transformers/tokenization_utils_fast.py", line 497, in _encode_plus
    batched_output = self._batch_encode_plus(
  File "/testbed/src/transformers/models/whisper/tokenization_whisper_fast.py", line 188, in _batch_encode_plus
    return super()._batch_encode_plus(*args, **kwargs)
TypeError: PreTrainedTokenizerFast._batch_encode_plus() got an unexpected keyword argument 'add_prefix_space'
Shell cwd was reset to /work/huggingface__transformers-23796/repo
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-23796; bin/envrun 'HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python repro_tmp.py 2>&1 | head -3'
cd testbed && sed -i '' 's/self("<|startofprev|>", text.strip(), add_prefix_space=True, add_special_tokens=False)/self("<|startofprev|>", " " + text.strip(), add_special_tokens=False)/' src/transformers/models/whisper/tokenization_whisper.py src/transformers/models/whisper/tokenization_whisper_fast.py && git diff --stat
```

tool result:

```
/usr/local/lib/python3.10/site-packages/huggingface_hub/file_download.py:945: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.
  warnings.warn(
[50361  2425    11  1002     0]

 src/transformers/models/whisper/tokenization_whisper.py      | 2 +-
 src/transformers/models/whisper/tokenization_whisper_fast.py | 2 +-
 2 files changed, 2 insertions(+), 2 deletions(-)
```

**assistant:** Slow output before the fix: `[50361 2425 11 1002 0]`. Now rerunning after the change:

**tool call: Bash**

```bash
cd /work/huggingface__transformers-23796; bin/envrun 'HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python repro_tmp.py 2>&1 | grep -v -i warn'
```

tool result:

```
[50361  2425    11  1002     0]
[50361  2425    11  1002     0]
[50361  2425    11  1002     0]
Shell cwd was reset to /work/huggingface__transformers-23796/repo
```

**assistant:** Slow output is unchanged, the fast tokenizer now works and matches it, and surrounding whitespace is handled. Running the Whisper tokenizer tests:

**tool call: Bash**

```bash
cd /work/huggingface__transformers-23796; rm testbed/repro_tmp.py; bin/envrun 'HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m pytest tests/models/whisper/test_tokenization_whisper.py -q 2>&1 | tail -5; git status --short'
```

tool result:

```
FAILED tests/models/whisper/test_tokenization_whisper.py::WhisperTokenizerTest::test_get_vocab
FAILED tests/models/whisper/test_tokenization_whisper.py::WhisperTokenizerTest::test_output_offsets
FAILED tests/models/whisper/test_tokenization_whisper.py::SpeechToTextTokenizerMultilinguialTest::test_offset_decoding
FAILED tests/models/whisper/test_tokenization_whisper.py::SpeechToTextTokenizerMultilinguialTest::test_tokenizer_equivalence
6 failed, 89 passed, 5 skipped, 98 warnings in 53.98s
 M src/transformers/models/whisper/tokenization_whisper.py
 M src/transformers/models/whisper/tokenization_whisper_fast.py
?? Dockerfile
Shell cwd was reset to /work/huggingface__transformers-23796/repo
```

**assistant:** Checking whether these failures already happen without my change:

**tool call: Bash**

```bash
cd /work/huggingface__transformers-23796; bin/envrun 'git stash -q && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m pytest tests/models/whisper/test_tokenization_whisper.py -q 2>&1 | grep -E "FAILED|passed"; git stash pop -q; git status --short'
```

tool result:

```
                Will be passed along to the Tokenizer `__init__` method.
                Will be passed to the Tokenizer `__init__` method. Can be used to set special tokens like `bos_token`,
                Will be passed along to the Tokenizer `__init__` method.
                Will be passed to the Tokenizer `__init__` method. Can be used to set special tokens like `bos_token`,
FAILED tests/models/whisper/test_tokenization_whisper.py::WhisperTokenizerTest::test_clean_up_tokenization_spaces
FAILED tests/models/whisper/test_tokenization_whisper.py::WhisperTokenizerTest::test_full_tokenizer
FAILED tests/models/whisper/test_tokenization_whisper.py::WhisperTokenizerTest::test_get_vocab
FAILED tests/models/whisper/test_tokenization_whisper.py::WhisperTokenizerTest::test_output_offsets
FAILED tests/models/whisper/test_tokenization_whisper.py::SpeechToTextTokenizerMultilinguialTest::test_offset_decoding
FAILED tests/models/whisper/test_tokenization_whisper.py::SpeechToTextTokenizerMultilinguialTest::test_tokenizer_equivalence
6 failed, 89 passed, 5 skipped, 98 warnings in 51.19s
 M src/transformers/models/whisper/tokenization_whisper.py
 M src/transformers/models/whisper/tokenization_whisper_fast.py
?? Dockerfile
Shell cwd was reset to /work/huggingface__transformers-23796/repo
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-23796; bin/envrun 'HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m pytest tests/models/whisper/test_tokenization_whisper.py -q -k prompt 2>&1 | tail -1; git diff'
```

tool result:

```
1 passed, 99 deselected, 2 warnings in 1.38s
diff --git a/src/transformers/models/whisper/tokenization_whisper.py b/src/transformers/models/whisper/tokenization_whisper.py
index 4c7c9c89f..428254a26 100644
--- a/src/transformers/models/whisper/tokenization_whisper.py
+++ b/src/transformers/models/whisper/tokenization_whisper.py
@@ -721,7 +721,7 @@ class WhisperTokenizer(PreTrainedTokenizer):
 
     def get_prompt_ids(self, text: str, return_tensors="np"):
         """Converts prompt text to IDs that can be passed to [`~WhisperForConditionalGeneration.generate`]."""
-        batch_encoding = self("<|startofprev|>", text.strip(), add_prefix_space=True, add_special_tokens=False)
+        batch_encoding = self("<|startofprev|>", " " + text.strip(), add_special_tokens=False)
 
         # Check for special tokens
         prompt_text_ids = batch_encoding["input_ids"][1:]
diff --git a/src/transformers/models/whisper/tokenization_whisper_fast.py b/src/transformers/models/whisper/tokenization_whisper_fast.py
index be4ad842a..a31fe0005 100644
--- a/src/transformers/models/whisper/tokenization_whisper_fast.py
+++ b/src/transformers/models/whisper/tokenization_whisper_fast.py
@@ -494,7 +494,7 @@ class WhisperTokenizerFast(PreTrainedTokenizerFast):
     # Copied from transformers.models.whisper.tokenization_whisper.WhisperTokenizer.get_prompt_ids
     def get_prompt_ids(self, text: str, return_tensors="np"):
         """Converts prompt text to IDs that can be passed to [`~WhisperForConditionalGeneration.generate`]."""
-        batch_encoding = self("<|startofprev|>", text.strip(), add_prefix_space=True, add_special_tokens=False)
+        batch_encoding = self("<|startofprev|>", " " + text.strip(), add_special_tokens=False)
 
         # Check for special tokens
         prompt_text_ids = batch_encoding["input_ids"][1:]
Shell cwd was reset to /work/huggingface__transformers-23796/repo
```

**assistant:** `WhisperTokenizerFast.get_prompt_ids` no longer throws an error. It now returns the same IDs as the slow tokenizer.

**Cause:** `get_prompt_ids` passed `add_prefix_space=True` when it called the tokenizer. The slow tokenizer handles that option in `prepare_for_tokenization`, but the fast tokenizer has no such step. The option went straight through to `PreTrainedTokenizerFast._batch_encode_plus`, which rejected it with a `TypeError`.

**Fix:** As the issue suggested, I add the leading space directly to the prompt text. I made the same one-line change in `tokenization_whisper.py` and `tokenization_whisper_fast.py`, since the fast version is marked as a copy of the slow one:

```python
batch_encoding = self("<|startofprev|>", " " + text.strip(), add_special_tokens=False)
```

**Checks:**
- **Before the fix:** the slow tokenizer returned `[50361 2425 11 1002 0]` for `"Hello, world!"`, and the fast one raised the `TypeError`.
- **After the fix:** both tokenizers return `[50361 2425 11 1002 0]`, so the slow tokenizer's output hasn't changed. Input with extra spaces at the start and end (`"  Hello, world!  "`) gives the same result.
- **Tests:** the prompt-ids test in `tests/models/whisper/test_tokenization_whisper.py` passes. The full file has 89 passed and 6 failed, and the same 6 fail on the original code with my change stashed, so this change doesn't cause them. They include `test_full_tokenizer`, `test_get_vocab` and `test_tokenizer_equivalence`. I didn't look into why they fail.

The wider question in the issue is out of scope here: other models' fast tokenizers also don't accept `add_prefix_space` at call time, and this change doesn't affect them. I deleted my reproduction script. The untracked `Dockerfile` in the repo isn't mine, and I left it alone.

_session end: success, turns 8, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 1.19 s: HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python repro_tmp.py 2>&1 | tail -5
- `rc=0` 1.02 s: HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python repro_tmp.py 2>&1 | head -3
- `rc=0` 1.03 s: HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python repro_tmp.py 2>&1 | grep -v -i warn
- `rc=0` 57.75 s: HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m pytest tests/models/whisper/test_tokenization_whisper.py -q 2>&1 | tail -5; git status --short
- `rc=0` 54.23 s: git stash -q && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m pytest tests/models/whisper/test_tokenization_whisper.py -q 2>&1 | grep -E "FAILED|passed"; git stash pop -q; git status --short
- `rc=0` 3.74 s: HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m pytest tests/models/whisper/test_tokenization_whisper.py -q -k prompt 2>&1 | tail -1; git diff
