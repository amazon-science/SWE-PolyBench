# AiWork.Code (claude-opus-5-5) — SWE-PolyBench Verified

**Organization:** Ant Digital Technologies

## Overview

A single autonomous coding agent running on Claude Opus 5.5 at high thinking effort, working
directly in the repository: file search and view, patch editing, shell execution, background
execution for long builds and tests. No multi-agent decomposition, no scratchpad handed between
runs, no task-specific routing; every instance starts from the same tool set and prompt.

### Tool scope

Nine tools were called across the 382 instances, 5123 calls in all: `exec` (2858),
`background_exec` (772), `read` (545), `rg` (440), `edit` (278),
`apply_patch` (201), `write` (20), `read_tool_result_page` (8) and
`tool_search` (1). The count is one per rendered tool-call heading, deduplicated by
tool-call id within an instance: the raw stream writes each call twice, so counting event lines
would double every number, and a global deduplication across instances merges the two re-run
instances out of the tally. That other count is 5097; the 26 calls it omits are
`coder__code-server-3277` (12 calls: `rg` 1, `exec` 8, `read` 1, `edit` 1, `background_exec` 1)
and `coder__code-server-4923` (14 calls: `exec` 9, `background_exec` 5), so 12 + 14 = 26, and per
tool the difference is `exec` +17, `background_exec` +6, `read` +1, `rg` +1, `edit` +1, which sums
to 26. Two independent counts, one by the submitting team and one by an independent reviewer,
produced the same 5123 and the same 26-call breakdown. The figures are reproducible from this
package alone:
`grep -h '^### Turn [0-9]* — tool call' trajs/*.md | wc -l` prints 5123 (`-h` is needed —
`grep -c` prints one count per file, not their sum). The agent CLI also
registers 32 deferred
tools that are not reachable directly: they can only be discovered through `tool_search`, and a
discovery result is a description, not an activation. The one return in this package named five
tools (`memory_store`, `generate_video`, `read_image`, `update_goal`, `skill_manage`). That return
is the subset matching that one query, not the whole registry: a different query returns a
different subset, and the registry holds 32 deferred tools in total. None of the five was called
in any instance. The call is in `apache__dubbo-3622` turn 39 and was looking for a web-fetch tool.
Web access is denied by configuration (`web_search`, `web_fetch`, `web_browse`, `browser` are on
the tool denylist) as well as by the proxy.

## SWE-PolyBench Verified Result

**274/382 resolved (71.73%)**

| Language | Resolved | Total | Rate | | Category | Resolved | Total | Rate |
|---|---:|---:|---:|---|---|---:|---:|---:|
| Python | 80 | 113 | 70.80% | | | Bug Fix | 217 | 299 | 72.58% |
| TypeScript | 78 | 100 | 78.00% | | | Feature | 48 | 70 | 68.57% |
| JavaScript | 67 | 100 | 67.00% | | | Refactoring | 9 | 13 | 69.23% |
| Java | 49 | 69 | 71.01% | | | | |

## Evaluation Configuration

- Model `claude-opus-5-5`, thinking effort `high`; one final submission per instance — the
  working-tree diff frozen when the agent stopped or when its 3600 s budget expired. The
  3 exceptions are the instances withdrawn after the leakage audit (below): `google__guava-3971`, `google__guava-5696`, `keras-team__keras-19915`. The
  evaluator resolved each on the patch the agent produced; that patch is not submitted, their
  `model_patch` is empty, and they count as unresolved.
- All 382 instances are the denominator. The upstream aggregator counts `total_instances` from
  `logs/`; every instance has a result file, so it recomputes exactly the `metadata.yaml` rate.
  The three instances that never started are counted as unresolved here; excluding them instead
  would give 72.30% (274/379). Both numbers are stated so a reader can see what the
  choice is worth: the difference is 0.57 percentage points. We report the first because
  the denominator is the dataset, not the subset that happened to start.
