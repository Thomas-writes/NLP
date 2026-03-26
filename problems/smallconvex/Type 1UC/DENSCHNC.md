# DENSCHNC

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
| CG | success | [1.7473 2.2967] | 0.183 | 0.000731 | 14 | Optimization terminated successfully. |
| CG | success | [2.4978 3.3976] | 0.183 | 0.000305 | 7 | Optimization terminated successfully. |
| CG | success | [2.1725 2.817] | 0.183 | 0.000504 | 12 | Optimization terminated successfully. |
| BFGS | success | [1.3644 3.0867] | 5.48e-13 | 0.000903 | 20 | Optimization terminated successfully. |
| BFGS | success | [2.231 3.2041] | 2.04e-12 | 0.00077 | 23 | Optimization terminated successfully. |
| BFGS | success | [2.2283 3.0125] | 1.1e-12 | 0.00067 | 20 | Optimization terminated successfully. |
| dogleg | success | [2.5133 2.6609] | 4.05e-26 | 0.000419 | 10 | Optimization terminated successfully. |
| dogleg | fail | [1.61 3.0404] | 0.329 | 0.000228 | 5 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | success | [1.7115 2.8947] | 9.94e-18 | 0.000402 | 11 | Optimization terminated successfully. |
| trust-ncg | fail | [1.4955 3.1003] | 0.0196 | 0.000928 | 34 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.0691 2.65] | 0.39 | 0.000773 | 31 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.8532 2.879] | 0.067 | 0.000801 | 33 | A bad approximation caused failure to predict improvement. |
