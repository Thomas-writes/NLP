# LANCZOS2LS

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
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.5365 0.44839 5.2007 5.6843 5.6283 8.2716] | 1.03e-06 | 0.0172 | 381 | Optimization terminated successfully. |
| CG | success | [1.5195 -0.45324 4.958 7.7515 6.3553 7.2408] | 5.09e-06 | 0.00716 | 131 | Optimization terminated successfully. |
| CG | success | [1.5493 -0.013605 5.3461 6.2017 7.4724 8.4799] | 9.46e-07 | 0.0245 | 473 | Optimization terminated successfully. |
| BFGS | success | [1.2705 0.10141 4.0247 4.8411 7.067 6.6006] | 4.3e-06 | 0.00384 | 97 | Optimization terminated successfully. |
| BFGS | success | [1.139 0.10181 4.6137 5.6695 6.0428 7.3741] | 4.3e-06 | 0.00351 | 95 | Optimization terminated successfully. |
| BFGS | success | [1.1095 0.64508 5.5111 7.3128 6.3819 7.3223] | 1.29e-07 | 0.00264 | 68 | Optimization terminated successfully. |
| dogleg | fail | [-1.4218 -0.62737 6.2516 6.3878 5.8661 6.7822] | 200 | 0.000136 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.95057 -0.21214 6.231 6.1746 6.5015 8.1214] | 271 | 8.12e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [2.2504 -1.1081 6.0478 5.7075 6.0625 7.0944] | 903 | 7.02e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [2.301 0.34667 4.5716 5.9965 7.7969 7.4803] | 141 | 0.00133 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.3206 0.25356 5.6825 5.1655 8.1319 7.1529] | 211 | 0.00122 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.2161 1.204 5.1774 5.9798 6.6265 7.5781] | 126 | 0.0011 | 28 | A bad approximation caused failure to predict improvement. |
