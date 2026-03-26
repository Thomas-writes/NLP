# CERI651DLS

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
| CG | fail | [386.28 -634.51 -466.16 435 1485.9 -1291.4 11891] | inf | 0.000101 | 0 | NaN result encountered. |
| CG | fail | [602.25 -559.54 1483.6 -1416.2 1385.6 482.51 12642] | nan | 0.00104 | 1 | NaN result encountered. |
| CG | fail | [1342.9 -113.75 979.53 -238.53 -2300.9 -294.06 11121] | inf | 5.62e-05 | 0 | NaN result encountered. |
| BFGS | fail | [4244.3 668.43 -1278.1 -910.56 465.66 -1970.7 10574] | 20.4 | 0.0138 | 263 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-414.98 1176.2 -643.36 1727.5 -1572.6 -509.22 13623] | inf | 9.67e-05 | 0 | NaN result encountered. |
| BFGS | fail | [-1555.9 450.66 -1417.2 488.15 -1512.4 1052.4 13219] | inf | 5.06e-05 | 0 | NaN result encountered. |
| dogleg | fail | [-507.89 3882.8 -621.65 1595.7 -2537 -220.56 14766] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [-1731.9 -587.39 891.5 -560.38 610.4 368.95 13255] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [63.925 -432.16 -82.771 1391.7 -101.05 1965.9 13227] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [1607 -61.121 1549.3 309.82 1265.6 1546.7 12925] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-144.57 1285.7 -134 -719.72 -2102.5 -212.32 13316] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [1443.2 -1278.4 2148.6 -504.31 -410 -3386.2 10992] | nan | nan | None | array must not contain infs or NaNs |
