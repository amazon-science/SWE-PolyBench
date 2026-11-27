# Mobile Coder + DeepSeek V4 Flash

This submission evaluates Mobile Coder 1.2.4 / DeepSeek V4 Flash / max on SWE-PolyBench Verified with strict
pass@1 generation. Each task uses a digest-pinned official image, a repository
sanitized to the exact base commit before the first model request, and an
outbound allowlist containing only the local model gateway.

The frozen task instruction asks Mobile Coder to modify implementation/source
files only and to leave tests, fixtures, snapshots, and evaluation files
unchanged because benchmark tests are applied separately by the evaluator.

The official evaluator was run sequentially (`--num-threads 1`) after predictions
were frozen. Result: 241/382 resolved (63.09%).
