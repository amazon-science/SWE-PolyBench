# iSWE-Agent

iSWE-Agent is a multi-agent system developed by IBM Research to tackle software engineering tasks. The latest release of iSWE focuses on Java development and is built using IBM’s [Prompt Declaration Language (PDL)](https://github.com/IBM/prompt-declaration-language). The iSWE Agent currently consists of three components: the _Localization_ agent, the _Editing_ agent, and the _Patch Selector_ agent which operate in a sequential workflow. Unlike the conventional approach that relies on `bash` for code navigation and `str_replace_edit` for patch generation, iSWE introduces a **novel** methodology for both code understanding and editing.

We evaluated the performance of this development version of the iSWE Agent on the Java subset of the SWE-PolyBench Verified dataset, where it achieves 46.4%

```
Total resolved: 32/69
Total pass rate: 46.4%

Pass rate by language:
Java: 32/69 (46.4%)

Pass rate by task category:
Bug Fix: 23/48 (47.92%)
Feature: 5/14 (35.71%)
Refactoring: 4/7 (57.14%)

File retrieval metrics by language:
            file_recall  file_precision  file_f1
language
Java               0.68            0.88     0.73
```

![iSWE-Agent Overview](images/overview.png)

The iSWE Localization Agent:
- uses a traditional function-calling approach rather than native tool-calling,
- restricts LLM access to bash, preventing execution of arbitrary shell commands, and
- implements 7 custom tools built on AST analysis and static code inspection, leveraging tree_sitter and IBM's [Codellm-Devkit](https://codellm-devkit.info/) toolkit. These tools can be invoked by the LLM: get_call_chain, get_class_info, get_file_info, get_function_callers, get_inheritance_hierarchy, get_method_info, get_symbol_info.

The iSWE Editing Agent:
- enhances the diff-based merge-conflict edit format with custom tweaks to support edits across multiple locations and files,
- integrates validation checks using both linting and compilation feedback to guarantee syntax correctness before applying changes, and
- does not use Anthropic's `str_replace_edit` tool, commonly used by other agents such as (M)SWE-Agent, (M)OpenHands and (M)Agentless.

The iSWE Patch Selector Agent:
- uses the same function-calling approach and the custom tools as used by Localization agent
- performs review of the input candidates and returns one answer

Our team is preparing an arXiv paper with additional details to be released soon.

### NOTE

iSWE submission

- [x] Pass@1 submission
- [x] Does not use the comments on the original issue as input, commonly referred to as `hints_text`
- [x] No Test knowledge (`PASS_TO_PASS`, `FAIL_TO_PASS`)
- [x] No cheating allowed: Does not allow the LLM to cheat by running `git log –all`, `git show <commit_id>` etc., since `bash` access is restricted and only a limited number of tools are allowed.

The full output from the SWE-PolyBench evaluation harness is provided below:

```
Total resolved: 32/382
Total pass rate: 8.38%

Pass rate by language:
Python: 0/113 (0.0%)
JavaScript: 0/100 (0.0%)
TypeScript: 0/100 (0.0%)
Java: 32/69 (46.4%)

Pass rate by task category:
Bug Fix: 23/299 (7.7%)
Feature: 5/70 (7.1%)
Refactoring: 4/13 (30.8%)

File retrieval metrics by language:
            file_recall  file_precision  file_f1
language
Java               0.68            0.88     0.73
JavaScript         0.00            0.00     0.00
Python             0.00            0.00     0.00
TypeScript         0.00            0.00     0.00

File retrieval metrics overall:
file_recall       0.12
file_precision    0.16
file_f1           0.13
```

## Performance across other leaderboards

Earlier versions of iSWE were designed for Python, achieved competitive rankings on the [SWE-Bench Lite leaderboard](https://www.swebench.com/), and were showcased at [IBM TechXchange 2024](https://research.ibm.com/blog/ibm-swe-agents).

| Benchmark | Agent/Model | %Resolved | Date | Site |
| --- | --- | --- | --- | --- |
| SWE-Bench Verified | IBM Research Agent-101 | 26.67 | 2024-06-12 | [README](https://github.com/swe-bench/experiments/tree/main/evaluation/lite/20240612_IBM_Research_Agent101) |
| SWE-Bench Verified | IBM AI Agent SWE-1.0 (with open LLMs) | 23.67 | 2024-10-16 | [README](https://github.com/swe-bench/experiments/tree/main/evaluation/lite/20241016_IBM-SWE-1.0) |

This submission uses an identical agent to our previous submission to the [Multi-SWE-Bench Java](https://research.ibm.com/blog/ibm-software-engineering-agent-tops-the-multi-swe-bench-leaderboard-for-java) leaderboard, described here for completeness.

| Benchmark | Agent/Model | %Resolved | Date | Site |
| --- | --- | --- | --- | --- |
| Multi-SWE-Bench (Java) | iSWE-Agent | 33.59 | 2024-12-01 | [README](https://github.com/multi-swe-bench/experiments/blob/main/evaluation/java/verified/20251201_iSWE_Agent/README.md) |
