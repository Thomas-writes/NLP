# GAUSS3LS

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [105.42 -8.023 90.836 121.57 40.118 78.217 144.25 60.564] | inf | 7.66e-05 | 0 | NaN result encountered. |
| CG | fail | [104.92 6.2825 95.531 127.4 11.545 53.212 134.16 35.577] | 1.35e+05 | 0.00103 | 6 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [86.965 -12.979 97.408 121.13 42.356 52.079 134.25 2.6558] | inf | 5.72e-05 | 0 | NaN result encountered. |
| BFGS | fail | [114.17 18.718 98.391 92.834 26.028 102.73 143.43 14.222] | 1.07e+04 | 0.0852 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [96.968 -4.2771 95.736 106.12 14.802 80.032 142.42 21.276] | nan | 0.00344 | 1 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [95.742 20.584 122.89 121.93 23.027 45.661 140.41 10.822] | 1.66e+05 | 0.00478 | 68 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [99.782 -9.6305 100.07 112.87 1.5097 51.735 139.14 14.168] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [95.362 9.1692 97.861 104.51 15.18 76.299 146.32 21.678] | 5.47e+05 | 0.00013 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [54.814 6.5692 94.732 82.328 21.758 74.158 155.2 23.041] | 7.33e+05 | 0.000127 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [108.28 -3.394 83.978 107.27 21.566 90.465 147.05 37.958] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [96.624 -3.2686 67.028 97.267 19.915 75.675 134.74 17.126] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [105.29 3.2971 66.281 96.299 8.8734 82.967 147.37 10.272] | nan | nan | None | array must not contain infs or NaNs |
