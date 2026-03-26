# BOXBODLS

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
| CG | fail | [0.97862 0.9899] | 4.91e+03 | 0.00126 | 3 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [1.0423 0.94255] | 4.91e+03 | 0.000804 | 3 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [1.1682 0.98387] | 4.91e+03 | 0.001 | 4 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [1.0407 0.96047] | 1.17e+03 | 0.000822 | 18 | Optimization terminated successfully. |
| BFGS | success | [1.1541 1.0028] | 1.17e+03 | 0.000666 | 15 | Optimization terminated successfully. |
| BFGS | fail | [1.0774 1.0719] | 5.42e+04 | 0.000259 | 1 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [1.0575 0.90441] | 1.86e+05 | 6.3e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.0373 1.0733] | 1.86e+05 | 5.49e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.95238 0.59363] | 1.87e+05 | 5.15e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.0943 1.0597] | 1.61e+05 | 0.000814 | 38 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.1568 1.0096] | 4.4e+04 | 0.000823 | 41 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.1614 0.92907] | 4.5e+04 | 0.000819 | 40 | A bad approximation caused failure to predict improvement. |
