# PALMER8C

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-02-19

## Classification
- **Convexity:** Convex
- **Degree:** Quadratic
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [1.04 1.16 1.12 1.05 1.03 1.03 0.881 1.05] | 0.565 | 0.0701 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.05 1.16 1.15 0.993 1.05 0.93 1.03 1.16] | 0.311 | 0.0751 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.05 1.02 0.928 0.976 1.15 1.24 0.971 0.959] | 0.426 | 0.0663 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [1.14 0.912 1.11 0.907 1.03 1.11 0.873 0.988] | 0.16 | 0.00161 | 51 | Optimization terminated successfully. |
| BFGS | success | [1.05 0.849 1.13 0.982 1.02 1.01 1.08 1.1] | 0.16 | 0.00148 | 50 | Optimization terminated successfully. |
| BFGS | success | [1.06 1.06 0.919 1.01 1.03 0.929 0.937 1.1] | 0.16 | 0.00165 | 54 | Optimization terminated successfully. |
| dogleg | success | [1.09 0.996 1.07 1.25 1.16 1.02 1.2 0.869] | 0.16 | 0.000478 | 9 | Optimization terminated successfully. |
| dogleg | success | [1.03 1 1.06 0.946 1.09 0.927 0.998 1.11] | 0.16 | 0.00045 | 9 | Optimization terminated successfully. |
| dogleg | success | [0.833 1.05 0.967 1.26 1.02 0.9 1 0.913] | 0.16 | 0.000461 | 9 | Optimization terminated successfully. |
| trust-ncg | fail | [0.959 1.04 0.983 1.03 0.844 0.989 0.96 1.22] | 707 | 0.000887 | 34 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.05 0.968 0.896 1.03 0.966 1.06 0.978 0.999] | 565 | 0.000869 | 35 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.07 0.872 0.788 1.16 1.04 0.954 0.876 0.958] | 559 | 0.000708 | 33 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: dogleg
- Time: 0.00045 s
- Iterations: 9
- Objective: 0.16

### Least Iterations (iter)
- Method: dogleg
- Time: 0.000478 s
- Iterations: 9
- Objective: 0.16

### Best Objective (f)
- Method: BFGS
- Time: 0.00161 s
- Iterations: 51
- Objective: 0.16
