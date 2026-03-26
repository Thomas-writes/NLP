# MGH17LS

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
| CG | success | [43.324 129.07 -83.072 5.7021 9.0272] | 1.11 | 0.000238 | 2 | Optimization terminated successfully. |
| CG | fail | [21.044 156.01 -50.937 -8.1683 22.907] | inf | 4.35e-05 | 0 | NaN result encountered. |
| CG | fail | [73.452 120.53 -89.237 3.2398 -1.3267] | nan | 0.00222 | 1 | NaN result encountered. |
| BFGS | success | [31.695 154.24 -88.704 26.243 2.5089] | 1.11 | 0.000295 | 7 | Optimization terminated successfully. |
| BFGS | fail | [51.041 165.46 -75.156 6.087 -14.288] | inf | 4.27e-05 | 0 | NaN result encountered. |
| BFGS | fail | [41.91 156.02 -106.35 24.334 -10.847] | inf | 4.37e-05 | 0 | NaN result encountered. |
| dogleg | fail | [58.848 141.49 -93.964 -2.8296 -12.167] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [59.777 127.32 -95.231 -5.1608 -4.4398] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [63.393 138.33 -107.95 4.2662 4.455] | 1.35e+05 | 5.3e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [46.02 145.54 -91.407 0.61956 2.3518] | 8.55e+03 | 0.00513 | 157 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [76.232 153.83 -83.236 1.124 1.1098] | 1.5e+04 | 0.0149 | 456 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [23.148 173.32 -107.52 -4.8628 17.595] | nan | nan | None | array must not contain infs or NaNs |
