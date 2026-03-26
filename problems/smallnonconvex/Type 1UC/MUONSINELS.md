# MUONSINELS

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
- **# of Variables (n):** 1
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [4.9369] | 4.39e+04 | 0.00218 | 5 | Desired error not necessarily achieved due to precision loss. |
| CG | success | [5.0081] | 4.75e+04 | 0.000979 | 6 | Optimization terminated successfully. |
| CG | success | [5.332] | 6.5e-06 | 0.000778 | 4 | Optimization terminated successfully. |
| BFGS | success | [4.9447] | 4.39e+04 | 0.000398 | 5 | Optimization terminated successfully. |
| BFGS | fail | [5.0455] | 4.66e+04 | 0.00222 | 8 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [5.478] | 6.5e-06 | 0.000366 | 4 | Optimization terminated successfully. |
| dogleg | success | [4.7682] | 4.39e+04 | 0.0004 | 3 | Optimization terminated successfully. |
| dogleg | fail | [5.5297] | 4.77e+04 | 0.0001 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [5.4675] | 5.46e+04 | 0.000103 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [4.8474] | 4.52e+04 | 0.00026 | 1 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [4.1299] | 5.44e+04 | 0.0033 | 30 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [4.8137] | 4.44e+04 | 0.00345 | 30 | A bad approximation caused failure to predict improvement. |
