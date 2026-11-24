# Instance: huggingface__transformers-28115

- Final resolved (evaluator, logs/huggingface__transformers-28115_result.json): False
- Run state: DONE
- One attempt. Duration 427.4 s, turns 9, actor cost $0.2555746, container commands 4
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/huggingface__transformers-28115/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-28115/repo. Consider the following issue description:

<issue_description>
Incorrect router probability calculation
### System Info

transformers version 4.36.0

### Who can help?

 @ArthurZucker and @younesbelkada

### Information

- [X] The official example scripts
- [ ] My own modified scripts

### Tasks

- [ ] An officially supported task in the `examples` folder (such as GLUE/SQuAD, ...)
- [ ] My own task or dataset (give details below)

### Reproduction

I think load_balancing_loss_func in modeling_mixtral creates router_prob_per_group_and_expert incorrectly
https://github.com/huggingface/transformers/blob/v4.36.0/src/transformers/models/mixtral/modeling_mixtral.py#L120

Trying to multiply something batch_size * num_hidden_layers, num_experts by batch_size * num_hidden_layers, topk, 1

`torch.mean(tokens_per_group_and_expert * router_prob_per_group_and_expert.unsqueeze(-1)) * (num_experts**2)`

Correct creation of routing_weights should likely be from gate_logits, which ensures it is the correct size

`routing_weights = gate_logits.softamx(dim=-1)`

The unsqueeze(-1) is necessary with this. Also router_prob_per_group_and_expert should average over axis=-2

`router_prob_per_group_and_expert = torch.mean(routing_weights, axis=-2)`

This follows the previous implementation in modeling_switch_transformers
https://github.com/huggingface/transformers/blob/v4.36.0/src/transformers/models/switch_transformers/modeling_switch_transformers.py#L91

### Expected behavior

Something like this would fix it

