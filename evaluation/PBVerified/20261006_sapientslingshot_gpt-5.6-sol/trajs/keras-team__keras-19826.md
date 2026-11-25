# SWE-keras-19826 Trajectory

---

**Exported:** 2026-09-25T18:52:07.152Z

---

## SWE Benchmark Metadata

- **instanceId:** keras-team__keras-19826
- **repo:** keras-team/keras
- **baseCommit:** 2305fada8889e86463493bb4893b13ee8a8f0573
- **taskIndex:** 10
- **status:** completed

---

## Execution Metrics
| Metric | Value |
|---|---:|
| Prompt tokens | 0 |
| Completion tokens | 0 |
| Total tokens | 880835 |
| Credits consumed | 0.510897 |
| Total execution time | 2m 33s |

---

## Complete Raw Conversation

# Chat Session Export

**Exported:** 2026-09-25T18:52:07.147Z

## 👤 **User**

The current working directory is already provisioned by the benchmark host at exactly the task base commit, with one reachable commit and no Git remotes. Work only in this isolated local source tree.

Do not add Git remotes, clone, fetch, or pull. Do not access GitHub, GitHub APIs, upstream pull requests, commits, patches, or issue solutions. Do not use curl/wget or web-search tools. The benchmark runtime blocks outbound tools and commands.

Fix the issue using only the problem statement and the isolated local source tree. Generate keras-team__keras-19826.patch from the git diff,verify that git diff keras-team__keras-19826.patch contains only implementation or production files and no test files or test artifacts and then place it at this exact path: /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/swe-results/keras-team__keras-19826.patch.

Repository: keras-team/keras
Base Commit: 2305fada8889e86463493bb4893b13ee8a8f0573
Problem:  `keras.ops.repeat` cannot return an exptected shape when `x` is a `KerasTensor` and the `axis` is `None`
Hello. Thank you for your contributions and maintenance for the best Keras.

I'm following the instructions of [Conditional GAN (code samples, uses Keras 3)](https://keras.io/examples/generative/conditional_gan/), and focusing on the `keras.ops.repeat` function that is used in it.

I have found, maybe, if the input tensor of  `keras.ops.repeat`  is a symbolic tensor, i.e., the `keras.KerasTensor`, and the arg `axis` is `None`, the returned one will not be my expected one.

As the following：
```python
batch_size = 64
class_num = 10
a = keras.KerasTensor(shape=(batch_size, class_num), dtype=tf.float32)
a = a[:, :, None, None] # [B,10,1,1]
b = keras.ops.repeat(a, repeats=[28 * 28])
print(b.shape)# (784,)
# expected output: (501760,)
```

If assign `axis`, it works as expected:
```python
a = keras.KerasTensor(shape=(batch_size, class_num), dtype=tf.float32)
a = a[:, :, None, None] # [B,10,1,1]
b = keras.ops.repeat(a, repeats=[28 * 28],axis=0)
print(b.shape)# (784, 10, 1, 1)
# expected output: (784, 10, 1, 1)
```

If not use the symbolic tensor, it also works as expected:
```python
a = keras.random.normal(shape=(batch_size, class_num), dtype=tf.float32)
a = a[:, :, None, None] # [B,10,1,1]
b = keras.ops.repeat(a, repeats=[28 * 28])
print(b.shape)# (501760,)
# expected output: (501760,)
```

So, is the above a bug? 

And my environment is:
- Keras: Version: 3.3.3
- Numpy: Version: 1.26.4
- TensorFlow: Version: 2.16.1

Thanks in advance.

---

## 🤖 **Slingshot**

*9/25/2026, 1:49:34 PM*

## Agent Execution Steps

1. **Tool call: register_tools**
Input:
```json
{
  "toolPurpose": "- I want to inspect the isolated Keras source tree, recall relevant session context, obtain framework guidance, implement the symbolic shape fix, validate it locally, and generate the required patch artifact without any network access.",
  "tool_names": [
    "get_agent_memory",
    "get_enriched_prompt",
    "grep",
    "find_files",
    "read_file",
    "edit_file",
    "run_terminal_command",
    "write_file",
    "add_agent_memory"
  ]
}
```
Output:
```
Tools [get_agent_memory, get_enriched_prompt, grep, find_files, read_file, edit_file, run_terminal_command, write_file, add_agent_memory] are now registered and immediately available for usage.
```

2. **Tool call: get_agent_memory**
Input:
```json
{
  "toolPurpose": "- I want to read prior agent context and persistent workspace learnings before inspecting or changing the isolated Keras repository, so I avoid duplicate work and respect established conventions."
}
```
Output:
```
Successfully read agent memory content:
Learnings from previous agent sessions: Successfully loaded 129 memory entries. Use these to inform your work and avoid creating duplicate memories when calling `add_agent_memory` tool.
Loaded memories:
* Autocomplete freeSolo text is preserved on blur by skipping input reset effects when the selected value has not changed.
* MUI system spacing keys are synchronized across spacing.js, spacing.d.ts, and Box/Box.d.ts.
* This benchmark workspace lacks node_modules, and Corepack selects Yarn 4, which cannot use the repository's Yarn 1 lockfile without installation.
* Material UI Stepper defaults to ol and Step defaults to li; both expose typed component overrides via OverridableComponent.
* MUI Base listbox and select onChange callbacks use event-first signatures, with null for programmatic changes and selected value second.
* FormControlLabel resolves `required` from its prop before the control prop and exposes required/asterisk utility classes.
* MUI DialogTitle must prefer its explicit id prop over the Dialog context titleId, while retaining titleId as the fallback.
* Material Autocomplete renderOption receives ownerState as its fourth argument; ownerState includes the resolved getOptionLabel callback.
* MUI Base and Joy Slider must consume aria-labelledby before root prop forwarding and pass it explicitly to useSlider for hidden inputs.
* Generated docs sandboxes load Material Icons and Material Icons Two Tone from the shared CreateReactApp HTML template.
* MUI responsiveFontSizes skips falsy typography styles so variants disabled with undefined are ignored safely.
* MuiTabs passes ownerState to its styled ScrollbarSize slot so functional theme overrides can safely inspect Tabs state.
* Tailwind core plugin configuration supports an `only` array that acts as an explicit allow-list while preserving existing false-based disabling.
* Tailwind flex utility definitions are centralized in src/generators/flex.js in this workspace.
* This code-server project configures Unix socket permissions with the string-valued --socket-mode option and removes sockets during app disposal.
* code-server's IPC registry path must stay synchronized between src/node/vscodeSocket.ts and both constructions in patches/store-socket.diff.
* Transformer-XL LM head uses shifted labels and hidden states, returning unreduced loss shaped batch_size by sequence_length minus one.
* AutoGPT list_files prunes hidden directories in-place during os.walk to exclude metadata trees such as .git from command output.
* Default data collator omits labels when first feature has label or label_ids set to None, enabling unlabeled prediction batches.
* This transformers workspace lacks sentencepiece and sacremoses, so mBART tests require dependency stubs or a provisioned test environment.
* The benchmark sandbox blocks pytest-rerunfailures from opening its localhost status socket; disable the plugin with -p no:rerunfailures.
* Transformer-XL adaptive vocabulary resizing must rebuild input and softmax partitions, preserve retained rows, update cutoffs, and restore ties.
* Benchmark options use positive fields inference, cuda, tpu, speed, memory, env_print, and multi_process, all defaulting to true.
* T5Tokenizer.prepare_seq2seq_batch must leave target labels unprefixed; model _shift_right adds the decoder-start pad token.
* Funnel mixed-precision attention promotes projected query, key, and value tensors to fp32 before einsum with fp32 relative-attention parameters.
* Focused pytest collection is blocked because installed datasets expects pyarrow.json_ and the installed pyarrow does not provide it.
* Longformer output_attentions returns local attentions in attentions and global-query probabilities in global_attentions for PyTorch and TensorFlow.
* Trainer checkpoint resume converts optimizer global steps to skipped dataloader batches by multiplying the epoch remainder by gradient accumulation steps.
* ProphetNet disabled n-gram targets use -100 and both LM loss paths use mean NLL reduction to match CrossEntropyLoss.
* Trainer.train treats resume_from_checkpoint=False as no checkpoint by normalizing it to None before checkpoint path handling.
* BART encoder hidden states must be transposed before collection and fed back into later layers so returned batch-first tensors remain ancestors of logits.
* GPT-Neo local attention cached continuations reshape queries and slice mask rows using the current sequence length, not a fixed length of one.
* HfArgumentParser registers true-default positive bool flags before no_* flags, with no_* action default False so CLI help shows unambiguous defaults.
* Wav2Vec2 direct padding must convert Python and NumPy float64 input_values to float32 before framework tensor conversion, while preserving float16.
* Generation rejects prompts at or above max_length with ValueError and recommends max_new_tokens, preventing misleading one-token output.
* BertTokenizerFast must synchronize tokenize_chinese_chars to backend BertNormalizer.handle_chinese_chars when loading tokenizer JSON.
* This Transformers base requires tokenizers` via `TO_LANGUAGE_CODE.values()`.
* Whisper get_prompt_ids prefixes stripped prompt text with an explicit space so slow and fast tokenizers share behavior without add_prefix_space.
* Wav2Vec2 batching treats shaped inputs with rank >1 as batched and splits their first axis before sequence padding.
* GenerationConfig.from_dict must instantiate from config_dict first, then apply kwargs via update so explicit overrides win and unknown kwargs remain reportable.
* Flax GPT-2 generation casts supplied attention masks to int32 before updating its int32 extended attention mask, permitting boolean masks.
* Pipeline.save_pretrained must save a distinct image_processor; feature_extractor aliasing alone does not cover modern vision pipelines.
* EncodecFeatureExtractor padding masks must include the audio channel axis to match input_values and prevent batch/channel broadcasting.
* Whisper prompt generation must reserve one decoder-start position: prompt-adjusted max_new_tokens must stay below max_target_positions.
* Whisper text prompts retain at most max_length // 2 - 1 tokens so max_new_tokens=max_length // 2 fits the decoder context.
* EncoderDecoderModel derives decoder_attention_mask from shifted label IDs only when no explicit mask is supplied.
* IDEFICS SDPA outputs must be zeroed for fully masked query rows so pre-image text tokens cannot receive image cross-attention.
* This Transformers sandbox has pytest API and huggingface-hub version mismatches; focused inline PyTorch checks remain usable.
* Swin2SR uses num_channels_in for input layers and num_channels_out for reconstruction heads, with legacy num_channels mapped to both.
* LlamaFlashAttention2 must honor pretraining_tp for Q/K/V and output projections to match LlamaAttention projection semantics.
* SAM mask preprocessing uses configurable 256-longest-edge resizing, 256x256 padding, nearest-neighbor sampling, and returns int64 labels.
* DETR-family aspect-ratio resizing must floor the constrained short edge so the derived long edge cannot exceed max_size.
* NLLB slow and fast tokenizers accept a language_codes list and persist the resolved list through tokenizer_config.json for save/load compatibility.
* SpeechT5 auto-generated speech decoder inputs downsample decoder attention masks with the configured reduction factor in TTS and speech-to-speech paths.
* OneFormer metadata loading opens an existing local class_info_file directly before falling back to a dataset Hub download.
* Mixtral router balancing uses full-expert softmax before top-k selection and averages router probabilities over the token axis.
* Mixtral load-balancing loss expands the 2D attention mask across layers and top-k routes so padding tokens do not affect expert averages.
* ESM tokenizer get_vocab must merge added_tokens_encoder, and _add_tokens must forward special_tokens so normal additions grow len(tokenizer).
* Whisper audio classification weighted sums must force hidden states and stack encoder_outputs[1] for tuple and ModelOutput compatibility.
* Wav2Vec2CTCTokenizer post-conversion filtering must compare token strings with all_special_tokens, including unknown IDs mapped to .
* IdeficsProcessor must preserve tokenizer attention masks when padding, then align them with any processor-added batch padding.
* Flax Mistral sliding_window must use triu offset 1-window so the configured size includes the current token, matching PyTorch.
* Mamba slow-path recurrence must clone cached SSM state before later in-place cache updates to preserve PyTorch autograd versioning.
* Seq2SeqTrainer strictly validates loaded generation configs so warnings become actionable errors before training and checkpoint saving.
* DataCollatorForSeq2Seq MAX_LENGTH label padding uses max(configured max_length, longest label), then applies pad_to_multiple_of.
* WhisperGenerationMixin now builds batched decoder prefixes so explicit language lists and mixed auto-detected languages work in short- and long-form generation.
* PyTorch model-file-not-found errors list model.safetensors alongside other supported weight filenames in the default loading path.
* PyTorch generate must fill missing special-token IDs in an explicit GenerationConfig from the model's generation config.
* NumPy center_crop uses ceiling leading padding so odd undersized dimensions preserve the requested size and PIL-compatible alignment.
* LlamaTokenizerFast must forward add_prefix_space to slow-tokenizer conversion; otherwise the converter silently uses the slow tokenizer's True default.
* VQA pipeline normalizes image/question lists into per-example dictionaries, broadcasts scalars, and rejects unequal paired-list lengths.
* StopStringCriteria embedding dimensions must default to one sentinel slot when matching-position or end-overlap maps are empty.
* Encodec forward and decode resolve return_dict only when it is None, preserving an explicit False tuple request.
* CSVLoader must use an empty csv_args mapping by default so csv.DictReader applies its built-in dialect defaults; csv.Dialect attributes are None.
* MRKL action parsing accepts arbitrary whitespace around action values and the Action Input delimiter, including LLaMA-style newlines.
* WhatsAppChatLoader timestamps must accept Unicode whitespace, including U+202F and U+00A0, before AM/PM in exported chats.
* OpenAI callback pricing normalizes legacy ':ft-' model IDs to base-finetuned and uses Ada/Babbage/Curie/Davinci fine-tune rates.
* WebBaseLoader custom header templates must bypass fake_useragent and preserve the caller-provided User-Agent.
* PydanticOutputParser parses extracted JSON with strict=False so literal newlines and other control characters in string values are accepted.
* Chroma.update_document must call embed_documents([document.page_content]) so one document is embedded instead of its individual characters.
* FAISS distance configuration uses DistanceStrategy from vectorstores/utils.py, with metric-aware relevance functions on VectorStore.
* RecursiveCharacterTextSplitter separators are literal strings; escape them before regex splitting when keep_separator is enabled.
* This LangChain 0.0.188 repo requires Pydantic 1; the host's Pydantic 2.13 blocks pytest collection at legacy root_validator usage.
* initialize_agent supports AgentType enum members and matching string values; tracing tags must handle both representations.
* BooleanOutputParser recognizes standalone case-insensitive true/false tokens in explanatory text using regex word boundaries, avoiding substring false positives.
* This LangChain core workspace cannot collect tests because the required langsmith package is absent; compile and Ruff checks remain available.
* yt-dlp LenientSimpleCookie ignores malformed fragments rejected by http.cookies.Morsel so later valid cookies remain parseable.
* yt-dlp system config precedence checks /etc/yt-dlp.conf before /etc/yt-dlp/config and config.txt.
* The benchmark sandbox blocks localhost socket binding, causing 10 core HTTP tests to fail despite 296 passing.
* DiscoveryPlus path tokens x-discovery-token/x-goog-token must be propagated as segment query params; DASH now honors extra_param_to_segment_url.
* yt-dlp default format selection must treat simulate=True as a real download while retaining download=False metadata-only behavior.
* Keras Torch conv manually applies SAME padding; compare padding case-insensitively because depthwise and separable conv delegate to it.
* This Keras benchmark environment lacks the absl package, so pytest collection fails before tests run; py_compile and AST contract checks remain available.
* YouTube nsig discovery supports indirect n-key construction via String.fromCharCode(110) and matched-index "nn" access.
* Keras TextVectorization deserialization must convert JSON list-valued ngrams back to tuples before constructor validation.
* Keras CompileLoss must flatten y_true with y_pred and resolve each generic loss against its corresponding output tensors.
* This Keras sandbox lacks absl and dm-tree, blocking focused pytest collection and runtime imports; py_compile and flake8 are available.
* Keras GaussianDropout must pass inputs.dtype to backend.random.normal so mixed-bfloat16 noise matches input precision.
* Keras ops.numpy.nonzero must route KerasTensor inputs through Nonzero().symbolic_call while concrete tensors call backend.numpy.nonzero directly.
* Keras optimizer zero-argument callables are evaluated without iteration; Adam resolves callable beta_1 and beta_2 before tensor casts and arithmetic.
* Keras DTypePolicy array-like inputs must convert without a forced dtype, then autocast only floating tensors; this preserves NumPy integer dtypes.
* Keras TensorFlow Conv3D channels-first must transpose NCDHW to NDHWC on CPU and transpose outputs back; grouped convolution keeps this inside XLA.
* Keras StringLookup must set encoding before IndexLookup.__init__, because superclass tensor-vocabulary setup decodes values through that attribute.
* Keras TensorFlow linspace casts tensor-valued num to the output dtype only for floating-point step arithmetic, preserving tf.linspace's integer num.
* Keras JAX distribution initialization forwards job_addresses to jax.distributed.initialize via the coordinator_address keyword.
* When redirecting RTK git diff to a patch file, use --no-compact; compacted output can omit headers and produce an invalid patch.
* RTK git diff redirected to a file may omit the final newline; validate with git apply --check and regenerate with direct git diff if corrupt.
* A timed-out RTK git clone may leave a child process running; verify HEAD again before patch generation and reset to the requested base if it moved.
* After cherry-pick --no-commit, use git reset and git add -N for new files so plain git diff captures the complete patch.
* When creating a nested Git repo inside another repo, run `git init` with the nested absolute path to avoid reinitializing the parent repository.
```

3. **Tool call: grep**
Input:
```json
{
  "pattern": "class Repeat|def repeat\\(",
  "searchPath": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826/keras",
  "glob": [
    "*.py"
  ],
  "outputMode": "matches",
  "context": 4,
  "headLimit": 100,
  "toolPurpose": "- I need to locate the Keras repeat operation and its symbolic output-shape implementation in the isolated source tree before making the minimal production fix."
}
```
Output:
```
{"success":true,"mode":"content","numFiles":7,"numLines":8,"pagination":{"offset":0,"limit":100,"returned":8,"total":8,"hasMore":false},"matches":[{"file":"src/legacy/backend.py","line":1307,"content":"def repeat(x, n):","contextBefore":[{"line":1303,"content":"return x"},{"line":1304,"content":""},{"line":1305,"content":""},{"line":1306,"content":"@keras_export(\"keras._legacy.backend.repeat\")"}],"contextAfter":[{"line":1308,"content":"\"\"\"DEPRECATED.\"\"\""},{"line":1309,"content":"assert ndim(x) == 2"},{"line":1310,"content":"x = tf.expand_dims(x, 1)"},{"line":1311,"content":"pattern = tf.stack([1, n, 1])"}],"matches":["def repeat("]},{"file":"src/ops/numpy.py","line":4337,"content":"class Repeat(Operation):","contextBefore":[{"line":4333,"content":"return Reciprocal().symbolic_call(x)"},{"line":4334,"content":"return backend.numpy.reciprocal(x)"},{"line":4335,"content":""},{"line":4336,"content":""}],"contextAfter":[{"line":4338,"content":"def __init__(self, repeats, axis=None):"},{"line":4339,"content":"super().__init__()"},{"line":4340,"content":"self.axis = axis"},{"line":4341,"content":"self.repeats = repeats"}],"matches":["class Repeat"]},{"file":"src/ops/numpy.py","line":4372,"content":"def repeat(x, repeats, axis=None):","contextBefore":[{"line":4368,"content":"return KerasTensor(output_shape, dtype=x.dtype)"},{"line":4369,"content":""},{"line":4370,"content":""},{"line":4371,"content":"@keras_export([\"keras.ops.repeat\", \"keras.ops.numpy.repeat\"])"}],"contextAfter":[{"line":4373,"content":"\"\"\"Repeat each element of a tensor after themselves."},{"line":4374,"content":""},{"line":4375,"content":"Args:"},{"line":4376,"content":"x: Input tensor."}],"matches":["def repeat("]},{"file":"src/backend/jax/numpy.py","line":854,"content":"def repeat(x, repeats, axis=None):","contextBefore":[{"line":850,"content":"x = convert_to_tensor(x)"},{"line":851,"content":"return jnp.reciprocal(x)"},{"line":852,"content":""},{"line":853,"content":""}],"contextAfter":[{"line":855,"content":"x = convert_to_tensor(x)"},{"line":856,"content":"return jnp.repeat(x, repeats, axis=axis)"},{"line":857,"content":""},{"line":858,"content":""}],"matches":["def repeat("]},{"file":"src/backend/tensorflow/numpy.py","line":1769,"content":"def repeat(x, repeats, axis=None):","contextBefore":[{"line":1765,"content":"x = convert_to_tensor(x)"},{"line":1766,"content":"return tf.math.reciprocal(x)"},{"line":1767,"content":""},{"line":1768,"content":""}],"contextAfter":[{"line":1770,"content":"x = convert_to_tensor(x)"},{"line":1771,"content":"# TODO: tf.repeat doesn't support uint16"},{"line":1772,"content":"if standardize_dtype(x.dtype) == \"uint16\":"},{"line":1773,"content":"x = tf.cast(x, \"uint32\")"}],"matches":["def repeat("]},{"file":"src/backend/numpy/numpy.py","line":778,"content":"def repeat(x, repeats, axis=None):","contextBefore":[{"line":774,"content":"def reciprocal(x):"},{"line":775,"content":"return np.reciprocal(x)"},{"line":776,"content":""},{"line":777,"content":""}],"contextAfter":[{"line":779,"content":"return np.repeat(x, repeats, axis=axis)"},{"line":780,"content":""},{"line":781,"content":""},{"line":782,"content":"def reshape(x, newshape):"}],"matches":["def repeat("]},{"file":"src/backend/torch/numpy.py","line":1167,"content":"def repeat(x, repeats, axis=None):","contextBefore":[{"line":1163,"content":"x = convert_to_tensor(x)"},{"line":1164,"content":"return torch.reciprocal(x)"},{"line":1165,"content":""},{"line":1166,"content":""}],"contextAfter":[{"line":1168,"content":"x = convert_to_tensor(x)"},{"line":1169,"content":""},{"line":1170,"content":"if get_device() == \"meta\":"},{"line":1171,"content":"x = KerasTensor(x.shape, standardize_dtype(x.dtype))"}],"matches":["def repeat("]},{"file":"src/layers/reshaping/repeat_vector.py","line":8,"content":"class RepeatVector(Layer):","contextBefore":[{"line":4,"content":"from keras.src.layers.layer import Layer"},{"line":5,"content":""},{"line":6,"content":""},{"line":7,"content":"@keras_export(\"keras.layers.RepeatVector\")"}],"contextAfter":[{"line":9,"content":"\"\"\"Repeats the input n times."},{"line":10,"content":""},{"line":11,"content":"Example:"},{"line":12,"content":""}],"matches":["class Repeat"]}]}
```

4. **Tool call: read_file**
Input:
```json
{
  "fileNames": [
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826/keras/src/ops/numpy.py",
      "startLine": 4310
    }
  ],
  "toolPurpose": "- I want to inspect the complete Repeat operation and nearby shape-inference conventions before implementing the symbolic axis=None correction."
}
```
Output:
```

