# HMigBot

## Overview

HMigBot is a single autonomous software-engineering agent running on
Claude Opus 4.8. The agent works directly in the repository with file search,
file viewing, patch editing, shell execution, persistent scratchpad state,
task-intent routing, and automated compile/test feedback.

Feature tasks use a structured workflow that records the requested contract,
an analogous implementation, the user-visible execution path, and the intended
patch boundary before editing. A small conditional experience library provides
additional guidance for selected feature patterns.

## SWE-PolyBench Verified Result

**196/382 resolved (51.31%)**

### By Language

| Language | Resolved | Rate |
|---|---:|---:|
| Python | 70/113 | 61.95% |
| TypeScript | 53/100 | 53.00% |
| JavaScript | 43/100 | 43.00% |
| Java | 30/69 | 43.48% |

### By Task Category

| Category | Resolved | Rate |
|---|---:|---:|
| Bug Fix | 156/299 | 52.17% |
| Feature | 35/70 | 50.00% |
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

## Temporal History Isolation Correction

A trajectory audit found that the original shared clones were checked out at
each instance's `base_commit`, but their Git object databases still retained
post-`base_commit` upstream history. Five trajectories identified by the audit
as reading a non-ancestor SHA were therefore regenerated and unconditionally
replaced in this submission.

For each replacement run:

- the worktree `HEAD` exactly matched the instance `base_commit`;
- visible Git objects were limited to `base_commit` and its ancestors;
- the repository had zero remotes, zero post-base ref commits, and zero
  unreachable objects;
- `git cat-file` and `git show` returned 128 for the identified future SHA;
- network access was disabled for the agent tool environment; and
- generation-time feedback availability was unchanged: no evaluator feedback
  was added, and unavailable test tooling remained
  `SKIP: missing_executable`.

The runner aborted before the first model request unless all of the following
preflight checks passed:

```text
git rev-parse HEAD                            == base_commit
git status --porcelain --untracked-files=all == empty
git remote                                    == empty
git rev-list --all --not <base_commit>        == empty
git fsck --no-reflogs --unreachable           == no unreachable/dangling objects
git cat-file -e <known_future_sha>^{commit}   == return code 128
git show <known_future_sha>                   == return code 128
Docker tool-container network mode            == none
```

The verified values for all five cases are included in
[`temporal_history_isolation_audit.json`](temporal_history_isolation_audit.json).
The audit also records SHA256 values for each submitted patch, trajectory,
result, and metrics file so that the isolation record is bound to the artifacts
in this package. Each replacement trajectory independently records the verified
boundary summary before its first model turn.

The five new patches were frozen and evaluated once, without returning
evaluation feedback to the agent and without rerun or best-of selection.

| Instance | Original | Isolated replacement |
|---|---:|---:|
| `mui__material-ui-28190` | resolved | resolved |
| `sveltejs__svelte-3702` | resolved | failed |
| `sveltejs__svelte-6414` | failed | failed |
| `serverless__serverless-3799` | failed | failed |
| `microsoft__vscode-177084` | failed | resolved |

The five-case subtotal remains 2/5, so the temporal-isolation replacement did
not change the submission's solved count. The frozen prediction set was then
re-evaluated with the official evaluator after resolving native/model-loading
compatibility in the evaluation environment. The unchanged patch for
`langchain-ai__langchain-5450` passed its one F2P and four P2P tests, bringing
the verified result to **196/382 (51.31%)**.

## Submitted Artifacts

- `all_preds.jsonl`: final 382 predictions
- `logs/`: per-instance evaluation result and retrieval metrics
- `trajs/`: per-instance operational trajectories
- `metadata.yaml`: leaderboard metadata
- `migbot-logo.png`: leaderboard logo
- `temporal_history_isolation_audit.json`: boundary checks and artifact hashes
  for the five isolated replacement runs
