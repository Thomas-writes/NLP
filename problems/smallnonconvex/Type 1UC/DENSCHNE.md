# DENSCHNE

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.36456 2.7084 -7.9675] | 8.28e-12 | 0.000781 | 10 | Optimization terminated successfully. |
| CG | success | [1.4455 4.2981 -7.4069] | 1.11e-12 | 0.000836 | 11 | Optimization terminated successfully. |
| CG | success | [3.2588 3.2569 -6.5489] | 4.12e-15 | 0.00082 | 13 | Optimization terminated successfully. |
| BFGS | success | [0.70296 3.1003 -7.5694] | 3e-12 | 0.00106 | 24 | Optimization terminated successfully. |
| BFGS | success | [1.4152 3.5567 -7.7899] | 2e-12 | 0.00119 | 28 | Optimization terminated successfully. |
| BFGS | success | [2.9005 3.8378 -6.8075] | 4.87e-13 | 0.0012 | 26 | Optimization terminated successfully. |
| dogleg | fail | [2.3679 3.2502 -8.6436] | 197 | 7.27e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [3.5658 1.6773 -7.438] | 33.9 | 6.01e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [2.5032 3.0349 -8.6508] | 157 | 5.4e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.8939 1.6559 -7.0779] | 0.999 | 0.000746 | 31 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.4317 3.5306 -8.0365] | 0.999 | 0.000778 | 33 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [3.6202 4.2497 -8.7738] | 1 | 0.000885 | 34 | A bad approximation caused failure to predict improvement. |
