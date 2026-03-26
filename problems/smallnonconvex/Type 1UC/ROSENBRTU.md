# ROSENBRTU

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
| CG | success | [-10.455 12.715] | 4.65e-12 | 0.00582 | 114 | Optimization terminated successfully. |
| CG | success | [-11.623 9.8225] | 2.66e-11 | 0.00468 | 92 | Optimization terminated successfully. |
| CG | success | [-12.278 8.5336] | 5.17e-15 | 0.00197 | 36 | Optimization terminated successfully. |
| BFGS | success | [-12.371 12.995] | 1.56e-15 | 0.00245 | 63 | Optimization terminated successfully. |
| BFGS | success | [-12.083 10.805] | 3.04e-17 | 0.00218 | 55 | Optimization terminated successfully. |
| BFGS | success | [-10.957 11.136] | 1.37e-14 | 0.00228 | 57 | Optimization terminated successfully. |
| dogleg | fail | [-12.309 9.2302] | 101 | 6.15e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-13.511 12.305] | 101 | 5.5e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-11.468 10.644] | 101 | 5.27e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-11.059 10.438] | 101 | 0.000248 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-12.958 9.0154] | 101 | 0.000475 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-10.681 9.3459] | 101 | 0.000162 | 0 | A bad approximation caused failure to predict improvement. |
