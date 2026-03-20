# YFITU

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-1.74 2.1209 14.845] | 1.27e-07 | 0.0207 | 552 | Optimization terminated successfully. |
| CG | success | [1.0314 -2.8475 19.966] | 3.7e-08 | 0.0147 | 390 | Optimization terminated successfully. |
| CG | success | [0.90525 0.40217 21.875] | 2.5e-07 | 0.00555 | 137 | Optimization terminated successfully. |
| BFGS | success | [1.2582 -0.54074 19.678] | 6.67e-13 | 0.0021 | 67 | Optimization terminated successfully. |
| BFGS | fail | [3.6516 -0.92328 21.904] | 5.32e+03 | 0.00195 | 57 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [1.5263 3.7787 16.323] | 6.67e-13 | 0.00423 | 115 | Optimization terminated successfully. |
| dogleg | fail | [-2.4658 -0.40838 15.714] | 9.43e+06 | 7.11e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-2.2337 -1.4787 19.865] | 7.71e+07 | 5.37e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-1.4787 0.33112 18.535] | 7.6e+04 | 0.000118 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.27221 -4.1335 20.866] | 5.23e+04 | 0.00223 | 81 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-1.9152 0.46171 15.036] | 7.14e+04 | 0.00237 | 77 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.8017 1.3749 24.167] | 2.67e+05 | 0.018 | 600 | Maximum number of iterations has been exceeded. |
