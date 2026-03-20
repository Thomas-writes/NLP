# LANCZOS1LS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-03

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.2001 0.23311 5.8408 4.2097 6.1311 8.4941] | 1.42e-06 | 0.0114 | 296 | Optimization terminated successfully. |
| CG | success | [0.42738 0.1339 4.8617 5.4626 7.4557 7.5725] | 2.01e-06 | 0.0139 | 349 | Optimization terminated successfully. |
| CG | success | [-0.06283 -0.067956 4.9323 4.3577 6.9036 8.2893] | 1.2e-05 | 0.00529 | 127 | Optimization terminated successfully. |
| BFGS | success | [1.5449 1.4448 4.357 4.4581 6.722 6.7809] | 3.93e-07 | 0.00661 | 61 | Optimization terminated successfully. |
| BFGS | success | [0.36358 1.6439 5.3528 6.0611 6.4015 6.8052] | 4.29e-06 | 0.00518 | 77 | Optimization terminated successfully. |
| BFGS | success | [1.0776 0.30966 3.3158 5.0651 7.0321 7.2202] | 1.4e-07 | 0.00258 | 63 | Optimization terminated successfully. |
| dogleg | fail | [1.9426 0.72041 6.0942 5.599 6.5272 7.2376] | 362 | 6.77e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.23713 0.10347 5.5748 4.0724 6.3579 8.7229] | 196 | 5.61e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.1998 -0.60481 4.3433 5.3981 7.0282 8.969] | 268 | 5.31e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.50339 0.16609 5.931 4.5836 6.4462 6.7864] | 157 | 0.00098 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.312 0.38153 5.1635 5.9084 6.8118 7.4667] | 166 | 0.000818 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.1901 -0.35664 6.2275 6.0136 7.3112 7.2686] | 223 | 0.000919 | 28 | A bad approximation caused failure to predict improvement. |
