# NELSONLS

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
| CG | success | [2.2174 -0.14163 -0.21572] | 54.4 | 0.000391 | 2 | Optimization terminated successfully. |
| CG | success | [1.7377 -0.17118 -0.37105] | 54.4 | 0.000276 | 2 | Optimization terminated successfully. |
| CG | fail | [1.7489 -0.37138 0.07114] | 53.5 | 0.000615 | 2 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [2.1366 0.12423 -0.17448] | 54.4 | 0.000151 | 2 | Optimization terminated successfully. |
| BFGS | success | [1.6116 -0.16225 -0.096517] | 54.4 | 0.000135 | 2 | Optimization terminated successfully. |
| BFGS | success | [2.1214 -0.022048 -0.254] | 54.4 | 0.000129 | 2 | Optimization terminated successfully. |
| dogleg | fail | [1.9068 0.1531 -0.21516] | 1.8e+54 | 9.76e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.713 0.04902 -0.15038] | 6.21e+37 | 6.79e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [2.2279 0.16395 0.13658] | 54.8 | 6.47e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [2.1875 -0.067858 -0.070157] | 157 | 0.00228 | 47 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.0866 -0.14283 -0.28329] | 232 | 0.00474 | 101 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.8404 -0.039152 -0.30279] | nan | nan | None | array must not contain infs or NaNs |
