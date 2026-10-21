# Instance: huggingface__transformers-26752
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
EncoderDecoder does not automatically create decoder_attention_mask to match decoder_input_ids
### System Info

```
- `transformers` version: 4.31.0
- Platform: Linux-4.15.0-192-generic-x86_64-with-glibc2.27
- Python version: 3.11.4
- Huggingface_hub version: 0.16.4
- Safetensors version: 0.3.1
- Accelerate version: 0.21.0
- Accelerate config:    not found
- PyTorch version (GPU?): 2.0.1+cu117 (True)
- Tensorflow version (GPU?): not installed (NA)
- Flax version (CPU?/GPU?/TPU?): not installed (NA)
- Jax version: not installed
- JaxLib version: not installed
- Using GPU in script?: yes
- Using distributed or parallel set-up in script?: no
```

### Who can help?

@ArthurZucker @NielsRogge 

### Information

- [ ] The official example scripts
- [X] My own modified scripts

### Tasks

- [ ] An officially supported task in the `examples` folder (such as GLUE/SQuAD, ...)
- [X] My own task or dataset (give details below)

### Reproduction

I'm using a pretrained BERT model to make a bert2bert model using an EncoderDecoderModel. According to the [documentation](https://huggingface.co/docs/transformers/model_doc/encoder-decoder#transformers.EncoderDecoderModel.forward.decoder_input_ids) and a deprecation warning in the [source code](https://github.com/huggingface/transformers/blob/bef02fd6b9cde975c51607fb936050ef706ff6d8/src/transformers/models/encoder_decoder/modeling_encoder_decoder.py#L42-L47), it says that you no longer need to pass in `decoder_input_ids` as they'll be automatically generated using `labels`. In the docs specifically, [it also goes on to say](https://huggingface.co/docs/transformers/model_doc/encoder-decoder#transformers.EncoderDecoderModel.forward.decoder_attention_mask) that the default behavior of `decoder_attention_mask` is to automatically generate it based on padded tokens in `decoder_input_ids`, so you don't need to pass the decoder attention mask either, as expected.

However, when trying to just pass `input_ids + attention_mask` for the encoder and `labels`, I get a warning that says something to the effect of "we strongly recommend passing an attention mask". If I explicitly pass `input_ids, attention_mask, decoder_input_ids, decoder_attention_mask, and labels`, the warning goes away. Looking at the implementation of creating the `decoder_input_ids` from `labels`, it does indeed seem to skip the generation of `decoder_attention_mask` and simply passes through the value from the arguments, in this case `None`:
https://github.com/huggingface/transformers/blob/e42587f596181396e1c4b63660abf0c736b10dae/src/transformers/models/encoder_decoder/modeling_encoder_decoder.py#L619-L637

You can recreate the warning in the notebook that Patrick made for the blog (https://colab.research.google.com/github/patrickvonplaten/notebooks/blob/master/Leveraging_Pre_trained_Checkpoints_for_Encoder_Decoder_Models.ipynb#scrollTo=yoN2q0hZUbXN&line=11&uniqifier=1). Specifically, in the `process_data_to_model_inputs` function, you can just comment out the lines which explicitly set `decoder_input_ids` and `decoder_attention_mask`.

### Expected behavior

I'd expect that if you can just pass `labels` to the forward call of EncoderDecoder and it will create `decoder_input_ids`, it would also create `decoder_attention_mask`. The fix is probably a few lines:

```python
        if (labels is not None) and (decoder_input_ids is None and decoder_inputs_embeds is None):
            decoder_input_ids = shift_tokens_right(
                labels, self.config.pad_token_id, self.config.decoder_start_token_id
            )
            if decoder_attention_mask is not None:
                raise Exception # some error for passing 1/2 of decoder input_id/attn_mask?
            decoder_attention_mask = torch.where(decoder_input_ids == self.config.pad_token_id, 0, 1)
```
````

## Operational trajectory

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "grep -n \"shift_tokens_right(\" -A4 src/transformers/models/encoder_decoder/modeling_encoder_decoder.py"
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
 "stdout": "151:def shift_tokens_right(input_ids: torch.Tensor, pad_token_id: int, decoder_start_token_id: int):\n152-    \"\"\"\n153-    Shift input ids one token to the right.\n154-    \"\"\"\n155-    shifted_input_ids = input_ids.new_zeros(input_ids.shape)\n--\n620:            decoder_input_ids = shift_tokens_right(\n621-                labels, self.config.pad_token_id, self.config.decoder_start_token_id\n622-            )\n623-\n624-        # Decode\n--\n666:        return shift_tokens_right(labels, self.config.pad_token_id, self.config.decoder_start_token_id)\n667-\n668-    def prepare_inputs_for_generation(\n669-        self, input_ids, past_key_values=None, attention_mask=None, use_cache=None, encoder_outputs=None, **kwargs\n670-    ):\n",
 "device_targets": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "src/transformers/models/encoder_decoder/modeling_encoder_decoder.py"
  ],
  "command_sha256": [
   "8af4f725f7a8dca3ff63476e75b0176457584c36e06623d30ea618af7089636b"
  ]
 },
 "duration_ms": 276
}
````

