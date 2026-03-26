# LSC2LS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-25

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [124.85 47.131 250.89] | 13.4 | 0.00588 | 101 | Optimization terminated successfully. |
| CG | success | [98.113 62.32 265.14] | 13.3 | 0.0101 | 173 | Optimization terminated successfully. |
| CG | success | [97.92 24.621 248.31] | 13.3 | 0.0112 | 183 | Optimization terminated successfully. |
| BFGS | fail | [126.82 22.601 282.48] | 13.6 | 0.0021 | 60 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [187.7 38.177 243.4] | 13.3 | 0.00182 | 53 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [106.51 68.212 264] | 13.6 | 0.00222 | 58 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [106.15 31.442 239.5] | 1.54e+05 | 7.31e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [103.86 23.902 250.67] | 1.83e+05 | 5.67e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [72.432 26.238 293.93] | 3.71e+05 | 5.29e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [90.363 4.6188 278.4] | 671 | 0.000696 | 18 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [133.22 4.883 318.6] | 451 | 0.000752 | 22 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [73.861 67.425 283.08] | 16.5 | 0.000701 | 23 | A bad approximation caused failure to predict improvement. |
