# Instance: langchain-ai__langchain-4009

- Final resolved (evaluator, logs/langchain-ai__langchain-4009_result.json): True
- Run state: DONE
- One attempt. Duration 61.1 s, turns 10, actor cost $0.22347780000000003, container commands 5
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/langchain-ai__langchain-4009/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/langchain-ai__langchain-4009/repo. Consider the following issue description:

<issue_description>
LangChain openAI callback doesn't allow finetuned models
Hi all!

I have an [application](https://github.com/ur-whitelab/BO-LIFT) based on langchain.
A few months ago, I used it with fine-tuned (FT) models.
We added a token usage counter later, and I haven't tried fine-tuned models again since then.

Recently we have been interested in using (FT) models again, but the callback to expose the token usage isn't accepting the model.

Minimal code to reproduce the error:

```
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

llm = OpenAI(
        model_name=FT_MODEL,
        temperature=0.7,
        n=5,
        max_tokens=64,
    )

with get_openai_callback() as cb:
        completion_response = llm.generate(["QUERY"])
        token_usage = cb.total_tokens
```

It works fine if the model name is a basic openAI model. For instance, ```model_name="text-davinci-003"```
But when I try to use one of my FT models, I get this error:

```
Error in on_llm_end callback: Unknown model: FT_MODEL. Please provide a valid OpenAI model name.Known models are: gpt-4, gpt-4-0314, gpt-4-completion, gpt-4-0314-completion, gpt-4-32k, gpt-4-32k-0314, gpt-4-32k-completion, gpt-4-32k-0314-completion, gpt-3.5-turbo, gpt-3.5-turbo-0301, text-ada-001, ada, text-babbage-001, babbage, text-curie-001, curie, text-davinci-003, text-davinci-002, code-davinci-002
```

It works if I remove the callback and avoid token counting, but it'd be nice to have any suggestions on how to make it work.

Is there a workaround for that?

Any help is welcome!
Thanks!

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/langchain-ai__langchain-4009/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/langchain-ai__langchain-4009/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/langchain-ai__langchain-4009/bin/envrun 'git status --short && ls'
Edits you make under /work/langchain-ai__langchain-4009/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cat langchain/callbacks/openai_info.py; ls tests/unit_tests/callbacks/
```

tool result:

```
"""Callback Handler that prints to std out."""
from typing import Any, Dict, List, Optional, Union

from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction, AgentFinish, LLMResult


def get_openai_model_cost_per_1k_tokens(
    model_name: str, is_completion: bool = False
) -> float:
    model_cost_mapping = {
        "gpt-4": 0.03,
        "gpt-4-0314": 0.03,
        "gpt-4-completion": 0.06,
        "gpt-4-0314-completion": 0.06,
        "gpt-4-32k": 0.06,
        "gpt-4-32k-0314": 0.06,
        "gpt-4-32k-completion": 0.12,
        "gpt-4-32k-0314-completion": 0.12,
        "gpt-3.5-turbo": 0.002,
        "gpt-3.5-turbo-0301": 0.002,
        "text-ada-001": 0.0004,
        "ada": 0.0004,
        "text-babbage-001": 0.0005,
        "babbage": 0.0005,
        "text-curie-001": 0.002,
        "curie": 0.002,
        "text-davinci-003": 0.02,
        "text-davinci-002": 0.02,
        "code-davinci-002": 0.02,
    }

    cost = model_cost_mapping.get(
        model_name.lower()
        + ("-completion" if is_completion and model_name.startswith("gpt-4") else ""),
        None,
    )
    if cost is None:
        raise ValueError(
            f"Unknown model: {model_name}. Please provide a valid OpenAI model name."
            "Known models are: " + ", ".join(model_cost_mapping.keys())
        )

    return cost


class OpenAICallbackHandler(BaseCallbackHandler):
    """Callback Handler that tracks OpenAI info."""

    total_tokens: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    successful_requests: int = 0
    total_cost: float = 0.0

    def __repr__(self) -> str:
        return (
            f"Tokens Used: {self.total_tokens}\n"
            f"\tPrompt Tokens: {self.prompt_tokens}\n"
            f"\tCompletion Tokens: {self.completion_tokens}\n"
            f"Successful Requests: {self.successful_requests}\n"
            f"Total Cost (USD): ${self.total_cost}"
        )

    @property
    def always_verbose(self) -> bool:
        """Whether to call verbose callbacks even if verbose is False."""
        return True

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Print out the prompts."""
        pass

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Print out the token."""
        pass

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Collect token usage."""
        if response.llm_output is not None:
            self.successful_requests += 1
            if "token_usage" in response.llm_output:
                token_usage = response.llm_output["token_usage"]
                if "model_name" in response.llm_output:
                    completion_cost = get_openai_model_cost_per_1k_tokens(
                        response.llm_output["model_name"], is_completion=True
                    ) * (token_usage.get("completion_tokens", 0) / 1000)
                    prompt_cost = get_openai_model_cost_per_1k_tokens(
                        response.llm_output["model_name"]
                    ) * (token_usage.get("prompt_tokens", 0) / 1000)

                    self.total_cost += prompt_cost + completion_cost

                if "total_tokens" in token_usage:
                    self.total_tokens += token_usage["total_tokens"]
                if "prompt_tokens" in token_usage:
                    self.prompt_tokens += token_usage["prompt_tokens"]
                if "completion_tokens" in token_usage:
                    self.completion_tokens += token_usage["completion_tokens"]

    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        """Do nothing."""
        pass

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> None:
        """Print out that we are entering a chain."""
        pass

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        """Print out that we finished a chain."""
        pass

    def on_chain_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        """Do nothing."""
        pass

    def on_tool_start(
        self,
        serialized: Dict[str, Any],
        input_str: str,
        **kwargs: Any,
    ) -> None:
        """Print out the log in specified color."""
        pass

    def on_tool_end(
        self,
        output: str,
        color: Optional[str] = None,
        observation_prefix: Optional[str] = None,
        llm_prefix: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """If not the final action, print out observation."""
        pass

    def on_tool_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        """Do nothing."""
        pass

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        """Run on agent action."""
        pass

    def on_agent_finish(
        self, finish: AgentFinish, color: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Run on agent end."""
        pass

    def __copy__(self) -> "OpenAICallbackHandler":
        """Return a copy of the callback handler."""
        return self

    def __deepcopy__(self, memo: Any) -> "OpenAICallbackHandler":
        """Return a deep copy of the callback handler."""
        return self
__init__.py
fake_callback_handler.py
test_callback_manager.py
tracers
```

**tool call: Bash**

```bash
grep -rn "get_openai_model_cost_per_1k_tokens\|OpenAICallbackHandler" --include=*.py . | grep -v "^./langchain/callbacks/openai_info.py"
```

tool result:

```
(eval):1: no matches found: --include=*.py
```

**tool call: Bash**

```bash
grep -rn "get_openai_model_cost_per_1k_tokens\|OpenAICallbackHandler" --include='*.py' . | grep -v "^./langchain/callbacks/openai_info.py"
```

tool result:

```
./langchain/callbacks/__init__.py:10:from langchain.callbacks.openai_info import OpenAICallbackHandler
./langchain/callbacks/__init__.py:16:    "OpenAICallbackHandler",
./langchain/callbacks/manager.py:20:from langchain.callbacks.openai_info import OpenAICallbackHandler
./langchain/callbacks/manager.py:28:openai_callback_var: ContextVar[Optional[OpenAICallbackHandler]] = ContextVar(
./langchain/callbacks/manager.py:37:def get_openai_callback() -> Generator[OpenAICallbackHandler, None, None]:
./langchain/callbacks/manager.py:39:    cb = OpenAICallbackHandler()
./langchain/callbacks/manager.py:746:            isinstance(handler, OpenAICallbackHandler)
```

**assistant:** Reproducing first:

**tool call: Bash**

```bash
cat > /tmp/repro.py <<'EOF'
from langchain.callbacks import OpenAICallbackHandler
from langchain.schema import LLMResult
for name in ["foo-bar", "text-davinci-003", "GPT-4"]:
    h = OpenAICallbackHandler()
    h.on_llm_end(LLMResult(generations=[], llm_output={"token_usage": {"prompt_tokens": 2, "completion_tokens": 1, "total_tokens": 3}, "model_name": name}))
    print(name, h.total_tokens, h.total_cost)
EOF
cp /tmp/repro.py ./repro.py && ../bin/envrun 'python repro.py'
```

tool result:

```
Exit code 1
(eval):1: operation not permitted: /tmp/repro.py
cp: /tmp/repro.py: No such file or directory
```

**tool call: Bash**

```bash
cat > repro.py <<'EOF'
from langchain.callbacks import OpenAICallbackHandler
from langchain.schema import LLMResult
for name in ["foo-bar", "text-davinci-003", "GPT-4"]:
    h = OpenAICallbackHandler()
    h.on_llm_end(LLMResult(generations=[], llm_output={"token_usage": {"prompt_tokens": 2, "completion_tokens": 1, "total_tokens": 3}, "model_name": name}))
    print(name, h.total_tokens, h.total_cost)
EOF
../bin/envrun 'python repro.py'
```

tool result:

```
Exit code 1
Traceback (most recent call last):
  File "/testbed/repro.py", line 5, in <module>
    h.on_llm_end(LLMResult(generations=[], llm_output={"token_usage": {"prompt_tokens": 2, "completion_tokens": 1, "total_tokens": 3}, "model_name": name}))
  File "/testbed/langchain/callbacks/openai_info.py", line 87, in on_llm_end
    completion_cost = get_openai_model_cost_per_1k_tokens(
  File "/testbed/langchain/callbacks/openai_info.py", line 39, in get_openai_model_cost_per_1k_tokens
    raise ValueError(
ValueError: Unknown model: foo-bar. Please provide a valid OpenAI model name.Known models are: gpt-4, gpt-4-0314, gpt-4-completion, gpt-4-0314-completion, gpt-4-32k, gpt-4-32k-0314, gpt-4-32k-completion, gpt-4-32k-0314-completion, gpt-3.5-turbo, gpt-3.5-turbo-0301, text-ada-001, ada, text-babbage-001, babbage, text-curie-001, curie, text-davinci-003, text-davinci-002, code-davinci-002
```

**assistant:** Reproduced. Now the fix: I'll hoist the cost table to a module-level constant and only compute cost when the model is known, while still counting tokens.

**tool call: Bash**

```bash
python3 - <<'EOF'
p = "langchain/callbacks/openai_info.py"
s = open(p).read()
old_start = s.index("def get_openai_model_cost_per_1k_tokens(")
old_end = s.index("class OpenAICallbackHandler")
new = '''MODEL_COST_PER_1K_TOKENS = {
    "gpt-4": 0.03,
    "gpt-4-0314": 0.03,
    "gpt-4-completion": 0.06,
    "gpt-4-0314-completion": 0.06,
    "gpt-4-32k": 0.06,
    "gpt-4-32k-0314": 0.06,
    "gpt-4-32k-completion": 0.12,
    "gpt-4-32k-0314-completion": 0.12,
    "gpt-3.5-turbo": 0.002,
    "gpt-3.5-turbo-0301": 0.002,
    "text-ada-001": 0.0004,
    "ada": 0.0004,
    "text-babbage-001": 0.0005,
    "babbage": 0.0005,
    "text-curie-001": 0.002,
    "curie": 0.002,
    "text-davinci-003": 0.02,
    "text-davinci-002": 0.02,
    "code-davinci-002": 0.02,
}


def standardize_model_name(model_name: str, is_completion: bool = False) -> str:
    model_name = model_name.lower()
    if is_completion and model_name.startswith("gpt-4"):
        return model_name + "-completion"
    return model_name


def get_openai_model_cost_per_1k_tokens(
    model_name: str, is_completion: bool = False
) -> float:
    model_name = standardize_model_name(model_name, is_completion=is_completion)
    if model_name not in MODEL_COST_PER_1K_TOKENS:
        raise ValueError(
            f"Unknown model: {model_name}. Please provide a valid OpenAI model name."
            "Known models are: " + ", ".join(MODEL_COST_PER_1K_TOKENS.keys())
        )
    return MODEL_COST_PER_1K_TOKENS[model_name]


'''
s = s[:old_start] + new + s[old_end:]

old_body = '''                token_usage = response.llm_output["token_usage"]
                if "model_name" in response.llm_output:
                    completion_cost = get_openai_model_cost_per_1k_tokens(
                        response.llm_output["model_name"], is_completion=True
                    ) * (token_usage.get("completion_tokens", 0) / 1000)
                    prompt_cost = get_openai_model_cost_per_1k_tokens(
                        response.llm_output["model_name"]
                    ) * (token_usage.get("prompt_tokens", 0) / 1000)

                    self.total_cost += prompt_cost + completion_cost
'''
new_body = '''                token_usage = response.llm_output["token_usage"]
                model_name = response.llm_output.get("model_name")
                # Only track cost for known models (e.g. not fine-tuned models).
                if (
                    model_name
                    and standardize_model_name(model_name) in MODEL_COST_PER_1K_TOKENS
                ):
                    completion_cost = get_openai_model_cost_per_1k_tokens(
                        model_name, is_completion=True
                    ) * (token_usage.get("completion_tokens", 0) / 1000)
                    prompt_cost = get_openai_model_cost_per_1k_tokens(model_name) * (
                        token_usage.get("prompt_tokens", 0) / 1000
                    )

                    self.total_cost += prompt_cost + completion_cost
'''
assert old_body in s
s = s.replace(old_body, new_body)
open(p, "w").write(s)
EOF
../bin/envrun 'python repro.py && black --check langchain/callbacks/openai_info.py; ruff langchain/callbacks/openai_info.py; mypy langchain/callbacks/openai_info.py 2>&1 | tail -2'
```

tool result:

```
foo-bar 3 0.0
text-davinci-003 3 6.000000000000001e-05
GPT-4 3 0.00012
bash: line 1: black: command not found
bash: line 1: ruff: command not found
bash: line 1: mypy: command not found
```

**assistant:** Unknown/fine-tuned models now count tokens without raising, and known models still get costed (the GPT-4 math checks out: 2×0.03/1k + 1×0.06/1k). Now I'll run the callback tests and clean up:

**tool call: Bash**

```bash
rm repro.py; ../bin/envrun 'python -m pytest tests/unit_tests/callbacks -q 2>&1 | tail -3; git status --short'
```

tool result:

```
ERROR tests/unit_tests/callbacks/tracers/test_tracer.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
2 warnings, 1 error in 1.58s
 D .dockerignore
 M Dockerfile
 M langchain/callbacks/openai_info.py
```

**tool call: Bash**

```bash
../bin/envrun 'python -m pytest tests/unit_tests/callbacks -q 2>&1 | grep -m3 Error; python -m pytest tests/unit_tests/callbacks -q --ignore=tests/unit_tests/callbacks/tracers 2>&1 | tail -2; git stash -q && python -m pytest tests/unit_tests/callbacks/tracers -q 2>&1 | tail -1; git stash pop -q'
```

tool result:

```
ImportError while importing test module '/testbed/tests/unit_tests/callbacks/tracers/test_tracer.py'.
E   ModuleNotFoundError: No module named 'freezegun'
FAILED tests/unit_tests/callbacks/test_callback_manager.py::test_async_callback_manager_sync_handler
2 failed, 6 passed, 2 warnings in 1.20s
1 error in 0.11s
```

**assistant:** The tracer error is a missing `freezegun` module in the environment. Next I'll check whether the 2 failures happen without my change too:

**tool call: Bash**

```bash
../bin/envrun 'python -m pytest tests/unit_tests/callbacks -q --ignore=tests/unit_tests/callbacks/tracers 2>&1 | grep -E "^E |FAILED" | head -5; git stash push -q langchain/callbacks/openai_info.py && python -m pytest tests/unit_tests/callbacks -q --ignore=tests/unit_tests/callbacks/tracers 2>&1 | tail -1; git stash pop -q; git status --short'
```

tool result:

```
FAILED tests/unit_tests/callbacks/test_callback_manager.py::test_async_callback_manager
FAILED tests/unit_tests/callbacks/test_callback_manager.py::test_async_callback_manager_sync_handler
2 failed, 6 passed, 2 warnings in 1.42s
 D .dockerignore
 M Dockerfile
 M langchain/callbacks/openai_info.py
```

**assistant:** I fixed the bug: the OpenAI callback no longer crashes on fine-tuned or other unknown model names. It still counts their tokens, but leaves cost at `$0` because there's no price on file for them.

**What was wrong:** in `langchain/callbacks/openai_info.py`, the callback looked up each model's price per 1k tokens and raised `ValueError` when the model wasn't in its list. That error stopped the whole callback, so fine-tuned models got no token counts either.

**The fix:**
- I moved the price table out of the function into a module-level constant, `MODEL_COST_PER_1K_TOKENS`.
- A new helper, `standardize_model_name`, lowercases the model name and adds the `-completion` suffix for GPT-4 completion pricing.
- The callback now only adds cost when the model is in the price table. Token counts and request counts are recorded for every model.
- `get_openai_model_cost_per_1k_tokens` keeps its signature and still raises for unknown models if you call it directly.
- Side effect: the GPT-4 completion-price check is now case-insensitive. Before, a name like `GPT-4` was charged the cheaper prompt price for completion tokens.

**Checked:**
- I reproduced the original `ValueError` with the model name `foo-bar`.
- After the fix, `foo-bar` records 3 tokens and $0 cost. `text-davinci-003` and `GPT-4` still get the correct costs ($0.00006 and $0.00012).
- I deleted the reproduction script.

**Tests:** I couldn't fully run the callback tests here.
- `tests/unit_tests/callbacks`: 6 passed, 2 failed (`test_async_callback_manager` and `test_async_callback_manager_sync_handler`). Both fail the same way with my change removed, so they aren't caused by it.
- The tracer tests didn't run because the container is missing the `freezegun` package.
- `black`, `ruff` and `mypy` aren't installed in the container, so the code wasn't linted or type-checked.

`git status` also shows `.dockerignore` deleted and `Dockerfile` modified. I didn't touch either, so I left them alone.

_session end: success, turns 10, is_error False_

## Container commands (task container, no network; broker log)

- `rc=1` 2.88 s: python repro.py
- `rc=0` 1.69 s: python repro.py && black --check langchain/callbacks/openai_info.py; ruff langchain/callbacks/openai_info.py; mypy langchain/callbacks/openai_info.py 2>&1 | tail -2
- `rc=0` 2.79 s: python -m pytest tests/unit_tests/callbacks -q 2>&1 | tail -3; git status --short
- `rc=0` 4.04 s: python -m pytest tests/unit_tests/callbacks -q 2>&1 | grep -m3 Error; python -m pytest tests/unit_tests/callbacks -q --ignore=tests/unit_tests/callbacks/tracers 2>&1 | tail -2; git stash -q && python -m pytest tests/unit_tests/callbacks/tracers -q 2>&1 | tail -1; git stash pop -q
- `rc=0` 4.48 s: python -m pytest tests/unit_tests/callbacks -q --ignore=tests/unit_tests/callbacks/tracers 2>&1 | grep -E "^E |FAILED" | head -5; git stash push -q langchain/callbacks/openai_info.py && python -m pytest tests/unit_tests/callbacks -q --ignore=tests/unit_tests/callbacks/tracers 2>&1 | tail -1; git stash pop -q; git status --short
