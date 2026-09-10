# Sapient Slingshot

## Overview

Sapient Slingshot is an autonomous software-engineering agent running on
GPT 5.6-sol. The agent works directly in the repository with writeTool, readTool, editFileTool, runTerminalCommandImplementation, findFilesConfig, grepToolConfig and getWorkspaceFilesListConfig


## SWE-PolyBench Verified Result

**364/382 resolved (95.29%)**

### Resolve rate by language:
| Language | Resolved | Rate |
|---|---:|---:|
| Java | 64/69 | 92.8% |
| JavaScript | 94/100 | 94.0% |
| Python | 111/113 | 98.2% |
| TypeScript | 95/100 | 95.0% |

### Resolve rate by complexity:
| Complexity | Resolved | Rate |
|---|---:|---:|
| Complexity 0 | 123/132 | 93.2% |
| Easy | 202/207 | 97.6% |
| Moderate | 37/41 | 90.2% |
| Hard | 2/2 | 100.0% |

### File retrieval metrics by language:
| language | recall | precision | f1 |
|---|---:|---:|---:|
| Java | 0.95 | 0.97 | 0.96 |
| JavaScript | 0.91 | 0.95 | 0.92 |
| Python | 0.99 | 1.00 | 1.00 |
| TypeScript | 0.94 | 0.98 | 0.95 |

### File retrieval metrics overall:
| Metrics | Rate |
|---|---:|
| recall | 0.95 |
| precision | 0.97 |
| f1 | 0.96 |

### Node retrieval metrics by language:
| language | recall | precision | f1 |
|---|---:|---:|---:|
| Java | 0.85 | 0.86 | 0.85 |
| JavaScript | 0.92 | 0.93 | 0.93 |
| Python | 0.88 | 0.90 | 0.88 |
| TypeScript | 0.65 | 0.65 | 0.65 |

### Node retrieval metrics overall:
| Metrics | Rate |
|---|---:|
| recall | 0.83 |
| precision | 0.83 |
| f1 | 0.83 |

### Validation:
- Result files found: 382
- Result files included: 382
- Metrics files found: 382
- Metrics files included: 272
- Result instances without matching annotations: 0
- Metrics instances without matching annotations: 0
- Invalid/incomplete metrics files: 110

First invalid/incomplete metrics files:
  - sveltejs__svelte-1376_metrics.json: missing node_retrieval_metrics
  - sveltejs__svelte-3403_metrics.json: missing node_retrieval_metrics
  - mui__material-ui-17829_metrics.json: invalid node_retrieval_metrics.recall
  - huggingface__transformers-13491_metrics.json: missing node_retrieval_metrics
  - huggingface__transformers-13865_metrics.json: missing node_retrieval_metrics
  - huggingface__transformers-16661_metrics.json: missing node_retrieval_metrics
  - huggingface__transformers-22649_metrics.json: missing node_retrieval_metrics
  - mui__material-ui-34158_metrics.json: missing node_retrieval_metrics
  - huggingface__transformers-19657_metrics.json: missing node_retrieval_metrics
  - trinodb__trino-2768_metrics.json: missing node_retrieval_metrics

## Evaluation Configuration

- Model: `gpt-5.6-sol`
- Inference: one final submitted patch per instance
- Agent architecture: single-agent free workflow
- Dataset: SWE-PolyBench Verified, 382 instances
- Languages: Java, JavaScript, Python, and TypeScript


## Submitted Artifacts

- `all_preds.jsonl`: final 382 predictions
- `logs/`: per-instance evaluation result and retrieval metrics
- `trajs/`: per-instance operational trajectories
- `metadata.yaml`: leaderboard metadata
- `slingshot-logo.png`: leaderboard logo
