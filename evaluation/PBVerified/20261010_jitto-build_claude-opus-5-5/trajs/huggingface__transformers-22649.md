# Instance: huggingface__transformers-22649

- Final resolved (evaluator, logs/huggingface__transformers-22649_result.json): True
- Run state: DONE
- One attempt. Duration 112.0 s, turns 8, actor cost $0.20530700000000002, container commands 5
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/huggingface__transformers-22649/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-22649/repo. Consider the following issue description:

<issue_description>
`modeling_opt.py` if `previous_key_values` given and `attention_mask==None` the model throws an error.
### System Info

- `transformers` version: 4.26.1
- Platform: Linux-4.18.0-147.el8.x86_64-x86_64-with-glibc2.28
- Python version: 3.9.16
- Huggingface_hub version: 0.12.1
- PyTorch version (GPU?): 1.13.1 (False)
- Tensorflow version (GPU?): not installed (NA)
- Flax version (CPU?/GPU?/TPU?): not installed (NA)
- Jax version: not installed
- JaxLib version: not installed
- Using GPU in script?: yes
- Using distributed or parallel set-up in script?: yes

### Who can help?

@ArthurZucker @younesbelkada 

### Information

- [ ] The official example scripts
- [X] My own modified scripts

### Tasks

- [ ] An officially supported task in the `examples` folder (such as GLUE/SQuAD, ...)
- [X] My own task or dataset (give details below)

### Reproduction

## Code
1. Load opt/tokenizer
```py
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "facebook/opt-125m"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer  = AutoTokenizer.from_pretrained(model_name)
```
2. Precompute `past_key_values`
```py
text1 = "let's find a"
tokenized1 = tokenizer(text1, return_tensors='pt')
past_key_values = model(**tokenized1, use_cache=True)["past_key_values"]
```
4. Compute another set of values without `attention_mask`
```py
text2 = "bug"
tokenized2 = tokenizer(text2, return_tensors='pt')
model(input_ids=tokenized2["input_ids"], past_key_values=past_key_values)
# error! The mistakenly created an attention_mask that is too small.
```
(try `distilgpt2` and it will work)

## stack trace

```
Traceback (most recent call last):
  File "/home/gkressi1/opt/ldet/rate_in-context.py", line 334, in <module>
    main()
  File "/home/gkressi1/opt/ldet/rate_in-context.py", line 325, in main
    output_config = compute_surprisals(config=config, model_object=model_object)
  File "/home/gkressi1/opt/ldet/rate_in-context.py", line 219, in compute_surprisals
    output_rating = model_object.incontext(config, prompt_list)
  File "/home/gkressi1/opt/ldet/src/model_objects/model_hf_causal_lm_big.py", line 85, in incontext
    output = self.get_model_output(rest_prompt, use_cache=True)
  File "/home/gkressi1/opt/ldet/src/model_objects/model_hf_causal_lm_big.py", line 63, in get_model_output
    output = self.model(
  File "/home/gkressi1/.conda/envs/llm/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "/home/gkressi1/.conda/envs/llm/lib/python3.9/site-packages/accelerate/hooks.py", line 158, in new_forward
    output = old_forward(*args, **kwargs)
  File "/home/gkressi1/.conda/envs/llm/lib/python3.9/site-packages/transformers/models/opt/modeling_opt.py", line 932, in forward
    outputs = self.model.decoder(
  File "/home/gkressi1/.conda/envs/llm/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "/home/gkressi1/.conda/envs/llm/lib/python3.9/site-packages/transformers/models/opt/modeling_opt.py", line 639, in forward
    attention_mask = self._prepare_decoder_attention_mask(
  File "/home/gkressi1/.conda/envs/llm/lib/python3.9/site-packages/transformers/models/opt/modeling_opt.py", line 546, in _prepare_decoder_attention_mask
    expanded_attn_mask if combined_attention_mask is None else expanded_attn_mask + combined_attention_mask
RuntimeError: The size of tensor a (93) must match the size of tensor b (1679) at non-singleton dimension 3
```

### Expected behavior

The model should create the attention mask by itself and not throw an error.

