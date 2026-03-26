# GAUSS3LS

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [109.15 6.6312 104.5 130.22 14.324 45.337 149.15 16.488] | 1.14e+04 | 0.0175 | 238 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [88.732 -15.409 121.31 117.81 26.931 75.347 141.33 53.134] | inf | 0.00011 | 0 | NaN result encountered. |
| CG | fail | [101.17 -0.4174 94.743 115.34 10.025 78.538 149.97 38.132] | 3.27e+05 | 0.000727 | 2 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [94.259 9.5703 93.736 104.96 -8.9731 69.125 132.78 21.859] | 2.36e+05 | 0.00171 | 10 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [98.842 -2.7838 94.428 93.891 18.715 88.568 136.03 16.88] | nan | 0.00379 | 1 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [101.89 10.07 88.673 133.91 42.545 76.914 135.77 39.368] | 1.71e+05 | 0.000959 | 9 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [74.413 11.049 106.76 135.68 9.3122 79.96 123.9 1.2549] | 1.04e+06 | 0.000195 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [120.39 -1.9114 85.759 94.198 38.192 60.917 137.91 11.267] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [84.002 23.041 68.512 97.751 27.186 73.032 131.39 11.406] | 6.41e+05 | 0.00013 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [125.84 15.021 99.037 103.57 16.745 85.75 178.58 5.317] | 1.68e+05 | 0.0274 | 216 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [91.646 -17.878 101.25 123.25 14.23 69.323 141.37 32.331] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [108.9 -1.7644 92.955 95.326 10.924 87.349 145.82 3.2529] | nan | nan | None | array must not contain infs or NaNs |
