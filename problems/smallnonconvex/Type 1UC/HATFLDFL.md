# HATFLDFL

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
| CG | success | [1.3421 -1.1925 1.0038] | 6.62e-05 | 0.000362 | 6 | Optimization terminated successfully. |
| CG | success | [1.3549 -1.16 1.0238] | 6.63e-05 | 0.000294 | 6 | Optimization terminated successfully. |
| CG | success | [1.162 -1.1783 0.7812] | 6.69e-05 | 0.000767 | 17 | Optimization terminated successfully. |
| BFGS | success | [1.3103 -1.3393 0.9813] | 6.59e-05 | 0.000253 | 5 | Optimization terminated successfully. |
| BFGS | success | [1.4269 -1.1847 0.82853] | 6.59e-05 | 0.000316 | 8 | Optimization terminated successfully. |
| BFGS | success | [1.2273 -0.96732 0.86962] | 6.73e-05 | 0.000255 | 6 | Optimization terminated successfully. |
| dogleg | fail | [1.3289 -1.231 0.89301] | 0.249 | 6.01e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.0436 -1.3241 1.0106] | 0.418 | 5.52e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.4497 -1.2971 0.95349] | 0.13 | 5.14e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.93319 -1.3658 1.1433] | 0.0198 | 0.000233 | 7 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.3485 -1.361 0.99511] | 0.000829 | 0.000153 | 4 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.218 -1.076 0.95061] | 0.00382 | 0.000794 | 37 | A bad approximation caused failure to predict improvement. |
