# GAUSS2LS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Convex
- **Objective Type:** sum of squares
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [118.38 -7.805 92.041 101.26 35.628 73.161 122.74 30.174] | inf | 8.86e-05 | 0 | NaN result encountered. |
| CG | fail | [88.322 17.047 120.04 116.48 21.959 74.051 154.68 41.348] | 2.89e+04 | 0.0103 | 141 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [97.279 20.551 119.13 100.29 21.464 57.876 186.14 -2.8368] | 1.26e+05 | 0.00195 | 12 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [75.042 -4.3196 109.41 94.587 34 66.34 140.82 27.325] | nan | 0.00365 | 1 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [118.34 1.4021 108.67 110.99 -12.173 74.89 143.68 20.606] | 1.25e+03 | 0.0033 | 25 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [92.365 0.15485 119.52 91.681 -6.3944 75.461 132.47 0.83978] | 2.52e+05 | 0.000651 | 1 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [98.227 16.27 106.79 98.035 0.29244 82.289 151.17 32.251] | 8.32e+05 | 0.000203 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [120.07 3.1484 118.85 113.21 14.863 92.399 140.48 -10.292] | 6.76e+05 | 0.000133 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [92.794 20.434 88.779 78.667 -0.93017 104.66 148.66 30.14] | 8.07e+05 | 0.000131 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| CG | fail | [96.502 -1.6634 88.993 116.24 12.179 58.384 153.5 19.393] | nan | 0.00478 | 1 | NaN result encountered. |
| CG | fail | [108.14 7.0763 103.76 103.46 -39.568 62.877 150.22 26.517] | 2.88e+04 | 0.00805 | 122 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [93.017 -14.909 123.66 91.343 11.809 91.696 148.13 22.87] | inf | 7.04e-05 | 0 | NaN result encountered. |
| BFGS | fail | [93.593 -9.8515 100.27 122 7.504 89.333 138.17 24.724] | inf | 6.82e-05 | 0 | NaN result encountered. |
| BFGS | fail | [101.11 16.966 119.61 102.62 -0.63731 75.705 135.64 27.758] | 7.38e+04 | 0.00482 | 80 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [93.449 -18.768 112.33 102.76 19.73 81.845 151.56 31.513] | inf | 6.66e-05 | 0 | NaN result encountered. |
| dogleg | fail | [75.988 -22.567 93.49 121.43 22.262 60.346 143.99 -5.0324] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [83.025 -8.0642 99.264 97.383 -2.019 91.75 153.97 -3.2466] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [110.85 15.295 74.906 104.45 34.386 81.248 152.78 18.516] | 4.3e+05 | 0.000125 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [83.488 -3.2232 121.61 94.642 3.2938 80.646 185.52 19.945] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [88.379 -3.4242 124.83 96.761 19.328 73.68 175.91 21.138] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [106.6 14.773 108.17 100.96 9.3902 104.83 157.61 41.029] | nan | nan | None | array must not contain infs or NaNs |
