# GAUSS1LS

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [126.13 1.0185 103.19 44.985 5.9744 76.634 158.79 -10.537] | 1.32e+03 | 0.0294 | 230 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [106.44 -4.5213 115.91 70.239 20.865 61.793 182.33 32.002] | inf | 0.000108 | 0 | NaN result encountered. |
| CG | fail | [97.849 6.4013 98.394 70.575 0.0057194 91.891 181.3 35.397] | 1.13e+06 | 0.000875 | 5 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [64.752 5.5044 125.2 82.538 14.258 72.41 179.13 -2.1064] | 9.91e+04 | 0.00113 | 6 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [95.825 -9.1649 98.379 69.007 18.191 106.89 170.45 21.012] | inf | 6.15e-05 | 0 | NaN result encountered. |
| BFGS | fail | [99.915 15.736 78.476 75.732 58.004 109.13 190.23 34.521] | 4.21e+04 | 0.00193 | 25 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [99.023 -22 87.174 78.926 24.518 64.078 178.19 -6.4092] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [86.888 -10.102 113.66 53.24 12.351 67.584 150.85 36.492] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [114.95 -2.3984 109.55 89.366 5.9734 61.26 184.89 22.841] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [90.873 7.9511 132.26 74.639 18.586 64.153 165.15 9.1042] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [111.24 -13.775 91.898 71.106 47.99 35.908 194.8 14.879] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [83.105 -7.8454 110.51 97.274 24.006 51.357 160.14 19.726] | nan | nan | None | array must not contain infs or NaNs |
