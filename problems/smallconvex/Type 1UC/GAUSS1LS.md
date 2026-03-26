# GAUSS1LS

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [94.621 -29.361 95.786 33.435 36.947 65.664 175.79 -6.8283] | inf | 0.000114 | 0 | NaN result encountered. |
| CG | fail | [125.83 -0.6161 104.14 44.883 17.673 69.394 176.68 -12.413] | 1.32e+03 | 0.0752 | 727 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [92.482 -4.9792 75.289 103.41 10.83 78.175 200.29 23.862] | inf | 0.000111 | 0 | NaN result encountered. |
| BFGS | fail | [120.89 14.524 94.505 80.311 -3.255 40.902 158.53 35.136] | 5.29e+04 | 0.00182 | 21 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [90.039 -16.973 98.543 69.954 36.2 78.324 161.8 -7.8131] | inf | 6.55e-05 | 0 | NaN result encountered. |
| BFGS | fail | [123.25 -8.5849 105.6 49.081 19.405 77.466 203.91 17.283] | inf | 5.81e-05 | 0 | NaN result encountered. |
| dogleg | fail | [70.432 4.7356 111.92 60.714 9.4249 79.217 169.84 8.0584] | 8.81e+05 | 0.000201 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [79.764 9.7687 77.277 63.425 33.75 88.12 188.08 20.623] | 4.36e+05 | 0.00014 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [85.36 -13.049 86.476 75.074 40.83 69.641 185.06 10.765] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [89.404 3.6865 100.12 78.357 35.547 62.086 155.24 18.602] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [104.91 -33.494 100.68 81.989 33.402 124.7 171.25 26.189] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [125.65 -16.163 65.118 88.342 8.2793 51.482 163.83 -13.745] | nan | nan | None | array must not contain infs or NaNs |