### Turn 2 — thinking

````text
I recall that upstream fixed this by auto-generating decoder_input_ids from labels when they're not provided, also deriving the decoder attention mask from the padding in those shifted labels.
````

### Turn 2 — tool call call_0002 (edit)

````json
{
 "file_path": "src/transformers/models/encoder_decoder/modeling_encoder_decoder.py",
 "old_string": "                labels, self.config.pad_token_id, self.config.decoder_start_token_id\n            )\n\n        # Decode",
 "new_string": "                labels, self.config.pad_token_id, self.config.decoder_start_token_id\n            )\n            if decoder_attention_mask is None:\n                decoder_attention_mask = decoder_input_ids.new_tensor(decoder_input_ids != self.config.pad_token_id)\n\n        # Decode"
}
````

Result:

````text
{
 "path": "src/transformers/models/encoder_decoder/modeling_encoder_decoder.py",
 "edited": true,
 "replacements": 1,
 "total_file_lines": 694,
 "total_file_size_bytes": 35967,
 "diff": "+             if decoder_attention_mask is None:\n+                 decoder_attention_mask = decoder_input_ids.new_tensor(decoder_input_ids != self.config.pad_token_id)",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "edit",
    "paths": [
     "src/transformers/models/encoder_decoder/modeling_encoder_decoder.py"
    ]
   }
  ]
 },
 "file_change": {
  "kind": "diff",
  "operation": "update",
  "path": "src/transformers/models/encoder_decoder/modeling_encoder_decoder.py",
  "patch": "+             if decoder_attention_mask is None:\n+                 decoder_attention_mask = decoder_input_ids.new_tensor(decoder_input_ids != self.config.pad_token_id)",
  "additions": 2,
  "deletions": 0,
  "truncated": false,
  "omitted_lines": 0
 }
}
````

### Turn 3 — thinking

````text
I realize using new_tensor triggers a UserWarning about copy-constructing from a tensor, so I should avoid that approach and instead compute the padding mask directly by comparing decoder_input_ids against the pad token value.
````

### Turn 3 — tool call call_0003 (exec)

````json
{
 "command": "cd /testbed && sed -i 's/decoder_attention_mask = decoder_input_ids.new_tensor(decoder_input_ids != self.config.pad_token_id)/decoder_attention_mask = (decoder_input_ids != self.config.pad_token_id).to(decoder_input_ids.dtype)/' src/transformers/models/encoder_decoder/modeling_encoder_decoder.py && git diff && python -c \"\nimport torch\nfrom transformers import EncoderDecoderModel, BertConfig, EncoderDecoderConfig\ne=BertConfig(hidden_size=32,num_hidden_layers=1,num_attention_heads=2,intermediate_size=37,vocab_size=99)\nd=BertConfig(hidden_size=32,num_hidden_layers=1,num_attention_heads=2,intermediate_size=37,vocab_size=99,is_decoder=True,add_cross_attention=True)\nc=EncoderDecoderConfig.from_encoder_decoder_configs(e,d); c.pad_token_id=0; c.decoder_start_token_id=2\nm=EncoderDecoderModel(config=c).eval()\nx=torch.tensor([[5,6,7,0]]); l=torch.tensor([[8,9,0,0]])\no=m(input_ids=x,attention_mask=(x!=0).long(),labels=l)\nfrom transformers.models.encoder_decoder.modeling_encoder_decoder import shift_tokens_right\ndi=shift_tokens_right(l,0,2)\no2=m(input_ids=x,attention_mask=(x!=0).long(),decoder_input_ids=di,decoder_attention_mask=(di!=0).long(),labels=l)\nprint(torch.allclose(o.logits,o2.logits))\n\""
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
 "stdout": "diff --git a/src/transformers/models/encoder_decoder/modeling_encoder_decoder.py b/src/transformers/models/encoder_decoder/modeling_encoder_decoder.py\nindex 3548e48c5..50e974fe3 100644\n--- a/src/transformers/models/encoder_decoder/modeling_encoder_decoder.py\n+++ b/src/transformers/models/encoder_decoder/modeling_encoder_decoder.py\n@@ -620,6 +620,8 @@ class EncoderDecoderModel(PreTrainedModel):\n             decoder_input_ids = shift_tokens_right(\n                 labels, self.config.pad_token_id, self.config.decoder_start_token_id\n             )\n+            if decoder_attention_mask is None:\n+                decoder_attention_mask = (decoder_input_ids != self.config.pad_token_id).to(decoder_input_ids.dtype)\n \n         # Decode\n         decoder_outputs = self.decoder(\nTrue\n",
 "stderr": "/testbed/src/transformers/utils/generic.py:311: FutureWarning: `torch.utils._pytree._register_pytree_node` is deprecated. Please use `torch.utils._pytree.register_pytree_node` instead.\n  torch.utils._pytree._register_pytree_node(\n/testbed/src/transformers/utils/generic.py:311: FutureWarning: `torch.utils._pytree._register_pytree_node` is deprecated. Please use `torch.utils._pytree.register_pytree_node` instead.\n  torch.utils._pytree._register_pytree_node(\n/testbed/src/transformers/models/encoder_decoder/modeling_encoder_decoder.py:644: FutureWarning: Version v4.12.0 introduces a better way to train encoder-decoder models by computing the loss inside the encoder-decoder framework rather than in the decoder itself. You may observe training discrepancies if fine-tuning a model trained with versions anterior to 4.12.0. The decoder_input_ids are now created based on the labels, no need to pass them yourself anymore.\n  warnings.warn(DEPRECATION_WARNING, FutureWarning)\n",
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 3940,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "write",
    "paths": [
     "src/transformers/models/encoder_decoder/modeling_encoder_decoder.py"
    ]
   }
  ],
  "reads": [
   "/testbed"
  ],
  "command_sha256": [
   "263f8520d5f6d624455a3a1c6911e3f915eed956666c4bc8cf099e7344833c9a"
  ]
 },
 "device_targets": []
}
````

