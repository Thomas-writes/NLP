# RECIPELS

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.9392 4.97 1.1406] | 9.26e-09 | 0.00129 | 20 | Optimization terminated successfully. |
| CG | success | [1.3173 5.0746 0.82867] | 8.81e-11 | 0.00095 | 22 | Optimization terminated successfully. |
| CG | success | [2.1646 4.963 0.60096] | 9.5e-14 | 0.000557 | 13 | Optimization terminated successfully. |
| BFGS | success | [0.94084 4.3994 1.1483] | 1.95e-08 | 0.00074 | 24 | Optimization terminated successfully. |
| BFGS | success | [1.2634 4.7535 1.1201] | 2.46e-09 | 0.000784 | 27 | Optimization terminated successfully. |
| BFGS | success | [1.1095 5.2817 1.4091] | 3.06e-08 | 0.000623 | 19 | Optimization terminated successfully. |
| dogleg | success | [2.3416 4.0917 0.26714] | 5.14e-10 | 0.00064 | 17 | Optimization terminated successfully. |
| dogleg | success | [1.8285 5.4378 1.0694] | 4.06e-10 | 0.000638 | 18 | Optimization terminated successfully. |
| dogleg | success | [0.71164 5.3415 0.072426] | 3.77e-10 | 0.000642 | 18 | Optimization terminated successfully. |
| trust-ncg | fail | [1.9284 4.3448 1.5109] | 50.6 | 0.012 | 600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [2.1196 4.4483 0.41664] | 2.72 | 0.000291 | 5 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.5586 4.1896 0.34443] | 2.47 | 0.00024 | 5 | A bad approximation caused failure to predict improvement. |