From the surface, this seems to be an easy fix:
1. Delete line [635](https://github.com/huggingface/transformers/blob/ae54e3c3b18bac0832ad62ea9b896dfd52a09850/src/transformers/models/opt/modeling_opt.py#L635) and [636](https://github.com/huggingface/transformers/blob/ae54e3c3b18bac0832ad62ea9b896dfd52a09850/src/transformers/models/opt/modeling_opt.py#L635)
2. Move line [639-642](https://github.com/huggingface/transformers/blob/ae54e3c3b18bac0832ad62ea9b896dfd52a09850/src/transformers/models/opt/modeling_opt.py#L639) of what is currently line [637](https://github.com/huggingface/transformers/blob/ae54e3c3b18bac0832ad62ea9b896dfd52a09850/src/transformers/models/opt/modeling_opt.py#L637)
3. Check TF/Flax models (?).

All the best!

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-22649/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-22649/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-22649/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-22649/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -n "attention_mask is None\|torch.ones(\|past_key_values_length\|mask_seq_length" src/transformers/models/opt/modeling_opt.py src/transformers/models/opt/modeling_tf_opt.py src/transformers/models/opt/modeling_flax_opt.py
```

tool result:

```
src/transformers/models/opt/modeling_opt.py:69:    input_ids_shape: torch.Size, dtype: torch.dtype, device: torch.device, past_key_values_length: int = 0
src/transformers/models/opt/modeling_opt.py:80:    if past_key_values_length > 0:
src/transformers/models/opt/modeling_opt.py:81:        mask = torch.cat([torch.zeros(tgt_len, past_key_values_length, dtype=dtype, device=device), mask], dim=-1)
src/transformers/models/opt/modeling_opt.py:82:    return mask[None, None, :, :].expand(bsz, 1, tgt_len, tgt_len + past_key_values_length)
src/transformers/models/opt/modeling_opt.py:110:    def forward(self, attention_mask: torch.LongTensor, past_key_values_length: int = 0):
src/transformers/models/opt/modeling_opt.py:117:        # cut positions if `past_key_values_length` is > 0
src/transformers/models/opt/modeling_opt.py:118:        positions = positions[:, past_key_values_length:]
src/transformers/models/opt/modeling_opt.py:533:    def _prepare_decoder_attention_mask(self, attention_mask, input_shape, inputs_embeds, past_key_values_length):
src/transformers/models/opt/modeling_opt.py:542:                past_key_values_length=past_key_values_length,
src/transformers/models/opt/modeling_opt.py:551:                expanded_attn_mask if combined_attention_mask is None else expanded_attn_mask + combined_attention_mask
src/transformers/models/opt/modeling_opt.py:634:        past_key_values_length = past_key_values[0][0].shape[2] if past_key_values is not None else 0
src/transformers/models/opt/modeling_opt.py:640:        if attention_mask is None:
src/transformers/models/opt/modeling_opt.py:641:            attention_mask = torch.ones(inputs_embeds.shape[:2], dtype=torch.bool, device=inputs_embeds.device)
src/transformers/models/opt/modeling_opt.py:642:        pos_embeds = self.embed_positions(attention_mask, past_key_values_length)
src/transformers/models/opt/modeling_opt.py:645:            attention_mask, input_shape, inputs_embeds, past_key_values_length
src/transformers/models/opt/modeling_tf_opt.py:62:def _make_causal_mask(input_ids_shape: tf.TensorShape, past_key_values_length: int = 0):
src/transformers/models/opt/modeling_tf_opt.py:73:    if past_key_values_length > 0:
src/transformers/models/opt/modeling_tf_opt.py:74:        mask = tf.concat([tf.zeros((tgt_len, past_key_values_length)), mask], axis=-1)
src/transformers/models/opt/modeling_tf_opt.py:104:    def call(self, attention_mask, past_key_values_length: int = 0):
src/transformers/models/opt/modeling_tf_opt.py:111:        # cut positions if `past_key_values_length` is > 0
src/transformers/models/opt/modeling_tf_opt.py:112:        positions = positions[:, past_key_values_length:]
src/transformers/models/opt/modeling_tf_opt.py:536:    def _prepare_decoder_attention_mask(self, attention_mask, input_shape, past_key_values_length):
src/transformers/models/opt/modeling_tf_opt.py:541:            combined_attention_mask = _make_causal_mask(input_shape, past_key_values_length=past_key_values_length)
src/transformers/models/opt/modeling_tf_opt.py:544:                tf.ones((input_shape[0], input_shape[1] + past_key_values_length)), tgt_len=input_shape[-1]
src/transformers/models/opt/modeling_tf_opt.py:631:        past_key_values_length = shape_list(past_key_values[0][0])[2] if past_key_values is not None else 0
src/transformers/models/opt/modeling_tf_opt.py:646:        if attention_mask is None:
src/transformers/models/opt/modeling_tf_opt.py:649:        pos_embeds = self.embed_positions(attention_mask, past_key_values_length)
src/transformers/models/opt/modeling_tf_opt.py:651:        attention_mask = self._prepare_decoder_attention_mask(attention_mask, input_shape, past_key_values_length)
src/transformers/models/opt/modeling_flax_opt.py:602:        if attention_mask is None:
```

**tool call: Bash**

```bash
sed -n 530,560p src/transformers/models/opt/modeling_opt.py; sed -n 625,660p src/transformers/models/opt/modeling_opt.py; sed -n 530,560p src/transformers/models/opt/modeling_tf_opt.py; sed -n 625,655p src/transformers/models/opt/modeling_tf_opt.py
```

tool result:

```
        self.embed_tokens = value

    # Copied from transformers.models.bart.modeling_bart.BartDecoder._prepare_decoder_attention_mask
    def _prepare_decoder_attention_mask(self, attention_mask, input_shape, inputs_embeds, past_key_values_length):
        # create causal mask
        # [bsz, seq_len] -> [bsz, 1, tgt_seq_len, src_seq_len]
        combined_attention_mask = None
        if input_shape[-1] > 1:
            combined_attention_mask = _make_causal_mask(
                input_shape,
                inputs_embeds.dtype,
                device=inputs_embeds.device,
                past_key_values_length=past_key_values_length,
            )

        if attention_mask is not None:
            # [bsz, seq_len] -> [bsz, 1, tgt_seq_len, src_seq_len]
            expanded_attn_mask = _expand_mask(attention_mask, inputs_embeds.dtype, tgt_len=input_shape[-1]).to(
                inputs_embeds.device
            )
            combined_attention_mask = (
                expanded_attn_mask if combined_attention_mask is None else expanded_attn_mask + combined_attention_mask
            )

        return combined_attention_mask

    def forward(
        self,
        input_ids: torch.LongTensor = None,
        attention_mask: Optional[torch.Tensor] = None,
        head_mask: Optional[torch.Tensor] = None,
            raise ValueError("You cannot specify both decoder_input_ids and decoder_inputs_embeds at the same time")
        elif input_ids is not None:
            input_shape = input_ids.size()
            input_ids = input_ids.view(-1, input_shape[-1])
        elif inputs_embeds is not None:
            input_shape = inputs_embeds.size()[:-1]
        else:
            raise ValueError("You have to specify either decoder_input_ids or decoder_inputs_embeds")

        past_key_values_length = past_key_values[0][0].shape[2] if past_key_values is not None else 0

        if inputs_embeds is None:
            inputs_embeds = self.embed_tokens(input_ids)

        # embed positions
        if attention_mask is None:
            attention_mask = torch.ones(inputs_embeds.shape[:2], dtype=torch.bool, device=inputs_embeds.device)
        pos_embeds = self.embed_positions(attention_mask, past_key_values_length)

        attention_mask = self._prepare_decoder_attention_mask(
            attention_mask, input_shape, inputs_embeds, past_key_values_length
        )

        if self.project_in is not None:
            inputs_embeds = self.project_in(inputs_embeds)

        hidden_states = inputs_embeds + pos_embeds

        if self.gradient_checkpointing and self.training:
            if use_cache:
                logger.warning_once(
                    "`use_cache=True` is incompatible with gradient checkpointing. Setting `use_cache=False`..."
                )
                use_cache = False

        # decoder layers
        self.embed_tokens.vocab_size = new_embeddings.shape[0]
        self.embed_tokens.weight = new_embeddings

    def get_input_embeddings(self):
        return self.embed_tokens

    def _prepare_decoder_attention_mask(self, attention_mask, input_shape, past_key_values_length):
        # create causal mask
        # # [bsz, seq_len] -> [bsz, 1, tgt_seq_len, src_seq_len]
        combined_attention_mask = None
        if input_shape[-1] > 1:
            combined_attention_mask = _make_causal_mask(input_shape, past_key_values_length=past_key_values_length)
        else:
            combined_attention_mask = _expand_mask(
                tf.ones((input_shape[0], input_shape[1] + past_key_values_length)), tgt_len=input_shape[-1]
            )

        if attention_mask is not None:
            combined_attention_mask = combined_attention_mask + _expand_mask(attention_mask, tgt_len=input_shape[-1])

        return combined_attention_mask

    @unpack_inputs
    def call(
        self,
        input_ids: Optional[TFModelInputType] = None,
        inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None,
        attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None,
        head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None,
        past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None,
        use_cache: Optional[bool] = None,
            input_shape = shape_list(input_ids)
        elif inputs_embeds is not None:
            input_shape = shape_list(inputs_embeds)[:-1]
        else:
            raise ValueError("You have to specify either decoder_input_ids or decoder_inputs_embeds")

        past_key_values_length = shape_list(past_key_values[0][0])[2] if past_key_values is not None else 0

        if inputs_embeds is None:
            # Note: tf.gather, on which the embedding layer is based, won't check positive out of bound
            # indices on GPU, returning zeros instead. This is a dangerous silent behavior.
            tf.debugging.assert_less(
                input_ids,
                tf.cast(self.embed_tokens.vocab_size, dtype=input_ids.dtype),
                message=(
                    "input_ids must be smaller than the embedding layer's input dimension (got"
                    f" {tf.math.reduce_max(input_ids)} >= {self.embed_tokens.vocab_size})"
                ),
            )
            inputs_embeds = self.embed_tokens(input_ids)

        if attention_mask is None:
            attention_mask = tf.ones(inputs_embeds.shape[:2], dtype=tf.bool)

        pos_embeds = self.embed_positions(attention_mask, past_key_values_length)

        attention_mask = self._prepare_decoder_attention_mask(attention_mask, input_shape, past_key_values_length)

        if self.project_in is not None:
            inputs_embeds = self.project_in(inputs_embeds)
```

**assistant:** Reproducing first with a tiny random OPT model (no network access):

**tool call: Bash**

```bash
cat > repro_opt.py <<'EOF'
import torch
from transformers import OPTConfig, OPTForCausalLM
torch.manual_seed(0)
cfg = OPTConfig(vocab_size=99, hidden_size=16, num_hidden_layers=2, ffn_dim=32, num_attention_heads=4, max_position_embeddings=64, word_embed_proj_dim=16)
m = OPTForCausalLM(cfg).eval()
ids = torch.randint(3, 99, (2, 5)); ids2 = torch.randint(3, 99, (2, 3))
pkv = m(ids, use_cache=True).past_key_values
out = m(input_ids=ids2, past_key_values=pkv).logits
full = m(torch.cat([ids, ids2], 1)).logits[:, -3:]
print("match:", torch.allclose(out, full, atol=1e-5))
EOF
/work/huggingface__transformers-22649/bin/envrun 'python repro_opt.py 2>&1 | tail -3'
```

tool result:

```
  File "/testbed/src/transformers/models/opt/modeling_opt.py", line 551, in _prepare_decoder_attention_mask
    expanded_attn_mask if combined_attention_mask is None else expanded_attn_mask + combined_attention_mask
RuntimeError: The size of tensor a (3) must match the size of tensor b (8) at non-singleton dimension 3
```

**assistant:** Reproduced. Now the fix in PyTorch and TF (Flax already builds its mask differently):

**tool call: Bash**

```bash
python3 - <<'EOF'
p='src/transformers/models/opt/modeling_opt.py'
s=open(p).read()
old='''        past_key_values_length = past_key_values[0][0].shape[2] if past_key_values is not None else 0

        if inputs_embeds is None:
            inputs_embeds = self.embed_tokens(input_ids)

        # embed positions
        if attention_mask is None:
            attention_mask = torch.ones(inputs_embeds.shape[:2], dtype=torch.bool, device=inputs_embeds.device)
'''
new='''        if inputs_embeds is None:
            inputs_embeds = self.embed_tokens(input_ids)

        batch_size, seq_length = input_shape
        past_key_values_length = past_key_values[0][0].shape[2] if past_key_values is not None else 0
        # required mask seq length can be calculated via length of past
        mask_seq_length = past_key_values_length + seq_length

        # embed positions
        if attention_mask is None:
            attention_mask = torch.ones(batch_size, mask_seq_length, device=inputs_embeds.device)
        elif attention_mask.shape[1] != mask_seq_length:
            raise ValueError(
                f"The provided attention mask has length {attention_mask.shape[1]}, but its length should be "
                f"{mask_seq_length} (sum of the lengths of current and past inputs)"
            )
'''
assert old in s; open(p,'w').write(s.replace(old,new))

p='src/transformers/models/opt/modeling_tf_opt.py'
s=open(p).read()
old='''        if attention_mask is None:
            attention_mask = tf.ones(inputs_embeds.shape[:2], dtype=tf.bool)
'''
new='''        if attention_mask is None:
            attention_mask = tf.ones((input_shape[0], input_shape[1] + past_key_values_length), dtype=tf.bool)
        else:
            tf.debugging.assert_equal(
                shape_list(attention_mask)[1],
                past_key_values_length + input_shape[1],
                message=(
                    f"The provided attention mask has length {tf.shape(attention_mask)[1]}, but its length should be "
                    f"{past_key_values_length + input_shape[1]} (sum of the lengths of current and past inputs)"
                ),
            )
'''
assert old in s; open(p,'w').write(s.replace(old,new))
EOF
/work/huggingface__transformers-22649/bin/envrun 'python repro_opt.py 2>&1 | tail -3'
```

tool result:

```
match: True
```

**assistant:** The cached output now matches the full forward pass. Next: check the TF path, `Copied from` consistency, and the OPT tests.

**tool call: Bash**

```bash
rm repro_opt.py && git status --short && /work/huggingface__transformers-22649/bin/envrun 'python utils/check_copies.py 2>&1 | tail -3; python -c "import tensorflow" 2>&1 | tail -1; python -m pytest tests/models/opt -q -x 2>&1 | tail -5'
```

tool result:

```
 M src/transformers/models/opt/modeling_opt.py
 M src/transformers/models/opt/modeling_tf_opt.py
?? Dockerfile
ModuleNotFoundError: No module named 'tensorflow'
-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED tests/models/opt/test_modeling_opt.py::OPTModelTest::test_pipeline_feature_extraction
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
1 failed, 42 passed, 63 skipped, 17 warnings in 7.98s
```

**tool call: Bash**

```bash
/work/huggingface__transformers-22649/bin/envrun 'python -m pytest tests/models/opt -q 2>&1 | grep -E "Error|FAILED|passed" | head; git stash -q; python -m pytest tests/models/opt -q 2>&1 | tail -3; git stash pop -q; git status --short'
```

tool result:

```
                Will be passed along to the Tokenizer `__init__` method.
                Will be passed to the Tokenizer `__init__` method. Can be used to set special tokens like `bos_token`,
                raise ValueError(
>           raise EnvironmentError(
E           OSError: Can't load tokenizer for 'hf-internal-testing/tiny-random-OPTModel'. If you were trying to load it from 'https://huggingface.co/models', make sure you don't have a local directory with the same name. Otherwise, make sure 'hf-internal-testing/tiny-random-OPTModel' is the correct path to a directory containing all relevant files for a GPT2Tokenizer tokenizer.
src/transformers/tokenization_utils_base.py:1795: OSError
                Will be passed along to the Tokenizer `__init__` method.
                Will be passed to the Tokenizer `__init__` method. Can be used to set special tokens like `bos_token`,
                raise ValueError(
>           raise EnvironmentError(
FAILED tests/models/opt/test_modeling_opt.py::OPTModelTest::test_torch_fx - A...
FAILED tests/models/opt/test_modeling_opt.py::OPTModelTest::test_torch_fx_output_loss
7 failed, 58 passed, 159 skipped, 29 warnings in 7.87s
 M src/transformers/models/opt/modeling_opt.py
 M src/transformers/models/opt/modeling_tf_opt.py
?? Dockerfile
```

**assistant:** Let me compare the exact failure lists with and without the fix.

**tool call: Bash**

```bash
/work/huggingface__transformers-22649/bin/envrun 'python -m pytest tests/models/opt -q -rf 2>&1 | grep ^FAILED | cut -c1-110 > /tmp/a; git stash -q; python -m pytest tests/models/opt -q -rf 2>&1 | grep ^FAILED | cut -c1-110 > /tmp/b; git stash pop -q; diff /tmp/a /tmp/b && echo SAME; cat /tmp/a'
```

tool result:

```
SAME
FAILED tests/models/opt/test_modeling_opt.py::OPTModelTest::test_pipeline_feature_extraction
FAILED tests/models/opt/test_modeling_opt.py::OPTModelTest::test_pipeline_question_answering
FAILED tests/models/opt/test_modeling_opt.py::OPTModelTest::test_pipeline_text_classification
FAILED tests/models/opt/test_modeling_opt.py::OPTModelTest::test_pipeline_text_generation
FAILED tests/models/opt/test_modeling_opt.py::OPTModelTest::test_pipeline_zero_shot
FAILED tests/models/opt/test_modeling_opt.py::OPTModelTest::test_torch_fx - A...
FAILED tests/models/opt/test_modeling_opt.py::OPTModelTest::test_torch_fx_output_loss
```

**assistant:** I fixed the bug in the PyTorch OPT model. Calling it with `past_key_values` and no `attention_mask` now works, and its output matches running the whole sequence in one go. I made the same change to the TensorFlow version, but TensorFlow isn't installed in the container, so that part hasn't been run.

**Cause:** when no mask was given, the decoder built a default mask covering only the new tokens. With a cache it has to cover the cached tokens as well, so the sizes didn't match and the model crashed.

**Changes:**
- **`src/transformers/models/opt/modeling_opt.py`**: the default mask now covers the cached tokens plus the new ones, sized from `past_key_values`. If you pass a mask of the wrong length, the model now raises a `ValueError` that names the expected length, instead of the confusing tensor-size error. Getting the length right also keeps the position numbers correct, because they are computed from the mask.
- **`src/transformers/models/opt/modeling_tf_opt.py`**: the same fix, with a `tf.debugging.assert_equal` length check.
- **Flax**: no change. It already builds its default mask a different way.

**Testing:**
- **Reproduction:** with a small random OPT model, the call from the issue failed with the same `RuntimeError`. After the fix it runs, and the cached output matches the full-sequence output (`torch.allclose`).
- **`tests/models/opt`:** 58 passed and 7 failed, and the same 7 fail without my change. Five are pipeline tests that need to download `hf-internal-testing/tiny-random-OPTModel`, which isn't possible offline. The other two, `test_torch_fx` and `test_torch_fx_output_loss`, fail with or without my change; I didn't look into why.

I deleted the reproduction script. The untracked `Dockerfile` was already there before I started.

_session end: success, turns 8, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 3.93 s: python repro_opt.py 2>&1 | tail -3
- `rc=0` 2.52 s: python repro_opt.py 2>&1 | tail -3
- `rc=0` 24.78 s: python utils/check_copies.py 2>&1 | tail -3; python -c "import tensorflow" 2>&1 | tail -1; python -m pytest tests/models/opt -q -x 2>&1 | tail -5
- `rc=0` 23.57 s: python -m pytest tests/models/opt -q 2>&1 | grep -E "Error|FAILED|passed" | head; git stash -q; python -m pytest tests/models/opt -q 2>&1 | tail -3; git stash pop -q; git status --short
- `rc=0` 22.54 s: python -m pytest tests/models/opt -q -rf 2>&1 | grep ^FAILED | cut -c1-110 > /tmp/a; git stash -q; python -m pytest tests/models/opt -q -rf 2>&1 | grep ^FAILED | cut -c1-110 > /tmp/b; git stash pop -q; diff /tmp/a /tmp/b && echo SAME; cat /tmp/a