### Turn 4 — thinking

````text
Good, that confirms the deprecation warning only triggers when decoder_input_ids is explicitly passed, so this is settled.
````

### Turn 5 — assistant text

I fixed it: when you pass only `labels`, `EncoderDecoderModel.forward` now builds a `decoder_attention_mask` along with the `decoder_input_ids` it already made by shifting the labels.

The change is two lines in `src/transformers/models/encoder_decoder/modeling_encoder_decoder.py`. Right after `shift_tokens_right` makes the decoder inputs, I added:

```python
if decoder_attention_mask is None:
    decoder_attention_mask = (decoder_input_ids != self.config.pad_token_id).to(decoder_input_ids.dtype)
```

The mask is 1 for real tokens and 0 for padding. It's only created when you haven't passed one, so a mask you supply yourself is still used as-is. I didn't add the error from the issue's sketch for when only the mask is passed, so that case keeps working the way it did before.

I checked it with a tiny randomly initialised bert2bert model. Passing only `input_ids`, `attention_mask` and `labels` gave the same logits (`torch.allclose` → `True`) as also passing the shifted `decoder_input_ids` and their padding mask by hand. I did not run the existing test suite, and I didn't look at whether the "we strongly recommend passing an attention mask" warning from the issue still appears.

### Turn 6 — assistant text

I fixed it: `EncoderDecoderModel.forward` now builds `decoder_attention_mask` itself when it creates `decoder_input_ids` from `labels`. The change is two lines in `src/transformers/models/encoder_decoder/modeling_encoder_decoder.py`:

```python
            if decoder_attention_mask is None:
                decoder_attention_mask = (decoder_input_ids != self.config.pad_token_id).to(decoder_input_ids.dtype)
```

The mask is 1 for real tokens and 0 for padding. If you pass your own `decoder_attention_mask`, it is still used unchanged.

I checked it with a small, randomly initialized bert2bert model. Passing only `input_ids`, `attention_mask` and `labels` gave the same logits as also passing the shifted `decoder_input_ids` and their padding mask. I did not run the project's test suite.

The run still printed the existing FutureWarning saying `decoder_input_ids` are now created from `labels`. That warning was already in the code, and I left it alone.

## Final answer

I fixed it: `EncoderDecoderModel.forward` now builds `decoder_attention_mask` itself when it creates `decoder_input_ids` from `labels`. The change is two lines in `src/transformers/models/encoder_decoder/modeling_encoder_decoder.py`:

```python
            if decoder_attention_mask is None:
                decoder_attention_mask = (decoder_input_ids != self.config.pad_token_id).to(decoder_input_ids.dtype)
```

The mask is 1 for real tokens and 0 for padding. If you pass your own `decoder_attention_mask`, it is still used unchanged.

I checked it with a small, randomly initialized bert2bert model. Passing only `input_ids`, `attention_mask` and `labels` gave the same logits as also passing the shifted `decoder_input_ids` and their padding mask. I did not run the project's test suite.

The run still printed the existing FutureWarning saying `decoder_input_ids` are now created from `labels`. That warning was already in the code, and I left it alone.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 75190 | 2257 | 70001 | 5175 | 77447 |
