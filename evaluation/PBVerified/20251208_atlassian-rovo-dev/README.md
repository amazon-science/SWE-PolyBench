# Atlassian Rovo Dev

[Rovo Dev](https://www.atlassian.com/rovo-dev)
is Atlassian's AI-powered software development assistant designed to boost developer productivity using
expert software development capabilities and deep integration with your organization's knowledge base, code, and task
management system. We are developing specialized agents to help our customers with coding, code review, code planning,
and build/deployment, with much more to come.

## Performance on SWE-PolyBench Verified

The current version of Rovo Dev Agent achieves 48.95% on SWE-PolyBench Verified:

```
Total resolved: 187/382
Total pass rate: 48.95%

Pass rate by language:
Python: 62/113 (54.9%)
JavaScript: 50/100 (50.0%)
TypeScript: 43/100 (43.0%)
Java: 32/69 (46.4%)

Pass rate by task category:
Bug Fix: 151/299 (50.5%)
Feature: 29/70 (41.4%)
Refactoring: 7/13 (53.8%)

File retrieval metrics by language:
            file_recall  file_precision  file_f1
language                                        
Java               0.70            0.84     0.73
JavaScript         0.66            0.76     0.67
Python             0.79            0.80     0.76
TypeScript         0.59            0.70     0.59

File retrieval metrics overall:
file_recall       0.69
file_precision    0.77
file_f1           0.69
```

## Technical Report

*This submission uses an identical agent to our previous submission to the SWE-Bench leaderboard, described here for completeness.*

The Rovo Dev Agent utilizes tool calling to navigate, plan, and resolve repo-level software development tasks.
This benchmark was achieved using a development version of Rovo Dev that includes minor differences from our production system, called out below.
Note these results represent a single agent trajectory with our production agent - no test time scaling and no repeated attempts were used.

For a detailed description of our foundational work on the Rovo Dev agent, please refer to [our paper published in ICSE 2025](https://arxiv.org/abs/2411.12924).
Since publication, we have moved to a purely agentic, rather than phased, approach, as described below.

### Tools

- View workspace / expand folder: Tools for viewing the file structure of the repo or subfolders
- Grep: A tool for searching file content across the entire repo (we use ripgrep under the hood)
- Open files: A tool that shows the agent a representation of a set of selected files. In most cases, we do not show the entirety of the file content, particularly for large files. Instead, we use a simple representation of the syntax tree based on (1) the previous actions take by the agent and (2) static analysis parsing of the code. See "Code Parsing" below.
- Inspect code: A tool for inspecting the context of specific code symbols or line ranges within a file
- Create file, delete file, find-and-replace code: Tools for code editing
- Bash: A tool for running bash commands (supports Powershell on Windows, but not relevant for SWE-PolyBench evaluation)
- Status: A tool that allows the agent to provide an indicator of the "phase" of the solution they are in (incomplete, verifying/testing, complete). This tool provides a structured way to extract reasoning from the agent on why a task is marked with a given status, and is also used to ensure that the agent run does not complete before the agent has marked the task as complete. If a trajectory is ended early (i.e., the task has not been marked as complete), the agent is re-prompted with `If you have fully completed the task, call the status function and mark it as 'complete'. Otherwise, please continue working on the task using the available functions.`

### Code Parsing

To enable more structured code retrieval, we have implemented a code parsing strategy that takes account of the agent's previous actions as well as the structure of the code.

For example, if a file is opened by the agent after the agent has called grep on certain symbols, any structural sections (e.g., methods or functions) of the code file that contained
matches in the prior grep call will be automatically shown, whereas other sections of the file will only show the syntax tree. This is achieved by breaking files down into semantically distinct sections
(such as functions, methods, and classes), checking for any relevant activity within each section and, if any is found, that section is highlighted in the tool response.

Similarly, portions of the code base that have been previously inspected or modified by the agent will be automatically highlighted when those files are opened by the agent.

These techniques enable the agent to more quickly identify relevant code without needing additional tool calls to traverse the code. Syntax trees are extracted using open source tree-sitter utilities.

### Tool Call Examples

Another simple modification made from our production system for evaluation is to initialize the agent trajectory with a single tool call example (which is always a call to the view workspace tool).
This provides useful information about the repo to the agent, and also provides a demonstration of the format/syntax that is required for tool calling, which prevents avoidable errors due to improperly formatted tool calls.

### Differences from the Rovo Dev product

The agent used for this benchmark did not have access to the internet, any of Atlassian's Jira, Confluence, or BitBucket data, or any other data outside of the repo itself. There was no human-in-the-loop assistance.
