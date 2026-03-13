# pando SWE-PolyBench Verified Submission

This folder is prepared for the `AmazonScience/SWE-PolyBench_Verified` split.

Split notes:
- This package targets the verified dataset, not the full `PB` or sampled `PB500` datasets.
- The live `AmazonScience/SWE-PolyBench_Verified` dataset page shows `382` rows in the `test` split.
- The language counts shown on that page are JavaScript `100`, TypeScript `100`, Python `113`, and Java `69`, which also sum to `382`.
- The dataset card text also mentions `394` verified instances, but that conflicts with both the displayed split size and the per-language counts. This submission therefore uses `382` as the operative verified-set size.

Model:
- `gpt-5.2-codex`

Contents:
- `all_preds.jsonl`: 382 verified-set entries
- `logs/`: 100 TypeScript evaluation result files for the verified TS subset
- `trajs/`: 100 reasoning traces for the verified TS subset
- `metadata.yaml`: leaderboard metadata

Submission composition:
- Non-empty predictions are included only for the 100 verified TypeScript tasks.
- All non-TypeScript verified tasks are present in `all_preds.jsonl` with empty patches.
- The TypeScript prediction source of truth is `vscode_ts_series_run/predictions_pbv_ts.jsonl`.
- Those 100 predictions exactly match the verified TypeScript task IDs.
- For the 7 rerun instances in `ts_pbv_retry_run/`, the retry trajectories are preferred in `trajs/`.

Layout note:
- The public SWE-PolyBench submission README documents `evaluation/PB` and `evaluation/PB500`, but does not currently document a verified-specific submission path.
- This folder uses `evaluation/PBVerified/...` to keep the verified submission separate from the full-benchmark `PB` package.

Pass rates:
- Overall verified submission rate with empty non-TypeScript patches: `12.30% (47/382)`
- TypeScript-only verified rate: `47.00% (47/100)`
- `metadata.yaml` uses the evaluated TypeScript subset rate, following the convention used by partial verified submissions already present on the `submission` branch.

Source artifacts used:
- `vscode_ts_series_run/predictions_pbv_ts.jsonl`
- `vscode_ts_series_run/eval/*_result.json`
- `vscode_ts_series_run/worker-*/logs/*.events.jsonl`
- `ts_pbv_retry_run/logs/*.events.jsonl`
