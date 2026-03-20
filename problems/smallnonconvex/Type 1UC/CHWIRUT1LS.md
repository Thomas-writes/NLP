# CHWIRUT1LS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.0055035 -0.12273 0.15201] | 3.15e+05 | 0.000143 | 2 | Optimization terminated successfully. |
| CG | fail | [0.20931 0.27082 0.20772] | 2.38e+03 | 0.00349 | 29 | Desired error not necessarily achieved due to precision loss. |
| CG | success | [-0.024534 -0.047652 -0.033478] | 3.15e+05 | 0.000687 | 5 | Optimization terminated successfully. |
| BFGS | fail | [0.034417 0.015366 0.14875] | 2.38e+03 | 0.00131 | 21 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [0.12514 0.0018292 -0.23319] | 3.15e+05 | 0.00141 | 3 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [0.18087 0.033055 0.089635] | 2.38e+03 | 0.00122 | 18 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [0.050327 -0.05372 -0.32442] | 3.17e+05 | 0.000391 | 4 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.12709 0.0085649 0.083282] | 1.71e+05 | 7.24e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.10364 0.013354 0.059876] | 1.73e+05 | 6.71e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.248 0.085998 0.13538] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [0.1689 -0.10016 -0.18028] | 3.21e+05 | 0.000186 | 1 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.20348 0.085074 0.11266] | nan | nan | None | array must not contain infs or NaNs |