File successfully read, file name numpy.py with file path: enc_file_sovfhn/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826/keras/src/ops/numpy.py

**File Read Information:**
- Lines read: 4310 to 6226 (1917 lines)
- Total lines in file: 6226
- Remaining lines: 0

Content:

    def compute_output_spec(self, x):
        return KerasTensor(x.shape)

@keras_export(
    [
        "keras.ops.reciprocal",
        "keras.ops.numpy.reciprocal",
    ]
)
def reciprocal(x):
    """Return the reciprocal of the argument, element-wise.

    Calculates `1/x`.

    Args:
        x: Input tensor.

    Returns:
        Output tensor, element-wise reciprocal of `x`.
    """
    if any_symbolic_tensors((x,)):
        return Reciprocal().symbolic_call(x)
    return backend.numpy.reciprocal(x)

class Repeat(Operation):
    def __init__(self, repeats, axis=None):
        super().__init__()
        self.axis = axis
        self.repeats = repeats

    def call(self, x):
        return backend.numpy.repeat(x, self.repeats, axis=self.axis)

    def compute_output_spec(self, x):
        x_shape = list(x.shape)
        if self.axis is None:
            if None in x_shape:
                return KerasTensor([None], dtype=x.dtype)

            x_flatten_size = int(np.prod(x_shape))
            if isinstance(self.repeats, int):
                output_shape = [x_flatten_size * self.repeats]
            else:
                output_shape = [int(np.sum(self.repeats))]
            return KerasTensor(output_shape, dtype=x.dtype)

        size_on_ax = x_shape[self.axis]
        output_shape = x_shape
        if isinstance(self.repeats, int):
            if size_on_ax is None:
                output_shape[self.axis] = None
            else:
                output_shape[self.axis] = size_on_ax * self.repeats
        else:
            output_shape[self.axis] = int(np.sum(self.repeats))
        return KerasTensor(output_shape, dtype=x.dtype)

@keras_export(["keras.ops.repeat", "keras.ops.numpy.repeat"])
def repeat(x, repeats, axis=None):
    """Repeat each element of a tensor after themselves.

    Args:
        x: Input tensor.
        repeats: The number of repetitions for each element.
        axis: The axis along which to repeat values. By default, use
            the flattened input array, and return a flat output array.

    Returns:
        Output tensor.
    """
    if any_symbolic_tensors((x,)):
        return Repeat(repeats, axis=axis).symbolic_call(x)
    return backend.numpy.repeat(x, repeats, axis=axis)

class Reshape(Operation):
    def __init__(self, newshape):
        super().__init__()
        self.newshape = newshape

    def call(self, x):
        return backend.numpy.reshape(x, self.newshape)

    def compute_output_spec(self, x):
        output_shape = operation_utils.compute_reshape_output_shape(
            x.shape, self.newshape, "newshape"
        )
        sparse = getattr(x, "sparse", False)
        return KerasTensor(output_shape, dtype=x.dtype, sparse=sparse)

@keras_export(["keras.ops.reshape", "keras.ops.numpy.reshape"])
def reshape(x, newshape):
    """Gives a new shape to a tensor without changing its data.

    Args:
        x: Input tensor.
        newshape: The new shape should be compatible with the original shape.
            One shape dimension can be -1 in which case the value is
            inferred from the length of the array and remaining dimensions.

    Returns:
        The reshaped tensor.
    """
    if any_symbolic_tensors((x,)):
        return Reshape(newshape).symbolic_call(x)
    return backend.numpy.reshape(x, newshape)

class Roll(Operation):
    def __init__(self, shift, axis=None):
        super().__init__()
        self.shift = shift
        self.axis = axis

    def call(self, x):
        return backend.numpy.roll(x, self.shift, self.axis)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)

@keras_export(["keras.ops.roll", "keras.ops.numpy.roll"])
def roll(x, shift, axis=None):
    """Roll tensor elements along a given axis.

    Elements that roll beyond the last position are re-introduced at the first.

    Args:
        x: Input tensor.
        shift: The number of places by which elements are shifted.
        axis: The axis along which elements are shifted. By default, the
            array is flattened before shifting, after which the original
            shape is restored.

    Returns:
        Output tensor.
    """
    if any_symbolic_tensors((x,)):
        return Roll(shift, axis=axis).symbolic_call(x)
    return backend.numpy.roll(x, shift, axis=axis)

class Round(Operation):
    def __init__(self, decimals=0):
        super().__init__()
        self.decimals = decimals

    def call(self, x):
        return backend.numpy.round(x, self.decimals)

    def compute_output_spec(self, x):
        sparse = getattr(x, "sparse", False)
        return KerasTensor(x.shape, dtype=x.dtype, sparse=sparse)

@keras_export(["keras.ops.round", "keras.ops.numpy.round"])
def round(x, decimals=0):
    """Evenly round to the given number of decimals.

    Args:
        x: Input tensor.
        decimals: Number of decimal places to round to. Defaults to `0`.

    Returns:
        Output tensor.
    """
    if any_symbolic_tensors((x,)):
        return Round(decimals).symbolic_call(x)
    return backend.numpy.round(x, decimals)

class Sign(Operation):
    def call(self, x):
        return backend.numpy.sign(x)

    def compute_output_spec(self, x):
        sparse = getattr(x, "sparse", False)
        return KerasTensor(x.shape, dtype=x.dtype, sparse=sparse)

@keras_export(["keras.ops.sign", "keras.ops.numpy.sign"])
def sign(x):
    """Returns a tensor with the signs of the elements of `x`.

    Args:
        x: Input tensor.

    Returns:
        Output tensor of same shape as `x`.
    """
    if any_symbolic_tensors((x,)):
        return Sign().symbolic_call(x)
    return backend.numpy.sign(x)

class Sin(Operation):
    def call(self, x):
        return backend.numpy.sin(x)

    def compute_output_spec(self, x):
        dtype = backend.standardize_dtype(getattr(x, "dtype", backend.floatx()))
        if dtype == "int64":
            dtype = backend.floatx()
        else:
            dtype = dtypes.result_type(dtype, float)
        sparse = getattr(x, "sparse", False)
        return KerasTensor(x.shape, dtype=dtype, sparse=sparse)

@keras_export(["keras.ops.sin", "keras.ops.numpy.sin"])
def sin(x):
    """Trigonometric sine, element-wise.

    Arguments:
        x: Input tensor.

    Returns:
        Output tensor of same shape as `x`.
    """
    if any_symbolic_tensors((x,)):
        return Sin().symbolic_call(x)
    return backend.numpy.sin(x)

class Sinh(Operation):
    def call(self, x):
        return backend.numpy.sinh(x)

    def compute_output_spec(self, x):
        dtype = backend.standardize_dtype(getattr(x, "dtype", backend.floatx()))
        if dtype == "int64":
            dtype = backend.floatx()
        else:
            dtype = dtypes.result_type(dtype, float)
        sparse = getattr(x, "sparse", False)
        return KerasTensor(x.shape, dtype=dtype, sparse=sparse)

@keras_export(["keras.ops.sinh", "keras.ops.numpy.sinh"])
def sinh(x):
    """Hyperbolic sine, element-wise.

    Arguments:
        x: Input tensor.

    Returns:
        Output tensor of same shape as `x`.
    """
    if any_symbolic_tensors((x,)):
        return Sinh().symbolic_call(x)
    return backend.numpy.sinh(x)

class Size(Operation):
    def call(self, x):
        return backend.numpy.size(x)

    def compute_output_spec(self, x):
        return KerasTensor([], dtype="int32")

@keras_export(["keras.ops.size", "keras.ops.numpy.size"])
def size(x):
    """Return the number of elements in a tensor.

    Args:
        x: Input tensor.

    Returns:
        Number of elements in `x`.
    """
    if any_symbolic_tensors((x,)):
        return Size().symbolic_call(x)
    return backend.numpy.size(x)

class Sort(Operation):
    def __init__(self, axis=-1):
        super().__init__()
        self.axis = axis

    def call(self, x):
        return backend.numpy.sort(x, axis=self.axis)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, x.dtype)

@keras_export(["keras.ops.sort", "keras.ops.numpy.sort"])
def sort(x, axis=-1):
    """Sorts the elements of `x` along a given axis in ascending order.

    Args:
        x: Input tensor.
        axis: Axis along which to sort. If `None`, the tensor is flattened
            before sorting. Defaults to `-1`; the last axis.

    Returns:
        Sorted tensor.
    """
    if any_symbolic_tensors((x,)):
        return Sort(axis=axis).symbolic_call(x)
    return backend.numpy.sort(x, axis=axis)

class Split(Operation):
    def __init__(self, indices_or_sections, axis=0):
        super().__init__()
        if not isinstance(indices_or_sections, int):
            indices_or_sections = tuple(indices_or_sections)
        self.indices_or_sections = indices_or_sections
        self.axis = axis

    def call(self, x):
        return backend.numpy.split(x, self.indices_or_sections, axis=self.axis)

    def compute_output_spec(self, x):
        x_shape = list(x.shape)
        x_size_on_axis = x_shape[self.axis]
        if isinstance(self.indices_or_sections, int):
            if x_size_on_axis is None:
                x_shape[self.axis] = None
                return [
                    KerasTensor(x_shape, dtype=x.dtype)
                    for _ in range(self.indices_or_sections)
                ]
            if np.mod(x_size_on_axis, self.indices_or_sections) != 0:
                raise ValueError(
                    "`x` size on given `axis` must be dividible by "
                    "`indices_or_sections` when `indices_or_sections` is an "
                    f"int. But received {x_size_on_axis} and "
                    f"{self.indices_or_sections}."
                )
            size = x_size_on_axis // self.indices_or_sections
            x_shape[self.axis] = size
            return [
                KerasTensor(x_shape, dtype=x.dtype)
                for _ in range(self.indices_or_sections)
            ]

        indices_or_sections = (0, *self.indices_or_sections, x_size_on_axis)
        output_size = np.diff(indices_or_sections)
        outputs = []
        for i in range(len(output_size)):
            output_shape = list(x_shape)
            output_shape[self.axis] = int(output_size[i])
            outputs.append(KerasTensor(output_shape, dtype=x.dtype))
        return outputs

@keras_export(["keras.ops.split", "keras.ops.numpy.split"])
def split(x, indices_or_sections, axis=0):
    """Split a tensor into chunks.

    Args:
        x: Input tensor.
        indices_or_sections: If an integer, N, the tensor will be split into N
            equal sections along `axis`. If a 1-D array of sorted integers,
            the entries indicate indices at which the tensor will be split
            along `axis`.
        axis: Axis along which to split. Defaults to `0`.

    Note:
        A split does not have to result in equal division when using
        Torch backend.

    Returns:
        A list of tensors.
    """
    if any_symbolic_tensors((x,)):
        return Split(indices_or_sections, axis=axis).symbolic_call(x)
    return backend.numpy.split(x, indices_or_sections, axis=axis)

class Stack(Operation):
    def __init__(self, axis=0):
        super().__init__()
        self.axis = axis

    def call(self, xs):
        return backend.numpy.stack(xs, axis=self.axis)

    def compute_output_spec(self, xs):
        first_shape = xs[0].shape
        dtypes_to_resolve = []
        for x in xs:
            if not shape_equal(x.shape, first_shape, axis=[], allow_none=True):
                raise ValueError(
                    "Every value in `xs` must have the same shape. But found "
                    f"element of shape {x.shape},  which is different from the "
                    f"first element's shape {first_shape}."
                )
            dtypes_to_resolve.append(getattr(x, "dtype", type(x)))

        size_on_axis = len(xs)
        output_shape = list(first_shape)
        if self.axis == -1:
            output_shape = output_shape + [size_on_axis]
        elif self.axis >= 0:
            output_shape.insert(self.axis, size_on_axis)
        else:
            output_shape.insert(self.axis + 1, size_on_axis)
        output_dtype = dtypes.result_type(*dtypes_to_resolve)
        return KerasTensor(output_shape, dtype=output_dtype)

@keras_export(["keras.ops.stack", "keras.ops.numpy.stack"])
def stack(x, axis=0):
    """Join a sequence of tensors along a new axis.

    The `axis` parameter specifies the index of the new axis in the
    dimensions of the result.

    Args:
        x: A sequence of tensors.
        axis: Axis along which to stack. Defaults to `0`.

    Returns:
        The stacked tensor.
    """
    if any_symbolic_tensors((x,)):
        return Stack(axis=axis).symbolic_call(x)
    return backend.numpy.stack(x, axis=axis)

class Std(Operation):
    def __init__(self, axis=None, keepdims=False):
        super().__init__()
        if isinstance(axis, int):
            self.axis = [axis]
        else:
            self.axis = axis
        self.keepdims = keepdims

    def call(self, x):
        return backend.numpy.std(x, axis=self.axis, keepdims=self.keepdims)

    def compute_output_spec(self, x):
        output_dtype = backend.standardize_dtype(x.dtype)
        if "int" in output_dtype or output_dtype == "bool":
            output_dtype = backend.floatx()
        return KerasTensor(
            reduce_shape(x.shape, axis=self.axis, keepdims=self.keepdims),
            dtype=output_dtype,
        )

@keras_export(["keras.ops.std", "keras.ops.numpy.std"])
def std(x, axis=None, keepdims=False):
    """Compute the standard deviation along the specified axis.

    Args:
        x: Input tensor.
        axis: Axis along which to compute standard deviation.
            Default is to compute the standard deviation of the
            flattened tensor.
        keepdims: If this is set to `True`, the axes which are reduced are left
            in the result as dimensions with size one.

    Returns:
        Output tensor containing the standard deviation values.
    """
    if any_symbolic_tensors((x,)):
        return Std(axis=axis, keepdims=keepdims).symbolic_call(x)
    return backend.numpy.std(x, axis=axis, keepdims=keepdims)

class Swapaxes(Operation):
    def __init__(self, axis1, axis2):
        super().__init__()

        self.axis1 = axis1
        self.axis2 = axis2

    def call(self, x):
        return backend.numpy.swapaxes(x, self.axis1, self.axis2)

    def compute_output_spec(self, x):
        x_shape = list(x.shape)
        tmp = x_shape[self.axis1]
        x_shape[self.axis1] = x_shape[self.axis2]
        x_shape[self.axis2] = tmp
        return KerasTensor(x_shape, dtype=x.dtype)

@keras_export(["keras.ops.swapaxes", "keras.ops.numpy.swapaxes"])
def swapaxes(x, axis1, axis2):
    """Interchange two axes of a tensor.

    Args:
        x: Input tensor.
        axis1: First axis.
        axis2: Second axis.

    Returns:
        A tensor with the axes swapped.
    """
    if any_symbolic_tensors((x,)):
        return Swapaxes(axis1, axis2).symbolic_call(x)
    return backend.numpy.swapaxes(x, axis1=axis1, axis2=axis2)

class Take(Operation):
    def __init__(self, axis=None):
        super().__init__()
        self.axis = axis

    def call(self, x, indices):
        return backend.numpy.take(x, indices, axis=self.axis)

    def compute_output_spec(self, x, indices):
        x_shape = list(x.shape)
        if isinstance(indices, KerasTensor):
            indices_shape = list(indices.shape)
        else:
            indices_shape = list(getattr(np.array(indices), "shape", []))
        if self.axis is None:
            return KerasTensor(indices_shape, dtype=x.dtype)

        # make sure axis is non-negative
        axis = len(x_shape) + self.axis if self.axis  len(repeats):
            repeats = [1] * (len(x_shape) - len(repeats)) + repeats
        else:
            x_shape = [1] * (len(repeats) - len(x_shape)) + x_shape

        output_shape = []
        for x_size, repeat in zip(x_shape, repeats):
            if x_size is None:
                output_shape.append(None)
            else:
                output_shape.append(x_size * repeat)
        return KerasTensor(output_shape, dtype=x.dtype)

@keras_export(["keras.ops.tile", "keras.ops.numpy.tile"])
def tile(x, repeats):
    """Repeat `x` the number of times given by `repeats`.

    If `repeats` has length `d`, the result will have dimension of
    `max(d, x.ndim)`.

    If `x.ndim  d`, `repeats` is promoted to `x.ndim` by prepending 1's to it.

    Args:
        x: Input tensor.
        repeats: The number of repetitions of `x` along each axis.

    Returns:
        The tiled output tensor.
    """
    if any_symbolic_tensors((x,)):
        return Tile(
            repeats,
        ).symbolic_call(x)
    return backend.numpy.tile(x, repeats)

class Trace(Operation):
    def __init__(self, offset=0, axis1=0, axis2=1):
        super().__init__()
        self.offset = offset
        self.axis1 = axis1
        self.axis2 = axis2

    def call(self, x):
        return backend.numpy.trace(
            x, offset=self.offset, axis1=self.axis1, axis2=self.axis2
        )

    def compute_output_spec(self, x):
        x_shape = list(x.shape)
        x_shape[self.axis1] = -1
        x_shape[self.axis2] = -1
        output_shape = list(filter((-1).__ne__, x_shape))
        output_dtype = backend.standardize_dtype(x.dtype)
        if output_dtype not in ("int64", "uint32", "uint64"):
            output_dtype = dtypes.result_type(output_dtype, "int32")
        return KerasTensor(output_shape, dtype=output_dtype)

@keras_export(["keras.ops.trace", "keras.ops.numpy.trace"])
def trace(x, offset=0, axis1=0, axis2=1):
    """Return the sum along diagonals of the tensor.

    If `x` is 2-D, the sum along its diagonal with the given offset is
    returned, i.e., the sum of elements `x[i, i+offset]` for all `i`.

    If a has more than two dimensions, then the axes specified by `axis1`
    and `axis2` are used to determine the 2-D sub-arrays whose traces are
    returned.

    The shape of the resulting tensor is the same as that of `x` with `axis1`
    and `axis2` removed.

    Args:
        x: Input tensor.
        offset: Offset of the diagonal from the main diagonal. Can be
            both positive and negative. Defaults to `0`.
        axis1: Axis to be used as the first axis of the 2-D sub-arrays.
            Defaults to `0`.(first axis).
        axis2: Axis to be used as the second axis of the 2-D sub-arrays.
            Defaults to `1` (second axis).

    Returns:
        If `x` is 2-D, the sum of the diagonal is returned. If `x` has
        larger dimensions, then a tensor of sums along diagonals is
        returned.
    """
    if any_symbolic_tensors((x,)):
        return Trace(offset, axis1, axis2).symbolic_call(x)
    return backend.numpy.trace(x, offset=offset, axis1=axis1, axis2=axis2)

class Tri(Operation):
    def __init__(self, k=0, dtype=None):
        super().__init__()
        self.k = k
        self.dtype = dtype or backend.floatx()

    def call(self, N, M=None):
        return backend.numpy.tri(N=N, M=M, k=self.k, dtype=self.dtype)

    def compute_output_spec(self, N, M=None):
        if M is None:
            M = N
        return KerasTensor((N, M), dtype=self.dtype)

@keras_export(["keras.ops.tri", "keras.ops.numpy.tri"])
def tri(N, M=None, k=0, dtype=None):
    """Return a tensor with ones at and below a diagonal and zeros elsewhere.

    Args:
        N: Number of rows in the tensor.
        M: Number of columns in the tensor.
        k: The sub-diagonal at and below which the array is filled.
            `k = 0` is the main diagonal, while `k  0` is above. The default is 0.
        dtype: Data type of the returned tensor. The default is "float32".

    Returns:
        Tensor with its lower triangle filled with ones and zeros elsewhere.
        `T[i, j] == 1` for `j  0` is above it.

    Returns:
        Lower triangle of `x`, of same shape and data type as `x`.
    """
    if any_symbolic_tensors((x,)):
        return Tril(k=k).symbolic_call(x)
    return backend.numpy.tril(x, k=k)

class Triu(Operation):
    def __init__(self, k=0):
        super().__init__()
        self.k = k

    def call(self, x):
        return backend.numpy.triu(x, k=self.k)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)

@keras_export(["keras.ops.triu", "keras.ops.numpy.triu"])
def triu(x, k=0):
    """Return upper triangle of a tensor.

    For tensors with `ndim` exceeding 2, `triu` will apply to the
    final two axes.

    Args:
        x: Input tensor.
        k: Diagonal below which to zero elements. Defaults to `0`. the
            main diagonal. `k  0` is above it.

    Returns:
        Upper triangle of `x`, of same shape and data type as `x`.
    """
    if any_symbolic_tensors((x,)):
        return Triu(k=k).symbolic_call(x)
    return backend.numpy.triu(x, k=k)

class Vdot(Operation):
    def call(self, x1, x2):
        return backend.numpy.vdot(x1, x2)

    def compute_output_spec(self, x1, x2):
        dtype = dtypes.result_type(
            getattr(x1, "dtype", type(x1)),
            getattr(x2, "dtype", type(x2)),
        )
        return KerasTensor([], dtype=dtype)

@keras_export(["keras.ops.vdot", "keras.ops.numpy.vdot"])
def vdot(x1, x2):
    """Return the dot product of two vectors.

    If the first argument is complex, the complex conjugate of the first
    argument is used for the calculation of the dot product.

    Multidimensional tensors are flattened before the dot product is taken.

    Args:
        x1: First input tensor. If complex, its complex conjugate is taken
            before calculation of the dot product.
        x2: Second input tensor.

    Returns:
        Output tensor.
    """
    if any_symbolic_tensors((x1, x2)):
        return Vdot().symbolic_call(x1, x2)
    return backend.numpy.vdot(x1, x2)

@keras_export(["keras.ops.vectorize", "keras.ops.numpy.vectorize"])
def vectorize(pyfunc, *, excluded=None, signature=None):
    """Turn a function into a vectorized function.

    Example:

    ```python
    def myfunc(a, b):
        return a + b

    vfunc = keras.ops.vectorize(myfunc)
    y = vfunc([1, 2, 3, 4], 2)  # Returns Tensor([3, 4, 5, 6])
    ```

    Args:
        pyfunc: Callable of a single tensor argument.
        excluded: Optional set of integers representing
            positional arguments for which the function
            will not be vectorized.
            These will be passed directly to `pyfunc` unmodified.
        signature: Optional generalized universal function signature,
            e.g., `"(m,n),(n)->(m)"` for vectorized
            matrix-vector multiplication. If provided,
            `pyfunc` will be called with (and expected to return)
            arrays with shapes given by the size of corresponding
            core dimensions. By default, `pyfunc` is assumed
            to take scalars tensors as input and output.

    Returns:
        A new function that applies `pyfunc` to every element
        of its input along axis 0 (the batch axis).
    """
    if not callable(pyfunc):
        raise ValueError(
            "Expected argument `pyfunc` to be a callable. "
            f"Received: pyfunc={pyfunc}"
        )
    return backend.numpy.vectorize(
        pyfunc, excluded=excluded, signature=signature
    )

