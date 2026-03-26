# MEYER3

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
| CG | fail | [418.99 3929.6 1151.8] | 6.31e+04 | 0.0288 | 600 | Maximum number of iterations has been exceeded. |
| CG | success | [-404.22 3580.9 -221.02] | 3.89e+09 | 0.000548 | 3 | Optimization terminated successfully. |
| CG | fail | [-307.07 3285.2 506.48] | 3.17e+05 | 0.0303 | 600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [-383.76 3532.2 -354.82] | 3.89e+09 | 0.000873 | 22 | Optimization terminated successfully. |
| BFGS | fail | [-427.76 4627.1 603.22] | 87.9 | 0.0221 | 574 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-208.59 4574.8 248.7] | 576 | 0.00174 | 39 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [-93.645 4521.1 -84.123] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [-177.18 4370 276.96] | 4.04e+16 | 5.35e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [26.758 4609.8 236.41] | 1.67e+17 | 5.63e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [280.91 4518.1 373.5] | 9.42e+08 | 0.00193 | 76 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-540.84 4492.5 672.89] | 1.23e+09 | 0.00519 | 193 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-427.81 3884 234.73] | 1.09e+09 | 0.00453 | 154 | A bad approximation caused failure to predict improvement. |
