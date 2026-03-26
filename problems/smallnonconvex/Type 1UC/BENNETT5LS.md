# BENNETT5LS

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
| CG | success | [-1749.9 273.81 253.06] | 49.3 | 0.00207 | 29 | Optimization terminated successfully. |
| CG | fail | [-2221.6 -39.819 -18.039] | nan | 7.01e-05 | 0 | NaN result encountered. |
| CG | success | [-2240.8 429.18 163.23] | 49.3 | 0.00296 | 36 | Optimization terminated successfully. |
| BFGS | fail | [-1975.4 63.096 -276.9] | nan | 0.00224 | 2 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-2325.2 95.466 -136.58] | nan | 0.00226 | 3 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [-1654.6 267.99 -114.4] | 49.3 | 0.000466 | 8 | Optimization terminated successfully. |
| dogleg | fail | [-2283.4 52.208 -87.647] | 8.59e+08 | 0.000101 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-1995.3 266.75 -290.07] | 6.17e+08 | 9.11e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-2156.4 254.31 401.23] | 6.75e+08 | 8.32e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-1847.1 40.544 -31.778] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-2053.9 -60.455 -127.67] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-2185.2 -62.91 83.389] | nan | nan | None | array must not contain infs or NaNs |
