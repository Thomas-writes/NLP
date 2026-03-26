# AKIVA

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-25

## Classification
- **Convexity:** Convex
- **Objective Type:** other
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-0.075485 -0.0057461] | 6.17 | 0.000854 | 11 | Optimization terminated successfully. |
| CG | success | [-0.10833 -0.081439] | 6.17 | 0.000529 | 9 | Optimization terminated successfully. |
| CG | success | [0.12252 -0.12641] | 6.17 | 0.000965 | 12 | Optimization terminated successfully. |
| BFGS | success | [-0.052149 -0.094375] | 6.17 | 0.000348 | 6 | Optimization terminated successfully. |
| BFGS | success | [0.02269 0.26247] | 6.17 | 0.000634 | 13 | Optimization terminated successfully. |
| BFGS | success | [0.17034 0.023117] | 6.17 | 0.000627 | 12 | Optimization terminated successfully. |
| dogleg | fail | [0.013421 0.15461] | 6.17 | 0.000353 | 5 | A bad approximation caused failure to predict improvement. |
| dogleg | success | [-0.23056 0.052277] | 6.17 | 0.000348 | 7 | Optimization terminated successfully. |
| dogleg | success | [0.046945 -0.0044631] | 6.17 | 0.000287 | 5 | Optimization terminated successfully. |
| trust-ncg | fail | [0.16881 -0.033757] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [0.18122 0.1122] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-0.24446 -0.13041] | nan | nan | None | array must not contain infs or NaNs |
