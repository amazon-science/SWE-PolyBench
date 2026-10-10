# Instance: huggingface__transformers-23141

- Final resolved (evaluator, logs/huggingface__transformers-23141_result.json): True
- Run state: DONE
- One attempt. Duration 70.7 s, turns 11, actor cost $0.24544000000000002, container commands 5
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/huggingface__transformers-23141/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-23141/repo. Consider the following issue description:

<issue_description>
Whisper generation support for passing acronym to language arg
### System Info

- `transformers` version: 4.29.0.dev0
- Platform: macOS-13.0-arm64-arm-64bit
- Python version: 3.9.16
- Huggingface_hub version: 0.12.0
- Safetensors version: 0.2.8
- PyTorch version (GPU?): 1.13.1 (False)
- Tensorflow version (GPU?): 2.11.0 (False)
- Flax version (CPU?/GPU?/TPU?): 0.5.3 (cpu)
- Jax version: 0.3.6
- JaxLib version: 0.3.5
- Using GPU in script?: No
- Using distributed or parallel set-up in script?: No

### Who can help?

@hollance @gante

### Information

- [ ] The official example scripts
- [X] My own modified scripts

### Tasks

- [ ] An officially supported task in the `examples` folder (such as GLUE/SQuAD, ...)
- [X] My own task or dataset (give details below)

### Reproduction

```py
processor = WhisperProcessor.from_pretrained("openai/whisper-tiny")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny")
ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
sample = ds[0]["audio"]["array"]
input_features = processor.feature_extractor(sample, return_tensors="pt").input_features

pred_ids = model.generate(input_features, language="de")
```

Throws this error:
<img width="778" alt="Screenshot 2023-05-03 at 6 29 38 PM" src="https://user-images.githubusercontent.com/78612354/236067028-ee7ab371-e9a2-44eb-9895-b5c8f3a2fcdd.png">

Then this error when that's fixed:
<img width="1198" alt="Screenshot 2023-05-03 at 6 30 34 PM" src="https://user-images.githubusercontent.com/78612354/236067052-8f1ae574-db51-44e4-800c-aa4f38b0200e.png">


### Expected behavior

