# WAYSEA1

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
| CG | success | [0.51114 4.6146] | 6.78e-20 | 0.00131 | 25 | Optimization terminated successfully. |
| CG | success | [1.1455 4.7224] | 9.63e-21 | 0.00124 | 31 | Optimization terminated successfully. |
| CG | success | [0.99008 4.4005] | 6.73e-18 | 0.000819 | 14 | Optimization terminated successfully. |
| BFGS | success | [2.2826 5.2102] | 6.05e-15 | 0.00126 | 35 | Optimization terminated successfully. |
| BFGS | success | [1.2144 5.2712] | 3.43e-14 | 0.00121 | 35 | Optimization terminated successfully. |
| BFGS | success | [0.34531 4.9728] | 3.14e-18 | 0.00122 | 38 | Optimization terminated successfully. |
| dogleg | success | [0.54487 5.7941] | 3.11e-28 | 0.000739 | 16 | Optimization terminated successfully. |
| dogleg | success | [0.52228 4.7289] | 7.51e-19 | 0.000568 | 14 | Optimization terminated successfully. |
| dogleg | success | [0.36472 4.5689] | 3.93e-21 | 0.00055 | 14 | Optimization terminated successfully. |
| trust-ncg | fail | [1.1789 5.1922] | 0.047 | 0.00841 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [1.0129 4.8184] | 0.088 | 0.00916 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [1.7279 3.6379] | 0.00577 | 0.000809 | 26 | A bad approximation caused failure to predict improvement. |
