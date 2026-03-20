# CHWIRUT2LS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-03

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [0.26466 0.054142 -0.08533] | 8.86e+04 | 0.000372 | 1 | Desired error not necessarily achieved due to precision loss. |
| CG | success | [-0.055832 -0.023832 -0.027039] | 9.05e+04 | 0.000134 | 2 | Optimization terminated successfully. |
| CG | success | [0.10405 -0.08708 0.012141] | 9.05e+04 | 0.000688 | 6 | Optimization terminated successfully. |
| BFGS | fail | [-0.21468 -0.083128 -0.17726] | 9.05e+04 | 0.00102 | 3 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [0.052138 -0.097843 -0.22924] | 9.05e+04 | 0.00124 | 3 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [0.10656 0.13491 0.016762] | 513 | 0.00251 | 29 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [0.19372 0.15901 -0.075302] | 1e+04 | 0.000839 | 16 | A bad approximation caused failure to predict improvement. |
| dogleg | fail | [-0.13993 0.32251 0.14388] | 8.24e+04 | 0.000168 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | success | [0.17126 -0.038381 -0.14733] | 9.05e+04 | 0.00117 | 24 | Optimization terminated successfully. |
| trust-ncg | fail | [0.06869 -0.18868 -0.059756] | 9.56e+04 | 0.000178 | 2 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.12809 0.057267 0.071798] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-0.015359 0.21837 -0.089398] | 2.37e+05 | 0.0157 | 600 | Maximum number of iterations has been exceeded. |