Should recognize and use language passed in acronym format as per the docstring

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-23141/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-23141/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-23141/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-23141/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/huggingface__transformers-23141/repo; grep -n "language" src/transformers/models/whisper/modeling_whisper.py | head -60; grep -n "language" src/transformers/models/whisper/modeling_tf_whisper.py src/transformers/models/whisper/modeling_flax_whisper.py | head -40
```

tool result:

```
13:# See the License for the specific language governing permissions and
1309:    "The Whisper Model with a language modeling head. Can be used for automatic speech recognition.",
1379:            Labels for computing the language modeling loss. Indices should either be in `[0, ..., config.vocab_size]`
1465:        language=None,
1471:        Generates sequences of token ids for models with a language modeling head.
1519:            language (`bool`, *optional*):
1521:                find all the possible language tokens in the `model.generation_config.lang_to_id` dictionary.
1564:        if language is not None:
1565:            generation_config.language = language
1570:        if task is not None or language is not None:
1571:            if hasattr(generation_config, "language"):
1572:                if generation_config.language in generation_config.lang_to_id.keys():
1573:                    language_token = generation_config.language
1574:                elif generation_config.language in TO_LANGUAGE_CODE.keys():
1575:                    language_token = f"<|{TO_LANGUAGE_CODE[generation_config.language]}|>"
1578:                        f"Unsupported language: {self.language}. Language should be one of:"
1579:                        f" {list(TO_LANGUAGE_CODE.keys()) if generation_config.language in TO_LANGUAGE_CODE.keys() else list(TO_LANGUAGE_CODE.values())}."
1581:                forced_decoder_ids.append((1, generation_config.lang_to_id[language_token]))
1583:                forced_decoder_ids.append((1, None))  # automatically detect the language
src/transformers/models/whisper/modeling_tf_whisper.py:13:# See the License for the specific language governing permissions and
src/transformers/models/whisper/modeling_tf_whisper.py:1207:    "The Whisper Model with a language modeling head. Can be used for automatic speech recognition.",
src/transformers/models/whisper/modeling_tf_whisper.py:1265:            Labels for computing the language modeling loss. Indices should either be in `[0, ..., config.vocab_size]`
src/transformers/models/whisper/modeling_flax_whisper.py:13:# See the License for the specific language governing permissions and
src/transformers/models/whisper/modeling_flax_whisper.py:1241:@add_start_docstrings("The Whisper Model with a language modeling head.", WHISPER_START_DOCSTRING)
src/transformers/models/whisper/modeling_flax_whisper.py:1387:        language=None,
src/transformers/models/whisper/modeling_flax_whisper.py:1403:        if language is not None:
src/transformers/models/whisper/modeling_flax_whisper.py:1404:            generation_config.language = language
src/transformers/models/whisper/modeling_flax_whisper.py:1414:            if hasattr(generation_config, "language"):
src/transformers/models/whisper/modeling_flax_whisper.py:1415:                forced_decoder_ids.append((1, generation_config.lang_to_id[generation_config.language]))
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-23141/repo; sed -n 1510,1600p src/transformers/models/whisper/modeling_whisper.py; sed -n 1380,1425p src/transformers/models/whisper/modeling_flax_whisper.py; grep -n "^from\|^import\|TO_LANGUAGE_CODE" src/transformers/models/whisper/modeling_*.py; ls tests/models/whisper; git log --oneline -1
```

tool result:

```
                for constrained generation conditioned on the prefix, as described in [Autoregressive Entity
                Retrieval](https://arxiv.org/abs/2010.00904).
            synced_gpus (`bool`, *optional*, defaults to `False`):
                Whether to continue running the while loop until max_length (needed for ZeRO stage 3)
            return_timestamps (`bool`, *optional*):
                Whether to return the timestamps with the text. This enables the `WhisperTimestampsLogitsProcessor`.
            task (`bool`, *optional*):
                Task to use for generation, either "translate" or "transcribe". The `model.config.forced_decoder_ids`
                will be updated accordingly.
            language (`bool`, *optional*):
                Language token to use for generation, can be either in the form of `<|en|>`, `en` or `english`. You can
                find all the possible language tokens in the `model.generation_config.lang_to_id` dictionary.
            is_multilingual (`bool`, *optional*):
                Whether or not the model is multilingual.
            kwargs:
                Ad hoc parametrization of `generate_config` and/or additional model-specific kwargs that will be
                forwarded to the `forward` function of the model. If the model is an encoder-decoder model, encoder
                specific kwargs should not be prefixed and decoder specific kwargs should be prefixed with *decoder_*.

        Return:
            [`~utils.ModelOutput`] or `torch.LongTensor`: A [`~utils.ModelOutput`] (if `return_dict_in_generate=True`
            or when `config.return_dict_in_generate=True`) or a `torch.FloatTensor`.

                If the model is *not* an encoder-decoder model (`model.config.is_encoder_decoder=False`), the possible
                [`~utils.ModelOutput`] types are:

                    - [`~generation.GreedySearchDecoderOnlyOutput`],
                    - [`~generation.SampleDecoderOnlyOutput`],
                    - [`~generation.BeamSearchDecoderOnlyOutput`],
                    - [`~generation.BeamSampleDecoderOnlyOutput`]

                If the model is an encoder-decoder model (`model.config.is_encoder_decoder=True`), the possible
                [`~utils.ModelOutput`] types are:

                    - [`~generation.GreedySearchEncoderDecoderOutput`],
                    - [`~generation.SampleEncoderDecoderOutput`],
                    - [`~generation.BeamSearchEncoderDecoderOutput`],
                    - [`~generation.BeamSampleEncoderDecoderOutput`]
        """
        if generation_config is None:
            generation_config = self.generation_config

        if return_timestamps is not None:
            if not hasattr(generation_config, "no_timestamps_token_id"):
                raise ValueError(
                    "You are trying to return timestamps, but the generation config is not properly set."
                    "Make sure to initialize the generation config with the correct attributes that are needed such as `no_timestamps_token_id`."
                    "For more details on how to generate the approtiate config, refer to https://github.com/huggingface/transformers/issues/21878#issuecomment-1451902363"
                )

            generation_config.return_timestamps = return_timestamps
        else:
            generation_config.return_timestamps = False

        if language is not None:
            generation_config.language = language
        if task is not None:
            generation_config.task = task

        forced_decoder_ids = []
        if task is not None or language is not None:
            if hasattr(generation_config, "language"):
                if generation_config.language in generation_config.lang_to_id.keys():
                    language_token = generation_config.language
                elif generation_config.language in TO_LANGUAGE_CODE.keys():
                    language_token = f"<|{TO_LANGUAGE_CODE[generation_config.language]}|>"
                else:
                    raise ValueError(
                        f"Unsupported language: {self.language}. Language should be one of:"
                        f" {list(TO_LANGUAGE_CODE.keys()) if generation_config.language in TO_LANGUAGE_CODE.keys() else list(TO_LANGUAGE_CODE.values())}."
                    )
                forced_decoder_ids.append((1, generation_config.lang_to_id[language_token]))
            else:
                forced_decoder_ids.append((1, None))  # automatically detect the language

            if hasattr(generation_config, "task"):
                if generation_config.task in TASK_IDS:
                    forced_decoder_ids.append((2, generation_config.task_to_id[generation_config.task]))
                else:
                    raise ValueError(
                        f"The `{generation_config.task}`task is not supported. The task should be one of `{TASK_IDS}`"
                    )
            else:
                forced_decoder_ids.append((2, generation_config.task_to_id["transcribe"]))  # defaults to transcribe
            if hasattr(generation_config, "no_timestamps_token_id") and not generation_config.return_timestamps:
                idx = forced_decoder_ids[-1][0] + 1 if forced_decoder_ids else 1
                forced_decoder_ids.append((idx, generation_config.no_timestamps_token_id))

        # Legacy code for backward compatibility
        elif hasattr(self.config, "forced_decoder_ids") and self.config.forced_decoder_ids is not None:
            forced_decoder_ids = self.config.forced_decoder_ids
    def generate(
        self,
        input_features,
        generation_config=None,
        logits_processor=None,
        return_timestamps=None,
        task=None,
        language=None,
        is_multilingual=None,
        **kwargs,
    ):
        if generation_config is None:
            generation_config = self.generation_config

        if return_timestamps is not None:
            generation_config
[... 6354 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-23141/repo; grep -n "language=" tests/models/whisper/test_modeling_whisper.py | head
```

tool result:

```
1188:            input_features, do_sample=False, max_length=20, language="<|en|>", task="transcribe"
1211:            input_features, do_sample=False, max_length=20, language="<|ja|>", task="transcribe"
1219:            input_features, do_sample=False, max_length=20, language="<|en|>", task="transcribe"
1227:            input_features, do_sample=False, max_length=20, language="<|ja|>", task="translate"
```

**assistant:** Reproduce with a tiny random model (no network):

**tool call: Bash**

```bash
cd /work/huggingface__transformers-23141/repo; cat > repro_lang.py <<'EOF'
import torch
from transformers import WhisperConfig, WhisperForConditionalGeneration, GenerationConfig
cfg = WhisperConfig(vocab_size=51865, d_model=16, encoder_layers=1, decoder_layers=1, encoder_attention_heads=2,
                    decoder_attention_heads=2, encoder_ffn_dim=16, decoder_ffn_dim=16, max_source_positions=1500)
model = WhisperForConditionalGeneration(cfg).eval()
gc = model.generation_config
gc.lang_to_id = {"<|en|>": 50259, "<|de|>": 50261}
gc.task_to_id = {"transcribe": 50359, "translate": 50358}
gc.no_timestamps_token_id = 50363
x = torch.randn(1, 80, 3000)
for lang in ["<|de|>", "de", "german", "German"]:
    out = model.generate(x, language=lang, max_length=5)
    print(lang, out[0, :4].tolist())
try:
    model.generate(x, language="xx", max_length=5)
except ValueError as e:
    print("ValueError:", e)
EOF
../bin/envrun 'python repro_lang.py 2>&1 | tail -5'
```

tool result:

```
  File "/testbed/src/transformers/models/whisper/modeling_whisper.py", line 1578, in generate
    f"Unsupported language: {self.language}. Language should be one of:"
  File "/usr/local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1931, in __getattr__
    raise AttributeError(
AttributeError: 'WhisperForConditionalGeneration' object has no attribute 'language'
```

**assistant:** Reproduced. Now fix the PyTorch implementation, also accepting case-insensitive names and a correct error message:

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/huggingface__transformers-23141/repo/src/transformers/models/whisper/modeling_whisper.py",
 "old_string": "        if language is not None:\n            generation_config.language = language\n        if task is not None:",
 "new_string": "        if language is not None:\n            language = language.lower()\n            generation_config.language = language\n        if task is not None:"
}
```

tool result:

```
The file /work/huggingface__transformers-23141/repo/src/transformers/models/whisper/modeling_whisper.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/huggingface__transformers-23141/repo/src/transformers/models/whisper/modeling_whisper.py",
 "old_string": "                    language_token = f\"<|{TO_LANGUAGE_CODE[generation_config.language]}|>\"\n                else:\n                    raise ValueError(\n                        f\"Unsupported language: {self.language}. Language should be one of:\"\n                        f\" {list(TO_LANGUAGE_CODE.keys()) if generation_config.language in TO_LANGUAGE_CODE.keys() else list(TO_LANGUAGE_CODE.values())}.\"\n                    )",
 "new_string": "                    language_token = f\"<|{TO_LANGUAGE_CODE[generation_config.language]}|>\"\n                elif generation_config.language in TO_LANGUAGE_CODE.values():\n                    language_token = f\"<|{generation_config.language}|>\"\n                else:\n                    is_language_code = len(generation_config.language) == 2\n                    raise ValueError(\n                        f\"Unsupported language: {generation_config.language}. Language should be one of:\"\n                        f\" {list(TO_LANGUAGE_CODE.values()) if is_language_code else list(TO_LANGUAGE_CODE.keys())}.\"\n                    )"
}
```

tool result:

```
The file /work/huggingface__transformers-23141/repo/src/transformers/models/whisper/modeling_whisper.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**assistant:** The Flax `generate` has the same problem (it indexes `lang_to_id` directly), so I'll apply the same handling there.

**tool call: Bash**

```bash
cd /work/huggingface__transformers-23141/repo; python3 - <<'EOF'
p='src/transformers/models/whisper/modeling_flax_whisper.py'
s=open(p).read()
s=s.replace("""from .configuration_whisper import WhisperConfig
""","""from .configuration_whisper import WhisperConfig
from .tokenization_whisper import TO_LANGUAGE_CODE
""",1)
old="""            if hasattr(generation_config, "language"):
                forced_decoder_ids.append((1, generation_config.lang_to_id[generation_config.language]))
"""
new="""            if hasattr(generation_config, "language"):
                if generation_config.language in generation_config.lang_to_id.keys():
                    language_token = generation_config.language
                elif generation_config.language in TO_LANGUAGE_CODE.keys():
                    language_token = f"<|{TO_LANGUAGE_CODE[generation_config.language]}|>"
                elif generation_config.language in TO_LANGUAGE_CODE.values():
                    language_token = f"<|{generation_config.language}|>"
                else:
                    is_language_code = len(generation_config.language) == 2
                    raise ValueError(
                        f"Unsupported language: {generation_config.language}. Language should be one of:"
                        f" {list(TO_LANGUAGE_CODE.values()) if is_language_code else list(TO_LANGUAGE_CODE.keys())}."
                    )
                forced_decoder_ids.append((1, generation_config.lang_to_id[language_token]))
"""
assert old in s
s=s.replace(old,new)
s=s.replace("""        if language is not None:
            generation_config.language = language
""","""        if language is not None:
            language = language.lower()
            generation_config.language = language
""",1)
open(p,'w').write(s)
EOF
git diff --stat; ../bin/envrun 'python repro_lang.py 2>&1 | tail -6'
```

tool result:

```
 src/transformers/models/whisper/modeling_flax_whisper.py | 16 +++++++++++++++-
 src/transformers/models/whisper/modeling_whisper.py      |  8 ++++++--
 2 files changed, 21 insertions(+), 3 deletions(-)
<|de|> [50257, 50261, 50359, 50363]
de [50257, 50261, 50359, 50363]
german [50257, 50261, 50359, 50363]
German [50257, 50261, 50359, 50363]
ValueError: Unsupported language: xx. Language should be one of: ['en', 'zh', 'de', 'es', 'ru', 'ko', 'fr', 'ja', 'pt', 'tr', 'pl', 'ca', 'nl', 'ar', 'sv', 'it', 'id', 'hi', 'fi', 'vi', 'he', 'uk', 'el', 'ms', 'cs', 'ro', 'da', 'hu', 'ta', 'no', 'th', 'ur', 'hr', 'bg', 'lt', 'la', 'mi', 'ml', 'cy', 'sk', 'te', 'fa', 'lv', 'bn', 'sr', 'az', 'sl', 'kn', 'et', 'mk', 'br', 'eu', 'is', 'hy', 'ne', 'mn', 'bs', 'kk', 'sq', 'sw', 'gl', 'mr', 'pa', 'si', 'km', 'sn', 'yo', 'so', 'af', 'oc', 'ka', 'be', 'tg', 'sd', 'gu', 'am', 'yi', 'lo', 'uz', 'fo', 'ht', 'ps', 'tk', 'nn', 'mt', 'sa', 'lb', 'my', 'bo', 'tl', 'mg', 'as', 'tt', 'haw', 'ln', 'ha', 'ba', 'jw', 'su', 'my', 'ca', 'nl', 'ht', 'lb', 'ps', 'pa', 'ro', 'ro', 'si', 'es'].
```

**assistant:** All forms work (`<|de|>`, `de`, `german`, `German`) and an invalid language gives a clean `ValueError`. Now a quick Flax check and the existing test suites:

**tool call: Bash**

```bash
cd /work/huggingface__transformers-23141/repo; rm repro_lang.py; ../bin/envrun 'python -c "import transformers.models.whisper.modeling_flax_whisper" && python -m pytest tests/models/whisper/test_modeling_whisper.py tests/models/whisper/test_modeling_flax_whisper.py -q -x 2>&1 | tail -3'; git status --short
```

tool result:

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/testbed/src/transformers/models/whisper/modeling_flax_whisper.py", line 21, in <module>
    import flax.linen as nn
ModuleNotFoundError: No module named 'flax'

 M src/transformers/models/whisper/modeling_flax_whisper.py
 M src/transformers/models/whisper/modeling_whisper.py
?? Dockerfile
```

**assistant:** Flax isn't installed in the container, so the Flax change can't be run here. Running the PyTorch tests:

**tool call: Bash**

```bash
cd /work/huggingface__transformers-23141/repo; ../bin/envrun 'python -m pytest tests/models/whisper/test_modeling_whisper.py -q 2>&1 | tail -3; python -m pyflakes src/transformers/models/whisper/modeling_flax_whisper.py 2>&1 || python -m py_compile src/transformers/models/whisper/modeling_flax_whisper.py && echo compiled'
```

tool result:

```
=========================== short test summary info ============================
FAILED tests/models/whisper/test_modeling_whisper.py::WhisperModelTest::test_pipeline_feature_extraction
1 failed, 124 passed, 64 skipped, 30 warnings in 12.67s
/usr/local/bin/python: No module named pyflakes
compiled
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-23141/repo; ../bin/envrun 'git stash -q && python -m pytest tests/models/whisper/test_modeling_whisper.py -q -k test_pipeline_feature_extraction 2>&1 | grep -E "Error|passed|failed" | tail -3; git stash pop -q && git status --short'
```

tool result:

```
E           OSError: Can't load tokenizer for 'hf-internal-testing/tiny-random-WhisperModel'. If you were trying to load it from 'https://huggingface.co/models', make sure you don't have a local directory with the same name. Otherwise, make sure 'hf-internal-testing/tiny-random-WhisperModel' is the correct path to a directory containing all relevant files for a WhisperTokenizer tokenizer.
src/transformers/tokenization_utils_base.py:1796: OSError
1 failed, 188 deselected, 2 warnings in 2.84s
 M src/transformers/models/whisper/modeling_flax_whisper.py
 M src/transformers/models/whisper/modeling_whisper.py
?? Dockerfile
```

**assistant:** I fixed it: `generate(..., language="de")` now works, along with `"<|de|>"`, `"german"` and `"German"`.

**What was wrong** (in `src/transformers/models/whisper/modeling_whisper.py`):
1. The code only recognised a language if it was a token like `<|de|>` or a full name like `german`. A short code like `"de"` was neither, so it fell through to the error branch.
2. That error branch then crashed by itself, because its message referred to `self.language`, which doesn't exist on the model. That's the first error in the issue.

**Changes:**
- **PyTorch `generate`:** a two-letter code (anything in `TO_LANGUAGE_CODE.values()`) is now converted to `<|code|>`. The language string is lowercased first, so `"German"` works too. The error message now uses `generation_config.language` and lists codes when you passed a code, or full names when you passed a name.
- **Flax `generate`** (`modeling_flax_whisper.py`): the same fix. It looked the language up in `lang_to_id` directly, so `"de"` and `"german"` both failed there. It now uses the same rules and imports `TO_LANGUAGE_CODE`.

**Testing:**
- I reproduced the `AttributeError` with a small randomly initialised model, since the container has no network. After the fix, `<|de|>`, `de`, `german` and `German` all produce the same forced decoder ids. An unsupported value like `"xx"` gives a clear `ValueError`.
- `tests/models/whisper/test_modeling_whisper.py`: 124 passed, 64 skipped, 1 failed. The failure is `test_pipeline_feature_extraction`, which fails the same way without my change because it tries to download a tokenizer from the Hub.
- Flax isn't installed in the container, so I couldn't run the Flax change; I only checked that the file compiles.

My reproduction script is deleted. There's an untracked `Dockerfile` in the repo that I didn't create, and I left it alone.

_session end: success, turns 11, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 3.74 s: python repro_lang.py 2>&1 | tail -5
- `rc=0` 3.13 s: python repro_lang.py 2>&1 | tail -6
- `rc=1` 1.07 s: python -c "import transformers.models.whisper.modeling_flax_whisper" && python -m pytest tests/models/whisper/test_modeling_whisper.py tests/models/whisper/test_modeling_flax_whisper.py -q -x 2>&1 | tail -3
- `rc=0` 15.95 s: python -m pytest tests/models/whisper/test_modeling_whisper.py -q 2>&1 | tail -3; python -m pyflakes src/transformers/models/whisper/modeling_flax_whisper.py 2>&1 || python -m py_compile src/transformers/models/whisper/modeling_flax_whisper.py && echo compiled
- `rc=0` 7.07 s: git stash -q && python -m pytest tests/models/whisper/test_modeling_whisper.py -q -k test_pipeline_feature_extraction 2>&1 | grep -E "Error|passed|failed" | tail -3; git stash pop -q && git status --short