- `scoring.py`, `polybench_data.py` and `metrics/` are byte-identical to upstream `main`. Two files
  differ, only in how the judge container is obtained and limited, never in what is scored:
  `docker_utils.py` pulls the published image by pinned tag instead of rebuilding it, sets
  `HF_ENDPOINT=https://hf-mirror.com`, and limits the container to 16 GB memory, 4 CPUs, 4096
  pids; `run_evaluation.py` neither rebuilds nor deletes images. Re-aggregating the same `logs/`
  with a clean upstream tree gives a byte-identical `result.json`. A read-only Maven
  `settings.xml` (central → mirror) was mounted into the judge container only; eight Java
  instances scored before it were re-scored under it.

## Repository Isolation

Before each agent start the runner verifies inside the container that `HEAD` equals the instance
`base_commit`; that `git status --porcelain` is empty; that there are no remotes, tags, stash
entries or refs beyond `HEAD`; that `git rev-list --all --reflog --not HEAD` is empty; that the
object database holds only HEAD's ancestors; and that `git fsck --unreachable` reports nothing.
Every run uses the image's own `/testbed`, never a shared clone. **The check passed before the
agent started in all 379 instances that ran.** The three that did not run split into two
different cases: in `coder__code-server-6278` the check itself stopped the run — the image ships a
git-lfs object store inside its `.git`, the check refuses by design to clean that, and the agent
was never started; in `huggingface__transformers-13989` and `keras-team__keras-19838` the image
could not be downloaded, so the check was never reached.

The check went through four revisions during the batch — 12 / 57 / 308 / 2 instances used the
first to fourth, each the revision current when that instance started. Agent, prompt, model,
configuration and budget were identical throughout; the revisions touch isolation only, never the
submitted patch or the scoring path. What each revision changed is recorded per revision in
`repository_isolation_audit.json`. Two instances (`coder__code-server-4923`,
`coder__code-server-3277`) were refused by the third revision for a Git-LFS residue it created
itself and re-run under the fourth; each was run once and scored once.

A trajectory audit covered every finished run for git-history reads: hex identifiers passed to
`git show/log/diff/blame/checkout` resolve only to ancestors; 13 trajectories used `git log --all`,
which can only list ancestors because the object database holds nothing else. One non-ancestor SHA
appears in one trajectory — the issue's own upstream fix commit, recalled by the model in a `curl`
command the proxy blocked; that instance submitted an empty patch and is not resolved.
Per-instance pre-run values and dispositions: `repository_isolation_audit.json`.

## Coverage and Disposition

| Class | Count |
|---|---:|
| Resolved | 274 |
| Resolved by the evaluator on the agent's patch, withdrawn after the leakage audit (empty patch submitted) | 3 |
| Ran, patch evaluated, not resolved | 101 |
| Ran, produced an empty patch | 1 |
| Never ran | 3 |

All 382 instances have a line in `all_preds.jsonl`, a `logs/<id>_result.json` and a
`logs/<id>_metrics.json`, and `trajs/` holds 382 files. Three of those files are notices rather
than trajectories: they belong to the three never-ran instances listed below (the same three),
were never started, and state their reason instead of showing steps. Classes, reasons and
evidence files are per instance in `repository_isolation_audit.json`.

Never-ran instances (counted as unresolved; nothing is removed from the denominator):

- `coder__code-server-6278` — the repository-isolation check refuses, by design, to clean a repository whose Git directory holds a git-lfs object store, so the agent was not started.
- `huggingface__transformers-13989` — the evaluation image (about 44 GB) could not be downloaded: after 887 s one attempt failed its layer digest check, and a later attempt transferred 5,714,739,333 of the expected 6,380,415,475 bytes before ending with a short read. The agent was not started.
- `keras-team__keras-19838` — the evaluation image (about 9.5 GB) could not be downloaded: two attempts ended with a short read at about 8.2 GB, and a third attempt was stopped by us at 143 s to keep the queue moving. The three attempts total 5889 s, and the first two alone (5745.9 s) already exceed the per-instance limit, so the agent was not started.

