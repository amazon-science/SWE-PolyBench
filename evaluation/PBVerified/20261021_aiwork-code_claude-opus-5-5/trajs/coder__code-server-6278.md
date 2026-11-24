# Instance: coder__code-server-6278
# Model: claude-opus-5-5
# Run status: not run
# Final resolved: False

## No trajectory: this instance was not run

The agent was never started for this instance, so there are no steps,
thoughts or tool calls to show. This file is a notice, not a trajectory.

Reason: the repository-isolation check refuses, by design, to clean a repository whose Git directory holds a git-lfs object store, so the agent was not started.

The prediction for this instance is an empty patch. Its `logs/` files were
written by the upstream evaluator's own empty-patch path
(`run_evaluation.py`, lines 97-118), which returns before any container is
created; the section "Coverage and Disposition" in the README covers this
distinction and states what `false` and `0.0` mean for these instances.
