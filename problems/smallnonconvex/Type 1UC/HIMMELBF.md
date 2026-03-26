# HIMMELBF

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [52.811 322.07 1475.6 -281.32] | 319 | 0.018 | 389 | Desired error not necessarily achieved due to precision loss. |
| CG | success | [-23.07 388.89 1481.7 71.482] | 319 | 0.0224 | 500 | Optimization terminated successfully. |
| CG | success | [-22.67 -70.915 1505 34.758] | 319 | 0.00678 | 115 | Optimization terminated successfully. |
| BFGS | success | [-13.08 144.36 1265.1 106.33] | 319 | 0.00376 | 88 | Optimization terminated successfully. |
| BFGS | success | [20.12 -124.63 1501.7 -13.516] | 319 | 0.00236 | 74 | Optimization terminated successfully. |
| BFGS | success | [101.39 83.505 1446.8 -236.56] | 457 | 0.00345 | 89 | Optimization terminated successfully. |
| dogleg | fail | [112.99 206.57 1713.5 -24.657] | 4.3e+10 | 6.23e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [87.877 178.21 1776 0.56565] | 2.31e+10 | 5.59e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-91.705 275.83 1541.7 -59.484] | 1.4e+10 | 5.37e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-4.006 163.61 1592.4 -161.33] | 6.27e+04 | 0.000663 | 26 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [260.84 -63.968 1586.9 58.774] | 3.68e+04 | 0.041 | 800 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [114.54 -41.455 1447.7 -118.94] | 3.84e+04 | 1.02 | 65 | A bad approximation caused failure to predict improvement. |
