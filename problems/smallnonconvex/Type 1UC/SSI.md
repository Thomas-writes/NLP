# SSI

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
| CG | success | [1.0856 0.97231 0.97792] | 4.82e-05 | 0.0239 | 394 | Optimization terminated successfully. |
| CG | fail | [0.94323 1.0345 0.9995] | 5.17e-05 | 0.0319 | 600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.91724 0.79327 1.2272] | 0.000108 | 0.026 | 600 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [1.0924 0.84161 1.0126] | 9.97e-07 | 0.021 | 600 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [0.87315 1.171 0.84691] | 9.48e-07 | 0.0257 | 600 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [1.0104 0.99977 1.2444] | 1.02e-06 | 0.0228 | 600 | Maximum number of iterations has been exceeded. |
| dogleg | fail | [0.81532 1.0312 1.1724] | 7.69 | 5.73e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.088 0.8634 1.0617] | 5.4 | 5.25e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.0575 0.97679 1.1486] | 5.9 | 5.03e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.91764 1.0117 0.98939] | 0.0523 | 0.0147 | 600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [1.0762 1.128 1.0372] | 0.0527 | 0.0161 | 567 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.89338 0.95421 0.97948] | 0.0516 | 0.0166 | 600 | Maximum number of iterations has been exceeded. |
