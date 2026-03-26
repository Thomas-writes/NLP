# WAYSEA2

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-25

## Classification
- **Convexity:** Convex
- **Objective Type:** sum of squares
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.63407 4.8642] | 5.23e-16 | 0.000854 | 13 | Optimization terminated successfully. |
| CG | success | [0.91809 4.6339] | 2.81e-16 | 0.000653 | 11 | Optimization terminated successfully. |
| CG | success | [0.62809 5.5325] | 6.08e-10 | 0.000719 | 11 | Optimization terminated successfully. |
| BFGS | success | [0.25719 5.1024] | 4.42e-15 | 0.00155 | 39 | Optimization terminated successfully. |
| BFGS | success | [1.0018 5.3395] | 5.59e-15 | 0.00134 | 37 | Optimization terminated successfully. |
| BFGS | success | [1.6491 5.5917] | 2.36e-13 | 0.00115 | 35 | Optimization terminated successfully. |
| dogleg | fail | [1.2063 4.1242] | 0.711 | 0.000354 | 9 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.2358 5.0985] | 1.34 | 0.000263 | 6 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.72817 5.1037] | 1.47 | 0.000247 | 6 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.244 5.3195] | 54.8 | 0.000837 | 30 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.4537 5.6767] | 85.1 | 0.000895 | 31 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.75821 5.8841] | 104 | 0.00123 | 37 | A bad approximation caused failure to predict improvement. |
