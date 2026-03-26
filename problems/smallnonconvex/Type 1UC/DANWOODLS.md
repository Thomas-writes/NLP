# DANWOODLS

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
| CG | fail | [0.92208 4.8367] | nan | 0.000656 | 1 | NaN result encountered. |
| CG | success | [1.1709 5.1859] | 0.00432 | 0.00152 | 28 | Optimization terminated successfully. |
| CG | success | [1.277 5.3747] | 0.00432 | 0.00122 | 26 | Optimization terminated successfully. |
| BFGS | success | [1.437 5.8005] | 0.00432 | 0.000771 | 22 | Optimization terminated successfully. |
| BFGS | success | [0.47108 5.0574] | 0.00432 | 0.000559 | 15 | Optimization terminated successfully. |
| BFGS | fail | [0.86494 5.4956] | nan | 0.000723 | 1 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [1.3019 4.723] | 3.4e+03 | 7.6e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.7033 3.614] | 5.05e+03 | 5.45e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.8653 5.1276] | 3.26e+05 | 5.95e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.2263 4.0883] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [1.5845 4.8784] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [1.1007 5.181] | nan | nan | None | array must not contain infs or NaNs |
