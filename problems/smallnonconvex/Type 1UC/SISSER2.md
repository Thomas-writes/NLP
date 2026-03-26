# SISSER2

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
| CG | success | [0.97262 0.12295] | 2.11e-08 | 0.000423 | 6 | Optimization terminated successfully. |
| CG | success | [1.036 0.21827] | 6.86e-09 | 0.000264 | 4 | Optimization terminated successfully. |
| CG | success | [0.94521 0.095796] | 9.93e-09 | 0.00036 | 6 | Optimization terminated successfully. |
| BFGS | success | [1.0392 0.15972] | 3.73e-08 | 0.000883 | 21 | Optimization terminated successfully. |
| BFGS | success | [1.0826 0.099264] | 1.31e-08 | 0.000678 | 19 | Optimization terminated successfully. |
| BFGS | success | [1.0942 0.16054] | 9.86e-09 | 0.000659 | 18 | Optimization terminated successfully. |
| dogleg | fail | [1.1366 -0.064203] | 5 | 9.75e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.0334 -0.03548] | 3.42 | 6.81e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.1087 0.22747] | 4.41 | 5.73e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | success | [1.0053 0.0056093] | 1.53e-10 | 0.000279 | 6 | Optimization terminated successfully. |
| trust-ncg | success | [0.95698 0.053666] | 4.73e-10 | 0.000486 | 14 | Optimization terminated successfully. |
| trust-ncg | success | [0.9822 -0.01684] | 8.57e-10 | 0.000449 | 16 | Optimization terminated successfully. |