For never-ran instances and for the 3 withdrawn instances the two `logs/` files come from the
upstream empty-patch path (`run_evaluation.py` lines 97-118), which returns before any container is
created; their `false` / `0.0` fields mean "not measured", not "ran and failed".

**Line endings in eight Java patches.** For `apache__dubbo-3317`, `apache__dubbo-4026`, `apache__dubbo-4678`, `apache__dubbo-5356`, `apache__dubbo-5783`, `apache__dubbo-8623`, `google__gson-2376`, `google__gson-2420`, the submitted `model_patch` differs
from the in-container diff only in line endings (container CRLF, prediction file LF). The
submitted patch is byte-identical to the scored patch in every case. The evaluator applies with
`git apply --ignore-whitespace` (fallback `patch --fuzz=5`) and all eight applied; under a strict
`git apply` these eight would not, while the in-container diff applies under both modes. We did
not re-score with the raw diff: submitted and scored bytes must be the same.

## Memorization of upstream fixes

Trajectories are published and we audited them for evidence that the model reproduced the upstream
fix. **57 of the 274 resolved instances carry direct evidence**: 52 via a line added by
the gold patch, either a comment line or any line of a documentation file (`.md`, `.rst`, `.txt`,
`.adoc`, code samples included), appearing verbatim in our `model_patch` and first
appearing in a model-authored tool call (absent from the problem statement, earlier tool output
and `base_commit`); 5 only via a pull request number that is the real merged fix, absent
from the same places. A further 13 instances show evidence but are not resolved.
Counting all 57 as unsolved gives a floor of **56.81% (217/382)**; the
reported result stays 71.73% (274/382). Dropping the 20-character minimum gives 56.02%;
restricting comment lines to eight words gives 57.85%. The withdrawn instance `google__guava-3971` had such evidence in its withdrawn patch; it is no longer resolved and is not counted, and its row says so. Code lines in source files are excluded by design — a
correct code line can be reached by reasoning. Counting code lines too would give about 198
instances; that figure comes from records that apply no 20-character minimum and do not record a
first-occurrence check, and it uses the 277 instances resolved before the withdrawals. Full criteria for both routes and per-instance records:
`memorization_audit.json`. We do not reproduce the upstream text itself.

In three trajectories (`keras-team__keras-19459`, `keras-team__keras-19915`, `keras-team__keras-20002`) the model's thinking says it is recalling the upstream fix
(first at lines 81, 995 and 1174 of their `trajs/` files). That is memory, not access to the
environment; it is not what the trajectory review of the leakage audit below counts.

## Leakage audit

Every instance was audited for four ways the fix could reach the agent other than by solving the
task. Method and result are in `repository_isolation_audit.json`: the top-level `leak_audit` key
holds the method and the totals, and every instance row holds its own `leak_audit` entry.

- **L1 — hints in the prompt.** The dataset's `hints_text` is non-empty for 269 of the 382
  instances and for 266 of the 379 that ran; the other 3 are the instances that
  never ran, which received no prompt. Each non-empty `hints_text` was searched as one string in the
  instance's task prompt: found in 0.
- **L2 — future git history.** The repository-isolation check described above passed before the
  agent started in 379 of the 379 instances that ran.
- **L3 — fetching the fix over the network.** The proxy permitted no host other than the model
  endpoint; the requests the agent made and their outcome are in the Network Egress section below.
