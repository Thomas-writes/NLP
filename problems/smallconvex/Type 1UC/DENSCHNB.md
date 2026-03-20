# DENSCHNB

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-03

## Classification
- **Convexity:** Convex
- **Objective Type:** sum of squares
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.75728 1.0828] | 1.82e-15 | 0.000365 | 7 | Optimization terminated successfully. |
| CG | success | [0.93195 1.0608] | 1.6e-15 | 0.000254 | 6 | Optimization terminated successfully. |
| CG | success | [0.84983 1.0176] | 5.13e-17 | 0.000284 | 7 | Optimization terminated successfully. |
| BFGS | success | [0.93988 1.0137] | 2.46e-15 | 0.000334 | 10 | Optimization terminated successfully. |
| BFGS | success | [1.0576 0.91537] | 1.09e-11 | 0.000313 | 10 | Optimization terminated successfully. |
| BFGS | success | [1.0231 0.92875] | 2.3e-12 | 0.000281 | 9 | Optimization terminated successfully. |
| dogleg | success | [1.0801 1.0619] | 8.26e-13 | 0.000255 | 5 | Optimization terminated successfully. |
| dogleg | fail | [1.0029 1.016] | 6.08 | 4.86e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | success | [1.1329 0.92857] | 1.13e-11 | 0.0002 | 4 | Optimization terminated successfully. |
| trust-ncg | fail | [0.99719 1.0101] | 0.0729 | 0.000133 | 2 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.93498 0.87603] | 0.0301 | 0.000106 | 2 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.97856 1.1712] | 0.187 | 0.000631 | 30 | A bad approximation caused failure to predict improvement. |
