# PALMER7C

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-02-12

## Classification
- **Convexity:** Convex
- **Degree:** Quadratic
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [1.08 0.941 1 0.936 1.06 1.16 0.918 0.979] | 2.64 | 0.0597 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.888 1.13 0.886 1.02 1.14 1 0.888 0.923] | 4.31 | 0.0626 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.915 1.08 0.883 0.994 1.01 1.13 1.06 0.836] | 4.01 | 0.065 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [1.04 0.825 1.13 0.932 1.06 0.953 1.2 1.21] | 0.602 | 0.00161 | 52 | Optimization terminated successfully. |
| BFGS | success | [1.2 0.876 1.02 1.19 0.91 0.946 0.906 1] | 0.602 | 0.00146 | 50 | Optimization terminated successfully. |
| BFGS | success | [0.979 0.981 1.05 0.949 0.912 1.03 1.13 1.09] | 0.602 | 0.00146 | 50 | Optimization terminated successfully. |
| dogleg | success | [0.745 0.847 0.942 1.08 0.985 1.12 0.978 0.97] | 0.602 | 0.000539 | 11 | Optimization terminated successfully. |
| dogleg | success | [1.01 1.17 0.954 0.985 1.12 1 0.982 0.884] | 0.602 | 0.000506 | 11 | Optimization terminated successfully. |
| dogleg | success | [0.967 1.01 1.08 0.948 1.12 1.15 1.01 0.89] | 0.602 | 0.000511 | 11 | Optimization terminated successfully. |
| trust-ncg | fail | [0.992 0.964 1 0.942 1.13 1.05 0.922 0.789] | 659 | 0.000907 | 35 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.04 0.914 1.01 0.967 1.05 1.11 1.03 0.948] | 353 | 0.000806 | 36 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.928 0.869 1.06 0.947 1.01 0.987 0.8 0.815] | 381 | 0.000756 | 34 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: dogleg
- Time: 0.000506 s
- Iterations: 11
- Objective: 0.602

### Least Iterations (iter)
- Method: dogleg
- Time: 0.000539 s
- Iterations: 11
- Objective: 0.602

### Best Objective (f)
- Method: BFGS
- Time: 0.00161 s
- Iterations: 52
- Objective: 0.602
