# SNAIL

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
- **Objective Type:** other
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [9.0104 10.466] | 3.3e-21 | 0.00387 | 73 | Optimization terminated successfully. |
| CG | success | [10.385 11.048] | 1.51e-19 | 0.00409 | 73 | Optimization terminated successfully. |
| CG | success | [9.9106 10.286] | 1.5e-13 | 0.00355 | 73 | Optimization terminated successfully. |
| BFGS | success | [9.8056 10.392] | 1.59e-13 | 0.00356 | 105 | Optimization terminated successfully. |
| BFGS | success | [8.6813 8.9428] | 7e-14 | 0.00306 | 100 | Optimization terminated successfully. |
| BFGS | success | [9.3112 10.008] | 2.7e-12 | 0.00339 | 99 | Optimization terminated successfully. |
| dogleg | fail | [9.8715 10.499] | 4.68 | 0.00229 | 68 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [10.527 9.7282] | 1.78 | 0.00236 | 66 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [9.4796 10.44] | 14.3 | 0.000116 | 1 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [9.3624 9.8625] | 14.5 | 0.000765 | 27 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [9.4972 10.706] | 14.3 | 0.000658 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [8.7662 9.0285] | 14.6 | 0.000662 | 29 | A bad approximation caused failure to predict improvement. |
