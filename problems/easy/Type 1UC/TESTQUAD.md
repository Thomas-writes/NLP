# TESTQUAD

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
- **# of Variables (n):** 10
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.14 0.864 0.94 0.986 0.954 0.971 0.956 1.07 1.15 1.15] | 5.61e-12 | 0.00653 | 178 | Optimization terminated successfully. |
| CG | success | [0.878 1.11 1 0.995 1.09 1.04 0.94 0.851 1.07 1.08] | 1.14e-12 | 0.00747 | 229 | Optimization terminated successfully. |
| CG | success | [0.926 1.05 0.96 0.928 0.974 0.912 0.953 1.05 0.956 0.969] | 4.78e-12 | 0.00887 | 275 | Optimization terminated successfully. |
| BFGS | success | [1.05 1.07 0.957 1.06 0.988 0.989 0.957 0.885 0.895 1.12] | 3.12e-18 | 0.00074 | 14 | Optimization terminated successfully. |
| BFGS | success | [1.03 1.09 0.945 1.2 0.811 0.853 1.14 0.971 1.04 0.967] | 4.87e-21 | 0.000715 | 15 | Optimization terminated successfully. |
| BFGS | success | [1.02 0.948 1.03 1.05 1.07 1 0.972 1.17 0.983 1.12] | 5.34e-20 | 0.000674 | 14 | Optimization terminated successfully. |
| dogleg | success | [1.01 1.01 1.15 1.05 0.986 0.824 1.06 1.07 0.962 0.94] | 3.25e-28 | 0.000191 | 3 | Optimization terminated successfully. |
| dogleg | success | [0.888 1.18 0.704 0.906 0.873 1.06 0.952 0.86 1.02 0.994] | 3.21e-29 | 0.000167 | 3 | Optimization terminated successfully. |
| dogleg | success | [0.982 1.12 0.994 1.02 1.13 1.04 1.02 0.929 0.975 1] | 2.73e-28 | 0.000165 | 3 | Optimization terminated successfully. |
| trust-ncg | fail | [0.978 1.04 0.967 0.999 1.08 1.05 0.983 1.06 1.14 1.04] | 6.08 | 0.0469 | 2000 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [1.06 1.06 1.09 0.897 0.933 0.976 1.19 1.06 0.951 1.09] | 6.62 | 0.0469 | 2000 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.982 0.839 1.1 1.03 0.924 0.839 1.19 0.939 1.01 1.01] | 4.46 | 0.0465 | 2000 | Maximum number of iterations has been exceeded. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: dogleg
- Time: 0.000165 s
- Iterations: 3
- Objective: 2.73e-28

### Least Iterations (iter)
- Method: dogleg
- Time: 0.000191 s
- Iterations: 3
- Objective: 3.25e-28

### Best Objective (f)
- Method: dogleg
- Time: 0.000167 s
- Iterations: 3
- Objective: 3.21e-29
