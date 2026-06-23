# MigBot

## Overview

MigBot is a single autonomous software-engineering agent running on
Claude Opus 4.8. The agent works directly in the repository with file search,
file viewing, patch editing, shell execution, persistent scratchpad state,
task-intent routing, and automated compile/test feedback.

Feature tasks use a structured workflow that records the requested contract,
an analogous implementation, the user-visible execution path, and the intended
patch boundary before editing. A small conditional experience library provides
additional guidance for selected feature patterns.

## SWE-PolyBench Verified Result

**195/382 resolved (51.05%)**

### By Language

| Language | Resolved | Rate |
|---|---:|---:|
| Python | 69/113 | 61.06% |
| TypeScript | 52/100 | 52.00% |
| JavaScript | 44/100 | 44.00% |
| Java | 30/69 | 43.48% |

### By Task Category

| Category | Resolved | Rate |
|---|---:|---:|
| Bug Fix | 156/299 | 52.17% |
| Feature | 34/70 | 48.57% |
| Refactoring | 5/13 | 38.46% |

## Evaluation Configuration

- Model: `claude-opus-4-8`
- Inference: one final submitted patch per instance
- Agent architecture: single-agent free workflow
- Dataset: SWE-PolyBench Verified, 382 instances
- Languages: Java, JavaScript, Python, and TypeScript

The full evaluation was assembled from a 70-instance Feature run and a
312-instance complementary run. Twenty-nine relay failures that produced empty
patches were retried at the infrastructure layer; the package contains exactly
one final non-empty prediction and its matching artifacts for every instance.

## Submitted Artifacts

- `all_preds.jsonl`: final 382 predictions
- `logs/`: per-instance evaluation result and retrieval metrics
- `trajs/`: per-instance operational trajectories
- `metadata.yaml`: leaderboard metadata
- `migbot-logo.png`: leaderboard logo
