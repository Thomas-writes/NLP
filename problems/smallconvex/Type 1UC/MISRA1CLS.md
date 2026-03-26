# MISRA1CLS

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
| CG | fail | [452.45 -22.335] | nan | 6.63e-05 | 0 | NaN result encountered. |
| CG | fail | [525 -10.394] | nan | 4.47e-05 | 0 | NaN result encountered. |
| CG | fail | [443.63 25.399] | nan | 0.00287 | 2 | NaN result encountered. |
| BFGS | fail | [511.75 -1.0794] | nan | 5.52e-05 | 0 | NaN result encountered. |
| BFGS | fail | [397.23 4.0168] | nan | 0.00144 | 1 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [545.54 8.7657] | nan | 0.00147 | 1 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [427.78 49.949] | 2.05e+06 | 6.79e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [492.3 -21.609] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [507.89 -70.707] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [440.57 40.151] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [547.94 -64.065] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [443.9 40.894] | nan | nan | None | array must not contain infs or NaNs |
