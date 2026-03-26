# LOGHAIRY

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
- **Objective Type:** other
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [-567.26 -765.24] | 4.88 | 0.00797 | 95 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [-589.5 -613.18] | 6.42 | 0.00103 | 7 | Desired error not necessarily achieved due to precision loss. |
| CG | success | [-602.17 -797.01] | 0.182 | 0.00406 | 44 | Optimization terminated successfully. |
| BFGS | success | [-524.27 -813.41] | 0.182 | 0.00411 | 51 | Optimization terminated successfully. |
| BFGS | success | [-487.5 -669.71] | 0.182 | 0.00686 | 112 | Optimization terminated successfully. |
| BFGS | success | [-521.89 -636.3] | 0.182 | 0.00303 | 45 | Optimization terminated successfully. |
| dogleg | fail | [-339.44 -829.5] | 6.72 | 6.25e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-478.69 -766.97] | 6.64 | 4.86e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-426.97 -702.2] | 6.56 | 5.21e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-501.54 -597.76] | 6.4 | 0.00028 | 6 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-517.18 -664.58] | 6.5 | 0.000726 | 32 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-412.49 -704.13] | 6.56 | 0.000717 | 32 | A bad approximation caused failure to predict improvement. |
