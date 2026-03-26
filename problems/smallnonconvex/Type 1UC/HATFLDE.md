# HATFLDE

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
| CG | success | [0.89272 -0.97262 0.025468] | 2.73e-06 | 0.00283 | 59 | Optimization terminated successfully. |
| CG | success | [0.98876 -1.0273 -0.013268] | 2.73e-06 | 0.00198 | 36 | Optimization terminated successfully. |
| CG | success | [0.85638 -0.9836 -0.033556] | 5.18e-07 | 0.0017 | 30 | Optimization terminated successfully. |
| BFGS | success | [1.0824 -0.90304 0.018031] | 5.12e-07 | 0.001 | 29 | Optimization terminated successfully. |
| BFGS | success | [0.96895 -1.0559 0.16898] | 5.12e-07 | 0.000989 | 30 | Optimization terminated successfully. |
| BFGS | success | [1.0033 -0.98277 0.11991] | 5.12e-07 | 0.00097 | 28 | Optimization terminated successfully. |
| dogleg | fail | [0.94736 -1.0412 0.18123] | 57.6 | 6.41e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.92557 -1.0626 -0.064851] | 45.6 | 5.87e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.0459 -0.98127 0.049697] | 45.8 | 5.74e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.0366 -1.0406 0.065798] | 9.38 | 0.000818 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.93638 -0.99509 -0.037974] | 8.93 | 0.000795 | 30 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.91263 -1.0987 -0.13134] | 9.84 | 0.000803 | 30 | A bad approximation caused failure to predict improvement. |
