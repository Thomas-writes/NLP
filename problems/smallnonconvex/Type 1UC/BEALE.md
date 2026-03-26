# BEALE

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
| CG | success | [0.97608 1.0221] | 1.82e-13 | 0.000508 | 9 | Optimization terminated successfully. |
| CG | success | [1.1269 1.0041] | 8.92e-19 | 0.000609 | 15 | Optimization terminated successfully. |
| CG | success | [0.98086 0.86802] | 1.26e-15 | 0.000649 | 13 | Optimization terminated successfully. |
| BFGS | success | [1.1348 0.86087] | 3.55e-13 | 0.000486 | 12 | Optimization terminated successfully. |
| BFGS | success | [0.90367 0.86619] | 1.21e-14 | 0.000457 | 13 | Optimization terminated successfully. |
| BFGS | success | [1.0122 1.2391] | 2.06e-13 | 0.000478 | 14 | Optimization terminated successfully. |
| dogleg | fail | [1.0172 1.044] | 15.5 | 6e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.93407 0.93386] | 12.6 | 5.53e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.85408 0.9831] | 13.8 | 5.21e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.92493 0.97869] | 1.85 | 0.000869 | 30 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0297 0.97279] | 1.55 | 0.000221 | 4 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0189 0.7738] | 1.54 | 0.00839 | 400 | Maximum number of iterations has been exceeded. |
