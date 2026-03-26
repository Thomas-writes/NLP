# MGH17SLS

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
- **# of Variables (n):** 5
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [40.855 139.86 -110.83 77.063 220.05] | 1.02 | 0.001 | 14 | Optimization terminated successfully. |
| CG | success | [26.207 168.18 -144.96 65.868 196.32] | 1.02 | 0.00174 | 42 | Optimization terminated successfully. |
| CG | success | [21.004 194.21 -104.24 106.17 193.82] | 1.02 | 0.00114 | 15 | Optimization terminated successfully. |
| BFGS | success | [59.193 163.18 -96.096 49.497 238.77] | 1.02 | 0.000722 | 20 | Optimization terminated successfully. |
| BFGS | success | [48.315 112.29 -48.069 77.699 174.75] | 1.02 | 0.000906 | 21 | Optimization terminated successfully. |
| BFGS | success | [53.591 166.8 -107.97 115.6 169.98] | 1.02 | 0.00133 | 30 | Optimization terminated successfully. |
| dogleg | fail | [16.414 139.56 -97.007 82.749 182.05] | 1.14e+04 | 6.97e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [59.283 164.32 -129.07 60.564 223.68] | 1.19e+05 | 6.31e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [68.082 166 -116.82 95.836 218.31] | 1.59e+05 | 5.94e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [28.265 147.04 -93.906 110.23 177.04] | 1.32e+04 | 0.0251 | 678 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [49.416 132.18 -118.95 78.25 173.5] | 1.11e+03 | 0.0184 | 454 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [40.877 173.92 -130.01 90.352 231.78] | 9.44e+03 | 0.0295 | 726 | A bad approximation caused failure to predict improvement. |
