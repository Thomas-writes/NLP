# CHWIRUT2LS

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.14637 0.032105 -0.0962] | 9.05e+04 | 0.000622 | 2 | Optimization terminated successfully. |
| CG | success | [0.1121 -0.16492 0.0043351] | 9.05e+04 | 0.00234 | 9 | Optimization terminated successfully. |
| CG | success | [0.02753 -0.071439 -0.19154] | 9.05e+04 | 0.0014 | 10 | Optimization terminated successfully. |
| BFGS | fail | [0.056793 -0.074105 0.12418] | 8.83e+04 | 0.000301 | 1 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [0.13149 0.10373 0.050116] | 513 | 0.00182 | 24 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [0.1654 -0.023412 -0.033315] | 9.05e+04 | 0.000114 | 2 | Optimization terminated successfully. |
| dogleg | fail | [0.032583 -0.20421 0.12684] | 9.71e+04 | 0.00049 | 3 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.12101 0.16602 -0.068549] | 8.37e+03 | 0.000719 | 14 | A bad approximation caused failure to predict improvement. |
| dogleg | fail | [0.10998 0.096063 0.15851] | 7.84e+04 | 6.65e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.096335 0.069638 -0.15101] | 4.45e+05 | 0.00515 | 169 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.057943 -0.097157 0.12373] | 6.41e+05 | 0.0184 | 600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.035449 -0.072387 -0.0094349] | 1.06e+05 | 0.000186 | 1 | A bad approximation caused failure to predict improvement. |
