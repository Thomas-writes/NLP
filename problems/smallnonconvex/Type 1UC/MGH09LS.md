# MGH09LS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-03

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [20.381 40.767 44.283 45.157] | 0.00181 | 0.00142 | 20 | Optimization terminated successfully. |
| CG | success | [28.655 40.31 43.987 36.973] | 0.00103 | 0.00244 | 35 | Optimization terminated successfully. |
| CG | success | [20.777 35.997 33.198 38.936] | 0.000933 | 0.00707 | 121 | Optimization terminated successfully. |
| BFGS | success | [24.9 37.289 38.532 42.641] | 0.000942 | 0.00376 | 119 | Optimization terminated successfully. |
| BFGS | success | [24.849 36.458 35.366 43.897] | 0.000942 | 0.00842 | 114 | Optimization terminated successfully. |
| BFGS | success | [27.707 41.594 45.791 38.527] | 0.00186 | 0.00285 | 26 | Optimization terminated successfully. |
| dogleg | fail | [31.242 39.46 33.14 39.191] | 1.88e+03 | 6.53e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [25.546 39.138 45.681 37.644] | 856 | 5.5e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [27.015 45.041 43.084 45.535] | 1.18e+03 | 5.22e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [16.104 31.451 37.836 43.594] | 252 | 0.000693 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [18.309 40.018 47.826 32.82] | 467 | 0.000652 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [25.326 37.446 46.015 36.129] | 787 | 0.00066 | 27 | A bad approximation caused failure to predict improvement. |
