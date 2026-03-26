# HIELOW

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-0.056713 0.17845 0.96144] | 874 | 0.042 | 46 | Optimization terminated successfully. |
| CG | fail | [-0.20482 -0.018347 1.0134] | 874 | 0.0372 | 32 | Desired error not necessarily achieved due to precision loss. |
| CG | success | [0.10814 -0.20794 0.74371] | 874 | 0.0319 | 35 | Optimization terminated successfully. |
| BFGS | success | [0.016857 0.12383 1.127] | 874 | 0.00859 | 17 | Optimization terminated successfully. |
| BFGS | success | [-0.11213 0.060421 1.0007] | 874 | 0.00662 | 12 | Optimization terminated successfully. |
| BFGS | success | [-0.25321 -0.013763 1.0026] | 874 | 0.0069 | 13 | Optimization terminated successfully. |
| dogleg | fail | [0.077307 -0.15352 0.8805] | 2.21e+03 | 0.0015 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.022822 -0.056309 1.0446] | 1.15e+03 | 0.00151 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.066634 -0.055302 0.97592] | 1.06e+03 | 0.00313 | 3 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.072073 -0.38123 1.0061] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [0.13199 -0.0019522 1.026] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-0.074246 -0.0012322 1.1741] | nan | nan | None | array must not contain infs or NaNs |
