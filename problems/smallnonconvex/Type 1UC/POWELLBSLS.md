# POWELLBSLS

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-0.15687 0.94909] | 1.69e-06 | 0.0017 | 36 | Optimization terminated successfully. |
| CG | success | [0.09042 1.0363] | 4.66e-06 | 0.00143 | 30 | Optimization terminated successfully. |
| CG | success | [-0.19702 0.84959] | 8.32e-07 | 0.00222 | 48 | Optimization terminated successfully. |
| BFGS | success | [0.082913 0.9281] | 2.72e-23 | 0.00543 | 166 | Optimization terminated successfully. |
| BFGS | success | [0.002998 0.91983] | 2.71e-21 | 0.00472 | 158 | Optimization terminated successfully. |
| BFGS | success | [0.13136 0.96708] | 2.76e-22 | 0.00543 | 172 | Optimization terminated successfully. |
| dogleg | fail | [0.010283 1.0133] | 1.06e+04 | 6.3e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.094333 1.1254] | 1.13e+06 | 4.84e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.017731 1.1549] | 4.23e+04 | 4.88e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.10366 0.78688] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-0.034695 1.0833] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-0.010368 1.1967] | nan | nan | None | array must not contain infs or NaNs |