- **L4 — the answer already in the image.** The evaluation image of each instance was pulled by the
  digest recorded at run time, scanned read-only and deleted; the scan reads the image, not the
  working tree the agent changed. 377 of the 382 instances were scanned; 2 were not,
  because the image pull failed when the scan reached them (`mui__material-ui-19072`, `mui__material-ui-19511`; not excluded, scores
  unchanged); 3 are not applicable — the three that never ran, whose submitted patch is empty,
  so they are unresolved whatever the image contains (`coder__code-server-6278`, `huggingface__transformers-13989`, `keras-team__keras-19838`). Looked for: L4a, leftover
  `*.orig` / `*.rej` / top-level `*.patch` files outside `.git` and `node_modules`; L4b, a copy of
  the project installed in the image (Python site-packages and pip, `node_modules` at any depth and
  global, `~/.m2`, `~/.gradle`) that is newer than the repository's own version at `base_commit`, or
  whose version cannot be ordered against it — a link or editable install back into the base
  worktree, or the same project at a version not newer, is not a hit; L4c, an added block of three
  or more lines of the test patch already present verbatim, or a file the test patch creates
  already existing. 52 of the 377 scanned instances have a hit (0 L4a, 34
  L4b newer, 17 L4b not orderable, 1 L4c), each in exactly one class:

| Class | Instances | Handling |
|---|---:|---|
| A newer release of the project itself in Python site-packages | 14 | trajectory audit |
| Artifacts of the project itself in the local Maven cache, whose versions cannot be ordered against the repository's own version (`HEAD-jre-SNAPSHOT`, no digits) | 2 | trajectory audit |
| A package with the name of a workspace package of the repository and a higher version; the installed copy records no repository or homepage, so it could not be shown to come from another project | 19 | trajectory audit |
| Newer releases of the project's own packages installed as dependencies in `node_modules` | 1 | trajectory audit |
| An artifact in the local Maven cache that the repository at `base_commit` declares as an external dependency at exactly the installed version (not a module of the repository, its version fixed in the build file and not the project's own; neither patch touches a build file or the artifact) | 15 | excluded; sensitivity check |
| The flagged test-patch block already occurs in the target file at `base_commit`; the image's file is byte-identical to the upstream file there | 1 | excluded; sensitivity check |

**Trajectory audit of the 36 hits that are not excluded.** The rules were fixed before any
trajectory was read. Access (A1): a tool-call argument contains the leaked path or its package
directory, or a tool output shows a file path or content line under that directory. Not access: a
recursive search that covers the directory but prints nothing from it (A2); a runtime import of the
package, unless the trajectory prints its source lines (A3). When in doubt, access (A4). An
independent reviewer judged all 36. We re-judged 5 of them, writing our judgement down
before reading the reviewer's per-instance evidence (we knew the reviewer's dispositions), and
disagreed on one: in `google__guava-3971` the agent located jars in the Maven cache by file name
and put them on the `javac` classpath; the reviewer read this as not access (A2, A3), we read it as
A4. The unfavourable side is taken. Result: 3 accessed and resolved, 1 accessed and not
resolved (`keras-team__keras-20002`, unchanged), 32 not accessed (unchanged);
3 + 1 + 32 = 36.

**Withdrawn after the leakage audit: `google__guava-3971`, `google__guava-5696`, `keras-team__keras-19915`.** The evaluator resolved each on the patch the
agent produced; that patch is not submitted. Their line in `all_preds.jsonl` carries an empty
`model_patch`, their two `logs/` files come from the upstream empty-patch path, and the reported
result counts them unresolved. The sha256 and byte length of each withdrawn patch are in the
instance's row (`leak_audit.withdrawn_patch`; the patch text is not shipped). The trajectories are
unchanged, so the edits the agent made are still in `trajs/`. Per instance, with the evidence
lines: `leak_audit.L4.trajectory_audit`.

**Sensitivity check, reported only.** The 16 excluded hits were judged with the same rules by
the same reviewer: accessed in 2 (`apache__rocketmq-7964`, resolved; `serverless__serverless-6534`, not resolved); A2 in 4 (`apache__dubbo-8623`, `apache__rocketmq-5037`, `apache__rocketmq-5062`, `apache__rocketmq-5633`); not
accessed in the other 10. A second reviewer reads the rule more strictly where a command
picks a jar out of the Maven cache by name; these 4 do not pick any jar by name. Treating
the excluded hits like the others would withdraw 1 more resolved instance and give
71.47% (273/382); the reported result does not do this.

