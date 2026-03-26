# CERI651BLS

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
| CG | fail | [1508.7 -931.16 -2637.2 2740.9 7029.2 2756.5 27919] | inf | 8.86e-05 | 0 | NaN result encountered. |
| CG | fail | [4120.7 3562 -244.85 1464.8 7533.7 601.61 24989] | nan | 0.00106 | 1 | NaN result encountered. |
| CG | fail | [56.303 4900.5 -2041.9 436.45 2949.5 -739.79 25363] | inf | 5.23e-05 | 0 | NaN result encountered. |
| BFGS | fail | [524.85 1830.5 436.46 3774.4 1988.5 3232.2 26658] | 679 | 0.00178 | 13 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [165.7 3723.3 5120.5 -3045.3 1105.9 5303.3 29400] | inf | 5.2e-05 | 0 | NaN result encountered. |
| BFGS | fail | [-867.48 -1759.2 -613.5 -527.2 550.08 -2970.3 26845] | 679 | 0.00211 | 46 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [-1234.2 1625.3 7941.5 193.7 2106.8 4366.9 25811] | 4.38e+16 | 9.36e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [266.37 1739.7 -416.65 -2035.7 -3078.5 -124.11 27934] | 5.02e+16 | 7.65e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-3161.7 1342.5 -1554.3 -1066.6 3471.7 -660.72 21084] | 2.99e+16 | 7.44e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1656.4 1918.3 1126 502.97 2994.2 -124.23 26941] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [3045 -2297 -764.24 -1417 1602.7 4317.8 27775] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-1522.3 -3038.7 -1637.5 4810.6 4612 509.05 22203] | nan | nan | None | array must not contain infs or NaNs |
