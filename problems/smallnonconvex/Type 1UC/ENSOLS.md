# ENSOLS

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
- **# of Variables (n):** 9
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [7.8545 2.2603 4.7816 41.218 0.045851 -8.5592 25.303 -1.0474 2.6003] | 889 | 0.00766 | 70 | Optimization terminated successfully. |
| CG | success | [18.733 -1.0203 -0.60686 40.17 8.4339 -5.477 21.786 0.70561 2.0662] | 889 | 0.00673 | 55 | Optimization terminated successfully. |
| CG | success | [9.5026 -4.345 -4.9007 42.724 0.5748 -1.8185 27.88 2.4653 -3.1921] | 789 | 0.0083 | 74 | Optimization terminated successfully. |
| BFGS | success | [12.049 -2.1185 -6.3259 42.342 -3.2532 5.1093 18.915 4.5544 3.8354] | 963 | 0.00303 | 30 | Optimization terminated successfully. |
| BFGS | success | [7.0384 2.169 5.7797 37.179 -0.40881 1.4724 28.69 -3.1436 6.4624] | 889 | 0.00371 | 43 | Optimization terminated successfully. |
| BFGS | success | [7.8791 5.0495 -2.3729 42.216 -5.5128 -7.0229 24.437 -0.52316 -0.62489] | 789 | 0.00277 | 39 | Optimization terminated successfully. |
| dogleg | fail | [14.091 3.4493 -8.1179 45.17 0.64443 -5.3585 20.191 2.0811 -0.44603] | 1.29e+04 | 0.000189 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [14.455 8.2845 3.0058 39.507 -1.4589 0.65651 29.245 -3.8987 -0.85674] | 8.7e+03 | 0.00015 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [12.346 3.8349 4.2353 40.711 -4.1315 4.5354 11.914 -8.6106 -2.6331] | 1.21e+04 | 0.000147 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [15.191 9.0644 -4.435 40.346 -0.83575 0.9772 25.909 -4.1624 4.1481] | 1.23e+04 | 0.000189 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [10.018 -1.819 0.76095 35.554 -5.4471 -5.4638 26.95 8.111 6.2231] | 1.76e+04 | 0.000679 | 3 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [7.3625 4.713 3.252 41.825 1.6816 5.9029 23.803 -1.8219 -1.1148] | 8.52e+03 | 0.000844 | 4 | A bad approximation caused failure to predict improvement. |
