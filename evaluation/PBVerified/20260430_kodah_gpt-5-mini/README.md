# Kodah

## Overview

**Kodah** is a proprietary autonomous system designed for software engineering tasks and automated code repair. This submission provides the evaluation results for the **SWE-PolyBench Verified** dataset.

The system is optimized for production-ready integration, prioritizing precision and autonomous verification across diverse programming environments.

## Performance on SWE-PolyBench Verified

Kodah delivers **enterprise-grade performance** on the SWE-PolyBench Verified benchmark, achieving results on par with flagship industry systems. Notably, Kodah maintains this level of proficiency using **gpt-5-mini** as its foundation, demonstrating high architectural efficiency and cost-effectiveness in resolving complex, repository-level issues.

### Results Summary

```
Total resolved: 107/382
Total pass rate: 28.01%

Pass rate by language:
Python: 37/113 (32.7%)
JavaScript: 25/100 (25.0%)
TypeScript: 26/100 (26.0%)
Java: 19/69 (27.5%)

Pass rate by task category:
Bug Fix: 92/299 (30.8%)
Feature: 12/70 (17.1%)
Refactoring: 3/13 (23.1%)

File retrieval metrics by language:
            file_recall  file_precision  file_f1
language
Java               0.52            0.73     0.56
JavaScript         0.47            0.68     0.52
Python             0.67            0.77     0.69
TypeScript         0.45            0.72     0.51

File retrieval metrics overall:
file_recall       0.53
file_precision    0.73
file_f1           0.61
```

## Evaluation Integrity & Compliance

This submission follows the standard evaluation protocols for the SWE-PolyBench Verified benchmark:

- [x] Pass@1 Submission: No repeated attempts or selection of best-of-N outputs.
- [x] 100% Autonomous: No human intervention or "human-in-the-loop" during the evaluation.
- [x] Restricted Environment: The system operates without access to external data or benchmark metadata (no access to hints_text, git log, or commit_id).
- [x] Standard Evaluation: No prior knowledge of PASS_TO_PASS or FAIL_TO_PASS test cases.

## Project Links

- **Commercial API:** [kodah.io](https://kodah.io/) (For production-ready integration)
- **Technical Portfolio & Benchmarks:** [silasdata.com/kodah-swe-polybench-verified](https://www.silasdata.com/kodah-swe-polybench-verified) (Detailed performance analysis and cost-efficiency data)