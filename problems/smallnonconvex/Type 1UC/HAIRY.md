# HAIRY

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
| CG | success | [-4.976 -6.7043] | 20 | 0.00144 | 20 | Optimization terminated successfully. |
| CG | success | [-5.5439 -6.0711] | 20 | 0.000893 | 17 | Optimization terminated successfully. |
| CG | success | [-4.9404 -6.1305] | 20 | 0.00104 | 18 | Optimization terminated successfully. |
| BFGS | success | [-4.3251 -7.6648] | 20 | 0.000749 | 16 | Optimization terminated successfully. |
| BFGS | success | [-5.4466 -6.9743] | 20 | 0.000679 | 15 | Optimization terminated successfully. |
| BFGS | success | [-6.2457 -7.4637] | 20 | 0.00071 | 14 | Optimization terminated successfully. |
| dogleg | fail | [-5.1546 -7.1153] | 736 | 6e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-5.1162 -6.691] | 694 | 5.54e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-5.9291 -6.5884] | 663 | 5.18e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-5.9065 -6.8045] | 686 | 0.000744 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-4.564 -7.7634] | 779 | 0.00055 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-5.0662 -6.5171] | 652 | 6e-05 | 0 | A bad approximation caused failure to predict improvement. |
