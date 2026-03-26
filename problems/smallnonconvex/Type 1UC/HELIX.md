# HELIX

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
| CG | success | [-0.96803 0.069465 0.12193] | 1.58e-12 | 0.00166 | 41 | Optimization terminated successfully. |
| CG | success | [-1.077 -0.19803 0.068615] | 3.77e-15 | 0.00109 | 28 | Optimization terminated successfully. |
| CG | success | [-0.94798 0.043502 -0.082295] | 7.66e-12 | 0.00154 | 38 | Optimization terminated successfully. |
| BFGS | success | [-1.1598 -0.026818 -0.0038784] | 1.97e-15 | 0.00102 | 30 | Optimization terminated successfully. |
| BFGS | success | [-1.1052 0.11634 0.038042] | 5.7e-14 | 0.00101 | 28 | Optimization terminated successfully. |
| BFGS | success | [-1.0923 0.12314 -0.030419] | 2.65e-13 | 0.000976 | 30 | Optimization terminated successfully. |
| dogleg | fail | [-1.1926 -0.09415 0.0080071] | 2.39e+03 | 7.35e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.92976 0.30721 0.038025] | 1.98e+03 | 5.87e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-1.1311 0.0098275 0.30526] | 2.19e+03 | 5.32e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.96836 0.017825 0.00042621] | 42.8 | 0.000153 | 3 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-0.83151 0.07201 0.089852] | 51.8 | 0.000133 | 3 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-0.92224 -0.15144 -0.095105] | 26.1 | 0.000137 | 3 | A bad approximation caused failure to predict improvement. |
