# HAHN1LS

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
| CG | fail | [8.9408 0.80974 -1.1499 0.5078 -0.44365 -1.8347 2.0411] | 41.5 | 0.054 | 659 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [10.356 -0.37526 0.59598 2.1 0.77677 0.12317 0.84902] | 39.4 | 0.11 | 1400 | Maximum number of iterations has been exceeded. |
| CG | fail | [9.2009 -1.5478 -0.47945 -0.99314 -1.019 0.11383 0.58037] | 44.7 | 0.101 | 1400 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [9.077 -2.8206 0.065932 1.6706 0.29759 0.51878 0.43867] | 1.53 | 0.01 | 195 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [10.731 -3.1821 -1.163 0.19371 -0.1947 -0.79736 -2.0973] | 32.1 | 0.00559 | 132 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [9.1904 -1.3651 0.047771 -0.58731 0.41567 -1.4347 1.3911] | 1.53 | 0.0128 | 213 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [9.4817 -1.0758 -0.41832 1.1856 0.04394 0.17701 -0.68377] | 6.78e+04 | 0.000173 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [11.532 -2.0733 -0.50024 0.28933 -0.27314 -0.26507 -0.50834] | 5.94e+04 | 0.000118 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [11.076 -1.6703 0.95399 -0.95123 1.17 2.738 -1.4459] | 5.12e+04 | 0.000114 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [10.804 -0.46703 -0.5737 -2.3203 -1.4687 -0.87013 -0.17453] | 6.9e+03 | 0.00533 | 55 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [9.8647 -0.53353 -1.2422 0.23712 0.58977 1.8416 0.30551] | 7.21e+03 | 0.00556 | 57 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [9.5168 -0.74218 1.8413 -1.0505 -0.54796 0.91055 0.85643] | 5.72e+04 | 0.00567 | 54 | A bad approximation caused failure to predict improvement. |
