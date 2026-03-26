# MISRA1ALS

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
| CG | fail | [594.71 -14.223] | nan | 0.00222 | 1 | NaN result encountered. |
| CG | fail | [515.69 -38.028] | nan | 0.00109 | 1 | NaN result encountered. |
| CG | success | [531.02 34.539] | 6.76e+03 | 0.00021 | 2 | Optimization terminated successfully. |
| BFGS | fail | [541.42 -85.576] | nan | 0.00166 | 1 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [434.89 76.852] | 6.76e+03 | 0.000191 | 3 | Optimization terminated successfully. |
| BFGS | fail | [494.43 -43.292] | nan | 0.00168 | 1 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [482.46 42.704] | 2.71e+06 | 6.33e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [517.53 -110.65] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [459.17 1.8869] | 2.43e+06 | 5.01e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [483.93 31.158] | 2.72e+06 | 0.000111 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [415.14 -58.831] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [523.41 16.754] | 3.23e+06 | 7.52e-05 | 0 | A bad approximation caused failure to predict improvement. |
