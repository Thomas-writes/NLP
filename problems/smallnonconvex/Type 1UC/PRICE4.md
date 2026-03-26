# PRICE4

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.69131 5.476] | 1.04e-07 | 0.0011 | 15 | Optimization terminated successfully. |
| CG | success | [1.1205 4.5842] | 1.13e-14 | 0.000585 | 11 | Optimization terminated successfully. |
| CG | success | [0.82455 4.6309] | 1.51e-15 | 0.000758 | 15 | Optimization terminated successfully. |
| BFGS | success | [0.19891 5.9296] | 9.01e-18 | 0.000865 | 20 | Optimization terminated successfully. |
| BFGS | success | [1.438 5.0375] | 6.83e-17 | 0.000579 | 16 | Optimization terminated successfully. |
| BFGS | success | [1.7468 4.9435] | 3.49e-17 | 0.000568 | 17 | Optimization terminated successfully. |
| dogleg | fail | [1.2018 4.9763] | 1.14e+04 | 9.63e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.72295 5.7968] | 3.68e+04 | 6.09e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.60744 5.5722] | 2.96e+04 | 6.07e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.1297 5.1316] | 1.47e+04 | 0.000132 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.4274 4.9372] | 11.5 | 0.00919 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [1.2257 4.9511] | 2.21 | 0.0109 | 332 | A bad approximation caused failure to predict improvement. |
