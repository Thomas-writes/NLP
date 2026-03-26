# HIMMELBB

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
| CG | success | [-1.0261 1.1669] | 4.05e-09 | 0.000291 | 3 | Optimization terminated successfully. |
| CG | success | [-1.3073 1.116] | 1.73e-18 | 0.000264 | 4 | Optimization terminated successfully. |
| CG | success | [-1.3149 0.95988] | 3.58e-13 | 0.000486 | 2 | Optimization terminated successfully. |
| BFGS | success | [-1.163 0.85311] | 3.29e-10 | 0.000314 | 8 | Optimization terminated successfully. |
| BFGS | success | [-1.2414 0.78341] | 1.18e-12 | 0.000272 | 4 | Optimization terminated successfully. |
| BFGS | success | [-1.2516 0.8704] | 6.55e-13 | 0.000185 | 5 | Optimization terminated successfully. |
| dogleg | fail | [-1.1025 1.056] | 1.23e+04 | 5.89e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-1.1419 0.93678] | 1.39e+04 | 5.6e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-1.0035 1.1822] | 5.86e+03 | 5.11e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | success | [-1.1305 1.1947] | 1.58e-10 | 0.000338 | 9 | Optimization terminated successfully. |
| trust-ncg | fail | [-1.0217 0.98034] | 2.48e-06 | 0.000236 | 7 | A bad approximation caused failure to predict improvement. |
| trust-ncg | success | [-1.1797 0.69893] | 6.78e-13 | 0.000461 | 17 | Optimization terminated successfully. |
