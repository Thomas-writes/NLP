# ROSZMAN1LS

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
| CG | success | [-73.026 -208.61 891.9 5.1898] | 0.0293 | 0.00581 | 67 | Optimization terminated successfully. |
| CG | fail | [-29.002 51.448 1010.6 6.3603] | 0.0789 | 0.136 | 800 | Maximum number of iterations has been exceeded. |
| CG | fail | [203.67 -58.523 904.36 -8.371] | 0.0229 | 0.00598 | 63 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [155.34 47.564 1009.6 29.549] | 0.0395 | 0.00333 | 100 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-66.02 -7.682 982 -96.167] | 0.0395 | 0.00353 | 114 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [106.75 -7.7301 1121.4 -308.02] | 0.0395 | 0.0033 | 90 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [-55.737 43.62 846.62 -161.94] | 2.8e+11 | 6.7e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [3.5338 -113.38 1052.3 -302.45] | 1.89e+12 | 5.97e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-2.5254 -26.708 975.51 -78.029] | 1.05e+11 | 5.68e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [57.921 233.07 978.26 -97.038] | 2.51e+04 | 0.00724 | 245 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-37.743 113.52 1006.7 -133.93] | 1.16e+04 | 0.00372 | 127 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [29.676 176.7 1046.3 -149.51] | 6.38e+03 | 0.00553 | 189 | A bad approximation caused failure to predict improvement. |
