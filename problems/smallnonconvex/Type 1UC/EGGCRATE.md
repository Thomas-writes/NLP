# EGGCRATE

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.81114 2.2444] | 9.49 | 0.000257 | 4 | Optimization terminated successfully. |
| CG | success | [1.1532 1.7548] | 9.49 | 0.000319 | 6 | Optimization terminated successfully. |
| CG | success | [0.80709 1.9757] | 9.49 | 0.000304 | 7 | Optimization terminated successfully. |
| BFGS | success | [1.1436 2.0058] | 9.49 | 0.000295 | 7 | Optimization terminated successfully. |
| BFGS | success | [0.69799 1.9231] | 9.49 | 0.000314 | 9 | Optimization terminated successfully. |
| BFGS | success | [0.53662 1.9501] | 9.49 | 0.000285 | 8 | Optimization terminated successfully. |
| dogleg | fail | [0.9135 2.0428] | 40.5 | 6.11e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.2556 1.7751] | 51.3 | 5.5e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.85483 2.0812] | 38.3 | 5.33e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.1286 1.8761] | 20.2 | 0.000728 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.73049 1.8934] | 20.4 | 0.000695 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0938 1.8262] | 22.2 | 0.000108 | 2 | A bad approximation caused failure to predict improvement. |
