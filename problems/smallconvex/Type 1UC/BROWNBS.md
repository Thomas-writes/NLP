# BROWNBS

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
| CG | success | [0.9152 1.0603] | 1.75e-11 | 0.00109 | 15 | Optimization terminated successfully. |
| CG | success | [1.0252 1.0228] | 0 | 0.000899 | 13 | Optimization terminated successfully. |
| CG | success | [1.118 1.0146] | 1.97e-31 | 0.000753 | 14 | Optimization terminated successfully. |
| BFGS | success | [0.93597 0.95258] | 2.51e-25 | 0.000644 | 15 | Optimization terminated successfully. |
| BFGS | success | [1.0301 0.95765] | 1.89e-23 | 0.000621 | 15 | Optimization terminated successfully. |
| BFGS | success | [0.82094 1.0436] | 6.04e-29 | 0.000686 | 17 | Optimization terminated successfully. |
| dogleg | fail | [1.246 0.92301] | 1e+12 | 0.00021 | 3 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.1356 1.0247] | 1e+12 | 0.000136 | 2 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.1206 0.91006] | 1e+12 | 0.00017 | 3 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.0554 1.0964] | 9.97e+11 | 0.0126 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [1.1541 0.97758] | 9.97e+11 | 0.0156 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.94785 0.93856] | 9.97e+11 | 0.0161 | 400 | Maximum number of iterations has been exceeded. |