**L1, L2 and L3 are excluded for all 382 instances; L4 is handled as above. None of this excludes
that the base model memorized fixes published in the public upstream repositories.** In the 136 instances whose
similarity to the gold patch (next section) is at least 0.8 under any of the calibers A, B, C
(measured on the patch the agent produced; for the withdrawn instances, the withdrawn patch),
25 have model-authored text — thinking, assistant text, tool-call input or final answer — that
contains an upstream pull-request, issue or commit number or URL that the task prompt does not
contain; the place of each is in that instance's row (`leak_audit.upstream_refs_in_model_text`).
Only those 136 instances were searched. The numbers are recorded as found; whether each is
correct, and where it came from, is not judged. 136 is the union over the three calibers; the
conservative score in the next section uses caliber C alone on the submitted patches (131 instances
at or above 0.8, 121 of them resolved), and 2 of the 136 are withdrawn
instances whose withdrawn patch is at or above 0.8.

## Similarity to the gold patch

Each `model_patch` in `all_preds.jsonl` was compared with the dataset's `patch` field by
`difflib.SequenceMatcher(a=gold_lines, b=model_lines, autojunk=False).ratio()` over the changed
lines (the `+` / `-` lines that are not diff headers), 0.0 when either side is empty.
`autojunk=False` is set because with the default, lines that occur often in a sequence of 200 or
more lines are ignored, so the matching rule would change with the patch length. The 3
withdrawn instances are compared as submitted (empty, 0.0); the similarity of each withdrawn patch is
in its row (`leak_audit.withdrawn_patch`). Three calibers:

- **A** — every changed line as it stands: marker kept, nothing stripped, whitespace-only lines
  kept, test files included.
- **B** — A without the lines of test files. A file is a test file when its path matches, case
  insensitively, `(^|/)(tests?|__tests__|__mocks__|specs?|testing|fixtures?|__snapshots__)/|(^|/)test[_-][^/]*|[_-]test\.|_test\.py$|conftest\.py$|[^/]*Tests?\.java$|(^|/)test/|\.test\.[jt]sx?$|\.spec\.[jt]sx?$|\.stories\.[jt]sx?$|setupTests|_test\.go$|_spec\.rb$`.
- **C** — B without blank lines and comment lines. A comment line is one whose text, with the
  marker removed and whitespace stripped, matches `^(//|#|/\*|\*/|\*|"""|\'\'\'|<!--|-->)`.

| Caliber | Resolved (274): ≥0.8 | ≥0.9 | ≥0.95 | identical | All (382): ≥0.8 | ≥0.9 | ≥0.95 | identical |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 110 | 83 | 70 | 61 | 119 | 91 | 76 | 66 |
| B | 112 | 84 | 71 | 62 | 121 | 92 | 77 | 67 |
| C | 121 | 100 | 83 | 75 | 131 | 109 | 90 | 81 |

Each instance's three values are in its row of `repository_isolation_audit.json` (`similarity`),
and the counts above are recomputed from those rows. **Conservative score: counting every resolved
instance at or above 0.8 under caliber C — the caliber with the most such instances,
121 — as unsolved gives 40.05% (153/382).** The `pass_rate` in `metadata.yaml`
stays the measured 71.73% (274/382).

## Network Egress

The agent reaches the model endpoint through a proxy. The proxy log holds 1811 permitted
(`ALLOW`) connections to a single host — the model endpoint. 1801 fall inside one of the
385 agent run windows; the other 10 fall outside every window, in the proxy's own
start-up check and the gaps between runs. Every other attempt was denied with nothing returned.

