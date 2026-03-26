# CERI651ALS

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
- **# of Variables (n):** 7
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [3952.4 -92.176 -1303 -3874.6 28987 -618.96 36147] | 3.7e+04 | 0.00277 | 32 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [3420.9 197.79 -878.56 -3351.2 30849 -6310.1 32795] | 5.34e+04 | 0.00116 | 1 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [913.91 3925.1 -66.212 -4627.2 26627 -5766.5 38556] | 5.34e+04 | 0.00191 | 9 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-553.6 -2317.3 1403.8 721.64 25789 -2479.1 42419] | nan | 0.0021 | 1 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [3279.6 -1549.2 2058.9 -716.78 28678 84.018 37070] | inf | 5.08e-05 | 0 | NaN result encountered. |
| BFGS | fail | [-1385.4 -78.04 4417.8 440.3 19415 -1628.8 41451] | nan | 0.00218 | 1 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [-3191.1 -4316.9 -606.38 -1254 24320 501.64 40397] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [505.91 467.5 1026.3 311.2 21763 693.6 29355] | 5.13e+15 | 7.05e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1714 3083.1 -4282.9 1711.3 23091 -2993.2 31622] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [2557.8 -2510.7 -848.02 22.21 25297 8414.3 39221] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-105.28 -677.36 3954.6 1145.8 24295 4479 41411] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [3764.6 -282.25 -6437.5 -3408.5 31192 -320.69 35403] | nan | nan | None | array must not contain infs or NaNs |
