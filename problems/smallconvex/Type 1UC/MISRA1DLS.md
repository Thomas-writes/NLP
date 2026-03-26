# MISRA1DLS

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
| CG | success | [464.55 -89.284] | 6.76e+03 | 0.00146 | 31 | Optimization terminated successfully. |
| CG | success | [443.69 -64.255] | 6.76e+03 | 0.00193 | 50 | Optimization terminated successfully. |
| CG | success | [409.87 8.1983] | 6.76e+03 | 0.00111 | 24 | Optimization terminated successfully. |
| BFGS | success | [499.79 -35.641] | 6.76e+03 | 0.00223 | 74 | Optimization terminated successfully. |
| BFGS | success | [564.2 -109.81] | 6.76e+03 | 0.00232 | 78 | Optimization terminated successfully. |
| BFGS | fail | [477.69 34.055] | 0.0564 | 0.00408 | 57 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [537.73 -44.385] | 6.76e+03 | 0.0167 | 400 | Maximum number of iterations has been exceeded. |
| dogleg | fail | [391.84 16.109] | 1.71e+06 | 0.000103 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [611.5 -39.805] | 6.76e+03 | 0.016 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [486.31 -28.973] | 2.75e+06 | 0.000715 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [499.14 -28.318] | 2.92e+06 | 0.000688 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [537.87 54.487] | 3.43e+06 | 0.000696 | 28 | A bad approximation caused failure to predict improvement. |
