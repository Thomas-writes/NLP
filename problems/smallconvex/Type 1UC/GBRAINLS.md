# GBRAINLS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-25

## Classification
- **Convexity:** Convex
- **Objective Type:** sum of squares
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-3.874 0.015991] | 28.5 | 0.00385 | 8 | Optimization terminated successfully. |
| CG | success | [-3.5753 -0.12315] | 28.5 | 0.00405 | 9 | Optimization terminated successfully. |
| CG | success | [-4.5218 -0.27754] | 28.5 | 0.0153 | 22 | Optimization terminated successfully. |
| BFGS | success | [-3.6754 -0.36521] | 28.5 | 0.0035 | 10 | Optimization terminated successfully. |
| BFGS | success | [-3.3068 0.27901] | 28.5 | 0.00347 | 10 | Optimization terminated successfully. |
| BFGS | success | [-3.5143 -0.013093] | 28.5 | 0.00261 | 8 | Optimization terminated successfully. |
| dogleg | fail | [-3.7502 0.12959] | 4.39e+03 | 0.000542 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-3.186 0.61907] | 2.42e+04 | 0.000459 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-4.835 -0.98091] | 1.61e+05 | 0.000457 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-4.783 -0.38758] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-3.5797 0.054111] | 28.8 | 0.0282 | 34 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-3.5762 -0.12028] | 32.3 | 0.0379 | 31 | A bad approximation caused failure to predict improvement. |
