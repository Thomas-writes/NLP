# EXP2

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
| CG | success | [0.97143 5.9069] | 1.9e-13 | 0.000367 | 9 | Optimization terminated successfully. |
| CG | success | [1.2271 4.691] | 2.58e-15 | 0.000449 | 9 | Optimization terminated successfully. |
| CG | success | [1.1721 4.6349] | 1.59e-13 | 0.000497 | 11 | Optimization terminated successfully. |
| BFGS | success | [0.66561 4.6428] | 9.93e-12 | 0.000384 | 11 | Optimization terminated successfully. |
| BFGS | success | [1.9319 4.7416] | 3.62e-13 | 0.000453 | 13 | Optimization terminated successfully. |
| BFGS | success | [1.0601 4.9015] | 4.21e-13 | 0.000295 | 9 | Optimization terminated successfully. |
| dogleg | fail | [1.3157 5.1711] | 4.23 | 0.000106 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.5354 5.2758] | 4.37 | 9.68e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | success | [0.74457 3.8664] | 2.41e-15 | 0.000361 | 7 | Optimization terminated successfully. |
| trust-ncg | fail | [0.75048 5.6705] | 2.28 | 7.57e-05 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.967 4.5193] | 7.94 | 0.000775 | 31 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.2535 4.9503] | 4.75 | 0.000754 | 31 | A bad approximation caused failure to predict improvement. |