```
def router_loss_func_test(gate_logits: torch.Tensor, top_k=2) -> float:
    if gate_logits is None:
        return 0

    if isinstance(gate_logits, tuple):
        # cat along the layers?
        gate_logits = torch.cat(gate_logits, dim=0) # batch_size * num_hidden_layers, sequence_length, num_experts

    num_experts = gate_logits.shape[-1]

    _, expert_indicies = torch.topk(gate_logits, top_k, dim=-1)  # this is done so you don't need to pass expert_indicies
    routing_probs = gate_logits.softmax(dim=-1) # routing probs

    if expert_indicies.dtype != torch.int64: # cast the expert indices to int64, otherwise one-hot encoding will fail
        expert_indicies = expert_indicies.to(torch.int64)

    if len(expert_indicies.shape) == 2:
        expert_indicies = expert_indicies.unsqueeze(2)

    expert_mask = torch.nn.functional.one_hot(expert_indicies, num_experts)

    # For a given token, determine if it was routed to a given expert.
    expert_mask = torch.max(expert_mask, axis=-2).values

    expert_mask = expert_mask.to(torch.float32) # cast to float32 otherwise mean will fail
    tokens_per_group_and_expert = torch.mean(expert_mask, axis=-2)

    router_prob_per_group_and_expert = torch.mean(routing_probs, axis=-2)

    loss = torch.mean(tokens_per_group_and_expert * router_prob_per_group_and_expert) * (num_experts**2)
    return loss
```

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-28115/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-28115/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-28115/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-28115/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/huggingface__transformers-28115/repo; grep -n "load_balancing_loss_func" -r src | head; sed -n 70,130p src/transformers/models/mixtral/modeling_mixtral.py
```

tool result:

```
src/transformers/models/nllb_moe/modeling_nllb_moe.py:96:def load_balancing_loss_func(router_probs: torch.Tensor, expert_indices: torch.Tensor) -> float:
src/transformers/models/nllb_moe/modeling_nllb_moe.py:1694:                encoder_aux_loss = load_balancing_loss_func(encoder_router_logits, encoder_expert_indexes)
src/transformers/models/nllb_moe/modeling_nllb_moe.py:1697:                decoder_aux_loss = load_balancing_loss_func(decoder_router_logits, decoder_expert_indexes)
src/transformers/models/mixtral/modeling_mixtral.py:76:def load_balancing_loss_func(gate_logits: torch.Tensor, num_experts: torch.Tensor = None, top_k=2) -> float:
src/transformers/models/mixtral/modeling_mixtral.py:1254:            aux_loss = load_balancing_loss_func(
src/transformers/models/switch_transformers/modeling_switch_transformers.py:91:def load_balancing_loss_func(router_probs: torch.Tensor, expert_indices: torch.Tensor) -> float:
src/transformers/models/switch_transformers/modeling_switch_transformers.py:1648:                encoder_aux_loss = load_balancing_loss_func(encoder_router_probs, encoder_expert_indexes)
src/transformers/models/switch_transformers/modeling_switch_transformers.py:1657:                decoder_aux_loss = load_balancing_loss_func(decoder_router_probs, decoder_expert_indexes)
src/transformers/models/gptsan_japanese/modeling_gptsan_japanese.py:74:# Copied from transformers.models.switch_transformers.modeling_switch_transformers.load_balancing_loss_func
src/transformers/models/gptsan_japanese/modeling_gptsan_japanese.py:75:def load_balancing_loss_func(router_probs: torch.Tensor, expert_indices: torch.Tensor) -> float:

logger = logging.get_logger(__name__)

_CONFIG_FOR_DOC = "MixtralConfig"


def load_balancing_loss_func(gate_logits: torch.Tensor, num_experts: torch.Tensor = None, top_k=2) -> float:
    r"""
    Computes auxiliary load balancing loss as in Switch Transformer - implemented in Pytorch.

    See Switch Transformer (https://arxiv.org/abs/2101.03961) for more details. This function implements the loss
    function presented in equations (4) - (6) of the paper. It aims at penalizing cases where the routing between
    experts is too unbalanced.

    Args:
        gate_logits (Union[`torch.Tensor`, Tuple[torch.Tensor]):
            Logits from the `gate`, should be a tuple of tensors. Shape: [batch_size, seqeunce_length, num_experts].
        num_experts (`int`, *optional*):
            Number of experts

    Returns:
        The auxiliary loss.
    """
    if gate_logits is None:
        return 0

    if isinstance(gate_logits, tuple):
        # cat along the layers?
        compute_device = gate_logits[0].device
        gate_logits = torch.cat([gate.to(compute_device) for gate in gate_logits], dim=0)

    routing_weights, selected_experts = torch.topk(gate_logits, top_k, dim=-1)
    routing_weights = routing_weights.softmax(dim=-1)

    # cast the expert indices to int64, otherwise one-hot encoding will fail
    if selected_experts.dtype != torch.int64:
        selected_experts = selected_experts.to(torch.int64)

    if len(selected_experts.shape) == 2:
        selected_experts = selected_experts.unsqueeze(2)

    expert_mask = torch.nn.functional.one_hot(selected_experts, num_experts)

    # For a given token, determine if it was routed to a given expert.
    expert_mask = torch.max(expert_mask, axis=-2).values

    # cast to float32 otherwise mean will fail
    expert_mask = expert_mask.to(torch.float32)
    tokens_per_group_and_expert = torch.mean(expert_mask, axis=-2)

    router_prob_per_group_and_expert = torch.mean(routing_weights, axis=-1)
    return torch.mean(tokens_per_group_and_expert * router_prob_per_group_and_expert.unsqueeze(-1)) * (num_experts**2)


# Copied from transformers.models.llama.modeling_llama._get_unpad_data
def _get_unpad_data(attention_mask):
    seqlens_in_batch = attention_mask.sum(dim=-1, dtype=torch.int32)
    indices = torch.nonzero(attention_mask.flatten(), as_tuple=False).flatten()
    max_seqlen_in_batch = seqlens_in_batch.max().item()
    cu_seqlens = F.pad(torch.cumsum(seqlens_in_batch, dim=0, dtype=torch.torch.int32), (1, 0))
    return (
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-28115/repo; grep -n "aux_loss\|load_balancing" -B3 -A12 tests/models/mixtral/test_modeling_mixtral.py | head -60; grep -n "router_logits = \|router_aux_loss_coef\|num_experts_per_tok" src/transformers/models/mixtral/modeling_mixtral.py | head
```

tool result:

```
462-        self.skipTest("Mixtral flash attention does not support right padding")
463-
464-    # Ignore copy
465:    def test_load_balancing_loss(self):
466-        r"""
467-        Let's make sure we can actually compute the loss and do a backward on it.
468-        """
469-
470-        config, input_dict = self.model_tester.prepare_config_and_inputs_for_common()
471-        config.num_labels = 3
472-        config.output_router_logits = True
473-        input_ids = input_dict["input_ids"]
474-        attention_mask = input_ids.ne(1).to(torch_device)
475-        model = MixtralForCausalLM(config)
476-        model.to(torch_device)
477-        model.eval()
478-        result = model(input_ids, attention_mask=attention_mask)
479-        self.assertEqual(result.router_logits[0].shape, (91, config.num_experts_per_tok))
480:        torch.testing.assert_close(result.aux_loss.cpu(), torch.tensor(1, dtype=torch.float32))
481-
482-
483-@require_torch
484-class MixtralIntegrationTest(unittest.TestCase):
485-    @slow
486-    @require_torch_gpu
487-    def test_small_model_logits(self):
488-        model_id = "hf-internal-testing/Mixtral-tiny"
489-        dummy_input = torch.LongTensor([[0, 1, 0], [0, 1, 0]]).to(torch_device)
490-
491-        model = MixtralForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, low_cpu_mem_usage=True).to(
492-            torch_device
705:        self.top_k = config.num_experts_per_tok
717:        router_logits = self.gate(hidden_states)
819:        hidden_states, router_logits = self.block_sparse_moe(hidden_states)
997:        output_router_logits = (
1071:        all_router_logits = () if output_router_logits else None
1144:        self.router_aux_loss_coef = config.router_aux_loss_coef
1146:        self.num_experts_per_tok = config.num_experts_per_tok
1212:        output_router_logits = (
1255:                outputs.router_logits if return_dict else outputs[-1], self.num_experts, self.num_experts_per_tok
1258:                loss += self.router_aux_loss_coef * aux_loss
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-28115/repo; grep -n "num_local_experts\|num_experts_per_tok\|router" tests/models/mixtral/test_modeling_mixtral.py | head; sed -n 1245,1262p src/transformers/models/mixtral/modeling_mixtral.py
```

tool result:

```
142:            num_experts_per_tok=2,
143:            num_local_experts=2,
472:        config.output_router_logits = True
479:        self.assertEqual(result.router_logits[0].shape, (91, config.num_experts_per_tok))
            loss_fct = CrossEntropyLoss()
            shift_logits = shift_logits.view(-1, self.config.vocab_size)
            shift_labels = shift_labels.view(-1)
            # Enable model parallelism
            shift_labels = shift_labels.to(shift_logits.device)
            loss = loss_fct(shift_logits, shift_labels)

        aux_loss = None
        if output_router_logits:
            aux_loss = load_balancing_loss_func(
                outputs.router_logits if return_dict else outputs[-1], self.num_experts, self.num_experts_per_tok
            )
            if labels is not None:
                loss += self.router_aux_loss_coef * aux_loss

        if not return_dict:
            output = (logits,) + outputs[1:]
            if output_router_logits:
```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-28115/repo; git log --oneline -1; ../bin/envrun 'python -m pytest tests/models/mixtral/test_modeling_mixtral.py -k load_balancing -q 2>&1 | tail -15'
```

tool result:

```
71d47f0ad More TF fixes (#28081)
  
    self._warn_or_fail_if_strict(f"Unknown config option: {key}\n")

<frozen importlib._bootstrap>:241
  <frozen importlib._bootstrap>:241: DeprecationWarning: builtin type SwigPyPacked has no __module__ attribute

<frozen importlib._bootstrap>:241
  <frozen importlib._bootstrap>:241: DeprecationWarning: builtin type SwigPyObject has no __module__ attribute

src/transformers/deepspeed.py:23
  /testbed/src/transformers/deepspeed.py:23: FutureWarning: transformers.deepspeed module is deprecated and will be removed in a future version. Please import deepspeed modules directly from transformers.integrations
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
1 passed, 133 deselected, 4 warnings in 4.61s
```

**assistant:** Reproducing with a real Mixtral-sized setup (8 experts, top-2) and comparing against a reference implementation of the Switch Transformer loss:

**tool call: Bash**

```bash
cd /work/huggingface__transformers-28115/repo; cat > repro_lb.py <<'EOF'
import torch
from transformers.models.mixtral.modeling_mixtral import load_balancing_loss_func
torch.manual_seed(0)
E, k = 8, 2
def ref(logits):
    p = logits.softmax(-1)
    _, sel = torch.topk(p, k, dim=-1)
    f = torch.nn.functional.one_hot(sel, E).float().sum(1).mean(0) / k  # fraction of routed assignments per expert
    P = p.mean(0)
    return E * k * torch.sum(f * P)
logits = tuple(torch.randn(50, E) for _ in range(3))
print("ours", load_balancing_loss_func(logits, E, k).item(), "ref", ref(torch.cat(logits)).item())
# perfectly balanced uniform logits -> loss should equal top_k (=k)
print("uniform-ish", load_balancing_loss_func((torch.zeros(64, E) + 1e-6*torch.randn(64,E),), E, k).item())
# collapsed routing: all tokens to experts 0,1 -> larger loss
col = torch.full((64, E), -10.); col[:, :2] = 10
print("collapsed", load_balancing_loss_func((col,), E, k).item())
EOF
../bin/envrun 'python repro_lb.py'
```

tool result:

```
ours 4.0 ref 2.0774827003479004
uniform-ish 4.0
collapsed 4.0
```

**thinking:**

```
Confirmed the loss stays constant at 4.0 regardless of routing because the softmax only uses top-k logits and averages over the wrong axis, giving no load-balancing signal. Now fixing the implementation.


```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-28115/repo; python3 - <<'EOF'
p='src/transformers/models/mixtral/modeling_mixtral.py'
s=open(p).read()
start=s.index("    if gate_logits is None:\n        return 0\n\n    if isinstance(gate_logits, tuple):\n        # cat along")
end=s.index("# Copied from transformers.models.llama.modeling_llama._get_unpad_data")
new='''    if gate_logits is None or not isinstance(gate_logits, tuple):
        return 0

    if isinstance(gate_logits, tuple):
        compute_device = gate_logits[0].device
        concatenated_gate_logits = torch.cat([layer_gate.to(compute_device) for layer_gate in gate_logits], dim=0)

    routing_weights = torch.nn.functional.softmax(concatenated_gate_logits, dim=-1)

    _, selected_experts = torch.topk(routing_weights, top_k, dim=-1)

    expert_mask = torch.nn.functional.one_hot(selected_experts, num_experts)

    # Compute the percentage of tokens routed to each experts
    tokens_per_expert = torch.mean(expert_mask.float(), dim=0)

    # Compute the average probability of routing to these experts
    router_prob_per_expert = torch.mean(routing_weights, dim=0)

    overall_loss = torch.sum(tokens_per_expert * router_prob_per_expert.unsqueeze(0))
    return overall_loss * num_experts


'''
s=s[:start]+new+s[end:]
s=s.replace("Logits from the `gate`, should be a tuple of tensors. Shape: [batch_size, seqeunce_length, num_experts].",
 "Logits from the `gate`, should be a tuple of model.config.num_hidden_layers tensors of\n            shape [batch_size X sequence_length, num_experts].")
open(p,'w').write(s)
EOF
git diff; ../bin/envrun 'python repro_lb.py'
```

tool result:

```
diff --git a/setup.py b/setup.py
index aba442ff4..c46faae79 100644
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
diff --git a/src/transformers/models/mixtral/modeling_mixtral.py b/src/transformers/models/mixtral/modeling_mixtral.py
index c07346c6d..f1cd8419c 100644
--- a/src/transformers/models/mixtral/modeling_mixtral.py
+++ b/src/transformers/models/mixtral/modeling_mixtral.py
@@ -83,42 +83,35 @@ def load_balancing_loss_func(gate_logits: torch.Tensor, num_experts: torch.Tenso
 
     Args:
         gate_logits (Union[`torch.Tensor`, Tuple[torch.Tensor]):
-            Logits from the `gate`, should be a tuple of tensors. Shape: [batch_size, seqeunce_length, num_experts].
+            Logits from the `gate`, should be a tuple of model.config.num_hidden_layers tensors of
+            shape [batch_size X sequence_length, num_experts].
         num_experts (`int`, *optional*):
             Number of experts
 
     Returns:
         The auxiliary loss.
     """
-    if gate_logits is None:
+    if gate_logits is None or not isinstance(gate_logits, tuple):
         return 0
 
     if isinstance(gate_logits, tuple):
-        # cat along the layers?
         compute_device = gate_logits[0].device
-        gate_logits = torch.cat([gate.to(compute_device) for gate in gate_logits], dim=0)
+        concatenated_gate_logits = torch.cat([layer_gate.to(compute_device) for layer_gate in gate_logits], dim=0)
 
-    routing_weights, selected_experts = torch.topk(gate_logits, top_k, dim=-1)
-    routing_weights = routing_weights.softmax(dim=-1)
+    routing_weights = torch.nn.functional.softmax(concatenated_gate_logits, dim=-1)
 
-    # cast the expert indices to int64, otherwise one-hot encoding will fail
-    if selected_experts.dtype != torch.int64:
-        selected_experts = selected_experts.to(torch.int64)
-
-    if len(selected_experts.shape) == 2:
-        selected_experts = selected_experts.unsqueeze(2)
+    _, selected_experts = torch.topk(routing_weights, top_k, dim=-1)
 
     expert_mask = torch.nn.functional.one_hot(selected_experts, num_experts)
 
-    # For a given token, determine if it was routed to a given expert.
-    expert_mask = torch.max(expert_mask, axis=-2).values
+    # Compute the percentage of tokens routed to each experts
+    tokens_per_expert = torch.mean(expert_mask.float(), dim=0)
 
-    # cast to float32 otherwise mean will fail
-    expert_mask = expert_mask.to(torch.float32)
-    tokens_per_group_and_expert = torch.mean(expert_mask, axis=-2)
+    # Compute the average probability of routing to these experts
+    router_prob_per_expert = torch.mean(routing_weights, dim=0)
 
-    router_prob_per_group_and_expert = torch.mean(routing_weights, axis=-1)
-    return torch.mean(tokens_per_group_and_expert * router_prob_per_group_and_expert.unsqueeze(-1)) * (num_experts**2)
+    overall_loss = torch.sum(tokens_per_expert * router_prob_per_expert.unsqueeze(0))
+    return overall_loss * num_experts
 
 
 # Copied from transformers.models.llama.modeling_llama._get_unpad_data
ours 2.0774827003479004 ref 2.0774827003479004
uniform-ish 2.0
collapsed 8.0
```

**thinking:**

```
The fix now matches the reference: loss is minimal when routing is balanced and rises to 8 when it collapses onto two experts. Next I'll run the Mixtral test suite and the repo consistency check.


```

**tool call: Bash**

```bash
cd /work/huggingface__transformers-28115/repo; rm repro_lb.py; ../bin/envrun 'python -m pytest tests/models/mixtral -q 2>&1 | grep -E "passed|failed|Error|assert" | tail -15; python utils/check_copies.py && echo copies-ok'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: byvafyu9p). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/8ced8970-d4e8-4205-a653-8a44e1677fa8/tasks/byvafyu9p.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /work/huggingface__transformers-28115/repo; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**tool call: Bash**

```bash
sleep 240; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/8ced8970-d4e8-4205-a653-8a44e1677fa8/tasks/byvafyu9p.output
```

tool result:

```
        self.assertEqual(result.router_logits[0].shape, (91, config.num_experts_per_tok))
>       torch.testing.assert_close(result.aux_loss.cpu(), torch.tensor(1, dtype=torch.float32))
E       AssertionError: Scalars are not close!
tests/models/mixtral/test_modeling_mixtral.py:480: AssertionError
  /testbed/tests/test_modeling_common.py:460: FutureWarning: `torch.testing.assert_allclose()` is deprecated since 1.12 and will be removed in a future release. Please use `torch.testing.assert_close()` instead. You can find detailed upgrade instructions in https://github.com/pytorch/pytorch/issues/61844.
    torch.testing.assert_allclose(init_instance.linear.bias, expected_bias, rtol=1e-3, atol=1e-4)
  /testbed/tests/test_modeling_common.py:463: FutureWarning: `torch.testing.assert_allclose()` is deprecated since 1.12 and will be removed in a future release. Please use `torch.testing.assert_close()` instead. You can find detailed upgrade instructions in https://github.com/pytorch/pytorch/issues/61844.
    torch.testing.assert_allclose(
  /usr/local/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py:632: UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. In version 2.5 we will raise an exception if use_reentrant is not passed. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
1 failed, 83 passed, 50 skipped, 22 warnings in 9.02s
copies-ok


[exited with code 0]
```

**assistant:** The fix is in place in `load_balancing_loss_func` (`src/transformers/models/mixtral/modeling_mixtral.py:76`). The Mixtral tests ran with 83 passed, 1 failed and 50 skipped. The one failure is `test_load_balancing_loss`, which still expects the old wrong value.

**What was wrong:** the code took the top-k logits first and then applied softmax to just those k values. It also averaged the probabilities over the wrong axis. Because of that, the loss came out the same no matter how tokens were routed. With 8 experts and top-2 it was always 4.0, so it never pushed the router toward balance.

**The fix**, as the issue suggests:
- Apply softmax over all experts' gate logits, then choose the top-k experts from those probabilities.
- `tokens_per_expert`: the share of tokens sent to each expert, averaged over all tokens from every layer.
- `router_prob_per_expert`: the average routing probability for each expert, over the same tokens.
- Loss = `num_experts * sum(tokens_per_expert * router_prob_per_expert)`, as in the Switch Transformer paper.

The function now returns 0 if `gate_logits` isn't a tuple of per-layer logits. I also corrected the docstring: each layer's logits have shape `[batch_size * sequence_length, num_experts]`.

**Checks (8 experts, top-2):**
- Random logits: 2.0775, the same value as a separate reference implementation (the old code gave 4.0).
- Evenly spread routing: 2.0, the lowest possible value (equal to top_k).
- All tokens sent to two experts: 8.0, so unbalanced routing now raises the loss.
- `utils/check_copies.py` passes.

**About the failing test:** it asserts `aux_loss == 1`, a value that only came from the old formula. Its config has 2 experts and top-2, so every token goes to both experts and the correct loss is exactly 2. You said you're handling the tests, so I didn't change it. The expected value there needs to become 2.

`git diff` also shows a change to `setup.py` (`av==9.2.0` → `av==10.0.0`). I didn't make that change and left it as it is. My test script has been deleted.

_session end: success, turns 9, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 11.32 s: python -m pytest tests/models/mixtral/test_modeling_mixtral.py -k load_balancing -q 2>&1 | tail -15
- `rc=0` 2.79 s: python repro_lb.py
- `rc=0` 3.06 s: python repro_lb.py
- `rc=0` 184.24 s: python -m pytest tests/models/mixtral -q 2>&1 | grep -E "passed|failed|Error|assert" | tail -15; python utils/check_copies.py && echo copies-ok
