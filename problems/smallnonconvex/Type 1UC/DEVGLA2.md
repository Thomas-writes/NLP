# DEVGLA2

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
- **# of Variables (n):** 5
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [23.877 -2.0516 -1.8784 3.4151 0.64221] | nan | 6.59e-05 | 0 | NaN result encountered. |
| CG | fail | [19.986 1.9427 0.80137 -0.4824 -0.38569] | nan | 0.00269 | 17 | NaN result encountered. |
| CG | success | [18.106 4.1147 -0.339 -0.74895 -0.26131] | 0.025 | 0.0192 | 395 | Optimization terminated successfully. |
| BFGS | success | [18.63 0.1165 0.9613 4.635 -0.7364] | 1.63e-16 | 0.00254 | 60 | Optimization terminated successfully. |
| BFGS | fail | [20.332 3.7927 3.2332 1.5134 -4.7924] | nan | 0.0018 | 2 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [22.336 1.0067 3.3071 1.9632 -1.3792] | nan | 0.0018 | 2 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [23.019 3.0734 1.8583 2.0813 -0.89916] | 9.32e+04 | 7.35e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [21.097 1.3372 0.71932 3.8285 3.4161] | 2.13e+04 | 6.21e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [23.737 1.8736 3.1403 4.5561 -3.0377] | 5.13e+04 | 5.85e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [19.898 4.0275 3.9378 1.7269 0.86411] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [21.12 1.877 2.7959 1.0444 1.3629] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [18.87 -0.062091 2.7281 0.4108 0.97697] | nan | nan | None | array must not contain infs or NaNs |
