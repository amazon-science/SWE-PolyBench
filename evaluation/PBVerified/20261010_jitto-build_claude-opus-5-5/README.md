# JamLabs Jitto Build (claude-opus-5-5) on SWE-PolyBench Verified

**293/382 resolved (76.70%)**, graded by the SWE-PolyBench evaluator (amazon-science/SWE-PolyBench @ 9c836c5) over
all 382 Verified instances. Per language (Java / JavaScript / TypeScript / Python): 53/69, 67/100,
76/100, 97/113. **Please read DISCLOSURES below before relying on the number.**

## System
- Agent: Claude Code (CLI 2.1.280) driving `claude-opus-5-5` (effort high), one session per task, run by the Jitto Build
  harness (JamLabs). Tools: Bash, Read, Write, Edit, Glob, Grep. No MCP servers, no hooks, no retrieval system, no tests
  generated from gold, no selection across attempts.
- Input: the instance's `problem_statement` only, inside a SWE-agent-style instruction (shown at the top of every trajectory).
  `hints_text` is not given.
- Environment: the instance's published GHCR image. The repository is a host copy of the image's working tree with git
  history cut back to `base_commit`; the actor runs commands in the task container (`--network none`) through a one-command
  broker (`envrun`), and edits are shared with the container through a bind mount. Dependency directories stay in the image.
- Prediction: the diff of the repository against the image's own working tree at the end of the session, with each changed
  file's original line endings preserved.
- Compute: one arm64 Mac running the x86_64 images under emulation in Docker Desktop. Mean actor cost $0.35
  per task (API list price; median 0.27).

## Files
- `all_preds.jsonl`: 382 predictions (2 empty: one interrupted session and one never attempted; see below).
- `logs/`: the evaluator's `<id>_result.json` and `<id>_metrics.json` for all 382, from an independent re-grade (below).
- `trajs/<id>.md`: one per instance: the instruction, every recorded nonempty thinking block and assistant comment,
  every tool call, tool outputs (capped at 6,000 characters each), container commands, and the run record.
  Only recorded text is included; empty thinking fields cannot be reconstructed. Local machine identifiers are redacted.
- `isolation_audit.json`: git-history isolation, network fence, transcript audit.

## DISCLOSURES
1. **Near-verbatim resolved patches (memorisation check).** We compared every resolved patch with the gold patch: difflib
   ratio over the signed changed lines of non-test files, whitespace and comment-only lines removed. 129 of 294 resolved
   patches (43.9%) score >= 0.8; 102 score >= 0.9; 13 match exactly on gold patches of 16-73 changed lines.
   Many are short fixes with one natural form (about half of resolved fixes of 1-10 lines score >= 0.8), but 59 of 160
   resolved fixes of 11+ lines also do. The same metric on the public Verified entries' resolved patches: HMigBot (Opus 4.8)
   39.8%, Atlassian Rovo Dev 21.4%, Prometheus v1.2 (GPT-5) 10.9%. On the 191 instances both we and HMigBot
   resolved, our median similarity is 0.778 against 0.5. We found no leak of the fixes: no gold or
   test-patch content outside base history in any repository (`isolation_audit.json`), the gold code is absent from the
   images (checked for three exact matches), the actor had no network, and the trajectories show the fix written after reading
   the target file. Some recorded reasoning explicitly refers to an upstream fix or design without an observed fetch.
   We cannot rule out that the model has seen these public repositories' history in training. **If every
   near-verbatim resolved patch were counted as unresolved, the score would be 165/382 (43.19%).**
   Resolved rate rises with task creation year (2016-17: 16/30; 2022-24: 131/156).
2. **Evaluator environment fix.** The evaluator's Java base image cannot build as published: its Dockerfile downloads Maven
   3.9.11 from dlcdn.apache.org, which now returns 404. We built it from the evaluator's own Dockerfile with that one URL
   changed to https://archive.apache.org/dist/maven/maven-3/3.9.11/ (the same artifact). Every instance itself runs in its
   prebuilt GHCR image; the base image is only the FROM of the evaluator's local-build fallback. `--repair-native-imports`
   (the evaluator's own flag) was set.
3. **Docker memory changed during the run.** The Docker VM had 8 GiB until 2026-10-09T11:15Z and 16 GiB after. The change
   was made between tasks (in-flight tasks finished and were graded first). 299 sessions started at 8 GiB and 82 at 16 GiB;
   298 and 82, respectively, completed. The remaining 8 GiB session was interrupted, as described below.
   No task was re-run.
4. **At most one attempt per task in this full run, no re-runs.** Of 382 planned instances, 380 completed, one was interrupted and one
   never started. Each attempted instance was dispatched once. The actor never saw a grade, a test result from
   the evaluator, the gold patch, the test patch or the FAIL_TO_PASS/PASS_TO_PASS lists. One instance
   (microsoft__vscode-149380, whose image keeps the repository at /app) first failed in our staging step before any actor
   started; it was staged again with our fix and then attempted once.
   Research pilots on 12 and 40 instances preceded this pre-registered full run. Their predictions are not included in
   this submission. Two mechanical export fixes before the full run preserved byte-level diffs and original line endings.
5. **No network for the actor.** Outbound connections were denied by an OS sandbox except the model API through a local
   allow-list proxy (431 allowed tunnels, 0 refused); task containers ran with `--network none`.
   The fence was proved before the first task: allowed paths work, and each of 7 deliberately broken variants fails for its
   own reason (`isolation_audit.json`). A transcript audit flagged 21 of 381 sessions; all were reviewed and are
   listed with reasons in `isolation_audit.json` (GitHub links written as text in CHANGELOG/doc edits, the agent reading its own
   session files, listing a cache directory the sandbox denied, a `git reflog` showing only base-commit entries).
6. **Two instances failed without a complete attempt** (counted as unresolved):
   - `sveltejs__svelte-1190`: the session started and worked for 208 s; a command in the task container was killed by the
     out-of-memory killer (exit 137, 8 GiB VM) and the agent process was then terminated before it produced a result. Its
     partial patch (4,512 bytes) was preserved locally, but the re-grade exporter excluded its incomplete run state.
     Its submitted prediction is empty and scores unresolved; the partial patch was not independently re-graded.
     It was not re-run.
   - `huggingface__transformers-13989`: not attempted. Preparing its environment (a 44 GB image plus a host copy of its
     repository) exhausted the run machine's disk; the instance was recorded as failed rather than retried.
7. **Grading.** `logs/` is an independent re-grade of `all_preds.jsonl` with a fresh clone of the evaluator at 9c836c5 in a
   new environment: 293/382. Our first grading during the run gave 294/382; the two agree on 381 of 382 instances. The
   difference is apache__rocketmq-4122, whose FAIL_TO_PASS test `DLedgerMultiPathTest.multiDirsStorageTest` passed in the first
   grading and failed in the re-grade with the same patch.
