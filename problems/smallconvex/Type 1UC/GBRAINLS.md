# GBRAINLS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-03

## Classification
- **Convexity:** Convex
- **Objective Type:** sum of squares
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [-4.2318 0.15297] | 28.5 | 0.011 | 12 | Desired error not necessarily achieved due to precision loss. |
| CG | success | [-3.8302 -0.059635] | 28.5 | 0.00449 | 12 | Optimization terminated successfully. |
| CG | success | [-4.2475 0.016385] | 28.5 | 0.00576 | 13 | Optimization terminated successfully. |
| BFGS | success | [-4.2903 -0.48802] | 28.5 | 0.004 | 12 | Optimization terminated successfully. |
| BFGS | success | [-2.9884 0.092215] | 28.5 | 0.00338 | 11 | Optimization terminated successfully. |
| BFGS | success | [-3.4157 -0.50537] | 28.5 | 0.00314 | 8 | Optimization terminated successfully. |
| dogleg | fail | [-4.5669 0.81971] | 1.22e+05 | 0.00058 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-3.5594 -0.013319] | 865 | 0.000468 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-3.65 0.41493] | 1.84e+04 | 0.000447 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-3.3657 -0.63643] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-4.1237 -0.7289] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-3.6188 -0.23799] | nan | nan | None | array must not contain infs or NaNs |
