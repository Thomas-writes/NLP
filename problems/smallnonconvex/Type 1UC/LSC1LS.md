# LSC1LS

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
| CG | success | [81.561 80.159 228.25] | 7.71 | 0.00292 | 56 | Optimization terminated successfully. |
| CG | success | [86.669 70.272 257.54] | 7.71 | 0.00242 | 44 | Optimization terminated successfully. |
| CG | success | [129.9 71.653 220.29] | 7.71 | 0.00316 | 55 | Optimization terminated successfully. |
| BFGS | success | [94.732 119.05 236.45] | 7.71 | 0.00215 | 56 | Optimization terminated successfully. |
| BFGS | success | [50.95 111.24 227.61] | 7.71 | 0.00177 | 44 | Optimization terminated successfully. |
| BFGS | success | [90.985 51.322 222.59] | 7.71 | 0.00173 | 47 | Optimization terminated successfully. |
| dogleg | fail | [103.86 71.257 201.83] | 4.92e+04 | 6.19e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [88.186 110.4 228.15] | 6.17e+04 | 5.68e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [106.13 135.66 265.25] | 6.94e+04 | 5.22e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [107.44 87.568 208.11] | 2.2e+03 | 0.0003 | 8 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [123.42 99.541 235.44] | 2.07e+03 | 0.000359 | 9 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [90.645 117.99 247.47] | 2.34e+03 | 0.00039 | 10 | A bad approximation caused failure to predict improvement. |
