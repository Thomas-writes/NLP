# MGH09LS

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [39.72 48.598 42.152 36.38] | 0.00102 | 0.00322 | 33 | Optimization terminated successfully. |
| CG | success | [25.546 41.046 44.114 44.318] | 0.00153 | 0.0026 | 40 | Optimization terminated successfully. |
| CG | success | [13.936 35.497 34.762 39.748] | 0.00171 | 0.00247 | 35 | Optimization terminated successfully. |
| BFGS | success | [18.039 35.853 35.43 34.348] | 0.000936 | 0.00298 | 86 | Optimization terminated successfully. |
| BFGS | success | [22.665 40.992 35.384 41.993] | 0.00181 | 0.000799 | 23 | Optimization terminated successfully. |
| BFGS | success | [27.866 47.061 45.814 42.984] | 0.00181 | 0.000818 | 24 | Optimization terminated successfully. |
| dogleg | fail | [29.614 33.88 44.776 40.385] | 859 | 7.69e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [29.078 43.652 46.456 33.106] | 1.46e+03 | 5.72e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [32.511 35.585 43.904 39.18] | 1.19e+03 | 5.28e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [29.743 39.083 48.533 39.371] | 1.04e+03 | 0.000805 | 27 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [21.906 29.649 44.454 40.028] | 367 | 0.0007 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [29.377 38.875 40.698 35.893] | 1.34e+03 | 0.000785 | 27 | A bad approximation caused failure to predict improvement. |