All of these numbers are recomputable from the `egress` key of
`repository_isolation_audit.json` alone. It carries one row per
agent run window (`instance_id`, `container`, `start`, `end`, where the window came from, and the
number of permitted connections inside it), one row per permitted connection, the ten rows that
fall outside every window — each naming the two window boundaries it fell between — and the
equation `1801 + 10 = 1811` written out. A permitted connection counts as in-window when its timestamp lies in
`[start - 1 s, end + 1 s]`; the margin covers the ordering between the proxy clock and the
runner's start and stop marks. The 385 windows are 383 runs plus 2
corrected re-runs. The permitted host is reported as `<model-endpoint>`; its name is not part of
the submission.

382 counts the dataset's instances (the denominator) and 379 the instances whose agent started;
6 instances have two windows, so the 385 windows cover 379 instances.

Requests the agent issued. 13 instances ran a command that uses a network tool (`curl`, `wget`,
`pip download|install`, `npm|yarn|pnpm install|view|add`, `git clone|fetch|ls-remote|pull`), 20
requests in all; one more instance is counted through a request its repository's own test made
(below). Each request is classed by what it asked for:

- **A** — content of the instance's own repository or package at a ref other than the base (a file,
  a clone or archive, a published package): 9 instances, 3 of them resolved (8
  through a network command, 1 through its repository's own test, below);
- **B** — only the repository's refs: 1 instance, 1 resolved;
- **M** — the repository's issue / pull-request metadata (the issue, pull-request and timeline API,
  search scoped to the repository, the issue and pull-request pages): 2 instances, 2
  resolved;
- **general** — a dependency, another repository or a registry root: 4 instances, 2
  resolved.

An instance is counted in every class it has a request in: `apache__dubbo-4678` is in B and M, `serverless__serverless-3804` is in A and general. One request was never sent
(`huggingface__transformers-4759`, `call_0029`: the container has no `curl`); each of the other 19 has at least
one proxy denial for its host inside the instance's window beyond the denials every agent start
makes. No host other than the model endpoint was permitted, so none of these requests returned
anything.

In `Significant-Gravitas__AutoGPT-4652` the agent ran the repository's unit tests, and the
repository's own test `test_download_file` requests `https://github.com/Significant-Gravitas/Auto-GPT/archive/refs/tags/v0.2.2.tar.gz`, an archive of the repository at a
ref other than the base. The proxy log has no path: that the 4 denials for `github.com` beyond
the baseline in that window are this request is inferred from the time window. The same window has
3 such denials for `raw.githubusercontent.com` whose path is recorded nowhere; that they asked
for a file of this repository at a ref other than the base cannot be excluded. The instance is
counted in A, also by inference, and is in the next class as well.

Denied connections opened by programs the agent ran (tests, package managers, libraries), with no
path recorded. Beyond the denials every agent start makes, 150 instances (108 resolved) have
denials for a host that none of their listed requests names. Per host — instances, resolved, and
instances whose window overlaps another run's window (there the time window alone cannot tie a
denial to one instance):

| Host | Instances | Resolved | Overlapping window |
|---|---:|---:|---:|
| `registry.npmjs.org` | 115 | 81 | 30 |
| `huggingface.co` | 25 | 18 | 0 |
| `s3.amazonaws.com` | 5 | 5 | 0 |
| `app.posthog.com` | 1 | 1 | 0 |
| `get.geojs.io` | 1 | 1 | 0 |
| `github.com` | 1 | 1 | 0 |
| `openaipublic.blob.core.windows.net` | 1 | 1 | 0 |
| `raw.githubusercontent.com` | 1 | 1 | 0 |
| `sts.amazonaws.com` | 1 | 0 | 0 |
| `www.youtube.com` | 1 | 1 | 0 |

