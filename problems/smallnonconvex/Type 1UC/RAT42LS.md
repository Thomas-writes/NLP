# RAT42LS

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
| CG | success | [99.687 -6.4208 5.3197] | 4.65e+03 | 0.000152 | 1 | Optimization terminated successfully. |
| CG | fail | [97.223 6.3496 -19.973] | 1.82e+04 | 4.16e-05 | 0 | NaN result encountered. |
| CG | success | [97.869 -14.207 -0.49758] | 1.82e+04 | 8.44e-05 | 1 | Optimization terminated successfully. |
| BFGS | fail | [99.15 14.625 -11.933] | 1.82e+04 | 4.88e-05 | 0 | NaN result encountered. |
| BFGS | success | [92.26 -3.6389 0.5737] | 8.06 | 0.00105 | 24 | Optimization terminated successfully. |
| BFGS | success | [92.282 15.396 2.1283] | 1.82e+04 | 8.24e-05 | 1 | Optimization terminated successfully. |
| dogleg | fail | [92.183 -2.4331 3.5797] | 3.03e+04 | 6.15e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [89.054 0.80787 10.969] | 2.73e+04 | 5.53e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [87.16 -6.823 2.9457] | 2.57e+04 | 5.2e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [128.1 11.494 10.129] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [126.61 -1.2234 0.10411] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [112.7 16.285 6.0807] | 5.38e+04 | 8.7e-05 | 0 | A bad approximation caused failure to predict improvement. |
