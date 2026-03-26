# GULF

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
| CG | success | [4.7751 2.9382 0.48479] | 9.83e-07 | 0.0036 | 49 | Optimization terminated successfully. |
| CG | success | [4.9774 2.0964 0.51816] | 2.74e-07 | 0.0033 | 36 | Optimization terminated successfully. |
| CG | success | [4.829 2.7183 0.32848] | 2.91e-09 | 0.00552 | 62 | Optimization terminated successfully. |
| BFGS | success | [4.3734 3.0491 0.97349] | 2.73e-13 | 0.00165 | 27 | Optimization terminated successfully. |
| BFGS | success | [4.6549 2.8506 1.3491] | 1.45e-13 | 0.00256 | 33 | Optimization terminated successfully. |
| BFGS | success | [6.2321 2.1762 -0.27504] | 1.49e-12 | 0.00182 | 29 | Optimization terminated successfully. |
| dogleg | fail | [5.3195 2.268 -0.14231] | 23.5 | 9.28e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [5.0471 2.4286 0.543] | 11.6 | 8.28e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [4.9445 2.2253 0.69442] | 22.3 | 8.3e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [5.9596 2.2953 -0.025848] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [4.7876 2.1507 0.18704] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [5.8518 2.8114 0.1003] | nan | nan | None | array must not contain infs or NaNs |
