# GAUSS2LS

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
| CG | fail | [97.317 -16.41 102.37 99.541 12.251 82.184 153.63 -10.854] | inf | 0.000116 | 0 | NaN result encountered. |
| CG | fail | [96.08 18.062 97.402 102.25 -8.6014 100.9 146.14 24.008] | 2.89e+04 | 0.0152 | 199 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [77.191 4.114 133.56 108.14 13.903 67.933 144.94 10.409] | 2.77e+05 | 0.000865 | 3 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [98.984 0.28335 92.824 131.24 32.176 58.747 156 26.173] | 1.25e+03 | 0.00358 | 23 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [92.353 7.9766 85.304 105.33 18.317 77.599 150.62 51.704] | 1.04e+05 | 0.000881 | 8 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [123.01 11.309 122.36 77.383 21.777 67.828 142.57 8.1561] | 3.15e+04 | 0.00826 | 143 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [99.078 -12.585 94.19 117.04 30.293 87.255 138.77 9.8472] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [116.04 2.1894 110.67 117.83 21.178 67.745 159.59 -1.0519] | 7.01e+05 | 0.000138 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [90.16 -7.7131 109.22 133.18 -4.3684 74.188 130.01 25.717] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [93.604 -1.2116 96.655 89.945 23.472 66.061 144.94 22.681] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [124.2 -21.758 122.58 122.84 -3.412 108 133.55 -2.7484] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [96.274 2.9638 101.54 103.28 26.004 67.647 156.9 13.868] | nan | nan | None | array must not contain infs or NaNs |