class Vstack(Operation):
    def call(self, xs):
        return backend.numpy.vstack(xs)

    def compute_output_spec(self, xs):
        first_shape = xs[0].shape
        total_size_on_axis = 0
        dtypes_to_resolve = []
        for x in xs:
            if not shape_equal(x.shape, first_shape, axis=[0], allow_none=True):
                raise ValueError(
                    "Every value in `xs` must have the same shape except on "
                    f"the `axis` dim. But found element of shape {x.shape}, "
                    f"which is different from the first element's "
                    f"shape {first_shape}."
                )
            if total_size_on_axis is None or x.shape[0] is None:
                total_size_on_axis = None
            else:
                total_size_on_axis += x.shape[0]
            dtypes_to_resolve.append(getattr(x, "dtype", type(x)))
        output_shape = list(first_shape)
        output_shape[0] = total_size_on_axis
        output_dtype = dtypes.result_type(*dtypes_to_resolve)
        return KerasTensor(output_shape, output_dtype)

@keras_export(["keras.ops.vstack", "keras.ops.numpy.vstack"])
def vstack(xs):
    """Stack tensors in sequence vertically (row wise).

    Args:
        xs: Sequence of tensors.

    Returns:
        Tensor formed by stacking the given tensors.
    """
    if any_symbolic_tensors((xs,)):
        return Vstack().symbolic_call(xs)
    return backend.numpy.vstack(xs)

class Where(Operation):
    def call(self, condition, x1=None, x2=None):
        return backend.numpy.where(condition, x1, x2)

    def compute_output_spec(self, condition, x1, x2):
        condition_shape = getattr(condition, "shape", [])
        x1_shape = getattr(x1, "shape", [])
        x2_shape = getattr(x2, "shape", [])
        output_shape = broadcast_shapes(condition_shape, x1_shape)
        output_shape = broadcast_shapes(output_shape, x2_shape)
        output_dtype = dtypes.result_type(
            getattr(x1, "dtype", type(x1) if x1 is not None else "int"),
            getattr(x2, "dtype", type(x2) if x2 is not None else "int"),
        )
        return KerasTensor(output_shape, dtype=output_dtype)

@keras_export(["keras.ops.where", "keras.ops.numpy.where"])
def where(condition, x1=None, x2=None):
    """Return elements chosen from `x1` or `x2` depending on `condition`.

    Args:
        condition: Where `True`, yield `x1`, otherwise yield `x2`.
        x1: Values from which to choose when `condition` is `True`.
        x2: Values from which to choose when `condition` is `False`.

    Returns:
        A tensor with elements from `x1` where `condition` is `True`, and
        elements from `x2` where `condition` is `False`.
    """
    if (x1 is None and x2 is not None) or (x1 is not None and x2 is None):
        raise ValueError(
            "`x1` and `x2` either both should be `None`"
            " or both should have non-None value."
        )
    if any_symbolic_tensors((condition, x1, x2)):
        return Where().symbolic_call(condition, x1, x2)
    return backend.numpy.where(condition, x1, x2)

class Subtract(Operation):
    def call(self, x1, x2):
        return backend.numpy.subtract(x1, x2)

    def compute_output_spec(self, x1, x2):
        x1_shape = getattr(x1, "shape", [])
        x2_shape = getattr(x2, "shape", [])
        output_shape = broadcast_shapes(x1_shape, x2_shape)
        x1_sparse = getattr(x1, "sparse", False)
        x2_sparse = getattr(x2, "sparse", False)
        output_sparse = x1_sparse and x2_sparse
        dtype = dtypes.result_type(
            getattr(x1, "dtype", type(x1)),
            getattr(x2, "dtype", type(x2)),
        )
        return KerasTensor(output_shape, dtype=dtype, sparse=output_sparse)

@keras_export(["keras.ops.subtract", "keras.ops.numpy.subtract"])
def subtract(x1, x2):
    """Subtract arguments element-wise.

    Args:
        x1: First input tensor.
        x2: Second input tensor.

    Returns:
        Output tensor, element-wise difference of `x1` and `x2`.
    """
    if any_symbolic_tensors((x1, x2)):
        return Subtract().symbolic_call(x1, x2)
    return backend.numpy.subtract(x1, x2)

class Multiply(Operation):
    def call(self, x1, x2):
        return backend.numpy.multiply(x1, x2)

    def compute_output_spec(self, x1, x2):
        x1_shape = getattr(x1, "shape", [])
        x2_shape = getattr(x2, "shape", [])
        output_shape = broadcast_shapes(x1_shape, x2_shape)
        x1_sparse = getattr(x1, "sparse", True)
        x2_sparse = getattr(x2, "sparse", True)
        output_sparse = x1_sparse or x2_sparse
        dtype = dtypes.result_type(
            getattr(x1, "dtype", type(x1)),
            getattr(x2, "dtype", type(x2)),
        )
        return KerasTensor(output_shape, dtype=dtype, sparse=output_sparse)

@keras_export(["keras.ops.multiply", "keras.ops.numpy.multiply"])
def multiply(x1, x2):
    """Multiply arguments element-wise.

    Args:
        x1: First input tensor.
        x2: Second input tensor.

    Returns:
        Output tensor, element-wise product of `x1` and `x2`.
    """
    if any_symbolic_tensors((x1, x2)):
        return Multiply().symbolic_call(x1, x2)
    return backend.numpy.multiply(x1, x2)

class Divide(Operation):
    def call(self, x1, x2):
        return backend.numpy.divide(x1, x2)

    def compute_output_spec(self, x1, x2):
        x1_shape = getattr(x1, "shape", [])
        x2_shape = getattr(x2, "shape", [])
        output_shape = broadcast_shapes(x1_shape, x2_shape)
        output_dtype = dtypes.result_type(
            getattr(x1, "dtype", type(x1)),
            getattr(x2, "dtype", type(x2)),
            float,
        )
        x1_sparse = getattr(x1, "sparse", False)
        x2_sparse = getattr(x2, "sparse", False)
        output_sparse = x1_sparse and not x2_sparse
        return KerasTensor(
            output_shape, dtype=output_dtype, sparse=output_sparse
        )

@keras_export(["keras.ops.divide", "keras.ops.numpy.divide"])
def divide(x1, x2):
    """Divide arguments element-wise.

    `keras.ops.true_divide` is an alias for this function.

    Args:
        x1: First input tensor.
        x2: Second input tensor.

    Returns:
        Output tensor, the quotient `x1/x2`, element-wise.
    """
    if any_symbolic_tensors((x1, x2)):
        return Divide().symbolic_call(x1, x2)
    return backend.numpy.divide(x1, x2)

class DivideNoNan(Operation):
    def call(self, x1, x2):
        return backend.numpy.divide_no_nan(x1, x2)

    def compute_output_spec(self, x1, x2):
        x1_shape = getattr(x1, "shape", [])
        x2_shape = getattr(x2, "shape", [])
        output_shape = broadcast_shapes(x1_shape, x2_shape)
        output_dtype = dtypes.result_type(
            getattr(x1, "dtype", type(x1)),
            getattr(x2, "dtype", type(x2)),
            float,
        )
        x1_sparse = getattr(x1, "sparse", False)
        x2_sparse = getattr(x2, "sparse", False)
        output_sparse = x1_sparse and not x2_sparse
        return KerasTensor(
            output_shape, dtype=output_dtype, sparse=output_sparse
        )

@keras_export(["keras.ops.divide_no_nan", "keras.ops.numpy.divide_no_nan"])
def divide_no_nan(x1, x2):
    """Safe element-wise division which returns 0 where the denominator is 0.

    Args:
        x1: First input tensor.
        x2: Second input tensor.

    Returns:
        The quotient `x1/x2`, element-wise, with zero where x2 is zero.
    """
    if any_symbolic_tensors((x1, x2)):
        return DivideNoNan().symbolic_call(x1, x2)
    return backend.numpy.divide_no_nan(x1, x2)

class TrueDivide(Operation):
    def call(self, x1, x2):
        return backend.numpy.true_divide(x1, x2)

    def compute_output_spec(self, x1, x2):
        x1_shape = getattr(x1, "shape", [])
        x2_shape = getattr(x2, "shape", [])
        output_shape = broadcast_shapes(x1_shape, x2_shape)
        output_dtype = dtypes.result_type(
            getattr(x1, "dtype", type(x1)),
            getattr(x2, "dtype", type(x2)),
            float,
        )
        x1_sparse = getattr(x1, "sparse", False)
        x2_sparse = getattr(x2, "sparse", False)
        output_sparse = x1_sparse and not x2_sparse
        return KerasTensor(
            output_shape, dtype=output_dtype, sparse=output_sparse
        )

@keras_export(
    [
        "keras.ops.true_divide",
        "keras.ops.numpy.true_divide",
    ]
)
def true_divide(x1, x2):
    """Alias for `keras.ops.divide`."""
    if any_symbolic_tensors((x1, x2)):
        return TrueDivide().symbolic_call(x1, x2)
    return backend.numpy.true_divide(x1, x2)

class Power(Operation):
    def call(self, x1, x2):
        return backend.numpy.power(x1, x2)

    def compute_output_spec(self, x1, x2):
        x1_shape = getattr(x1, "shape", [])
        x2_shape = getattr(x2, "shape", [])
        output_shape = broadcast_shapes(x1_shape, x2_shape)
        output_dtype = dtypes.result_type(
            getattr(x1, "dtype", type(x1)), getattr(x2, "dtype", type(x2))
        )
        return KerasTensor(output_shape, dtype=output_dtype)

@keras_export(["keras.ops.power", "keras.ops.numpy.power"])
def power(x1, x2):
    """First tensor elements raised to powers from second tensor, element-wise.

    Args:
        x1: The bases.
        x2: The exponents.

    Returns:
        Output tensor, the bases in `x1` raised to the exponents in `x2`.
    """
    if any_symbolic_tensors((x1, x2)):
        return Power().symbolic_call(x1, x2)
    return backend.numpy.power(x1, x2)

class Negative(Operation):
    def call(self, x):
        return backend.numpy.negative(x)

    def compute_output_spec(self, x):
        sparse = getattr(x, "sparse", False)
        return KerasTensor(x.shape, dtype=x.dtype, sparse=sparse)

@keras_export(["keras.ops.negative", "keras.ops.numpy.negative"])
def negative(x):
    """Numerical negative, element-wise.

    Args:
        x: Input tensor.

    Returns:
        Output tensor, `y = -x`.
    """
    if any_symbolic_tensors((x,)):
        return Negative().symbolic_call(x)
    return backend.numpy.negative(x)

class Square(Operation):
    def call(self, x):
        return backend.numpy.square(x)

    def compute_output_spec(self, x):
        sparse = getattr(x, "sparse", False)
        dtype = backend.standardize_dtype(x.dtype)
        if dtype == "bool":
            dtype = "int32"
        return KerasTensor(x.shape, dtype=dtype, sparse=sparse)

@keras_export(["keras.ops.square", "keras.ops.numpy.square"])
def square(x):
    """Return the element-wise square of the input.

    Args:
        x: Input tensor.

    Returns:
        Output tensor, the square of `x`.
    """
    if any_symbolic_tensors((x,)):
        return Square().symbolic_call(x)
    return backend.numpy.square(x)

class Sqrt(Operation):
    def call(self, x):
        x = backend.convert_to_tensor(x)
        return backend.numpy.sqrt(x)

    def compute_output_spec(self, x):
        dtype = (
            backend.floatx()
            if backend.standardize_dtype(x.dtype) == "int64"
            else dtypes.result_type(x.dtype, float)
        )
        sparse = getattr(x, "sparse", False)
        return KerasTensor(x.shape, dtype=dtype, sparse=sparse)

@keras_export(["keras.ops.sqrt", "keras.ops.numpy.sqrt"])
def sqrt(x):
    """Return the non-negative square root of a tensor, element-wise.

    Args:
        x: Input tensor.

    Returns:
        Output tensor, the non-negative square root of `x`.
    """
    if any_symbolic_tensors((x,)):
        return Sqrt().symbolic_call(x)
    x = backend.convert_to_tensor(x)
    return backend.numpy.sqrt(x)

class Squeeze(Operation):
    def __init__(self, axis=None):
        super().__init__()
        self.axis = axis

    def call(self, x):
        return backend.numpy.squeeze(x, axis=self.axis)

    def compute_output_spec(self, x):
        input_shape = list(x.shape)
        sparse = getattr(x, "sparse", False)
        axis = to_tuple_or_list(self.axis)
        if axis is None:
            output_shape = list(filter((1).__ne__, input_shape))
            return KerasTensor(output_shape, dtype=x.dtype, sparse=sparse)
        else:
            for a in axis:
                if input_shape[a] != 1:
                    raise ValueError(
                        f"Cannot squeeze axis {a}, because the dimension "
                        "is not 1."
                    )
            axis = [canonicalize_axis(a, len(input_shape)) for a in axis]
            for a in sorted(axis, reverse=True):
                del input_shape[a]
            return KerasTensor(input_shape, dtype=x.dtype, sparse=sparse)

@keras_export(["keras.ops.squeeze", "keras.ops.numpy.squeeze"])
def squeeze(x, axis=None):
    """Remove axes of length one from `x`.

    Args:
        x: Input tensor.
        axis: Select a subset of the entries of length one in the shape.

    Returns:
        The input tensor with all or a subset of the dimensions of
        length 1 removed.
    """
    if any_symbolic_tensors((x,)):
        return Squeeze(axis=axis).symbolic_call(x)
    return backend.numpy.squeeze(x, axis=axis)

class Transpose(Operation):
    def __init__(self, axes=None):
        super().__init__()
        self.axes = axes

    def call(self, x):
        return backend.numpy.transpose(x, axes=self.axes)

    def compute_output_spec(self, x):
        output_shape = operation_utils.compute_transpose_output_shape(
            x.shape, self.axes
        )
        sparse = getattr(x, "sparse", False)
        return KerasTensor(output_shape, dtype=x.dtype, sparse=sparse)

@keras_export(["keras.ops.transpose", "keras.ops.numpy.transpose"])
def transpose(x, axes=None):
    """Returns a tensor with `axes` transposed.

    Args:
        x: Input tensor.
        axes: Sequence of integers. Permutation of the dimensions of `x`.
            By default, the order of the axes are reversed.

    Returns:
        `x` with its axes permuted.
    """
    if any_symbolic_tensors((x,)):
        return Transpose(axes=axes).symbolic_call(x)
    return backend.numpy.transpose(x, axes=axes)

class Mean(Operation):
    def __init__(self, axis=None, keepdims=False):
        super().__init__()
        if isinstance(axis, int):
            axis = [axis]
        self.axis = axis
        self.keepdims = keepdims

    def call(self, x):
        return backend.numpy.mean(x, axis=self.axis, keepdims=self.keepdims)

    def compute_output_spec(self, x):
        ori_dtype = backend.standardize_dtype(x.dtype)
        compute_dtype = dtypes.result_type(x.dtype, "float32")
        if "int" in ori_dtype or ori_dtype == "bool":
            result_dtype = compute_dtype
        else:
            result_dtype = ori_dtype
        sparse = getattr(x, "sparse", False)
        return KerasTensor(
            reduce_shape(x.shape, axis=self.axis, keepdims=self.keepdims),
            dtype=result_dtype,
            sparse=sparse,
        )

@keras_export(["keras.ops.mean", "keras.ops.numpy.mean"])
def mean(x, axis=None, keepdims=False):
    """Compute the arithmetic mean along the specified axes.

    Args:
        x: Input tensor.
        axis: Axis or axes along which the means are computed. The default
            is to compute the mean of the flattened tensor.
        keepdims: If this is set to `True`, the axes which are reduced are left
            in the result as dimensions with size one.

    Returns:
        Output tensor containing the mean values.
    """
    if any_symbolic_tensors((x,)):
        return Mean(axis=axis, keepdims=keepdims).symbolic_call(x)
    return backend.numpy.mean(x, axis=axis, keepdims=keepdims)

class Var(Operation):
    def __init__(self, axis=None, keepdims=False):
        super().__init__()
        if isinstance(axis, int):
            axis = [axis]
        self.axis = axis
        self.keepdims = keepdims

    def call(self, x):
        return backend.numpy.var(x, axis=self.axis, keepdims=self.keepdims)

    def compute_output_spec(self, x):
        output_dtype = backend.result_type(getattr(x, "dtype", type(x)), float)
        return KerasTensor(
            reduce_shape(x.shape, axis=self.axis, keepdims=self.keepdims),
            dtype=output_dtype,
        )

@keras_export(["keras.ops.var", "keras.ops.numpy.var"])
def var(x, axis=None, keepdims=False):
    """Compute the variance along the specified axes.

    Args:
        x: Input tensor.
        axis: Axis or axes along which the variance is computed. The default
            is to compute the variance of the flattened tensor.
        keepdims: If this is set to `True`, the axes which are reduced are left
            in the result as dimensions with size one.

    Returns:
        Output tensor containing the variance.
    """
    if any_symbolic_tensors((x,)):
        return Var(axis=axis, keepdims=keepdims).symbolic_call(x)
    return backend.numpy.var(x, axis=axis, keepdims=keepdims)

class Sum(Operation):
    def __init__(self, axis=None, keepdims=False):
        super().__init__()
        if isinstance(axis, int):
            axis = [axis]
        self.axis = axis
        self.keepdims = keepdims

    def call(self, x):
        return backend.numpy.sum(x, axis=self.axis, keepdims=self.keepdims)

    def compute_output_spec(self, x):
        dtype = dtypes.result_type(getattr(x, "dtype", backend.floatx()))
        # follow jax's rule
        if dtype in ("bool", "int8", "int16"):
            dtype = "int32"
        elif dtype in ("uint8", "uint16"):
            dtype = "uint32"
        # TODO: torch doesn't support uint32
        if backend.backend() == "torch" and dtype == "uint32":
            dtype = "int32"
        sparse = getattr(x, "sparse", False)
        return KerasTensor(
            reduce_shape(x.shape, axis=self.axis, keepdims=self.keepdims),
            dtype=dtype,
            sparse=sparse,
        )

@keras_export(["keras.ops.sum", "keras.ops.numpy.sum"])
def sum(x, axis=None, keepdims=False):
    """Sum of a tensor over the given axes.

    Args:
        x: Input tensor.
        axis: Axis or axes along which the sum is computed. The default is to
            compute the sum of the flattened tensor.
        keepdims: If this is set to `True`, the axes which are reduced are left
            in the result as dimensions with size one.

    Returns:
        Output tensor containing the sum.
    """
    if any_symbolic_tensors((x,)):
        return Sum(axis=axis, keepdims=keepdims).symbolic_call(x)
    return backend.numpy.sum(x, axis=axis, keepdims=keepdims)

class Zeros(Operation):
    def call(self, shape, dtype=None):
        return backend.numpy.zeros(shape, dtype=dtype)

    def compute_output_spec(self, shape, dtype=None):
        dtype = dtype or backend.floatx()
        return KerasTensor(shape, dtype=dtype)

@keras_export(["keras.ops.zeros", "keras.ops.numpy.zeros"])
def zeros(shape, dtype=None):
    """Return a new tensor of given shape and type, filled with zeros.

    Args:
        shape: Shape of the new tensor.
        dtype: Desired data type of the tensor.

    Returns:
        Tensor of zeros with the given shape and dtype.
    """
    return backend.numpy.zeros(shape, dtype=dtype)

class Ones(Operation):
    def call(self, shape, dtype=None):
        return backend.numpy.ones(shape, dtype=dtype)

    def compute_output_spec(self, shape, dtype=None):
        dtype = dtype or backend.floatx()
        return KerasTensor(shape, dtype=dtype)

@keras_export(["keras.ops.ones", "keras.ops.numpy.ones"])
def ones(shape, dtype=None):
    """Return a new tensor of given shape and type, filled with ones.

    Args:
        shape: Shape of the new tensor.
        dtype: Desired data type of the tensor.

    Returns:
        Tensor of ones with the given shape and dtype.
    """
    return backend.numpy.ones(shape, dtype=dtype)

class Eye(Operation):
    def __init__(self, k=0, dtype=None):
        super().__init__()
        self.k = k
        self.dtype = dtype or backend.floatx()

    def call(self, N, M=None):
        return backend.numpy.eye(N, M=M, k=self.k, dtype=self.dtype)

    def compute_output_spec(self, N, M=None):
        if M is None:
            M = N
        return KerasTensor((N, M), dtype=self.dtype)

@keras_export(["keras.ops.eye", "keras.ops.numpy.eye"])
def eye(N, M=None, k=0, dtype=None):
    """Return a 2-D tensor with ones on the diagonal and zeros elsewhere.

    Args:
        N: Number of rows in the output.
        M: Number of columns in the output. If `None`, defaults to `N`.
        k: Index of the diagonal: 0 (the default) refers to the main
            diagonal, a positive value refers to an upper diagonal,
            and a negative value to a lower diagonal.
        dtype: Data type of the returned tensor.

    Returns:
        Tensor with ones on the k-th diagonal and zeros elsewhere.
    """
    return backend.numpy.eye(N, M=M, k=k, dtype=dtype)

class FloorDivide(Operation):
    def call(self, x1, x2):
        return backend.numpy.floor_divide(x1, x2)

    def compute_output_spec(self, x1, x2):
        x1_shape = getattr(x1, "shape", [])
        x2_shape = getattr(x2, "shape", [])
        output_shape = broadcast_shapes(x1_shape, x2_shape)
        output_dtype = dtypes.result_type(
            getattr(x1, "dtype", type(x1)),
            getattr(x2, "dtype", type(x2)),
        )
        return KerasTensor(output_shape, dtype=output_dtype)

@keras_export(["keras.ops.floor_divide", "keras.ops.numpy.floor_divide"])
def floor_divide(x1, x2):
    """Returns the largest integer smaller or equal to the division of inputs.

    Args:
        x1: Numerator.
        x2: Denominator.

    Returns:
        Output tensor, `y = floor(x1/x2)`
    """
    if any_symbolic_tensors((x1, x2)):
        return FloorDivide().symbolic_call(x1, x2)
    return backend.numpy.floor_divide(x1, x2)

class LogicalXor(Operation):
    def call(self, x1, x2):
        return backend.numpy.logical_xor(x1, x2)

    def compute_output_spec(self, x1, x2):
        x1_shape = getattr(x1, "shape", [])
        x2_shape = getattr(x2, "shape", [])
        output_shape = broadcast_shapes(x1_shape, x2_shape)
        return KerasTensor(output_shape, dtype="bool")

