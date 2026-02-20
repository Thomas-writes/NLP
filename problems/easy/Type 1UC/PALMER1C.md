# PALMER1C

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
| CG | fail | [1.05 1.1 1.04 0.895 0.871 1.18 1.09 1.11] | 2.34 | 0.0713 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.06 0.973 0.987 0.827 1.18 1.03 1.05 1] | 4.37 | 0.0729 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.991 1.06 0.878 1.15 1.02 0.945 0.895 0.945] | 5 | 0.0757 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [0.989 0.906 0.965 1.04 1.16 1.08 1.03 0.901] | 0.0976 | 0.00112 | 37 | Optimization terminated successfully. |
| BFGS | success | [0.913 1.07 1.14 1 0.876 0.931 0.937 0.969] | 0.0976 | 0.00111 | 37 | Optimization terminated successfully. |
| BFGS | success | [1.25 0.915 0.825 0.964 1.16 1.05 0.971 1.03] | 0.0976 | 0.0013 | 37 | Optimization terminated successfully. |
| dogleg | success | [1.01 1.04 1.05 0.96 1.08 1.01 0.989 0.957] | 0.0976 | 0.000506 | 9 | Optimization terminated successfully. |
| dogleg | success | [1 0.98 1.09 1.04 1.01 0.998 1.01 1] | 0.0976 | 0.000485 | 9 | Optimization terminated successfully. |
| dogleg | success | [1.13 0.993 1.06 0.984 0.99 0.899 0.882 1.11] | 0.0976 | 0.000479 | 9 | Optimization terminated successfully. |
| trust-ncg | fail | [0.971 0.989 0.924 0.92 1.03 1.06 0.954 1.03] | 1.6e+05 | 0.000913 | 33 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.09 1.07 0.913 1.03 0.99 1 1.03 0.878] | 1.76e+05 | 0.000219 | 6 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.07 1.03 1.25 0.928 1.11 1.18 1.17 1.11] | 2.13e+05 | 0.00025 | 7 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: trust-ncg
- Time: 0.000219 s
- Iterations: 6
- Objective: 1.76e+05

### Least Iterations (iter)
- Method: trust-ncg
- Time: 0.000219 s
- Iterations: 6
- Objective: 1.76e+05

### Best Objective (f)
- Method: BFGS
- Time: 0.00112 s
- Iterations: 37
- Objective: 0.0976
