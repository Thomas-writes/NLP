# ROSENBR

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
| CG | success | [-1.1352 1.0622] | 2.54e-11 | 0.00148 | 29 | Optimization terminated successfully. |
| CG | success | [-1.3447 1.1455] | 2.59e-15 | 0.00121 | 29 | Optimization terminated successfully. |
| CG | success | [-1.381 1.2483] | 3.92e-16 | 0.00158 | 25 | Optimization terminated successfully. |
| BFGS | success | [-1.0621 1.0778] | 3.22e-17 | 0.00127 | 33 | Optimization terminated successfully. |
| BFGS | success | [-1.0689 1.0226] | 3.55e-14 | 0.00115 | 33 | Optimization terminated successfully. |
| BFGS | success | [-1.0716 1.0812] | 2.63e-14 | 0.0012 | 36 | Optimization terminated successfully. |
| dogleg | success | [-1.0908 1.0126] | 1.77e-17 | 0.000882 | 25 | Optimization terminated successfully. |
| dogleg | fail | [-1.0048 1.019] | 4.03 | 5.58e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | success | [-1.1971 1.0742] | 7.21e-21 | 0.000824 | 22 | Optimization terminated successfully. |
| trust-ncg | fail | [-1.3039 0.91111] | 4.04 | 0.000702 | 33 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-1.2242 0.83516] | 4.28 | 0.00066 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-1.2575 1.0637] | 4.25 | 0.000733 | 30 | A bad approximation caused failure to predict improvement. |
