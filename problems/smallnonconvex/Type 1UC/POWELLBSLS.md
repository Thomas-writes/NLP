# POWELLBSLS

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-0.097981 1.0898] | 3.5e-06 | 0.00184 | 38 | Optimization terminated successfully. |
| CG | success | [0.022451 1.0108] | 2.33e-06 | 0.00122 | 26 | Optimization terminated successfully. |
| CG | success | [0.042864 0.86274] | 8.32e-07 | 0.00167 | 34 | Optimization terminated successfully. |
| BFGS | success | [0.01511 0.96711] | 3.01e-22 | 0.00551 | 153 | Optimization terminated successfully. |
| BFGS | success | [-0.0088623 1.1178] | 1.39e-21 | 0.00557 | 170 | Optimization terminated successfully. |
| BFGS | success | [-0.0014372 0.96979] | 9.95e-22 | 0.0058 | 155 | Optimization terminated successfully. |
| dogleg | fail | [-0.074944 0.95599] | 5.15e+05 | 5.99e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.030731 0.98639] | 9.25e+04 | 5.85e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.031943 1.0126] | 1.05e+05 | 5.25e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.059872 1.1173] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [0.056634 1.1097] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [0.047373 0.84896] | nan | nan | None | array must not contain infs or NaNs |
