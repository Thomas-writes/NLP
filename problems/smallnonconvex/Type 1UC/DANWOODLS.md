# DANWOODLS

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
| CG | success | [1.6003 5.1079] | 0.00432 | 0.00128 | 22 | Optimization terminated successfully. |
| CG | success | [1.3177 5.3103] | 0.00432 | 0.00145 | 33 | Optimization terminated successfully. |
| CG | success | [0.68274 5.1219] | 0.00432 | 0.000662 | 13 | Optimization terminated successfully. |
| BFGS | fail | [-0.18845 5.2073] | nan | 6.79e-05 | 0 | NaN result encountered. |
| BFGS | success | [1.6242 5.6901] | 0.00432 | 0.00102 | 29 | Optimization terminated successfully. |
| BFGS | success | [1.6145 5.5729] | 0.00432 | 0.000761 | 20 | Optimization terminated successfully. |
| dogleg | fail | [1.5852 5.0414] | 4.96e+04 | 0.000227 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.62594 4.9944] | 64.8 | 5.19e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.62566 4.4504] | 64.7 | 5.28e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.64473 5.2445] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [0.60423 4.6854] | 1.14 | 0.00417 | 258 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.3875 4.9303] | nan | nan | None | array must not contain infs or NaNs |