@keras_export(["keras.ops.logical_xor", "keras.ops.numpy.logical_xor"])
def logical_xor(x1, x2):
    """Compute the truth value of `x1 XOR x2`, element-wise.

    Args:
        x1: First input tensor.
        x2: Second input tensor.

    Returns:
        Output boolean tensor.
    """
    if any_symbolic_tensors((x1, x2)):
        return LogicalXor().symbolic_call(x1, x2)
    return backend.numpy.logical_xor(x1, x2)

class Correlate(Operation):
    def __init__(self, mode="valid"):
        super().__init__()
        self.mode = mode

    def call(self, x1, x2):
        return backend.numpy.correlate(x1, x2, mode=self.mode)

    def compute_output_spec(self, x1, x2):
        x1_shape = getattr(x1, "shape", [])
        x2_shape = getattr(x2, "shape", [])
        if len(x1_shape) != 1:
            raise ValueError(
                "`x1` must be a 1-dimensional tensor, but received"
                + f"shape {x1_shape}"
            )
        if len(x2_shape) != 1:
            raise ValueError(
                "`x2` must be a 1-dimensional tensor, but received"
                + f"shape {x2_shape}"
            )
        x1_len, x2_len = x1_shape[0], x2_shape[0]
        output_shape = (
            np.maximum(x1_len, x2_len) - np.minimum(x1_len, x2_len) + 1,
        )
        if self.mode == "same":
            output_shape = (np.maximum(x1_len, x2_len),)
        elif self.mode == "full":
            output_shape = (x1_len + x2_len - 1,)
        if self.mode not in ("valid", "same", "full"):
            raise ValueError(
                "`mode` must be either `valid`, `same`, or `full`, but"
                f"received: {self.mode}"
            )
        output_dtype = dtypes.result_type(
            getattr(x1, "dtype", type(x1)),
            getattr(x2, "dtype", type(x2)),
        )
        if output_dtype == "int64":
            output_dtype = "float64"
        elif output_dtype not in ["bfloat16", "float16", "float64"]:
            output_dtype = "float32"
        return KerasTensor(output_shape, dtype=output_dtype)

@keras_export(["keras.ops.correlate", "keras.ops.numpy.correlate"])
def correlate(x1, x2, mode="valid"):
    """Compute the cross-correlation of two 1-dimensional tensors.

    Args:
        x1: First 1-dimensional input tensor of length M.
        x2: Second 1-dimensional input tensor of length N.
        mode: Either `valid`, `same` or `full`.
            By default the mode is set to `valid`, which returns
            an output of length max(M, N) - min(M, N) + 1.
            `same` returns an output of length max(M, N).
            `full` mode returns the convolution at each point of
            overlap, with an output length of N+M-1

    Returns:
        Output tensor, cross-correlation of `x1` and `x2`.
    """
    if any_symbolic_tensors((x1, x2)):
        return Correlate(mode=mode).symbolic_call(x1, x2)
    return backend.numpy.correlate(x1, x2, mode=mode)

class Select(Operation):
    def __init__(self):
        super().__init__()

    def call(self, condlist, choicelist, default=0):
        return backend.numpy.select(condlist, choicelist, default)

    def compute_output_spec(self, condlist, choicelist, default=0):
        first_element = choicelist[0]
        return KerasTensor(first_element.shape, dtype=first_element.dtype)

@keras_export(["keras.ops.select", "keras.ops.numpy.select"])
def select(condlist, choicelist, default=0):
    """Return elements from `choicelist`, based on conditions in `condlist`.

    Args:
        condlist: List of boolean tensors.
            The list of conditions which determine from which array
            in choicelist the output elements are taken.
            When multiple conditions are satisfied,
            the first one encountered in condlist is used.
        choicelist: List of tensors.
            The list of tensors from which the output elements are taken.
            This list has to be of the same length as `condlist`.
        defaults: Optional scalar value.
            The element inserted in the output
            when all conditions evaluate to `False`.

    Returns:
        Tensor where the output at position `m` is the `m`-th element
        of the tensor in `choicelist` where the `m`-th element of the
        corresponding tensor in `condlist` is `True`.

    Example:

    ```python
    from keras import ops

    x = ops.arange(6)
    condlist = [x3]
    choicelist = [x, x**2]
    ops.select(condlist, choicelist, 42)
    # Returns: tensor([0,  1,  2, 42, 16, 25])
    ```
    """
    if not isinstance(condlist, (list, tuple)) or not isinstance(
        choicelist, (list, tuple)
    ):
        raise ValueError(
            "condlist and choicelist must be lists. Received: "
            f"type(condlist) = {type(condlist)}, "
            f"type(choicelist) = {type(choicelist)}"
        )
    condlist = list(condlist)
    choicelist = list(choicelist)
    if not condlist or not choicelist:
        raise ValueError(
            "condlist and choicelist must not be empty. Received: "
            f"condlist = {condlist}, "
            f"choicelist = {choicelist}"
        )
    if any_symbolic_tensors(condlist + choicelist + [default]):
        return Select().symbolic_call(condlist, choicelist, default)
    return backend.numpy.select(condlist, choicelist, default)

class Slogdet(Operation):
    def __init__(self):
        super().__init__()

    def call(self, x):
        return backend.numpy.slogdet(x)

    def compute_output_spec(self, x):
        sign = KerasTensor((), dtype=x.dtype)
        logabsdet = KerasTensor((), dtype=x.dtype)
        return (sign, logabsdet)

@keras_export(["keras.ops.slogdet", "keras.ops.numpy.slogdet"])
def slogdet(x):
    """Compute the sign and natural logarithm of the determinant of a matrix.

    Args:
        x: Input matrix. It must 2D and square.

    Returns:
        A tuple `(sign, logabsdet)`. `sign` is a number representing
        the sign of the determinant. For a real matrix, this is 1, 0, or -1.
        For a complex matrix, this is a complex number with absolute value 1
        (i.e., it is on the unit circle), or else 0.
        `logabsdet` is the natural log of the absolute value of the determinant.
    """
    if any_symbolic_tensors((x,)):
        return Slogdet().symbolic_call(x)
    return backend.numpy.slogdet(x)

class Argpartition(Operation):
    def __init__(self, kth, axis=-1):
        super().__init__()
        if not isinstance(kth, int):
            raise ValueError("kth must be an integer. Received:" f"kth = {kth}")
        self.kth = kth
        self.axis = axis

    def call(self, x):
        return backend.numpy.argpartition(x, kth=self.kth, axis=self.axis)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype="int32")

@keras_export(["keras.ops.argpartition", "keras.ops.numpy.argpartition"])
def argpartition(x, kth, axis=-1):
    """Performs an indirect partition along the given axis.

    It returns an array
    of indices of the same shape as `x` that index data along the given axis
    in partitioned order.

    Args:
        a: Array to sort.
        kth: Element index to partition by.
            The k-th element will be in its final sorted position and all
            smaller elements will be moved before it and all larger elements
            behind it. The order of all elements in the partitions is undefined.
            If provided with a sequence of k-th it will partition all of them
            into their sorted position at once.
        axis: Axis along which to sort. The default is -1 (the last axis).
            If `None`, the flattened array is used.

    Returns:
        Array of indices that partition `x` along the specified `axis`.
    """
    if any_symbolic_tensors((x,)):
        return Argpartition(kth, axis).symbolic_call(x)
    return backend.numpy.argpartition(x, kth, axis)

