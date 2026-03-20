# HIMMELBB

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** other
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-1.1563 1.0456] | 7.96e-09 | 0.000501 | 5 | Optimization terminated successfully. |
| CG | fail | [-1.4473 1.0398] | 3.4 | 0.000327 | 1 | Desired error not necessarily achieved due to precision loss. |
| CG | success | [-1.4197 0.72264] | 5.72e-11 | 0.000256 | 3 | Optimization terminated successfully. |
| BFGS | success | [-0.86578 0.96823] | 1.24e-10 | 0.000233 | 4 | Optimization terminated successfully. |
| BFGS | success | [-1.1701 1.0595] | 9.34e-15 | 0.000245 | 8 | Optimization terminated successfully. |
| BFGS | success | [-1.347 1.0513] | 2.18e-14 | 0.00022 | 7 | Optimization terminated successfully. |
| dogleg | fail | [-1.2275 0.92163] | 2.88e+04 | 7.05e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-1.116 0.96423] | 1.16e+04 | 5.24e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-1.2735 1.081] | 5.85e+04 | 5.11e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-1.1958 1.0772] | 3.04e-06 | 0.000262 | 8 | A bad approximation caused failure to predict improvement. |
| trust-ncg | success | [-1.2877 0.95148] | 1.99e-08 | 0.000269 | 10 | Optimization terminated successfully. |
| trust-ncg | fail | [-1.205 1.0384] | 3.82e-06 | 0.000265 | 9 | A bad approximation caused failure to predict improvement. |
