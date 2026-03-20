# LANCZOS2LS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.67978 1.1909 5.156 5.0061 7.9719 7.0748] | 9.39e-06 | 0.00982 | 236 | Optimization terminated successfully. |
| CG | success | [2.2501 -0.30361 6.116 6.7656 6.428 7.753] | 7.57e-06 | 0.00495 | 129 | Optimization terminated successfully. |
| CG | success | [1.9815 -0.24217 5.7009 4.4733 7.0102 7.9804] | 1e-05 | 0.0203 | 512 | Optimization terminated successfully. |
| BFGS | success | [0.81772 0.79838 5.1419 4.3228 7.9888 9.1361] | 4.3e-06 | 0.00416 | 128 | Optimization terminated successfully. |
| BFGS | success | [1.4461 1.1047 5.2335 4.6701 6.3734 6.9462] | 3.31e-07 | 0.00211 | 62 | Optimization terminated successfully. |
| BFGS | success | [1.4692 -0.60108 4.3584 5.8561 7.7793 7.1372] | 4.3e-06 | 0.00383 | 125 | Optimization terminated successfully. |
| dogleg | fail | [0.39164 -0.55124 5.463 4.7395 6.5729 7.0448] | 225 | 7.31e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.77212 -0.11051 7.172 4.8064 5.5055 6.9552] | 301 | 5.38e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.3525 0.64772 6.4848 5.2165 8.102 7.0692] | 424 | 5.09e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.60151 1.602 6.5655 7.0583 6.7314 8.3041] | 170 | 0.00081 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.2014 0.24475 5.0347 4.6989 8.3825 5.6526] | 213 | 0.000985 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.075771 0.21881 5.4162 5.2161 6.6579 6.5792] | 188 | 0.000965 | 28 | A bad approximation caused failure to predict improvement. |