```

5. **Tool call: find_files**
Input:
```json
{
  "globPatterns": [
    "**/ops/*[nN][uU][mM][pP][yY]*[tT][eE][sS][tT].py"
  ],
  "toolPurpose": "- I want to locate the existing NumPy ops test file to understand the expected repeat contracts and run the smallest relevant baseline checks without modifying tests."
}
```
Output:
```
Below are the 3 files found for the specified glob patterns (**/ops/*[nN][uU][mM][pP][yY]*[tT][eE][sS][tT].py):

keras-team__keras-19826/keras/src/ops/numpy_test.py
keras-team__keras-19201/keras/ops/numpy_test.py
keras-team__keras-19775/keras/src/ops/numpy_test.py

```

6. **Tool call: grep**
Input:
```json
{
  "pattern": "test_repeat|Repeat\\(",
  "searchPath": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826/keras/src/ops/numpy_test.py",
  "outputMode": "matches",
  "context": 10,
  "headLimit": 50,
  "toolPurpose": "- I need to inspect existing repeat tests and shape expectations in the repository so the production fix matches the established operation contract."
}
```
Output:
```
{"success":false,"error":"Search failed","details":"spawn ENOTDIR","code":"ENOTDIR","context":"Error occurred while searching: /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826/keras/src/ops/numpy_test.py"}
```

7. **Tool call: read_file**
Input:
```json
{
  "fileNames": [
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826/keras/src/ops/numpy_test.py",
      "startLine": 1
    }
  ],
  "toolPurpose": "- I want to read the existing NumPy operation tests to find repeat-specific test cases and confirm current symbolic shape conventions before changing production code."
}
```
Output:
```

File successfully read, file name numpy_test.py with file path: enc_file_sovfhn/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826/keras/src/ops/numpy_test.py

**File Read Information:**
- Lines read: 1 to 3000 (3000 lines)
- Total lines in file: 7982
- Remaining lines: 4982

**IMPORTANT:**
 - In case the required context is not found in below content, then only read next set of lines using startLine: 3001

Content:
import contextlib
import functools
import itertools
import math
import warnings

import numpy as np
import pytest
from absl.testing import parameterized

import keras
from keras.src import backend
from keras.src import testing
from keras.src.backend.common import dtypes
from keras.src.backend.common import standardize_dtype
from keras.src.backend.common.keras_tensor import KerasTensor
from keras.src.ops import numpy as knp
from keras.src.testing.test_utils import named_product

class NumpyTwoInputOpsDynamicShapeTest(testing.TestCase):
    def test_add(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.add(x, y).shape, (2, 3))

    def test_subtract(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.subtract(x, y).shape, (2, 3))

    def test_multiply(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.multiply(x, y).shape, (2, 3))

    def test_matmul(self):
        x = KerasTensor((None, 3, 4))
        y = KerasTensor((3, None, 4, 5))
        self.assertEqual(knp.matmul(x, y).shape, (3, None, 3, 5))

    def test_power(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.power(x, y).shape, (2, 3))

    def test_divide(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.divide(x, y).shape, (2, 3))

    def test_divide_no_nan(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.divide_no_nan(x, y).shape, (2, 3))

    def test_true_divide(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.true_divide(x, y).shape, (2, 3))

    def test_append(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.append(x, y).shape, (None,))

    def test_arctan2(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.arctan2(x, y).shape, (2, 3))

    def test_cross(self):
        x1 = KerasTensor((2, 3, 3))
        x2 = KerasTensor((1, 3, 2))
        y = KerasTensor((None, 1, 2))
        self.assertEqual(knp.cross(x1, y).shape, (2, 3, 3))
        self.assertEqual(knp.cross(x2, y).shape, (None, 3))

    def test_einsum(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((3, 4))
        self.assertEqual(knp.einsum("ij,jk->ik", x, y).shape, (None, 4))
        self.assertEqual(knp.einsum("ij,jk->ikj", x, y).shape, (None, 4, 3))
        self.assertEqual(knp.einsum("ii", x).shape, ())
        self.assertEqual(knp.einsum(",ij", 5, x).shape, (None, 3))

        x = KerasTensor((None, 3, 4))
        y = KerasTensor((None, 4, 5))
        z = KerasTensor((1, 1, 1, 9))
        self.assertEqual(knp.einsum("ijk,jkl->li", x, y).shape, (5, None))
        self.assertEqual(knp.einsum("ijk,jkl->lij", x, y).shape, (5, None, 3))
        self.assertEqual(
            knp.einsum("...,...j->...j", x, y).shape, (None, 3, 4, 5)
        )
        self.assertEqual(
            knp.einsum("i...,...j->i...j", x, y).shape, (None, 3, 4, 5)
        )
        self.assertEqual(knp.einsum("i...,...j", x, y).shape, (3, 4, None, 5))
        self.assertEqual(
            knp.einsum("i...,...j,...k", x, y, z).shape, (1, 3, 4, None, 5, 9)
        )
        self.assertEqual(
            knp.einsum("mij,ijk,...", x, y, z).shape, (1, 1, 1, 9, 5, None)
        )

        with self.assertRaises(ValueError):
            x = KerasTensor((None, 3))
            y = KerasTensor((3, 4))
            knp.einsum("ijk,jk->ik", x, y)

    def test_full_like(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.full_like(x, KerasTensor((1, 3))).shape, (None, 3))

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.full_like(x, 2).shape, (None, 3, 3))

    def test_greater(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.greater(x, y).shape, (2, 3))

    def test_greater_equal(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.greater_equal(x, y).shape, (2, 3))

    def test_isclose(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.isclose(x, y).shape, (2, 3))

    def test_less(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.less(x, y).shape, (2, 3))

    def test_less_equal(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.less_equal(x, y).shape, (2, 3))

    def test_linspace(self):
        start = KerasTensor((None, 3, 4))
        stop = KerasTensor((2, 3, 4))
        self.assertEqual(
            knp.linspace(start, stop, 10, axis=1).shape, (2, 10, 3, 4)
        )

        start = KerasTensor((None, 3))
        stop = 2
        self.assertEqual(
            knp.linspace(start, stop, 10, axis=1).shape, (None, 10, 3)
        )

    def test_logical_and(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.logical_and(x, y).shape, (2, 3))

    def test_logical_or(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.logical_or(x, y).shape, (2, 3))

    def test_logspace(self):
        start = KerasTensor((None, 3, 4))
        stop = KerasTensor((2, 3, 4))
        self.assertEqual(
            knp.logspace(start, stop, 10, axis=1).shape, (2, 10, 3, 4)
        )

        start = KerasTensor((None, 3))
        stop = 2
        self.assertEqual(
            knp.logspace(start, stop, 10, axis=1).shape, (None, 10, 3)
        )

    def test_maximum(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.maximum(x, y).shape, (2, 3))

    def test_minimum(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.minimum(x, y).shape, (2, 3))

    def test_mod(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.mod(x, y).shape, (2, 3))

    def test_not_equal(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.not_equal(x, y).shape, (2, 3))

    def test_outer(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.outer(x, y).shape, (None, None))

    def test_quantile(self):
        x = KerasTensor((None, 3))

        # q as scalar
        q = KerasTensor(())
        self.assertEqual(knp.quantile(x, q).shape, ())

        # q as 1D tensor
        q = KerasTensor((2,))
        self.assertEqual(knp.quantile(x, q).shape, (2,))
        self.assertEqual(knp.quantile(x, q, axis=1).shape, (2, None))
        self.assertEqual(
            knp.quantile(x, q, axis=1, keepdims=True).shape,
            (2, None, 1),
        )

    def test_take(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.take(x, 1).shape, ())
        self.assertEqual(knp.take(x, [1, 2]).shape, (2,))
        self.assertEqual(
            knp.take(x, [[1, 2], [1, 2]], axis=1).shape, (None, 2, 2)
        )

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.take(x, 1, axis=1).shape, (None, 3))
        self.assertEqual(knp.take(x, [1, 2]).shape, (2,))
        self.assertEqual(
            knp.take(x, [[1, 2], [1, 2]], axis=1).shape, (None, 2, 2, 3)
        )

        # test with negative axis
        self.assertEqual(knp.take(x, 1, axis=-2).shape, (None, 3))

        # test with multi-dimensional indices
        x = KerasTensor((None, 3, None, 5))
        indices = KerasTensor((6, 7))
        self.assertEqual(knp.take(x, indices, axis=2).shape, (None, 3, 6, 7, 5))

    def test_take_along_axis(self):
        x = KerasTensor((None, 3))
        indices = KerasTensor((1, 3))
        self.assertEqual(knp.take_along_axis(x, indices, axis=0).shape, (1, 3))
        self.assertEqual(
            knp.take_along_axis(x, indices, axis=1).shape, (None, 3)
        )

        x = KerasTensor((None, 3, 3))
        indices = KerasTensor((1, 3, None))
        self.assertEqual(
            knp.take_along_axis(x, indices, axis=1).shape, (None, 3, 3)
        )

    def test_tensordot(self):
        x = KerasTensor((None, 3, 4))
        y = KerasTensor((3, 4))
        self.assertEqual(knp.tensordot(x, y, axes=1).shape, (None, 3, 4))
        self.assertEqual(knp.tensordot(x, y, axes=[[0, 1], [1, 0]]).shape, (4,))

    def test_vdot(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((None, 3))
        self.assertEqual(knp.vdot(x, y).shape, ())

        x = KerasTensor((None, 3, 3))
        y = KerasTensor((None, 3, 3))
        self.assertEqual(knp.vdot(x, y).shape, ())

    def test_where(self):
        condition = KerasTensor((2, None, 1))
        x = KerasTensor((None, 1))
        y = KerasTensor((None, 3))
        self.assertEqual(knp.where(condition, x, y).shape, (2, None, 3))
        self.assertEqual(knp.where(condition).shape, (2, None, 1))

    def test_floor_divide(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.floor_divide(x, y).shape, (2, 3))

    def test_xor(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.logical_xor(x, y).shape, (2, 3))

    def test_shape_equal_basic_equality(self):
        x = KerasTensor((3, 4)).shape
        y = KerasTensor((3, 4)).shape
        self.assertTrue(knp.shape_equal(x, y))
        y = KerasTensor((3, 5)).shape
        self.assertFalse(knp.shape_equal(x, y))

    def test_shape_equal_allow_none(self):
        x = KerasTensor((3, 4, None)).shape
        y = KerasTensor((3, 4, 5)).shape
        self.assertTrue(knp.shape_equal(x, y, allow_none=True))
        self.assertFalse(knp.shape_equal(x, y, allow_none=False))

    def test_shape_equal_different_shape_lengths(self):
        x = KerasTensor((3, 4)).shape
        y = KerasTensor((3, 4, 5)).shape
        self.assertFalse(knp.shape_equal(x, y))

    def test_shape_equal_ignore_axes(self):
        x = KerasTensor((3, 4, 5)).shape
        y = KerasTensor((3, 6, 5)).shape
        self.assertTrue(knp.shape_equal(x, y, axis=1))
        y = KerasTensor((3, 6, 7)).shape
        self.assertTrue(knp.shape_equal(x, y, axis=(1, 2)))
        self.assertFalse(knp.shape_equal(x, y, axis=1))

    def test_shape_equal_only_none(self):
        x = KerasTensor((None, None)).shape
        y = KerasTensor((5, 6)).shape
        self.assertTrue(knp.shape_equal(x, y, allow_none=True))

    def test_shape_equal_axis_as_list(self):
        x = KerasTensor((3, 4, 5)).shape
        y = KerasTensor((3, 6, 5)).shape
        self.assertTrue(knp.shape_equal(x, y, axis=[1]))

    def test_shape_non_equal_with_negative_axis(self):
        x = KerasTensor((3, 4, 5)).shape
        y = KerasTensor((3, 4, 6)).shape
        self.assertFalse(knp.shape_equal(x, y, axis=-2))

    def test_shape_equal_with_negative_axis(self):
        x = KerasTensor((3, 4, 5)).shape
        y = KerasTensor((3, 4, 5)).shape
        self.assertTrue(knp.shape_equal(x, y, axis=-1))

    def test_shape_equal_zeros(self):
        x = KerasTensor((0, 4)).shape
        y = KerasTensor((0, 4)).shape
        self.assertTrue(knp.shape_equal(x, y))
        y = KerasTensor((0, 5)).shape
        self.assertFalse(knp.shape_equal(x, y))

    def test_broadcast_shapes_conversion_to_list(self):
        shape1 = KerasTensor((1, 2)).shape
        shape2 = KerasTensor((3, 1)).shape
        expected_output = [3, 2]
        self.assertEqual(knp.broadcast_shapes(shape1, shape2), expected_output)

    def test_broadcast_shapes_shape1_longer_than_shape2(self):
        shape1 = KerasTensor((5, 3, 2)).shape
        shape2 = KerasTensor((1, 3)).shape
        with self.assertRaisesRegex(ValueError, "Cannot broadcast shape"):
            knp.broadcast_shapes(shape1, shape2)

    def test_broadcast_shapes_shape2_longer_than_shape1(self):
        shape1 = KerasTensor((5, 3)).shape
        shape2 = KerasTensor((2, 5, 3)).shape
        expected_output = [2, 5, 3]
        self.assertEqual(knp.broadcast_shapes(shape1, shape2), expected_output)

    def test_broadcast_shapes_broadcasting_shape1_is_1(self):
        shape1 = KerasTensor((1, 3)).shape
        shape2 = KerasTensor((5, 1)).shape
        expected_output = [5, 3]
        self.assertEqual(knp.broadcast_shapes(shape1, shape2), expected_output)

    def test_broadcast_shapes_broadcasting_shape1_is_none(self):
        shape1 = KerasTensor((None, 3)).shape
        shape2 = KerasTensor((5, 1)).shape
        expected_output = [5, 3]
        self.assertEqual(knp.broadcast_shapes(shape1, shape2), expected_output)

        shape1 = KerasTensor((None, 3)).shape
        shape2 = KerasTensor((5, 3)).shape
        expected_output = [5, 3]
        self.assertEqual(knp.broadcast_shapes(shape1, shape2), expected_output)

    def test_broadcast_shapes_broadcasting_shape2_conditions(self):
        shape1 = KerasTensor((5, 3, 2)).shape
        shape2 = KerasTensor((1, 3, 2)).shape
        expected_output = [5, 3, 2]
        self.assertEqual(knp.broadcast_shapes(shape1, shape2), expected_output)

        shape1 = KerasTensor((5, 3, 2)).shape
        shape2 = KerasTensor((1, None, 2)).shape
        expected_output = [5, 3, 2]
        self.assertEqual(knp.broadcast_shapes(shape1, shape2), expected_output)

class NumpyTwoInputOpsStaticShapeTest(testing.TestCase):
    def test_add(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.add(x, y).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.add(x, y)

    def test_subtract(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.subtract(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.subtract(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.subtract(x, y)

    def test_multiply(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.multiply(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.multiply(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.multiply(x, y)

    def test_matmul(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((3, 2))
        self.assertEqual(knp.matmul(x, y).shape, (2, 2))

        with self.assertRaises(ValueError):
            x = KerasTensor((3, 4))
            y = KerasTensor((2, 3, 4))
            knp.matmul(x, y)

    def test_matmul_sparse(self):
        x = KerasTensor((2, 3), sparse=True)
        y = KerasTensor((3, 2))
        result = knp.matmul(x, y)
        self.assertEqual(result.shape, (2, 2))

        x = KerasTensor((2, 3))
        y = KerasTensor((3, 2), sparse=True)
        result = knp.matmul(x, y)
        self.assertEqual(result.shape, (2, 2))

        x = KerasTensor((2, 3), sparse=True)
        y = KerasTensor((3, 2), sparse=True)
        result = knp.matmul(x, y)
        self.assertEqual(result.shape, (2, 2))
        self.assertTrue(result.sparse)

    def test_power(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.power(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.power(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.power(x, y)

    def test_divide(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.divide(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.divide(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.divide(x, y)

    def test_divide_no_nan(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.divide_no_nan(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.divide_no_nan(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.divide_no_nan(x, y)

    def test_true_divide(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.true_divide(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.true_divide(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.true_divide(x, y)

    def test_append(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.append(x, y).shape, (12,))

        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.append(x, y, axis=0).shape, (4, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.append(x, y, axis=2)

    def test_arctan2(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.arctan2(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.arctan2(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.arctan2(x, y)

    def test_cross(self):
        x1 = KerasTensor((2, 3, 3))
        x2 = KerasTensor((1, 3, 2))
        y1 = KerasTensor((2, 3, 3))
        y2 = KerasTensor((2, 3, 2))
        self.assertEqual(knp.cross(x1, y1).shape, (2, 3, 3))
        self.assertEqual(knp.cross(x2, y2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.cross(x, y)

        with self.assertRaises(ValueError):
            x = KerasTensor((4, 3, 3))
            y = KerasTensor((2, 3, 3))
            knp.cross(x, y)

    def test_einsum(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((3, 4))
        self.assertEqual(knp.einsum("ij,jk->ik", x, y).shape, (2, 4))
        self.assertEqual(knp.einsum("ij,jk->ikj", x, y).shape, (2, 4, 3))
        self.assertEqual(knp.einsum("ii", x).shape, ())
        self.assertEqual(knp.einsum(",ij", 5, x).shape, (2, 3))

        x = KerasTensor((2, 3, 4))
        y = KerasTensor((3, 4, 5))
        z = KerasTensor((1, 1, 1, 9))
        self.assertEqual(knp.einsum("ijk,jkl->li", x, y).shape, (5, 2))
        self.assertEqual(knp.einsum("ijk,jkl->lij", x, y).shape, (5, 2, 3))
        self.assertEqual(knp.einsum("...,...j->...j", x, y).shape, (2, 3, 4, 5))
        self.assertEqual(
            knp.einsum("i...,...j->i...j", x, y).shape, (2, 3, 4, 5)
        )
        self.assertEqual(knp.einsum("i...,...j", x, y).shape, (3, 4, 2, 5))
        self.assertEqual(knp.einsum("i...,...j", x, y).shape, (3, 4, 2, 5))
        self.assertEqual(
            knp.einsum("i...,...j,...k", x, y, z).shape, (1, 3, 4, 2, 5, 9)
        )
        self.assertEqual(
            knp.einsum("mij,ijk,...", x, y, z).shape, (1, 1, 1, 9, 5, 2)
        )

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((3, 4))
            knp.einsum("ijk,jk->ik", x, y)

    def test_full_like(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.full_like(x, 2).shape, (2, 3))

    def test_greater(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.greater(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.greater(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.greater(x, y)

    def test_greater_equal(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.greater_equal(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.greater_equal(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.greater_equal(x, y)

    def test_isclose(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.isclose(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.isclose(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.isclose(x, y)

    def test_less(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.less(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.less(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.less(x, y)

    def test_less_equal(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.less_equal(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.less_equal(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.less_equal(x, y)

    def test_linspace(self):
        start = KerasTensor((2, 3, 4))
        stop = KerasTensor((2, 3, 4))
        self.assertEqual(knp.linspace(start, stop, 10).shape, (10, 2, 3, 4))

        with self.assertRaises(ValueError):
            start = KerasTensor((2, 3))
            stop = KerasTensor((2, 3, 4))
            knp.linspace(start, stop)

    def test_logical_and(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.logical_and(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.logical_and(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.logical_and(x, y)

    def test_logical_or(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.logical_or(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.logical_or(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.logical_or(x, y)

    def test_logspace(self):
        start = KerasTensor((2, 3, 4))
        stop = KerasTensor((2, 3, 4))
        self.assertEqual(knp.logspace(start, stop, 10).shape, (10, 2, 3, 4))

        with self.assertRaises(ValueError):
            start = KerasTensor((2, 3))
            stop = KerasTensor((2, 3, 4))
            knp.logspace(start, stop)

    def test_maximum(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.maximum(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.maximum(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.maximum(x, y)

    def test_minimum(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.minimum(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.minimum(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.minimum(x, y)

    def test_mod(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.mod(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.mod(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.mod(x, y)

    def test_not_equal(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.not_equal(x, y).shape, (2, 3))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.not_equal(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.not_equal(x, y)

    def test_outer(self):
        x = KerasTensor((3,))
        y = KerasTensor((4,))
        self.assertEqual(knp.outer(x, y).shape, (3, 4))

        x = KerasTensor((2, 3))
        y = KerasTensor((4, 5))
        self.assertEqual(knp.outer(x, y).shape, (6, 20))

        x = KerasTensor((2, 3))
        self.assertEqual(knp.outer(x, 2).shape, (6, 1))

    def test_quantile(self):
        x = KerasTensor((3, 3))

        # q as scalar
        q = KerasTensor(())
        self.assertEqual(knp.quantile(x, q).shape, ())

        # q as 1D tensor
        q = KerasTensor((2,))
        self.assertEqual(knp.quantile(x, q).shape, (2,))
        self.assertEqual(knp.quantile(x, q, axis=1).shape, (2, 3))
        self.assertEqual(
            knp.quantile(x, q, axis=1, keepdims=True).shape,
            (2, 3, 1),
        )

    def test_take(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.take(x, 1).shape, ())
        self.assertEqual(knp.take(x, [1, 2]).shape, (2,))
        self.assertEqual(knp.take(x, [[1, 2], [1, 2]], axis=1).shape, (2, 2, 2))

        # test with multi-dimensional indices
        x = KerasTensor((2, 3, 4, 5))
        indices = KerasTensor((6, 7))
        self.assertEqual(knp.take(x, indices, axis=2).shape, (2, 3, 6, 7, 5))

    def test_take_along_axis(self):
        x = KerasTensor((2, 3))
        indices = KerasTensor((1, 3))
        self.assertEqual(knp.take_along_axis(x, indices, axis=0).shape, (1, 3))
        self.assertEqual(knp.take_along_axis(x, indices, axis=1).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            indices = KerasTensor((1, 4))
            knp.take_along_axis(x, indices, axis=0)

    def test_tensordot(self):
        x = KerasTensor((2, 3, 3))
        y = KerasTensor((3, 3, 4))
        self.assertEqual(knp.tensordot(x, y, axes=1).shape, (2, 3, 3, 4))
        self.assertEqual(knp.tensordot(x, y, axes=2).shape, (2, 4))
        self.assertEqual(
            knp.tensordot(x, y, axes=[[1, 2], [0, 1]]).shape, (2, 4)
        )

    def test_vdot(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.vdot(x, y).shape, ())

    def test_where(self):
        condition = KerasTensor((2, 3))
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.where(condition, x, y).shape, (2, 3))
        self.assertAllEqual(knp.where(condition).shape, (2, 3))

    def test_floor_divide(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.floor_divide(x, y).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.floor_divide(x, y)

    def test_xor(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.logical_xor(x, y).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3, 4))
            knp.logical_xor(x, y)

    def test_digitize(self):
        x = KerasTensor((2, 3))
        bins = KerasTensor((3,))
        self.assertEqual(knp.digitize(x, bins).shape, (2, 3))
        self.assertTrue(knp.digitize(x, bins).dtype == "int32")

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            bins = KerasTensor((2, 3, 4))
            knp.digitize(x, bins)

    def test_correlate_mode_valid(self):
        x = KerasTensor((3,))
        y = KerasTensor((3,))
        self.assertEqual(knp.correlate(x, y).shape, (1,))
        self.assertTrue(knp.correlate(x, y).dtype == "float32")

        with self.assertRaises(ValueError):
            x = KerasTensor((3,))
            y = KerasTensor((3, 4))
            knp.correlate(x, y)

    def test_correlate_mode_same(self):
        x = KerasTensor((3,))
        y = KerasTensor((3,))
        self.assertEqual(knp.correlate(x, y, mode="same").shape, (3,))
        self.assertTrue(knp.correlate(x, y, mode="same").dtype == "float32")

        with self.assertRaises(ValueError):
            x = KerasTensor((3,))
            y = KerasTensor((3, 4))
            knp.correlate(x, y, mode="same")

    def test_correlate_mode_full(self):
        x = KerasTensor((3,))
        y = KerasTensor((3,))
        self.assertEqual(knp.correlate(x, y, mode="full").shape, (5,))
        self.assertTrue(knp.correlate(x, y, mode="full").dtype == "float32")

        with self.assertRaises(ValueError):
            x = KerasTensor((3))
            y = KerasTensor((3, 4))
            knp.correlate(x, y, mode="full")

class NumpyOneInputOpsDynamicShapeTest(testing.TestCase):
    def test_mean(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.mean(x).shape, ())

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.mean(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.mean(x, axis=1, keepdims=True).shape, (None, 1, 3))

    def test_all(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.all(x).shape, ())

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.all(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.all(x, axis=1, keepdims=True).shape, (None, 1, 3))

    def test_any(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.any(x).shape, ())

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.any(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.any(x, axis=1, keepdims=True).shape, (None, 1, 3))

    def test_var(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.var(x).shape, ())

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.var(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.var(x, axis=1, keepdims=True).shape, (None, 1, 3))

    def test_sum(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.sum(x).shape, ())

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.sum(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.sum(x, axis=1, keepdims=True).shape, (None, 1, 3))

    def test_amax(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.amax(x).shape, ())

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.amax(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.amax(x, axis=1, keepdims=True).shape, (None, 1, 3))

    def test_amin(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.amin(x).shape, ())

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.amin(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.amin(x, axis=1, keepdims=True).shape, (None, 1, 3))

    def test_square(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.square(x).shape, (None, 3))

    def test_negative(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.negative(x).shape, (None, 3))

    def test_abs(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.abs(x).shape, (None, 3))

    def test_absolute(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.absolute(x).shape, (None, 3))

    def test_squeeze(self):
        x = KerasTensor((None, 1))
        self.assertEqual(knp.squeeze(x).shape, (None,))
        self.assertEqual(knp.squeeze(x, axis=1).shape, (None,))

        with self.assertRaises(ValueError):
            x = KerasTensor((None, 1))
            knp.squeeze(x, axis=0)

        # Multiple axes
        x = KerasTensor((None, 1, 1, 1))
        self.assertEqual(knp.squeeze(x, (1, 2)).shape, (None, 1))
        self.assertEqual(knp.squeeze(x, (-1, -2)).shape, (None, 1))
        self.assertEqual(knp.squeeze(x, (1, 2, 3)).shape, (None,))
        self.assertEqual(knp.squeeze(x, (-1, 1)).shape, (None, 1))

    def test_transpose(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.transpose(x).shape, (3, None))

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.transpose(x, (2, 0, 1)).shape, (3, None, 3))

    def test_arccos(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.arccos(x).shape, (None, 3))

    def test_arccosh(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.arccosh(x).shape, (None, 3))

    def test_arcsin(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.arcsin(x).shape, (None, 3))

    def test_arcsinh(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.arcsinh(x).shape, (None, 3))

    def test_arctan(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.arctan(x).shape, (None, 3))

    def test_arctanh(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.arctanh(x).shape, (None, 3))

    def test_argmax(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.argmax(x).shape, ())
        self.assertEqual(knp.argmax(x, keepdims=True).shape, (None, 3))

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.argmax(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.argmax(x, keepdims=True).shape, (None, 3, 3))

    def test_argmin(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.argmin(x).shape, ())
        self.assertEqual(knp.argmin(x, keepdims=True).shape, (None, 3))

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.argmin(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.argmin(x, keepdims=True).shape, (None, 3, 3))

    def test_argsort(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.argsort(x).shape, (None, 3))

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.argsort(x, axis=1).shape, (None, 3, 3))

    def test_array(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.array(x).shape, (None, 3))

    def test_average(self):
        x = KerasTensor((None, 3))
        weights = KerasTensor((None, 3))
        self.assertEqual(knp.average(x, weights=weights).shape, ())

        x = KerasTensor((None, 3))
        weights = KerasTensor((3,))
        self.assertEqual(knp.average(x, axis=1, weights=weights).shape, (None,))

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.average(x, axis=1).shape, (None, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((None, 3, 3))
            weights = KerasTensor((None, 4))
            knp.average(x, weights=weights)

    def test_broadcast_to(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.broadcast_to(x, (2, 3, 3)).shape, (2, 3, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((3, 3))
            knp.broadcast_to(x, (2, 2, 3))

    def test_ceil(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.ceil(x).shape, (None, 3))

    def test_clip(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.clip(x, 1, 2).shape, (None, 3))

    def test_concatenate(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((None, 3))
        self.assertEqual(
            knp.concatenate(
                [x, y],
            ).shape,
            (None, 3),
        )
        self.assertEqual(knp.concatenate([x, y], axis=1).shape, (None, 6))

        with self.assertRaises(ValueError):
            self.assertEqual(knp.concatenate([x, y], axis=None).shape, (None,))

        with self.assertRaises(ValueError):
            x = KerasTensor((None, 3, 5))
            y = KerasTensor((None, 4, 6))
            knp.concatenate([x, y], axis=1)

    def test_concatenate_sparse(self):
        x = KerasTensor((2, 3), sparse=True)
        y = KerasTensor((2, 3))
        result = knp.concatenate([x, y], axis=1)
        self.assertEqual(result.shape, (2, 6))
        self.assertFalse(result.sparse)

        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3), sparse=True)
        result = knp.concatenate([x, y], axis=1)
        self.assertEqual(result.shape, (2, 6))
        self.assertFalse(result.sparse)

        x = KerasTensor((2, 3), sparse=True)
        y = KerasTensor((2, 3), sparse=True)
        result = knp.concatenate([x, y], axis=1)
        self.assertEqual(result.shape, (2, 6))
        self.assertTrue(result.sparse)

    def test_conjugate(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.conjugate(x).shape, (None, 3))

    def test_conj(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.conj(x).shape, (None, 3))

    def test_copy(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.copy(x).shape, (None, 3))

    def test_cos(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.cos(x).shape, (None, 3))

    def test_cosh(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.cosh(x).shape, (None, 3))

    def test_count_nonzero(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.count_nonzero(x).shape, ())

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.count_nonzero(x, axis=1).shape, (None, 3))

    def test_cumprod(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.cumprod(x).shape, (None,))

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.cumprod(x, axis=1).shape, (None, 3, 3))

    def test_cumsum(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.cumsum(x).shape, (None,))

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.cumsum(x, axis=1).shape, (None, 3, 3))

    def test_diag(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.diag(x).shape, (None,))
        self.assertEqual(knp.diag(x, k=3).shape, (None,))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3, 4))
            knp.diag(x)

    def test_diagonal(self):
        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.diagonal(x).shape, (3, None))

    def test_diff(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.diff(x).shape, (None, 2))
        self.assertEqual(knp.diff(x, n=2).shape, (None, 1))
        self.assertEqual(knp.diff(x, n=3).shape, (None, 0))
        self.assertEqual(knp.diff(x, n=4).shape, (None, 0))

        self.assertEqual(knp.diff(x, axis=0).shape, (None, 3))
        self.assertEqual(knp.diff(x, n=2, axis=0).shape, (None, 3))

    def test_dot(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((3, 2))
        z = KerasTensor((None, None, 2))
        self.assertEqual(knp.dot(x, y).shape, (None, 2))
        self.assertEqual(knp.dot(x, 2).shape, (None, 3))
        self.assertEqual(knp.dot(x, z).shape, (None, None, 2))

        x = KerasTensor((None,))
        y = KerasTensor((5,))
        self.assertEqual(knp.dot(x, y).shape, ())

    def test_exp(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.exp(x).shape, (None, 3))

    def test_expand_dims(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.expand_dims(x, -1).shape, (None, 3, 1))
        self.assertEqual(knp.expand_dims(x, 0).shape, (1, None, 3))
        self.assertEqual(knp.expand_dims(x, 1).shape, (None, 1, 3))
        self.assertEqual(knp.expand_dims(x, -2).shape, (None, 1, 3))

        # Multiple axes
        self.assertEqual(knp.expand_dims(x, (1, 2)).shape, (None, 1, 1, 3))
        self.assertEqual(knp.expand_dims(x, (-1, -2)).shape, (None, 3, 1, 1))
        self.assertEqual(knp.expand_dims(x, (-1, 1)).shape, (None, 1, 3, 1))

    def test_expm1(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.expm1(x).shape, (None, 3))

    def test_flip(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.flip(x).shape, (None, 3))

    def test_floor(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.floor(x).shape, (None, 3))

    def test_get_item(self):
        x = KerasTensor((None, 5, 16))
        # Simple slice.
        sliced = knp.get_item(x, 5)
        self.assertEqual(sliced.shape, (5, 16))
        # Ellipsis slice.
        sliced = knp.get_item(x, np.s_[..., -1])
        self.assertEqual(sliced.shape, (None, 5))
        # `newaxis` slice.
        sliced = knp.get_item(x, np.s_[:, np.newaxis, ...])
        self.assertEqual(sliced.shape, (None, 1, 5, 16))
        # Strided slice.
        sliced = knp.get_item(x, np.s_[:5, 3:, 3:12:2])
        self.assertEqual(sliced.shape, (None, 2, 5))
        # Error states.
        with self.assertRaises(ValueError):
            sliced = knp.get_item(x, np.s_[:, 17, :])
        with self.assertRaises(ValueError):
            sliced = knp.get_item(x, np.s_[..., 5, ...])
        with self.assertRaises(ValueError):
            sliced = knp.get_item(x, np.s_[:, :, :, :])

    def test_hstack(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((None, 3))
        self.assertEqual(knp.hstack([x, y]).shape, (None, 6))

        x = KerasTensor((None, 3))
        y = KerasTensor((None, None))
        self.assertEqual(knp.hstack([x, y]).shape, (None, None))

    def test_imag(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.imag(x).shape, (None, 3))

    def test_isfinite(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.isfinite(x).shape, (None, 3))

    def test_isinf(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.isinf(x).shape, (None, 3))

    def test_isnan(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.isnan(x).shape, (None, 3))

    def test_log(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.log(x).shape, (None, 3))

    def test_log10(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.log10(x).shape, (None, 3))

    def test_log1p(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.log1p(x).shape, (None, 3))

    def test_log2(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.log2(x).shape, (None, 3))

    def test_logaddexp(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.logaddexp(x, x).shape, (None, 3))

    def test_logical_not(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.logical_not(x).shape, (None, 3))

    def test_max(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.max(x).shape, ())

    def test_median(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.median(x).shape, ())

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.median(x, axis=1).shape, (None, 3))
        self.assertEqual(
            knp.median(x, axis=1, keepdims=True).shape, (None, 1, 3)
        )

    def test_meshgrid(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((None, 3))
        self.assertEqual(knp.meshgrid(x, y)[0].shape, (None, None))
        self.assertEqual(knp.meshgrid(x, y)[1].shape, (None, None))

        with self.assertRaises(ValueError):
            knp.meshgrid(x, y, indexing="kk")

    def test_moveaxis(self):
        x = KerasTensor((None, 3, 4, 5))
        self.assertEqual(knp.moveaxis(x, 0, -1).shape, (3, 4, 5, None))
        self.assertEqual(knp.moveaxis(x, -1, 0).shape, (5, None, 3, 4))
        self.assertEqual(
            knp.moveaxis(x, [0, 1], [-1, -2]).shape, (4, 5, 3, None)
        )
        self.assertEqual(knp.moveaxis(x, [0, 1], [1, 0]).shape, (3, None, 4, 5))
        self.assertEqual(
            knp.moveaxis(x, [0, 1], [-2, -1]).shape, (4, 5, None, 3)
        )

    def test_ndim(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.ndim(x).shape, (2,))

    def test_nonzero(self):
        x = KerasTensor((None, 5, 6))
        self.assertEqual(knp.nonzero(x).shape, (None, None, None))

    def test_ones_like(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.ones_like(x).shape, (None, 3))
        self.assertEqual(knp.ones_like(x).dtype, x.dtype)

    def test_zeros_like(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.zeros_like(x).shape, (None, 3))
        self.assertEqual(knp.zeros_like(x).dtype, x.dtype)

    def test_pad(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.pad(x, 1).shape, (None, 5))
        self.assertEqual(knp.pad(x, (1, 2)).shape, (None, 6))
        self.assertEqual(knp.pad(x, ((1, 2), (3, 4))).shape, (None, 10))

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.pad(x, 1).shape, (None, 5, 5))
        self.assertEqual(knp.pad(x, (1, 2)).shape, (None, 6, 6))
        self.assertEqual(
            knp.pad(x, ((1, 2), (3, 4), (5, 6))).shape, (None, 10, 14)
        )

    def test_prod(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.prod(x).shape, ())
        self.assertEqual(knp.prod(x, axis=0).shape, (3,))
        self.assertEqual(knp.prod(x, axis=1, keepdims=True).shape, (None, 1))

    def test_ravel(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.ravel(x).shape, (None,))

    def test_real(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.real(x).shape, (None, 3))

    def test_reciprocal(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.reciprocal(x).shape, (None, 3))

    def test_repeat(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.repeat(x, 2).shape, (None,))
        self.assertEqual(knp.repeat(x, 3, axis=1).shape, (None, 9))
        self.assertEqual(knp.repeat(x, [1, 2], axis=0).shape, (3, 3))
        self.assertEqual(knp.repeat(x, 2, axis=0).shape, (None, 3))

    def test_reshape(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.reshape(x, (3, 2)).shape, (3, 2))
        self.assertEqual(knp.reshape(x, (3, -1)).shape, (3, None))

    def test_roll(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.roll(x, 1).shape, (None, 3))
        self.assertEqual(knp.roll(x, 1, axis=1).shape, (None, 3))
        self.assertEqual(knp.roll(x, 1, axis=0).shape, (None, 3))

    def test_round(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.round(x).shape, (None, 3))

    def test_sign(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.sign(x).shape, (None, 3))

    def test_sin(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.sin(x).shape, (None, 3))

    def test_sinh(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.sinh(x).shape, (None, 3))

    def test_size(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.size(x).shape, ())

    def test_sort(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.sort(x).shape, (None, 3))
        self.assertEqual(knp.sort(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.sort(x, axis=0).shape, (None, 3))

    def test_split(self):
        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.split(x, 2)[0].shape, (None, 3, 3))
        self.assertEqual(knp.split(x, 3, axis=1)[0].shape, (None, 1, 3))
        self.assertEqual(len(knp.split(x, [1, 3], axis=1)), 3)
        self.assertEqual(knp.split(x, [1, 3], axis=1)[0].shape, (None, 1, 3))
        self.assertEqual(knp.split(x, [1, 3], axis=1)[1].shape, (None, 2, 3))
        self.assertEqual(knp.split(x, [1, 3], axis=1)[2].shape, (None, 0, 3))

    def test_sqrt(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.sqrt(x).shape, (None, 3))

    def test_stack(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((None, 3))
        self.assertEqual(knp.stack([x, y]).shape, (2, None, 3))
        self.assertEqual(knp.stack([x, y], axis=-1).shape, (None, 3, 2))

    def test_std(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.std(x).shape, ())

        x = KerasTensor((None, 3, 3))
        self.assertEqual(knp.std(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.std(x, axis=1, keepdims=True).shape, (None, 1, 3))

    def test_swapaxes(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.swapaxes(x, 0, 1).shape, (3, None))

    def test_tan(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.tan(x).shape, (None, 3))

    def test_tanh(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.tanh(x).shape, (None, 3))

    def test_tile(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.tile(x, [2]).shape, (None, 6))
        self.assertEqual(knp.tile(x, [1, 2]).shape, (None, 6))
        self.assertEqual(knp.tile(x, [2, 1, 2]).shape, (2, None, 6))

    def test_trace(self):
        x = KerasTensor((None, 3, None, 5))
        self.assertEqual(knp.trace(x).shape, (None, 5))
        self.assertEqual(knp.trace(x, axis1=2, axis2=3).shape, (None, 3))

    def test_tril(self):
        x = KerasTensor((None, 3, None, 5))
        self.assertEqual(knp.tril(x).shape, (None, 3, None, 5))
        self.assertEqual(knp.tril(x, k=1).shape, (None, 3, None, 5))
        self.assertEqual(knp.tril(x, k=-1).shape, (None, 3, None, 5))

    def test_triu(self):
        x = KerasTensor((None, 3, None, 5))
        self.assertEqual(knp.triu(x).shape, (None, 3, None, 5))
        self.assertEqual(knp.triu(x, k=1).shape, (None, 3, None, 5))
        self.assertEqual(knp.triu(x, k=-1).shape, (None, 3, None, 5))

    def test_vstack(self):
        x = KerasTensor((None, 3))
        y = KerasTensor((None, 3))
        self.assertEqual(knp.vstack([x, y]).shape, (None, 3))

        x = KerasTensor((None, 3))
        y = KerasTensor((None, None))
        self.assertEqual(knp.vstack([x, y]).shape, (None, 3))

    def test_argpartition(self):
        x = KerasTensor((None, 3))
        self.assertEqual(knp.argpartition(x, 3).shape, (None, 3))
        self.assertEqual(knp.argpartition(x, 1, axis=1).shape, (None, 3))

        with self.assertRaises(ValueError):
            knp.argpartition(x, (1, 3))

class NumpyOneInputOpsStaticShapeTest(testing.TestCase):
    def test_mean(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.mean(x).shape, ())

    def test_all(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.all(x).shape, ())

    def test_any(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.any(x).shape, ())

    def test_var(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.var(x).shape, ())

    def test_sum(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.sum(x).shape, ())

    def test_amax(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.amax(x).shape, ())

    def test_amin(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.amin(x).shape, ())

    def test_square(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.square(x).shape, (2, 3))

    def test_negative(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.negative(x).shape, (2, 3))

    def test_abs(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.abs(x).shape, (2, 3))

    def test_absolute(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.absolute(x).shape, (2, 3))

    def test_squeeze(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.squeeze(x).shape, (2, 3))

        x = KerasTensor((2, 1, 3))
        self.assertEqual(knp.squeeze(x).shape, (2, 3))
        self.assertEqual(knp.squeeze(x, axis=1).shape, (2, 3))
        self.assertEqual(knp.squeeze(x, axis=-2).shape, (2, 3))

        with self.assertRaises(ValueError):
            knp.squeeze(x, axis=0)

        # Multiple axes
        x = KerasTensor((2, 1, 1, 1))
        self.assertEqual(knp.squeeze(x, (1, 2)).shape, (2, 1))
        self.assertEqual(knp.squeeze(x, (-1, -2)).shape, (2, 1))
        self.assertEqual(knp.squeeze(x, (1, 2, 3)).shape, (2,))
        self.assertEqual(knp.squeeze(x, (-1, 1)).shape, (2, 1))

    def test_transpose(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.transpose(x).shape, (3, 2))

    def test_arccos(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.arccos(x).shape, (2, 3))

    def test_arccosh(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.arccosh(x).shape, (2, 3))

    def test_arcsin(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.arcsin(x).shape, (2, 3))

    def test_arcsinh(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.arcsinh(x).shape, (2, 3))

    def test_arctan(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.arctan(x).shape, (2, 3))

    def test_arctanh(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.arctanh(x).shape, (2, 3))

    def test_argmax(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.argmax(x).shape, ())
        self.assertEqual(knp.argmax(x, keepdims=True).shape, (2, 3))

    def test_argmin(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.argmin(x).shape, ())
        self.assertEqual(knp.argmin(x, keepdims=True).shape, (2, 3))

    def test_argsort(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.argsort(x).shape, (2, 3))
        self.assertEqual(knp.argsort(x, axis=None).shape, (6,))

    def test_array(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.array(x).shape, (2, 3))

    def test_average(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.average(x).shape, ())

    def test_broadcast_to(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.broadcast_to(x, (2, 2, 3)).shape, (2, 2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((3, 3))
            knp.broadcast_to(x, (2, 2, 3))

    def test_ceil(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.ceil(x).shape, (2, 3))

    def test_clip(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.clip(x, 1, 2).shape, (2, 3))

    def test_concatenate(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.concatenate([x, y]).shape, (4, 3))
        self.assertEqual(knp.concatenate([x, y], axis=1).shape, (2, 6))

        with self.assertRaises(ValueError):
            self.assertEqual(knp.concatenate([x, y], axis=None).shape, (None,))

    def test_conjugate(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.conjugate(x).shape, (2, 3))

    def test_conj(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.conj(x).shape, (2, 3))

    def test_copy(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.copy(x).shape, (2, 3))

    def test_cos(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.cos(x).shape, (2, 3))

    def test_cosh(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.cosh(x).shape, (2, 3))

    def test_count_nonzero(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.count_nonzero(x).shape, ())

    def test_cumprod(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.cumprod(x).shape, (6,))

    def test_cumsum(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.cumsum(x).shape, (6,))

    def test_diag(self):
        x = KerasTensor((3,))
        self.assertEqual(knp.diag(x).shape, (3, 3))
        self.assertEqual(knp.diag(x, k=3).shape, (6, 6))
        self.assertEqual(knp.diag(x, k=-2).shape, (5, 5))

        x = KerasTensor((3, 5))
        self.assertEqual(knp.diag(x).shape, (3,))
        self.assertEqual(knp.diag(x, k=3).shape, (2,))
        self.assertEqual(knp.diag(x, k=-2).shape, (1,))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3, 4))
            knp.diag(x)

    def test_diagonal(self):
        x = KerasTensor((3, 3))
        self.assertEqual(knp.diagonal(x).shape, (3,))
        self.assertEqual(knp.diagonal(x, offset=1).shape, (2,))

        x = KerasTensor((3, 5, 5))
        self.assertEqual(knp.diagonal(x).shape, (5, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor((3,))
            knp.diagonal(x)

    def test_diff(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.diff(x).shape, (2, 2))
        self.assertEqual(knp.diff(x, n=2).shape, (2, 1))
        self.assertEqual(knp.diff(x, n=3).shape, (2, 0))
        self.assertEqual(knp.diff(x, n=4).shape, (2, 0))

        self.assertEqual(knp.diff(x, axis=0).shape, (1, 3))
        self.assertEqual(knp.diff(x, n=2, axis=0).shape, (0, 3))
        self.assertEqual(knp.diff(x, n=3, axis=0).shape, (0, 3))

    def test_dot(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((3, 2))
        z = KerasTensor((4, 3, 2))
        self.assertEqual(knp.dot(x, y).shape, (2, 2))
        self.assertEqual(knp.dot(x, 2).shape, (2, 3))
        self.assertEqual(knp.dot(x, z).shape, (2, 4, 2))

        x = KerasTensor((5,))
        y = KerasTensor((5,))
        self.assertEqual(knp.dot(x, y).shape, ())

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((2, 3))
            knp.dot(x, y)

    def test_exp(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.exp(x).shape, (2, 3))

    def test_expand_dims(self):
        x = KerasTensor((2, 3, 4))
        self.assertEqual(knp.expand_dims(x, 0).shape, (1, 2, 3, 4))
        self.assertEqual(knp.expand_dims(x, 1).shape, (2, 1, 3, 4))
        self.assertEqual(knp.expand_dims(x, -2).shape, (2, 3, 1, 4))

        # Multiple axes
        self.assertEqual(knp.expand_dims(x, (1, 2)).shape, (2, 1, 1, 3, 4))
        self.assertEqual(knp.expand_dims(x, (-1, -2)).shape, (2, 3, 4, 1, 1))
        self.assertEqual(knp.expand_dims(x, (-1, 1)).shape, (2, 1, 3, 4, 1))

    def test_expm1(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.expm1(x).shape, (2, 3))

    def test_flip(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.flip(x).shape, (2, 3))

    def test_floor(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.floor(x).shape, (2, 3))

    def test_get_item(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.get_item(x, 1).shape, (3,))

        x = KerasTensor((5, 3, 2))
        self.assertEqual(knp.get_item(x, 3).shape, (3, 2))

        x = KerasTensor(
            [
                2,
            ]
        )
        self.assertEqual(knp.get_item(x, 0).shape, ())

    def test_hstack(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.hstack([x, y]).shape, (2, 6))

    def test_imag(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.imag(x).shape, (2, 3))

    def test_isfinite(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.isfinite(x).shape, (2, 3))

    def test_isinf(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.isinf(x).shape, (2, 3))

    def test_isnan(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.isnan(x).shape, (2, 3))

    def test_log(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.log(x).shape, (2, 3))

    def test_log10(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.log10(x).shape, (2, 3))

    def test_log1p(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.log1p(x).shape, (2, 3))

    def test_log2(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.log2(x).shape, (2, 3))

    def test_logaddexp(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.logaddexp(x, x).shape, (2, 3))

    def test_logical_not(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.logical_not(x).shape, (2, 3))

    def test_max(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.max(x).shape, ())

    def test_median(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.median(x).shape, ())

        x = KerasTensor((2, 3, 3))
        self.assertEqual(knp.median(x, axis=1).shape, (2, 3))
        self.assertEqual(knp.median(x, axis=1, keepdims=True).shape, (2, 1, 3))

    def test_meshgrid(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3, 4))
        z = KerasTensor((2, 3, 4, 5))
        self.assertEqual(knp.meshgrid(x, y)[0].shape, (24, 6))
        self.assertEqual(knp.meshgrid(x, y)[1].shape, (24, 6))
        self.assertEqual(knp.meshgrid(x, y, indexing="ij")[0].shape, (6, 24))
        self.assertEqual(
            knp.meshgrid(x, y, z, indexing="ij")[0].shape, (6, 24, 120)
        )
        with self.assertRaises(ValueError):
            knp.meshgrid(x, y, indexing="kk")

    def test_moveaxis(self):
        x = KerasTensor((2, 3, 4, 5))
        self.assertEqual(knp.moveaxis(x, 0, -1).shape, (3, 4, 5, 2))
        self.assertEqual(knp.moveaxis(x, -1, 0).shape, (5, 2, 3, 4))
        self.assertEqual(knp.moveaxis(x, [0, 1], [-1, -2]).shape, (4, 5, 3, 2))
        self.assertEqual(knp.moveaxis(x, [0, 1], [1, 0]).shape, (3, 2, 4, 5))
        self.assertEqual(knp.moveaxis(x, [0, 1], [-2, -1]).shape, (4, 5, 2, 3))

    def test_ndim(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.ndim(x).shape, (2,))

    def test_ones_like(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.ones_like(x).shape, (2, 3))
        self.assertEqual(knp.ones_like(x).dtype, x.dtype)

    def test_zeros_like(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.zeros_like(x).shape, (2, 3))
        self.assertEqual(knp.zeros_like(x).dtype, x.dtype)

    def test_pad(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.pad(x, 1).shape, (4, 5))
        self.assertEqual(knp.pad(x, (1, 2)).shape, (5, 6))
        self.assertEqual(knp.pad(x, ((1, 2), (3, 4))).shape, (5, 10))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            knp.pad(x, ((1, 2), (3, 4), (5, 6)))

    def test_prod(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.prod(x).shape, ())
        self.assertEqual(knp.prod(x, axis=0).shape, (3,))
        self.assertEqual(knp.prod(x, axis=1).shape, (2,))

    def test_ravel(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.ravel(x).shape, (6,))

    def test_real(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.real(x).shape, (2, 3))

    def test_reciprocal(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.reciprocal(x).shape, (2, 3))

    def test_repeat(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.repeat(x, 2).shape, (12,))
        self.assertEqual(knp.repeat(x, 3, axis=1).shape, (2, 9))
        self.assertEqual(knp.repeat(x, [1, 2], axis=0).shape, (3, 3))

    def test_reshape(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.reshape(x, (3, 2)).shape, (3, 2))
        self.assertEqual(knp.reshape(x, (3, -1)).shape, (3, 2))
        self.assertEqual(knp.reshape(x, (6,)).shape, (6,))
        self.assertEqual(knp.reshape(x, (-1,)).shape, (6,))

    def test_roll(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.roll(x, 1).shape, (2, 3))
        self.assertEqual(knp.roll(x, 1, axis=1).shape, (2, 3))
        self.assertEqual(knp.roll(x, 1, axis=0).shape, (2, 3))

    def test_round(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.round(x).shape, (2, 3))

    def test_sign(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.sign(x).shape, (2, 3))

    def test_sin(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.sin(x).shape, (2, 3))

    def test_sinh(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.sinh(x).shape, (2, 3))

    def test_size(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.size(x).shape, ())

    def test_sort(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.sort(x).shape, (2, 3))
        self.assertEqual(knp.sort(x, axis=1).shape, (2, 3))
        self.assertEqual(knp.sort(x, axis=0).shape, (2, 3))

    def test_split(self):
        x = KerasTensor((2, 3))
        self.assertEqual(len(knp.split(x, 2)), 2)
        self.assertEqual(knp.split(x, 2)[0].shape, (1, 3))
        self.assertEqual(knp.split(x, 3, axis=1)[0].shape, (2, 1))
        self.assertEqual(len(knp.split(x, [1, 3], axis=1)), 3)
        self.assertEqual(knp.split(x, [1, 3], axis=1)[0].shape, (2, 1))
        self.assertEqual(knp.split(x, [1, 3], axis=1)[1].shape, (2, 2))
        self.assertEqual(knp.split(x, [1, 3], axis=1)[2].shape, (2, 0))

        with self.assertRaises(ValueError):
            knp.split(x, 2, axis=1)

    def test_sqrt(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.sqrt(x).shape, (2, 3))

    def test_stack(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.stack([x, y]).shape, (2, 2, 3))
        self.assertEqual(knp.stack([x, y], axis=-1).shape, (2, 3, 2))

        with self.assertRaises(ValueError):
            x = KerasTensor((2, 3))
            y = KerasTensor((3, 3))
            knp.stack([x, y])

    def test_std(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.std(x).shape, ())

    def test_swapaxes(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.swapaxes(x, 0, 1).shape, (3, 2))

    def test_tan(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.tan(x).shape, (2, 3))

    def test_tanh(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.tanh(x).shape, (2, 3))

    def test_tile(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.tile(x, [2]).shape, (2, 6))
        self.assertEqual(knp.tile(x, [1, 2]).shape, (2, 6))
        self.assertEqual(knp.tile(x, [2, 1, 2]).shape, (2, 2, 6))

    def test_trace(self):
        x = KerasTensor((2, 3, 4, 5))
        self.assertEqual(knp.trace(x).shape, (4, 5))
        self.assertEqual(knp.trace(x, axis1=2, axis2=3).shape, (2, 3))

    def test_tril(self):
        x = KerasTensor((2, 3, 4, 5))
        self.assertEqual(knp.tril(x).shape, (2, 3, 4, 5))
        self.assertEqual(knp.tril(x, k=1).shape, (2, 3, 4, 5))
        self.assertEqual(knp.tril(x, k=-1).shape, (2, 3, 4, 5))

    def test_triu(self):
        x = KerasTensor((2, 3, 4, 5))
        self.assertEqual(knp.triu(x).shape, (2, 3, 4, 5))
        self.assertEqual(knp.triu(x, k=1).shape, (2, 3, 4, 5))
        self.assertEqual(knp.triu(x, k=-1).shape, (2, 3, 4, 5))

    def test_vstack(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.vstack([x, y]).shape, (4, 3))

    def test_argpartition(self):
        x = KerasTensor((2, 3))
        self.assertEqual(knp.argpartition(x, 3).shape, (2, 3))
        self.assertEqual(knp.argpartition(x, 1, axis=1).shape, (2, 3))

        with self.assertRaises(ValueError):
            knp.argpartition(x, (1, 3))

class NumpyTwoInputOpsCorretnessTest(testing.TestCase, parameterized.TestCase):
    def test_add(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        z = np.array([[[1, 2, 3], [3, 2, 1]]])
        self.assertAllClose(knp.add(x, y), np.add(x, y))
        self.assertAllClose(knp.add(x, z), np.add(x, z))

        self.assertAllClose(knp.Add()(x, y), np.add(x, y))
        self.assertAllClose(knp.Add()(x, z), np.add(x, z))

    def test_subtract(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        z = np.array([[[1, 2, 3], [3, 2, 1]]])
        self.assertAllClose(knp.subtract(x, y), np.subtract(x, y))
        self.assertAllClose(knp.subtract(x, z), np.subtract(x, z))

        self.assertAllClose(knp.Subtract()(x, y), np.subtract(x, y))
        self.assertAllClose(knp.Subtract()(x, z), np.subtract(x, z))

    def test_multiply(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        z = np.array([[[1, 2, 3], [3, 2, 1]]])
        self.assertAllClose(knp.multiply(x, y), np.multiply(x, y))
        self.assertAllClose(knp.multiply(x, z), np.multiply(x, z))

        self.assertAllClose(knp.Multiply()(x, y), np.multiply(x, y))
        self.assertAllClose(knp.Multiply()(x, z), np.multiply(x, z))

    def test_matmul(self):
        x = np.ones([2, 3, 4, 5])
        y = np.ones([2, 3, 5, 6])
        z = np.ones([5, 6])
        p = np.ones([4])
        self.assertAllClose(knp.matmul(x, y), np.matmul(x, y))
        self.assertAllClose(knp.matmul(x, z), np.matmul(x, z))
        self.assertAllClose(knp.matmul(p, x), np.matmul(p, x))

        self.assertAllClose(knp.Matmul()(x, y), np.matmul(x, y))
        self.assertAllClose(knp.Matmul()(x, z), np.matmul(x, z))
        self.assertAllClose(knp.Matmul()(p, x), np.matmul(p, x))

    @parameterized.named_parameters(
        named_product(
            (
                {
                    "testcase_name": "rank2",
                    "x_shape": (5, 3),
                    "y_shape": (3, 4),
                },
                {
                    "testcase_name": "rank3",
                    "x_shape": (2, 5, 3),
                    "y_shape": (2, 3, 4),
                },
                {
                    "testcase_name": "rank4",
                    "x_shape": (2, 2, 5, 3),
                    "y_shape": (2, 2, 3, 4),
                },
            ),
            dtype=["float16", "float32", "float64", "int32"],
            x_sparse=[False, True],
            y_sparse=[False, True],
        )
    )
    @pytest.mark.skipif(
        not backend.SUPPORTS_SPARSE_TENSORS,
        reason="Backend does not support sparse tensors.",
    )
    def test_matmul_sparse(self, dtype, x_shape, y_shape, x_sparse, y_sparse):
        if backend.backend() == "tensorflow":
            import tensorflow as tf

            if x_sparse and y_sparse and dtype in ("float16", "int32"):
                pytest.skip(
                    f"Sparse sparse matmul unsupported for {dtype}"
                    " with TensorFlow backend"
                )

            dense_to_sparse = tf.sparse.from_dense
        elif backend.backend() == "jax":
            import jax.experimental.sparse as jax_sparse

            dense_to_sparse = functools.partial(
                jax_sparse.BCOO.fromdense, n_batch=len(x_shape) - 2
            )

        rng = np.random.default_rng(0)

        x = x_np = (4 * rng.standard_normal(x_shape)).astype(dtype)
        if x_sparse:
            x_np = np.multiply(x_np, rng.random(x_shape) il", x, y),
            np.einsum("ijk,lkj->il", x, y),
        )
        self.assertAllClose(
            knp.einsum("ijk,ikj->i", x, y),
            np.einsum("ijk,ikj->i", x, y),
        )
        self.assertAllClose(
            knp.einsum("i...,j...k->...ijk", x, y),
            np.einsum("i..., j...k->...ijk", x, y),
        )
        self.assertAllClose(knp.einsum(",ijk", 5, y), np.einsum(",ijk", 5, y))

        self.assertAllClose(
            knp.Einsum("ijk,lkj->il")(x, y),
            np.einsum("ijk,lkj->il", x, y),
        )
        self.assertAllClose(
            knp.Einsum("ijk,ikj->i")(x, y),
            np.einsum("ijk,ikj->i", x, y),
        )
        self.assertAllClose(
            knp.Einsum("i...,j...k->...ijk")(x, y),
            np.einsum("i...,j...k->...ijk", x, y),
        )
        self.assertAllClose(knp.Einsum(",ijk")(5, y), np.einsum(",ijk", 5, y))

    @pytest.mark.skipif(
        backend.backend() != "tensorflow",
        reason=f"{backend.backend()} doesn't implement custom ops for einsum.",
    )
    def test_einsum_custom_ops_for_tensorflow(self):
        subscripts = "a,b->ab"
        x = np.arange(2).reshape([2]).astype("float32")
        y = np.arange(3).reshape([3]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "ab,b->a"
        x = np.arange(6).reshape([2, 3]).astype("float32")
        y = np.arange(3).reshape([3]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "ab,bc->ac"
        x = np.arange(6).reshape([2, 3]).astype("float32")
        y = np.arange(12).reshape([3, 4]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "ab,cb->ac"
        x = np.arange(6).reshape([2, 3]).astype("float32")
        y = np.arange(12).reshape([4, 3]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abc,cd->abd"
        x = np.arange(24).reshape([2, 3, 4]).astype("float32")
        y = np.arange(20).reshape([4, 5]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abc,cde->abde"
        x = np.arange(24).reshape([2, 3, 4]).astype("float32")
        y = np.arange(120).reshape([4, 5, 6]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abc,dc->abd"
        x = np.arange(24).reshape([2, 3, 4]).astype("float32")
        y = np.arange(20).reshape([5, 4]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abc,dce->abde"
        x = np.arange(24).reshape([2, 3, 4]).astype("float32")
        y = np.arange(120).reshape([5, 4, 6]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abc,dec->abde"
        x = np.arange(24).reshape([2, 3, 4]).astype("float32")
        y = np.arange(120).reshape([5, 6, 4]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abcd,abde->abce"
        x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")
        y = np.arange(180).reshape([2, 3, 5, 6]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abcd,abed->abce"
        x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")
        y = np.arange(180).reshape([2, 3, 6, 5]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abcd,acbe->adbe"
        x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")
        y = np.arange(144).reshape([2, 4, 3, 6]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abcd,adbe->acbe"
        x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")
        y = np.arange(180).reshape([2, 5, 3, 6]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abcd,aecd->acbe"
        x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")
        y = np.arange(240).reshape([2, 6, 4, 5]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abcd,aecd->aceb"
        x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")
        y = np.arange(240).reshape([2, 6, 4, 5]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abcd,cde->abe"
        x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")
        y = np.arange(120).reshape([4, 5, 6]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abcd,ced->abe"
        x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")
        y = np.arange(120).reshape([4, 6, 5]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abcd,ecd->abe"
        x = np.arange(120).reshape([2, 3, 4, 5]).astype("float32")
        y = np.arange(120).reshape([6, 4, 5]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abcde,aebf->adbcf"
        x = np.arange(720).reshape([2, 3, 4, 5, 6]).astype("float32")
        y = np.arange(252).reshape([2, 6, 3, 7]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

        subscripts = "abcde,afce->acdbf"
        x = np.arange(720).reshape([2, 3, 4, 5, 6]).astype("float32")
        y = np.arange(336).reshape([2, 7, 4, 6]).astype("float32")
        self.assertAllClose(
            knp.einsum(subscripts, x, y), np.einsum(subscripts, x, y)
        )

    def test_full_like(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(knp.full_like(x, 2), np.full_like(x, 2))
        self.assertAllClose(
            knp.full_like(x, 2, dtype="float32"),
            np.full_like(x, 2, dtype="float32"),
        )
        self.assertAllClose(
            knp.full_like(x, np.ones([2, 3])),
            np.full_like(x, np.ones([2, 3])),
        )

        self.assertAllClose(knp.FullLike()(x, 2), np.full_like(x, 2))
        self.assertAllClose(
            knp.FullLike()(x, 2, dtype="float32"),
            np.full_like(x, 2, dtype="float32"),
        )
        self.assertAllClose(
            knp.FullLike()(x, np.ones([2, 3])),
            np.full_like(x, np.ones([2, 3])),
        )

    def test_greater(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        self.assertAllClose(knp.greater(x, y), np.greater(x, y))
        self.assertAllClose(knp.greater(x, 2), np.greater(x, 2))
        self.assertAllClose(knp.greater(2, x), np.greater(2, x))

        self.assertAllClose(knp.Greater()(x, y), np.greater(x, y))
        self.assertAllClose(knp.Greater()(x, 2), np.greater(x, 2))
        self.assertAllClose(knp.Greater()(2, x), np.greater(2, x))

    def test_greater_equal(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        self.assertAllClose(
            knp.greater_equal(x, y),
            np.greater_equal(x, y),
        )
        self.assertAllClose(
            knp.greater_equal(x, 2),
            np.greater_equal(x, 2),
        )
        self.assertAllClose(
            knp.greater_equal(2, x),
            np.greater_equal(2, x),
        )

        self.assertAllClose(
            knp.GreaterEqual()(x, y),
            np.greater_equal(x, y),
        )
        self.assertAllClose(
            knp.GreaterEqual()(x, 2),
            np.greater_equal(x, 2),
        )
        self.assertAllClose(
            knp.GreaterEqual()(2, x),
            np.greater_equal(2, x),
        )

    def test_isclose(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        self.assertAllClose(knp.isclose(x, y), np.isclose(x, y))
        self.assertAllClose(knp.isclose(x, 2), np.isclose(x, 2))
        self.assertAllClose(knp.isclose(2, x), np.isclose(2, x))

        self.assertAllClose(knp.Isclose()(x, y), np.isclose(x, y))
        self.assertAllClose(knp.Isclose()(x, 2), np.isclose(x, 2))
        self.assertAllClose(knp.Isclose()(2, x), np.isclose(2, x))

    def test_less(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        self.assertAllClose(knp.less(x, y), np.less(x, y))
        self.assertAllClose(knp.less(x, 2), np.less(x, 2))
        self.assertAllClose(knp.less(2, x), np.less(2, x))

        self.assertAllClose(knp.Less()(x, y), np.less(x, y))
        self.assertAllClose(knp.Less()(x, 2), np.less(x, 2))
        self.assertAllClose(knp.Less()(2, x), np.less(2, x))

    def test_less_equal(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        self.assertAllClose(knp.less_equal(x, y), np.less_equal(x, y))
        self.assertAllClose(knp.less_equal(x, 2), np.less_equal(x, 2))
        self.assertAllClose(knp.less_equal(2, x), np.less_equal(2, x))

        self.assertAllClose(knp.LessEqual()(x, y), np.less_equal(x, y))
        self.assertAllClose(knp.LessEqual()(x, 2), np.less_equal(x, 2))
        self.assertAllClose(knp.LessEqual()(2, x), np.less_equal(2, x))

    def test_linspace(self):
        self.assertAllClose(knp.linspace(0, 10, 5), np.linspace(0, 10, 5))
        self.assertAllClose(
            knp.linspace(0, 10, 5, endpoint=False),
            np.linspace(0, 10, 5, endpoint=False),
        )
        self.assertAllClose(knp.Linspace(num=5)(0, 10), np.linspace(0, 10, 5))
        self.assertAllClose(
            knp.Linspace(num=5, endpoint=False)(0, 10),
            np.linspace(0, 10, 5, endpoint=False),
        )
        self.assertAllClose(
            knp.Linspace(num=0, endpoint=False)(0, 10),
            np.linspace(0, 10, 0, endpoint=False),
        )

        start = np.zeros([2, 3, 4])
        stop = np.ones([2, 3, 4])
        self.assertAllClose(
            knp.linspace(start, stop, 5, retstep=True)[0],
            np.linspace(start, stop, 5, retstep=True)[0],
        )
        self.assertAllClose(
            knp.linspace(start, stop, 5, endpoint=False, retstep=True)[0],
            np.linspace(start, stop, 5, endpoint=False, retstep=True)[0],
        )
        self.assertAllClose(
            knp.linspace(
                start, stop, 5, endpoint=False, retstep=True, dtype="int32"
            )[0],
            np.linspace(
                start, stop, 5, endpoint=False, retstep=True, dtype="int32"
            )[0],
        )

        self.assertAllClose(
            knp.Linspace(5, retstep=True)(start, stop)[0],
            np.linspace(start, stop, 5, retstep=True)[0],
        )
        self.assertAllClose(
            knp.Linspace(5, endpoint=False, retstep=True)(start, stop)[0],
            np.linspace(start, stop, 5, endpoint=False, retstep=True)[0],
        )
        self.assertAllClose(
            knp.Linspace(5, endpoint=False, retstep=True, dtype="int32")(
                start, stop
            )[0],
            np.linspace(
                start, stop, 5, endpoint=False, retstep=True, dtype="int32"
            )[0],
        )

        # Test `num` as a tensor
        # https://github.com/keras-team/keras/issues/19772
        self.assertAllClose(
            knp.linspace(0, 10, backend.convert_to_tensor(5)),
            np.linspace(0, 10, 5),
        )
        self.assertAllClose(
            knp.linspace(0, 10, backend.convert_to_tensor(5), endpoint=False),
            np.linspace(0, 10, 5, endpoint=False),
        )

    def test_logical_and(self):
        x = np.array([[True, False], [True, True]])
        y = np.array([[False, False], [True, False]])
        self.assertAllClose(knp.logical_and(x, y), np.logical_and(x, y))
        self.assertAllClose(knp.logical_and(x, True), np.logical_and(x, True))
        self.assertAllClose(knp.logical_and(True, x), np.logical_and(True, x))

        self.assertAllClose(knp.LogicalAnd()(x, y), np.logical_and(x, y))
        self.assertAllClose(knp.LogicalAnd()(x, True), np.logical_and(x, True))
        self.assertAllClose(knp.LogicalAnd()(True, x), np.logical_and(True, x))

    def test_logical_or(self):
        x = np.array([[True, False], [True, True]])
        y = np.array([[False, False], [True, False]])
        self.assertAllClose(knp.logical_or(x, y), np.logical_or(x, y))
        self.assertAllClose(knp.logical_or(x, True), np.logical_or(x, True))
        self.assertAllClose(knp.logical_or(True, x), np.logical_or(True, x))

        self.assertAllClose(knp.LogicalOr()(x, y), np.logical_or(x, y))
        self.assertAllClose(knp.LogicalOr()(x, True), np.logical_or(x, True))
        self.assertAllClose(knp.LogicalOr()(True, x), np.logical_or(True, x))

    def test_logspace(self):
        self.assertAllClose(knp.logspace(0, 10, 5), np.logspace(0, 10, 5))
        self.assertAllClose(
            knp.logspace(0, 10, 5, endpoint=False),
            np.logspace(0, 10, 5, endpoint=False),
        )
        self.assertAllClose(knp.Logspace(num=5)(0, 10), np.logspace(0, 10, 5))
        self.assertAllClose(
            knp.Logspace(num=5, endpoint=False)(0, 10),
            np.logspace(0, 10, 5, endpoint=False),
        )

        start = np.zeros([2, 3, 4])
        stop = np.ones([2, 3, 4])

        self.assertAllClose(
            knp.logspace(start, stop, 5, base=10),
            np.logspace(start, stop, 5, base=10),
        )
        self.assertAllClose(
            knp.logspace(start, stop, 5, endpoint=False, base=10),
            np.logspace(start, stop, 5, endpoint=False, base=10),
        )

        self.assertAllClose(
            knp.Logspace(5, base=10)(start, stop),
            np.logspace(start, stop, 5, base=10),
        )
        self.assertAllClose(
            knp.Logspace(5, endpoint=False, base=10)(start, stop),
            np.logspace(start, stop, 5, endpoint=False, base=10),
        )

    def test_maximum(self):
        x = np.array([[1, 2], [3, 4]])
        y = np.array([[5, 6], [7, 8]])
        self.assertAllClose(knp.maximum(x, y), np.maximum(x, y))
        self.assertAllClose(knp.maximum(x, 1), np.maximum(x, 1))
        self.assertAllClose(knp.maximum(1, x), np.maximum(1, x))

        self.assertAllClose(knp.Maximum()(x, y), np.maximum(x, y))
        self.assertAllClose(knp.Maximum()(x, 1), np.maximum(x, 1))
        self.assertAllClose(knp.Maximum()(1, x), np.maximum(1, x))

    def test_minimum(self):
        x = np.array([[1, 2], [3, 4]])
        y = np.array([[5, 6], [7, 8]])
        self.assertAllClose(knp.minimum(x, y), np.minimum(x, y))
        self.assertAllClose(knp.minimum(x, 1), np.minimum(x, 1))
        self.assertAllClose(knp.minimum(1, x), np.minimum(1, x))

        self.assertAllClose(knp.Minimum()(x, y), np.minimum(x, y))
        self.assertAllClose(knp.Minimum()(x, 1), np.minimum(x, 1))
        self.assertAllClose(knp.Minimum()(1, x), np.minimum(1, x))

    def test_mod(self):
        x = np.array([[1, 2], [3, 4]])
        y = np.array([[5, 6], [7, 8]])
        self.assertAllClose(knp.mod(x, y), np.mod(x, y))
        self.assertAllClose(knp.mod(x, 1), np.mod(x, 1))
        self.assertAllClose(knp.mod(1, x), np.mod(1, x))

        self.assertAllClose(knp.Mod()(x, y), np.mod(x, y))
        self.assertAllClose(knp.Mod()(x, 1), np.mod(x, 1))
        self.assertAllClose(knp.Mod()(1, x), np.mod(1, x))

    def test_not_equal(self):
        x = np.array([[1, 2], [3, 4]])
        y = np.array([[5, 6], [7, 8]])
        self.assertAllClose(knp.not_equal(x, y), np.not_equal(x, y))
        self.assertAllClose(knp.not_equal(x, 1), np.not_equal(x, 1))
        self.assertAllClose(knp.not_equal(1, x), np.not_equal(1, x))

        self.assertAllClose(knp.NotEqual()(x, y), np.not_equal(x, y))
        self.assertAllClose(knp.NotEqual()(x, 1), np.not_equal(x, 1))
        self.assertAllClose(knp.NotEqual()(1, x), np.not_equal(1, x))

    def test_outer(self):
        x = np.array([1, 2, 3])
        y = np.array([4, 5, 6])
        self.assertAllClose(knp.outer(x, y), np.outer(x, y))
        self.assertAllClose(knp.Outer()(x, y), np.outer(x, y))

        x = np.ones([2, 3, 4])
        y = np.ones([2, 3, 4, 5, 6])
        self.assertAllClose(knp.outer(x, y), np.outer(x, y))
        self.assertAllClose(knp.Outer()(x, y), np.outer(x, y))

    def test_quantile(self):
        x = np.arange(24).reshape([2, 3, 4]).astype("float32")

        # q as scalar
        q = np.array(0.5, dtype="float32")
        self.assertAllClose(knp.quantile(x, q), np.quantile(x, q))
        self.assertAllClose(
            knp.quantile(x, q, keepdims=True), np.quantile(x, q, keepdims=True)
        )

        # q as 1D tensor
        q = np.array([0.5, 1.0], dtype="float32")
        self.assertAllClose(knp.quantile(x, q), np.quantile(x, q))
        self.assertAllClose(
            knp.quantile(x, q, keepdims=True), np.quantile(x, q, keepdims=True)
        )
        self.assertAllClose(
            knp.quantile(x, q, axis=1), np.quantile(x, q, axis=1)
        )
        self.assertAllClose(
            knp.quantile(x, q, axis=1, keepdims=True),
            np.quantile(x, q, axis=1, keepdims=True),
        )

        # multiple axes
        self.assertAllClose(
            knp.quantile(x, q, axis=(1, 2)), np.quantile(x, q, axis=(1, 2))
        )

        # test all supported methods
        q = np.array([0.501, 1.0], dtype="float32")
        for method in ["linear", "lower", "higher", "midpoint", "nearest"]:
            self.assertAllClose(
                knp.quantile(x, q, method=method),
                np.quantile(x, q, method=method),
            )
            self.assertAllClose(
                knp.quantile(x, q, axis=1, method=method),
                np.quantile(x, q, axis=1, method=method),
            )

    def test_take(self):
        x = np.arange(24).reshape([1, 2, 3, 4])
        indices = np.array([0, 1])
        self.assertAllClose(knp.take(x, indices), np.take(x, indices))
        self.assertAllClose(knp.take(x, 0), np.take(x, 0))
        self.assertAllClose(knp.take(x, 0, axis=1), np.take(x, 0, axis=1))

        self.assertAllClose(knp.Take()(x, indices), np.take(x, indices))
        self.assertAllClose(knp.Take()(x, 0), np.take(x, 0))
        self.assertAllClose(knp.Take(axis=1)(x, 0), np.take(x, 0, axis=1))

        # Test with multi-dimensional indices
        rng = np.random.default_rng(0)
        x = rng.standard_normal((2, 3, 4, 5))
        indices = rng.integers(0, 4, (6, 7))
        self.assertAllClose(
            knp.take(x, indices, axis=2), np.take(x, indices, axis=2)
        )

        # Test with negative axis
        self.assertAllClose(
            knp.take(x, indices, axis=-2), np.take(x, indices, axis=-2)
        )

        # Test with axis=None & x.ndim=2
        x = np.array(([1, 2], [3, 4]))
        indices = np.array([2, 3])
        self.assertAllClose(
            knp.take(x, indices, axis=None), np.take(x, indices, axis=None)
        )

        # Test with negative indices
        x = rng.standard_normal((2, 3, 4, 5))
        indices = rng.integers(-3, 0, (6, 7))
        self.assertAllClose(
            knp.take(x, indices, axis=2), np.take(x, indices, axis=2)
        )

    @parameterized.named_parameters(
        named_product(
            [
                {"testcase_name": "axis_none", "axis": None},
                {"testcase_name": "axis_0", "axis": 0},
                {"testcase_name": "axis_1", "axis": 1},
                {"testcase_name": "axis_minus1", "axis": -1},
            ],
            dtype=[
                "float16",
                "float32",
                "float64",
                "uint8",
                "int8",
                "int16",
                "int32",
            ],
        )
    )
    @pytest.mark.skipif(
        not backend.SUPPORTS_SPARSE_TENSORS,
        reason="Backend does not support sparse tensors.",
    )
    def test_take_sparse(self, dtype, axis):
        rng = np.random.default_rng(0)
        x = (4 * rng.standard_normal((3, 4, 5))).astype(dtype)

        if backend.backend() == "tensorflow":
            import tensorflow as tf

            indices = tf.SparseTensor([[0, 0], [1, 2]], [1, 2], (2, 3))
        elif backend.backend() == "jax":
            import jax.experimental.sparse as jax_sparse

            indices = jax_sparse.BCOO(([1, 2], [[0, 0], [1, 2]]), shape=(2, 3))

        self.assertAllClose(
            knp.take(x, indices, axis=axis),
            np.take(x, backend.convert_to_numpy(indices), axis=axis),
        )

    def test_take_along_axis(self):
        x = np.arange(24).reshape([1, 2, 3, 4])
        indices = np.ones([1, 4, 1, 1], dtype=np.int32)
        self.assertAllClose(
            knp.take_along_axis(x, indices, axis=1),
            np.take_along_axis(x, indices, axis=1),
        )
        self.assertAllClose(
            knp.TakeAlongAxis(axis=1)(x, indices),
            np.take_along_axis(x, indices, axis=1),
        )

        x = np.arange(12).reshape([1, 1, 3, 4])
        indices = np.ones([1, 4, 1, 1], dtype=np.int32)
        self.assertAllClose(
            knp.take_along_axis(x, indices, axis=2),
            np.take_along_axis(x, indices, axis=2),
        )
        self.assertAllClose(
            knp.TakeAlongAxis(axis=2)(x, indices),
            np.take_along_axis(x, indices, axis=2),
        )

        # Test with axis=None
        x = np.arange(12).reshape([1, 1, 3, 4])
        indices = np.array([1, 2, 3], dtype=np.int32)
        self.assertAllClose(
            knp.take_along_axis(x, indices, axis=None),
            np.take_along_axis(x, indices, axis=None),
        )
        self.assertAllClose(
            knp.TakeAlongAxis(axis=None)(x, indices),
            np.take_along_axis(x, indices, axis=None),
        )

        # Test with negative indices
        x = np.arange(12).reshape([1, 1, 3, 4])
        indices = np.full([1, 4, 1, 1], -1, dtype=np.int32)
        self.assertAllClose(
            knp.take_along_axis(x, indices, axis=2),
            np.take_along_axis(x, indices, axis=2),
        )
        self.assertAllClose(
            knp.TakeAlongAxis(axis=2)(x, indices),
            np.take_along_axis(x, indices, axis=2),
        )

    def test_tensordot(self):
        x = np.arange(24).reshape([1, 2, 3, 4]).astype("float32")
        y = np.arange(24).reshape([3, 4, 1, 2]).astype("float32")
        self.assertAllClose(
            knp.tensordot(x, y, axes=2), np.tensordot(x, y, axes=2)
        )
        self.assertAllClose(
            knp.tensordot(x, y, axes=([0, 1], [2, 3])),
            np.tensordot(x, y, axes=([0, 1], [2, 3])),
        )
        self.assertAllClose(
            knp.Tensordot(axes=2)(x, y),
            np.tensordot(x, y, axes=2),
        )
        self.assertAllClose(
            knp.Tensordot(axes=([0, 1], [2, 3]))(x, y),
            np.tensordot(x, y, axes=([0, 1], [2, 3])),
        )
        self.assertAllClose(
            knp.Tensordot(axes=[0, 2])(x, y),
            np.tensordot(x, y, axes=[0, 2]),
        )

    def test_vdot(self):
        x = np.array([1.0, 2.0, 3.0])
        y = np.array([4.0, 5.0, 6.0])
        self.assertAllClose(knp.vdot(x, y), np.vdot(x, y))
        self.assertAllClose(knp.Vdot()(x, y), np.vdot(x, y))

    def test_where(self):
        x = np.array([1, 2, 3])
        y = np.array([4, 5, 6])
        self.assertAllClose(knp.where(x > 1, x, y), np.where(x > 1, x, y))
        self.assertAllClose(knp.Where()(x > 1, x, y), np.where(x > 1, x, y))
        self.assertAllClose(knp.where(x > 1), np.where(x > 1))
        self.assertAllClose(knp.Where()(x > 1), np.where(x > 1))

        with self.assertRaisesRegexp(
            ValueError, "`x1` and `x2` either both should be `None`"
        ):
            knp.where(x > 1, x, None)

    def test_digitize(self):
        x = np.array([0.0, 1.0, 3.0, 1.6])
        bins = np.array([0.0, 3.0, 4.5, 7.0])
        self.assertAllClose(knp.digitize(x, bins), np.digitize(x, bins))
        self.assertAllClose(knp.Digitize()(x, bins), np.digitize(x, bins))
        self.assertTrue(
            standardize_dtype(knp.digitize(x, bins).dtype) == "int32"
        )
        self.assertTrue(
            standardize_dtype(knp.Digitize()(x, bins).dtype) == "int32"
        )

        x = np.array([0.2, 6.4, 3.0, 1.6])
        bins = np.array([0.0, 1.0, 2.5, 4.0, 10.0])
        self.assertAllClose(knp.digitize(x, bins), np.digitize(x, bins))
        self.assertAllClose(knp.Digitize()(x, bins), np.digitize(x, bins))
        self.assertTrue(
            standardize_dtype(knp.digitize(x, bins).dtype) == "int32"
        )
        self.assertTrue(
            standardize_dtype(knp.Digitize()(x, bins).dtype) == "int32"
        )

        x = np.array([1, 4, 10, 15])
        bins = np.array([4, 10, 14, 15])
        self.assertAllClose(knp.digitize(x, bins), np.digitize(x, bins))
        self.assertAllClose(knp.Digitize()(x, bins), np.digitize(x, bins))
        self.assertTrue(
            standardize_dtype(knp.digitize(x, bins).dtype) == "int32"
        )
        self.assertTrue(
            standardize_dtype(knp.Digitize()(x, bins).dtype) == "int32"
        )

class NumpyOneInputOpsCorrectnessTest(testing.TestCase, parameterized.TestCase):
    def test_mean(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(knp.mean(x), np.mean(x))
        self.assertAllClose(knp.mean(x, axis=()), np.mean(x, axis=()))
        self.assertAllClose(knp.mean(x, axis=1), np.mean(x, axis=1))
        self.assertAllClose(knp.mean(x, axis=(1,)), np.mean(x, axis=(1,)))
        self.assertAllClose(
            knp.mean(x, axis=1, keepdims=True),
            np.mean(x, axis=1, keepdims=True),
        )

        self.assertAllClose(knp.Mean()(x), np.mean(x))
        self.assertAllClose(knp.Mean(axis=1)(x), np.mean(x, axis=1))
        self.assertAllClose(
            knp.Mean(axis=1, keepdims=True)(x),
            np.mean(x, axis=1, keepdims=True),
        )

        # test overflow
        x = np.array([65504, 65504, 65504], dtype="float16")
        self.assertAllClose(knp.mean(x), np.mean(x))

    def test_all(self):
        x = np.array([[True, False, True], [True, True, True]])
        self.assertAllClose(knp.all(x), np.all(x))
        self.assertAllClose(knp.all(x, axis=()), np.all(x, axis=()))
        self.assertAllClose(knp.all(x, axis=1), np.all(x, axis=1))
        self.assertAllClose(knp.all(x, axis=(1,)), np.all(x, axis=(1,)))
        self.assertAllClose(
            knp.all(x, axis=1, keepdims=True),
            np.all(x, axis=1, keepdims=True),
        )

        self.assertAllClose(knp.All()(x), np.all(x))
        self.assertAllClose(knp.All(axis=1)(x), np.all(x, axis=1))
        self.assertAllClose(
            knp.All(axis=1, keepdims=True)(x),
            np.all(x, axis=1, keepdims=True),
        )

    def test_any(self):
        x = np.array([[True, False, True], [True, True, True]])
        self.assertAllClose(knp.any(x), np.any(x))
        self.assertAllClose(knp.any(x, axis=()), np.any(x, axis=()))
        self.assertAllClose(knp.any(x, axis=1), np.any(x, axis=1))
        self.assertAllClose(knp.any(x, axis=(1,)), np.any(x, axis=(1,)))
        self.assertAllClose(
            knp.any(x, axis=1, keepdims=True),
            np.any(x, axis=1, keepdims=True),
        )

        self.assertAllClose(knp.Any()(x), np.any(x))
        self.assertAllClose(knp.Any(axis=1)(x), np.any(x, axis=1))
        self.assertAllClose(
            knp.Any(axis=1, keepdims=True)(x),
            np.any(x, axis=1, keepdims=True),
        )

    def test_var(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(knp.var(x), np.var(x))
        self.assertAllClose(knp.var(x, axis=()), np.var(x, axis=()))
        self.assertAllClose(knp.var(x, axis=1), np.var(x, axis=1))
        self.assertAllClose(knp.var(x, axis=(1,)), np.var(x, axis=(1,)))
        self.assertAllClose(
            knp.var(x, axis=1, keepdims=True),
            np.var(x, axis=1, keepdims=True),
        )

        self.assertAllClose(knp.Var()(x), np.var(x))
        self.assertAllClose(knp.Var(axis=1)(x), np.var(x, axis=1))
        self.assertAllClose(
            knp.Var(axis=1, keepdims=True)(x),
            np.var(x, axis=1, keepdims=True),
        )

    def test_sum(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(knp.sum(x), np.sum(x))
        self.assertAllClose(knp.sum(x, axis=()), np.sum(x, axis=()))
        self.assertAllClose(knp.sum(x, axis=1), np.sum(x, axis=1))
        self.assertAllClose(knp.sum(x, axis=(1,)), np.sum(x, axis=(1,)))
        self.assertAllClose(
            knp.sum(x, axis=1, keepdims=True),
            np.sum(x, axis=1, keepdims=True),
        )

        self.assertAllClose(knp.Sum()(x), np.sum(x))
        self.assertAllClose(knp.Sum(axis=1)(x), np.sum(x, axis=1))
        self.assertAllClose(
            knp.Sum(axis=1, keepdims=True)(x),
            np.sum(x, axis=1, keepdims=True),
        )

    def test_amax(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(knp.amax(x), np.amax(x))
        self.assertAllClose(knp.amax(x, axis=()), np.amax(x, axis=()))
        self.assertAllClose(knp.amax(x, axis=1), np.amax(x, axis=1))
        self.assertAllClose(knp.amax(x, axis=(1,)), np.amax(x, axis=(1,)))
        self.assertAllClose(
            knp.amax(x, axis=1, keepdims=True),
            np.amax(x, axis=1, keepdims=True),
        )

        self.assertAllClose(knp.Amax()(x), np.amax(x))
        self.assertAllClose(knp.Amax(axis=1)(x), np.amax(x, axis=1))
        self.assertAllClose(
            knp.Amax(axis=1, keepdims=True)(x),
            np.amax(x, axis=1, keepdims=True),
        )

    def test_amin(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(knp.amin(x), np.amin(x))

```

8. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git status --short && /Users/sankanum1/.slingshot/bin/rtk git rev-parse HEAD",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk python -c \"import numpy as np; x=np.empty((64,10,1,1)); print(np.repeat(x, [784]).shape); print(np.repeat(x, [784], axis=0).shape)\"",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- I want to confirm the repository is clean at the required base commit and establish NumPy's repeat shape semantics for singleton sequence repeats before editing production code."
}
```
Output:
```
I ran all provided commands and below are the outcomes for each command with their status. Please analyze each output carefully and run the commands again for which you see errors to get their output by correcting the command and other parameters.

=== EXECUTION SUMMARY ===
Total Commands: 2
Number of Successful Commands: 2
Number of Failed Commands: 0
Number of Timed Out Commands: 0
========================

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 1 of 2                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git status --short && /Users/sankanum1/.slingshot/bin/rtk git rev-parse HEAD'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
2305fada8889e86463493bb4893b13ee8a8f0573
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 2 of 2                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk python -c "import numpy as np; x=np.empty((64,10,1,1)); print(np.repeat(x, [784]).shape); print(np.repeat(x, [784], axis=0).shape)"'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
(501760,)
(50176, 10, 1, 1)
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

```

9. **Tool call: edit_file**
Input:
```json
{
  "operations": [
    {
      "filePath": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826/keras/src/ops/numpy.py",
      "originalContent": "class Repeat(Operation):\n    def __init__(self, repeats, axis=None):\n        super().__init__()\n        self.axis = axis\n        self.repeats = repeats\n\n    def call(self, x):\n        return backend.numpy.repeat(x, self.repeats, axis=self.axis)\n\n    def compute_output_spec(self, x):\n        x_shape = list(x.shape)\n        if self.axis is None:\n            if None in x_shape:\n                return KerasTensor([None], dtype=x.dtype)\n\n            x_flatten_size = int(np.prod(x_shape))\n            if isinstance(self.repeats, int):\n                output_shape = [x_flatten_size * self.repeats]\n            else:\n                output_shape = [int(np.sum(self.repeats))]\n            return KerasTensor(output_shape, dtype=x.dtype)\n\n        size_on_ax = x_shape[self.axis]\n        output_shape = x_shape\n        if isinstance(self.repeats, int):\n            if size_on_ax is None:\n                output_shape[self.axis] = None\n            else:\n                output_shape[self.axis] = size_on_ax * self.repeats\n        else:\n            output_shape[self.axis] = int(np.sum(self.repeats))\n        return KerasTensor(output_shape, dtype=x.dtype)\n\n\n@keras_export([\"keras.ops.repeat\", \"keras.ops.numpy.repeat\"])\ndef repeat(x, repeats, axis=None):\n    \"\"\"Repeat each element of a tensor after themselves.\n\n    Args:\n        x: Input tensor.\n        repeats: The number of repetitions for each element.\n        axis: The axis along which to repeat values. By default, use\n            the flattened input array, and return a flat output array.\n\n    Returns:\n        Output tensor.\n    \"\"\"\n    if any_symbolic_tensors((x,)):\n        return Repeat(repeats, axis=axis).symbolic_call(x)\n    return backend.numpy.repeat(x, repeats, axis=axis)\n",
      "newContent": "class Repeat(Operation):\n    def __init__(self, repeats, axis=None):\n        super().__init__()\n        self.axis = axis\n        self.repeats = repeats\n\n    def call(self, x):\n        return backend.numpy.repeat(x, self.repeats, axis=self.axis)\n\n    def compute_output_spec(self, x):\n        x_shape = list(x.shape)\n        if self.axis is None:\n            if None in x_shape:\n                return KerasTensor([None], dtype=x.dtype)\n\n            x_flatten_size = int(np.prod(x_shape))\n            if isinstance(self.repeats, int):\n                output_shape = [x_flatten_size * self.repeats]\n            elif len(self.repeats) == 1:\n                output_shape = [x_flatten_size * self.repeats[0]]\n            else:\n                output_shape = [int(np.sum(self.repeats))]\n            return KerasTensor(output_shape, dtype=x.dtype)\n\n        size_on_ax = x_shape[self.axis]\n        output_shape = x_shape\n        if isinstance(self.repeats, int):\n            if size_on_ax is None:\n                output_shape[self.axis] = None\n            else:\n                output_shape[self.axis] = size_on_ax * self.repeats\n        else:\n            output_shape[self.axis] = int(np.sum(self.repeats))\n        return KerasTensor(output_shape, dtype=x.dtype)\n\n\n@keras_export([\"keras.ops.repeat\", \"keras.ops.numpy.repeat\"])\ndef repeat(x, repeats, axis=None):\n    \"\"\"Repeat each element of a tensor after themselves.\n\n    Args:\n        x: Input tensor.\n        repeats: The number of repetitions for each element.\n        axis: The axis along which to repeat values. By default, use\n            the flattened input array, and return a flat output array.\n\n    Returns:\n        Output tensor.\n    \"\"\"\n    if any_symbolic_tensors((x,)):\n        return Repeat(repeats, axis=axis).symbolic_call(x)\n    return backend.numpy.repeat(x, repeats, axis=axis)\n"
    }
  ],
  "toolPurpose": "- I want to update Repeat symbolic shape inference so a singleton sequence of repeat counts is broadcast across every element of a flattened static-shape KerasTensor, matching NumPy and backend behavior.",
  "references": {
    "hasJiraContext": false,
    "hasFigmaContext": false
  }
}
```
Output:
```
Successfully replaced content in file Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826/keras/src/ops/numpy.py
```

10. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk python -m py_compile keras/src/ops/numpy.py",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk python -m pytest keras/src/ops/numpy_test.py::NumpyOneInputOpsStaticShapeTest::test_repeat -q",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 120000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --check && /Users/sankanum1/.slingshot/bin/rtk git --no-pager diff -- keras/src/ops/numpy.py",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- I want to run syntax validation, the smallest existing repeat test, and diff quality checks after the production shape-inference change."
}
```
Output:
```
I ran all provided commands and below are the outcomes for each command with their status. Please analyze each output carefully and run the commands again for which you see errors to get their output by correcting the command and other parameters.

=== EXECUTION SUMMARY ===
Total Commands: 3
Number of Successful Commands: 2
Number of Failed Commands: 1
Number of Timed Out Commands: 0
========================

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 1 of 3                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk python -m py_compile keras/src/ops/numpy.py'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 2 of 3                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk python -m pytest keras/src/ops/numpy_test.py::NumpyOneInputOpsStaticShapeTest::test_repeat -q'
Status: ERROR
─────────────────────────────────────────────────────────────────────────
Output:
Command failed with exit code 4.

--- Full Output ---
ImportError while loading conftest '/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826/conftest.py'.
conftest.py:17: in 
    from keras.src.backend import backend  # noqa: E402
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
keras/__init__.py:10: in 
    from keras.api import *  # noqa: F403
    ^^^^^^^^^^^^^^^^^^^^^^^
keras/api/__init__.py:7: in 
    from keras.api import _tf_keras
keras/api/_tf_keras/__init__.py:1: in 
    from keras.api._tf_keras import keras
keras/api/_tf_keras/keras/__init__.py:7: in 
    from keras.api import activations
keras/api/activations/__init__.py:7: in 
    from keras.src.activations import deserialize
keras/src/__init__.py:1: in 
    from keras.src import activations
keras/src/activations/__init__.py:3: in 
    from keras.src.activations.activations import elu
keras/src/activations/activations.py:1: in 
    from keras.src import backend
keras/src/backend/__init__.py:9: in 
    from keras.src.backend.common.dtypes import result_type
keras/src/backend/common/__init__.py:2: in 
    from keras.src.backend.common.dtypes import result_type
keras/src/backend/common/dtypes.py:5: in 
    from keras.src.backend.common.variables import standardize_dtype
keras/src/backend/common/variables.py:10: in 
    from keras.src.utils.module_utils import tensorflow as tf
keras/src/utils/__init__.py:1: in 
    from keras.src.utils.audio_dataset_utils import audio_dataset_from_directory
keras/src/utils/audio_dataset_utils.py:4: in 
    from keras.src.utils import dataset_utils
keras/src/utils/dataset_utils.py:10: in 
    from keras.src.utils import io_utils
keras/src/utils/io_utils.py:3: in 
    from absl import logging
E   ModuleNotFoundError: No module named 'absl'
__CMD_FINISHED__ 4
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 3 of 3                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --check && /Users/sankanum1/.slingshot/bin/rtk git --no-pager diff -- keras/src/ops/numpy.py'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
keras/src/ops/numpy.py | 2 ++
 1 file changed, 2 insertions(+)

Changes:

keras/src/ops/numpy.py
@@ -4352,6 +4352,8 @@ class Repeat(Operation):
             x_flatten_size = int(np.prod(x_shape))
             if isinstance(self.repeats, int):
                 output_shape = [x_flatten_size * self.repeats]
+            elif len(self.repeats) == 1:
+                output_shape = [x_flatten_size * self.repeats[0]]
             else:
                 output_shape = [int(np.sum(self.repeats))]
             return KerasTensor(output_shape, dtype=x.dtype)
  +2 -0
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

```

11. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk python -c \"import ast, numpy as np; p='keras/src/ops/numpy.py'; tree=ast.parse(open(p).read(), p); node=next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name=='Repeat'); ns={'Operation':type('Operation',(),{}),'KerasTensor':lambda shape,dtype=None:type('Spec',(),{'shape':tuple(shape),'dtype':dtype})(),'np':np,'backend':None}; exec(compile(ast.Module(body=[node],type_ignores=[]),p,'exec'),ns); R=ns['Repeat']; X=lambda shape:type('X',(),{'shape':shape,'dtype':'float32'})(); assert R([784]).compute_output_spec(X((64,10,1,1))).shape==(501760,); assert R((2,)).compute_output_spec(X((2,3))).shape==(12,); assert R([1,2,3,4,5,6]).compute_output_spec(X((2,3))).shape==(21,); assert R([784]).compute_output_spec(X((None,10,1,1))).shape==(None,); print('Repeat symbolic shape checks passed')\"",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git status --short",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- I want to execute the actual Repeat class shape-inference method in isolation despite the missing test dependency, covering the reported singleton-list case plus tuple, per-element, and dynamic-shape edge cases, then confirm only the intended production file is modified."
}
```
Output:
```
I ran all provided commands and below are the outcomes for each command with their status. Please analyze each output carefully and run the commands again for which you see errors to get their output by correcting the command and other parameters.

=== EXECUTION SUMMARY ===
Total Commands: 2
Number of Successful Commands: 2
Number of Failed Commands: 0
Number of Timed Out Commands: 0
========================

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 1 of 2                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk python -c "import ast, numpy as np; p='"'"'keras/src/ops/numpy.py'"'"'; tree=ast.parse(open(p).read(), p); node=next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name=='"'"'Repeat'"'"'); ns={'"'"'Operation'"'"':type('"'"'Operation'"'"',(),{}),'"'"'KerasTensor'"'"':lambda shape,dtype=None:type('"'"'Spec'"'"',(),{'"'"'shape'"'"':tuple(shape),'"'"'dtype'"'"':dtype})(),'"'"'np'"'"':np,'"'"'backend'"'"':None}; exec(compile(ast.Module(body=[node],type_ignores=[]),p,'"'"'exec'"'"'),ns); R=ns['"'"'Repeat'"'"']; X=lambda shape:type('"'"'X'"'"',(),{'"'"'shape'"'"':shape,'"'"'dtype'"'"':'"'"'float32'"'"'})(); assert R([784]).compute_output_spec(X((64,10,1,1))).shape==(501760,); assert R((2,)).compute_output_spec(X((2,3))).shape==(12,); assert R([1,2,3,4,5,6]).compute_output_spec(X((2,3))).shape==(21,); assert R([784]).compute_output_spec(X((None,10,1,1))).shape==(None,); print('"'"'Repeat symbolic shape checks passed'"'"')"'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
Repeat symbolic shape checks passed
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 2 of 2                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git status --short'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
M keras/src/ops/numpy.py__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

```

12. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --no-compact -- keras/src/ops/numpy.py > /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/swe-results/keras-team__keras-19826.patch",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826",
      "profileName": "zsh",
      "readTerminalFullOutput": false,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- I want to generate the required benchmark patch artifact from the complete git diff of the sole modified production file at the exact requested results path."
}
```
Output:
```
I ran all provided commands and below are the outcomes for each command with their status. Please analyze each output carefully and run the commands again for which you see errors to get their output by correcting the command and other parameters.

=== EXECUTION SUMMARY ===
Total Commands: 1
Number of Successful Commands: 1
Number of Failed Commands: 0
Number of Timed Out Commands: 0
========================

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 1 of 1                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --no-compact -- keras/src/ops/numpy.py > /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/swe-results/keras-team__keras-19826.patch'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Output (last 1 lines, 18 chars) ---
__CMD_FINISHED__ 0
--- End of Output ---
═════════════════════════════════════════════════════════════════════════

```

13. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk python -c \"from pathlib import Path; import re, subprocess; patch=Path('/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/swe-results/keras-team__keras-19826.patch'); data=patch.read_bytes(); expected=subprocess.check_output(['git','--no-pager','diff','--','keras/src/ops/numpy.py']); assert data==expected, 'patch differs from git diff'; assert data.endswith(b'\\n'), 'patch lacks final newline'; paths=re.findall(rb'^diff --git a/(.+?) b/(.+?)$', data, re.M); assert paths==[(b'keras/src/ops/numpy.py',b'keras/src/ops/numpy.py')], paths; assert not any(re.search(rb'(^|/)(tests?|testing|test_artifacts?)(/|$)|(_test|\\.test|\\.spec)\\.', p[0], re.I) for p in paths), paths; print(f'Validated patch: {len(data)} bytes; production paths: {[p[0].decode() for p in paths]}')\"",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git apply --check --reverse /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/swe-results/keras-team__keras-19826.patch",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk cat /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/swe-results/keras-team__keras-19826.patch",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/keras-team__keras-19826",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- I want to verify the generated artifact exactly matches the current git diff, contains only the intended production file and no test files or artifacts, has valid patch structure, and can be reverse-applied cleanly to the modified tree."
}
```
Output:
```
I ran all provided commands and below are the outcomes for each command with their status. Please analyze each output carefully and run the commands again for which you see errors to get their output by correcting the command and other parameters.

=== EXECUTION SUMMARY ===
Total Commands: 3
Number of Successful Commands: 3
Number of Failed Commands: 0
Number of Timed Out Commands: 0
========================

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 1 of 3                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk python -c "from pathlib import Path; import re, subprocess; patch=Path('"'"'/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/swe-results/keras-team__keras-19826.patch'"'"'); data=patch.read_bytes(); expected=subprocess.check_output(['"'"'git'"'"','"'"'--no-pager'"'"','"'"'diff'"'"','"'"'--'"'"','"'"'keras/src/ops/numpy.py'"'"']); assert data==expected, '"'"'patch differs from git diff'"'"'; assert data.endswith(b'"'"'\n'"'"'), '"'"'patch lacks final newline'"'"'; paths=re.findall(rb'"'"'^diff --git a/(.+?) b/(.+?)$'"'"', data, re.M); assert paths==[(b'"'"'keras/src/ops/numpy.py'"'"',b'"'"'keras/src/ops/numpy.py'"'"')], paths; assert not any(re.search(rb'"'"'(^|/)(tests?|testing|test_artifacts?)(/|$)|(_test|\.test|\.spec)\.'"'"', p[0], re.I) for p in paths), paths; print(f'"'"'Validated patch: {len(data)} bytes; production paths: {[p[0].decode() for p in paths]}'"'"')"'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
Validated patch: 608 bytes; production paths: ['keras/src/ops/numpy.py']
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 2 of 3                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git apply --check --reverse /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/swe-results/keras-team__keras-19826.patch'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 3 of 3                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk cat /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/swe-results/keras-team__keras-19826.patch'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
diff --git a/keras/src/ops/numpy.py b/keras/src/ops/numpy.py
index e8289ee..4d9d41e 100644
--- a/keras/src/ops/numpy.py
+++ b/keras/src/ops/numpy.py
@@ -4352,6 +4352,8 @@ class Repeat(Operation):
             x_flatten_size = int(np.prod(x_shape))
             if isinstance(self.repeats, int):
                 output_shape = [x_flatten_size * self.repeats]
+            elif len(self.repeats) == 1:
+                output_shape = [x_flatten_size * self.repeats[0]]
             else:
                 output_shape = [int(np.sum(self.repeats))]
             return KerasTensor(output_shape, dtype=x.dtype)
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

```

14. **Tool call: add_agent_memory**
Input:
```json
{
  "memories": [
    {
      "content": "Keras Repeat symbolic shape inference must multiply flattened size by a singleton sequence repeat count because backend repeat broadcasts that count to every element.",
      "scope": "workspace"
    }
  ],
  "toolPurpose": "- I want to preserve the project-specific repeat shape-inference rule discovered in this fix so future work in this Keras workspace maintains backend-compatible singleton-sequence semantics."
}
```
Output:
```
Processed 1 memory item(s): 1 stored, 0 skipped (duplicates), 0 failed.
```

## Final Response

## Fix

Updated symbolic shape inference for `keras.ops.repeat` when:

- `axis=None`
- `repeats` is a singleton sequence such as `[784]`

The repeat count is now broadcast across all flattened input elements, producing the expected shape `(501760,)`.

## 📝 Files Modified

- [numpy.py](keras/src/ops/numpy.py) — Corrected `Repeat.compute_output_spec()` singleton-repeat handling. **+2 −0 lines**

## Validation

- Python compilation: passed
- Symbolic shape checks: passed, including reported case and dynamic-shape edge case
- Git diff validation: passed
- Focused pytest: blocked by missing environment dependency `absl`
- Patch integrity and reverse-apply check: passed
- Confirmed patch contains only the production file above—no tests or test artifacts

## Patch Artifact

Created at:

`/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env2/swe-results/keras-team__keras-19826.patch`

---
