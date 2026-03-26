# GROWTHLS

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
| CG | success | [108.49 14.656 -13.157] | 3.54e+03 | 9.63e-05 | 0 | Optimization terminated successfully. |
| CG | success | [95.678 -23.416 13.808] | 3.54e+03 | 0.00033 | 2 | Optimization terminated successfully. |
| CG | success | [97.348 -11.202 -18.226] | 3.54e+03 | 4.79e-05 | 0 | Optimization terminated successfully. |
| BFGS | fail | [91.119 -0.79661 2.992] | 1.27e+19 | 0.000305 | 1 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [102.06 3.6073 18.041] | 2.92e+176 | 0.00197 | 0 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [92.143 8.9032 13.758] | 1.32e+143 | 0.00022 | 1 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [87.762 -1.7485 1.2398] | 1.58e+10 | 7e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | success | [130.36 -4.3478 -14.047] | 3.54e+03 | 5.02e-05 | 0 | Optimization terminated successfully. |
| dogleg | success | [113.18 -10.781 -10.451] | 3.54e+03 | 3.95e-05 | 0 | Optimization terminated successfully. |
| trust-ncg | fail | [107.88 8.3202 -3.7279] | 1.37e+04 | 0.000884 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [102.95 2.868 -2.3486] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [118.65 4.2995 18.469] | 2.41e+182 | 0.0002 | 0 | A bad approximation caused failure to predict improvement. |
