# Sapient Slingshot

## Overview

Sapient Slingshot is an autonomous software-engineering agent running on
GPT 5.6-sol. The agent works directly in the repository with writeTool, readTool, editFileTool, runTerminalCommandImplementation, findFilesConfig, grepToolConfig and getWorkspaceFilesListConfig

## SWE-PolyBench Verified Result

**185/382 resolved (48.43%)**

### Resolve Rate by Language

| Language | Resolved | Total | Resolve Rate |
| --- | ---: | ---: | ---: |
| Java | 29 | 69 | 42.0% |
| JavaScript | 41 | 100 | 41.0% |
| Python | 64 | 113 | 56.6% |
| TypeScript | 51 | 100 | 51.0% |

### Resolve Rate by Complexity

| Complexity | Resolved | Total | Resolve Rate |
| --- | ---: | ---: | ---: |
| Complexity 0 | 82 | 132 | 62.1% |
| Easy | 94 | 207 | 45.4% |
| Moderate | 9 | 41 | 22.0% |
| Hard | 0 | 2 | 0.0% |

### File Retrieval Metrics by Language

| Language | Recall | Precision | F1 |
| --- | ---: | ---: | ---: |
| Java | 0.70 | 0.90 | 0.75 |
| JavaScript | 0.65 | 0.83 | 0.69 |
| Python | 0.80 | 0.89 | 0.82 |
| TypeScript | 0.65 | 0.93 | 0.71 |

### File Retrieval Metrics Overall

| Metric | Score |
| --- | ---: |
| Recall | 0.71 |
| Precision | 0.89 |
| F1 | 0.75 |

### Node Retrieval Metrics by Language

| Language | Recall | Precision | F1 |
| --- | ---: | ---: | ---: |
| Java | 0.57 | 0.81 | 0.61 |
| JavaScript | 0.65 | 0.75 | 0.66 |
| Python | 0.65 | 0.82 | 0.68 |
| TypeScript | 0.57 | 0.69 | 0.60 |

### Node Retrieval Metrics Overall

| Metric | Score |
| --- | ---: |
| Recall | 0.62 |
| Precision | 0.77 |
| F1 | 0.64 |

### Validation

| Validation Check | Count |
| --- | ---: |
| Result files found | 382 |
| Result files included | 382 |
| Metrics files found | 380 |
| Metrics files included | 348 |
| Result instances without matching annotations | 0 |
| Metrics instances without matching annotations | 0 |
| Invalid/incomplete metrics files | 32 |

### First Invalid/Incomplete Metrics Files

| File | Validation Error |
| --- | --- |
| `mui__material-ui-17829_metrics.json` | Invalid `node_retrieval_metrics.recall` |
| `tailwindlabs__tailwindcss-550_metrics.json` | Invalid `node_retrieval_metrics.recall` |
| `mui__material-ui-23701_metrics.json` | Invalid `node_retrieval_metrics.recall` |
| `mui__material-ui-26061_metrics.json` | Invalid `node_retrieval_metrics.recall` |
| `mui__material-ui-20232_metrics.json` | Invalid `node_retrieval_metrics.recall` |
| `mui__material-ui-23229_metrics.json` | Invalid `node_retrieval_metrics.recall` |
| `sveltejs__svelte-3305_metrics.json` | Invalid `node_retrieval_metrics.recall` |
| `mui__material-ui-20657_metrics.json` | Invalid `node_retrieval_metrics.recall` |
| `mui__material-ui-38544_metrics.json` | Invalid `node_retrieval_metrics.recall` |
| `sveltejs__svelte-6458_metrics.json` | Invalid `node_retrieval_metrics.recall` |

## Evaluation Configuration

| Setting | Value |
| --- | --- |
| Model | `gpt-5.6-sol` |
| Inference | One final submitted patch per instance |
| Agent architecture | Single-agent free workflow |
| Dataset | SWE-PolyBench Verified, 382 instances |
| Languages | Java, JavaScript, Python, and TypeScript |

## Submitted Artifacts

| Artifact | Description |
| --- | --- |
| `all_preds.jsonl` | Final 382 predictions |
| `logs/` | Per-instance evaluation result and retrieval metrics |
| `trajs/` | Per-instance operational trajectories |
| `metadata.yaml` | Leaderboard metadata |
| `slingshot-logo.png` | Leaderboard logo |


