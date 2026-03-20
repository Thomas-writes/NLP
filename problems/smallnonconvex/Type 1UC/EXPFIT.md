# EXPFIT

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-0.11349 -0.081447] | 0.241 | 0.00082 | 16 | Optimization terminated successfully. |
| CG | success | [0.19279 -0.0054625] | 0.241 | 0.000516 | 9 | Optimization terminated successfully. |
| CG | success | [0.01974 -0.15265] | 0.241 | 0.00063 | 15 | Optimization terminated successfully. |
| BFGS | success | [-0.11985 0.011086] | 0.241 | 0.000459 | 12 | Optimization terminated successfully. |
| BFGS | success | [-0.074931 0.11382] | 0.241 | 0.00044 | 13 | Optimization terminated successfully. |
| BFGS | success | [-0.0072582 0.081935] | 0.241 | 0.000398 | 13 | Optimization terminated successfully. |
| dogleg | fail | [-0.10544 0.090178] | 27.6 | 7.75e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.030806 0.031527] | 25 | 6.1e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.10685 0.024412] | 21.1 | 5.48e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.040099 0.12926] | 5.7 | 0.00013 | 1 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.042618 0.0027841] | 6.49 | 9.8e-05 | 1 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.12959 -0.0011815] | 5.74 | 9.65e-05 | 1 | A bad approximation caused failure to predict improvement. |
