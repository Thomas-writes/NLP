# MUONSINELS

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
- **Objective Type:** sum of squares
- **# of Variables (n):** 1
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [4.7683] | 4.39e+04 | 0.000793 | 4 | Optimization terminated successfully. |
| CG | success | [5.463] | 6.5e-06 | 0.000619 | 4 | Optimization terminated successfully. |
| CG | success | [5.5417] | 6.5e-06 | 0.000605 | 5 | Optimization terminated successfully. |
| BFGS | fail | [5.2836] | 4.75e+04 | 0.00609 | 8 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [5.3267] | 6.5e-06 | 0.000657 | 5 | Optimization terminated successfully. |
| BFGS | success | [5.0716] | 4.66e+04 | 0.000538 | 8 | Optimization terminated successfully. |
| dogleg | success | [4.9181] | 4.39e+04 | 0.000485 | 4 | Optimization terminated successfully. |
| dogleg | fail | [5.6085] | 3.73e+04 | 9.64e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | success | [5.8085] | 6.5e-06 | 0.000438 | 4 | Optimization terminated successfully. |
| trust-ncg | fail | [5.9277] | 1.71e+03 | 0.000137 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [5.1414] | 5.87e+04 | 0.000192 | 1 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [5.9783] | 158 | 0.000121 | 0 | A bad approximation caused failure to predict improvement. |