6 of these instances are also in another class: `Significant-Gravitas__AutoGPT-4652` (A), `mui__material-ui-20657` (A), `serverless__serverless-3804` (A, general), `serverless__serverless-7277` (A), `sveltejs__svelte-6759` (M), `tailwindlabs__tailwindcss-116` (A). The proxy log records the host, not the path or the process.
Several of these repositories are themselves published on npm; for them it cannot be excluded that
a denied `registry.npmjs.org` request asked for another version of the project's own package. For
the other hosts, too, only the host and the counts are known. In 9 instances an error
printed in the trace names the path, and the row carries it; URL text that merely appears in a
trace (a lockfile line, a test's source) is listed apart in the row and is not evidence of a
request. In all, 158 instances (113 resolved) are in at least one of the five classes.
Per instance: `leak_audit.L3` in `repository_isolation_audit.json`.

Every window also has denials whose log line names no host: `REJECT POST` (per window median
5, from 3 to 10) and `REJECT PUT` (median 2, from 1 to
27) in all 385 windows, and `REJECT GET` in 5 windows of 5 instances (37
lines). All were denied; where they came from cannot be seen from the log, and they are not classed.

## Submitted Artifacts

`all_preds.jsonl`, `logs/`, `trajs/`, `metadata.yaml`, this README, `memorization_audit.json`,
`repository_isolation_audit.json` (which also carries the per-instance disposition, the per-instance
`leak_audit` and `similarity` rows, and the egress window list under its `egress` key).

Replacements in the traces. Each trace is rendered from the agent's raw event stream. Three
kinds of mechanical replacement were applied, each by a fixed mapping; the model's own output
and the patches were not edited, and nothing else in the traces was changed.

1. Internal names. The internal names of our agent runtime and of its command-line tool were
replaced by the neutral names `agent` and `agent-cli` (7002 and 1242
replacements). In all, 8244 replacements in 379 of the 379 trace files:
1834 inside JSON object keys (311 files; the key `_agent_context_projection` 1084
times, and a key that was exactly the runtime's name, now `agent`, 750 times), 6409 in
tool-output text (379 files), and 1 in the model's thinking (1 file).
By where they occur: 8243 of the 8244 are inside tool results and 1 inside the
model's thinking; none is in the task prompt, the assistant's text, a tool-call input or the final
answer.

2. Internal path. One path into our internal workspace, inside the tool catalog the agent listed
with `tool_search` (`trajs/apache__dubbo-3622.md`, line 2146), was replaced by `<internal-path>`:
1 replacement in 1 file, in tool-output text.

3. Run-environment identifiers. In one instance the agent ran `ps`, which printed the harness's
own command line; those identifiers were replaced in that file only
(`trajs/mui__material-ui-20657.md`, lines 1888 and 2841, 12 substitutions) using a fixed
mapping (mount paths → `/work` and `/tools`, state directory → `<agent-state>`, harness script
names → `<harness-script>`, harness-only flags and argument values → `<internal-flag>`); the
number of lines and the observation (which processes ran, with which arguments) are intact.
sha256 of that file without/with this mapping:
`bf7ecf7728918d578e89f14f47f88ad29f1d71763234e2a9a3eba70ee2aeb76e` /
`d44c19e30b38a0a8d5aaf8b004f2a6c9de10da1e49b78d72ffa8ea3c3e93fd1c`. A second file carries the
2 credential-shaped replacements described in the next paragraph.

How we checked that nothing else changed: every trace was rendered twice from the same raw
stream, once with replacements 1 and 2 switched off and once with them on. The two renderings
differ on 8241 lines in 379 files, and each of those lines equals the
switched-off line with replacements 1 and 2 applied; no line differs for any other reason.
Replacements of kind 3 occur in 2 files (12 and 2) and in none of the other
377 trace files.

One task statement (`trajs/yt-dlp__yt-dlp-10390.md`) contains the upstream issue reporter's own
`-vU` debug output, in which a proxy URL is written with the literal words `user` and `password`
at a port on the reporter's machine. Those two words are what the reporter typed in place of a
real credential; the string carries no real credential and substituting it removes nothing from
the record. The replacement is disclosed here because a string of that shape cannot be told
apart from a real one by a scanner.
