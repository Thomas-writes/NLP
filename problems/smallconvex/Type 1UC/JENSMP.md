# JENSMP

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
- **Objective Type:** sum of squares
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [0.62151 0.40111] | 462 | 0.000253 | 1 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [0.35185 0.25814] | 124 | 0.002 | 27 | Desired error not necessarily achieved due to precision loss. |
| CG | success | [0.38299 0.35189] | 124 | 0.00155 | 17 | Optimization terminated successfully. |
| BFGS | success | [0.15769 0.34242] | 124 | 0.0005 | 11 | Optimization terminated successfully. |
| BFGS | success | [0.13448 0.47273] | 124 | 0.00124 | 30 | Optimization terminated successfully. |
| BFGS | success | [0.32277 0.46772] | 124 | 0.00108 | 25 | Optimization terminated successfully. |
| dogleg | success | [0.38248 0.50794] | 124 | 0.000575 | 12 | Optimization terminated successfully. |
| dogleg | success | [0.38419 0.50502] | 124 | 0.000558 | 12 | Optimization terminated successfully. |
| dogleg | fail | [0.24582 0.46174] | 124 | 0.000523 | 11 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.34895 0.28348] | 125 | 0.000974 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.24135 0.56703] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [0.34754 0.46038] | nan | nan | None | array must not contain infs or NaNs |
