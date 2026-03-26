# ECKERLE4LS

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
| CG | success | [-14.464 1.9724 445.04] | 0.00146 | 0.00144 | 18 | Optimization terminated successfully. |
| CG | success | [45.04 -64.666 468.27] | 0.00146 | 0.0019 | 23 | Optimization terminated successfully. |
| CG | success | [-46.273 3.357 482.8] | 0.00146 | 0.00325 | 39 | Optimization terminated successfully. |
| BFGS | success | [3.0565 95.548 465.98] | 0.00146 | 0.00165 | 44 | Optimization terminated successfully. |
| BFGS | success | [3.0675 34.126 524.33] | 0.00146 | 0.002 | 53 | Optimization terminated successfully. |
| BFGS | success | [-97.571 41.172 598.17] | 0.7 | 0.000428 | 11 | Optimization terminated successfully. |
| dogleg | fail | [9.5938 17.889 506.96] | 1.33 | 6.58e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-70.546 -61.487 481] | 28.4 | 5.96e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-15.509 46.955 557.14] | 0.942 | 5.69e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-8.3142 30 544] | 0.483 | 0.0236 | 600 | Maximum number of iterations has been exceeded. |
| trust-ncg | success | [33.484 -22.134 525.1] | 0.7 | 0.000428 | 7 | Optimization terminated successfully. |
| trust-ncg | success | [23.591 -24.133 489.49] | 0.00146 | 0.0185 | 477 | Optimization terminated successfully. |
