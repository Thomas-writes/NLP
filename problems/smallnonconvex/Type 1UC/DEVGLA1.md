# DEVGLA1

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [2.3143 1.7436 2.1807 1.8136] | 8.82e-18 | 0.00792 | 180 | Optimization terminated successfully. |
| CG | success | [2.2168 2.0337 1.9693 2.0359] | 3.09e-14 | 0.00575 | 128 | Optimization terminated successfully. |
| CG | success | [2.1146 2.0995 2.214 1.9971] | 9.93e-17 | 0.0182 | 291 | Optimization terminated successfully. |
| BFGS | success | [2.019 1.5082 1.845 2.0071] | 1.24e-15 | 0.00192 | 46 | Optimization terminated successfully. |
| BFGS | success | [1.9996 2.128 2.2093 1.8144] | 1.04e-17 | 0.00134 | 33 | Optimization terminated successfully. |
| BFGS | success | [2.1563 1.7529 2.0607 2.1797] | 5.14e-17 | 0.00135 | 34 | Optimization terminated successfully. |
| dogleg | fail | [1.5816 1.9457 1.7674 1.9418] | 1.09e+05 | 6.88e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [2.2266 2.0189 2.0392 2.0306] | 1.04e+05 | 6.49e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.805 1.8747 2.0094 2.0137] | 1.05e+05 | 5.6e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [2.4004 2.2021 2.1973 2.2752] | 9.55e+04 | 8.42e-05 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.9916 2.2889 2.3478 1.8198] | 9.87e+04 | 0.000564 | 27 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.9071 1.733 2.0237 1.9252] | nan | nan | None | array must not contain infs or NaNs |
