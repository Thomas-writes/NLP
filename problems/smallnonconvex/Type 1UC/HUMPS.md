# HUMPS

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
- **Objective Type:** other
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-474.34 -627.4] | 1.18e-13 | 0.00323 | 48 | Optimization terminated successfully. |
| CG | success | [-467.44 -591.5] | 5.09e-13 | 0.00239 | 31 | Optimization terminated successfully. |
| CG | success | [-463.86 -440.2] | 1.35e-12 | 0.00282 | 38 | Optimization terminated successfully. |
| BFGS | success | [-575.2 -416.03] | 8.93e-12 | 0.00357 | 56 | Optimization terminated successfully. |
| BFGS | success | [-561.47 -452.46] | 1.47e-11 | 0.00513 | 94 | Optimization terminated successfully. |
| BFGS | success | [-447.93 -547.18] | 5.03e-11 | 0.00816 | 139 | Optimization terminated successfully. |
| dogleg | fail | [-521.53 -480.05] | 2.51e+04 | 6.16e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-513.17 -538.55] | 2.77e+04 | 5.55e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-496.85 -541.51] | 2.7e+04 | 5.41e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-491.19 -621.9] | 3.14e+04 | 0.00948 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [-534.1 -501.5] | 2.68e+04 | 0.0094 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [-469.01 -533.8] | 2.52e+04 | 0.00955 | 400 | Maximum number of iterations has been exceeded. |
