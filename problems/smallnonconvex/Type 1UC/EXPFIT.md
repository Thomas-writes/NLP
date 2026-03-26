# EXPFIT

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
| CG | success | [-0.06291 0.038139] | 0.241 | 0.000613 | 11 | Optimization terminated successfully. |
| CG | success | [-0.059858 -0.012428] | 0.241 | 0.000594 | 14 | Optimization terminated successfully. |
| CG | success | [0.037787 -6.8376e-06] | 0.241 | 0.000543 | 11 | Optimization terminated successfully. |
| BFGS | success | [-0.088642 -0.097238] | 0.241 | 0.000521 | 13 | Optimization terminated successfully. |
| BFGS | success | [0.086728 0.098372] | 0.241 | 0.000444 | 11 | Optimization terminated successfully. |
| BFGS | success | [0.045355 -0.011217] | 0.241 | 0.000407 | 11 | Optimization terminated successfully. |
| dogleg | fail | [0.04249 0.049725] | 22.8 | 7.35e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.11867 -0.059169] | 21.2 | 5.82e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.10579 -0.021199] | 27 | 5.39e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.020236 -0.03431] | 3.5 | 0.0011 | 37 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.049411 -0.064366] | 4.65 | 0.00103 | 35 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-0.043004 -0.074563] | nan | nan | None | array must not contain infs or NaNs |
