# CERI651ELS

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
| CG | fail | [1351.8 51.914 -72.661 1653.2 1623 -986.28 12282] | inf | 0.000147 | 0 | NaN result encountered. |
| CG | fail | [-2114.7 1823.3 143.67 -664.3 637.61 -820.91 10647] | inf | 5.6e-05 | 0 | NaN result encountered. |
| CG | fail | [2968.9 -1866.3 -221.75 -951.95 -1944.3 1663.7 11996] | nan | 0.00184 | 1 | NaN result encountered. |
| BFGS | fail | [-642.91 -583.09 859.49 -403.26 -1041.4 1537.7 15180] | inf | 8.44e-05 | 0 | NaN result encountered. |
| BFGS | fail | [1369.9 -946.56 3309.8 -784.32 628.58 1016.1 12824] | nan | 0.00261 | 1 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-909.57 -1332.6 -860.52 -2232.1 2728.8 -728.57 14512] | 29.9 | 0.00209 | 18 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [-358.16 -2330.5 20.589 -1518.4 9.7221 -624.54 14782] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [1034.9 393.05 808.36 481.35 -1262.6 -1293.3 14332] | nan | nan | None | array must not contain infs or NaNs |
| dogleg | fail | [1827 -354.88 -998.1 -1099 -15.775 355.72 12825] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [834.45 -2131.6 1430.2 -150.61 -664.47 -133.82 16038] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [1082.1 -601.17 539.67 -1319.3 -191.61 -252 13065] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [1228.7 601.68 -2741.5 -321.87 -1464.6 3173 13226] | nan | nan | None | array must not contain infs or NaNs |
