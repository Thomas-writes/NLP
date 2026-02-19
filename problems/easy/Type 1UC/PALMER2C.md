# PALMER2C

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
| CG | fail | [1.06 0.837 0.992 0.914 1.2 0.901 1.12 0.976] | 0.172 | 0.0645 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.948 0.936 1.02 1.02 1.03 0.887 1.03 1.08] | 0.132 | 0.0735 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.974 0.894 1.03 1.01 1.08 1.17 1.14 0.949] | 0.138 | 0.0694 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [1.01 0.945 0.973 1.14 0.948 1.01 1.1 0.805] | 0.0144 | 0.00151 | 49 | Optimization terminated successfully. |
| BFGS | success | [1.02 0.99 1.11 0.872 1.15 0.963 1.05 0.943] | 0.0144 | 0.00157 | 48 | Optimization terminated successfully. |
| BFGS | success | [0.925 1.1 0.935 1.11 0.9 1.04 1.03 1.15] | 0.0144 | 0.00161 | 51 | Optimization terminated successfully. |
| dogleg | success | [1.15 0.991 1.05 1.07 0.977 0.897 1.03 1.22] | 0.0144 | 0.000378 | 7 | Optimization terminated successfully. |
| dogleg | success | [1.01 0.926 0.87 1.15 1.01 1.01 0.951 1.11] | 0.0144 | 0.000362 | 7 | Optimization terminated successfully. |
| dogleg | success | [1.18 1.05 0.986 0.94 0.965 0.686 1.02 0.827] | 0.0144 | 0.00037 | 7 | Optimization terminated successfully. |
| trust-ncg | fail | [1.04 0.99 1.14 1.29 0.98 0.979 0.998 0.996] | 1.14e+04 | 0.00097 | 34 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.994 1.17 1.15 0.801 1.1 0.895 1.06 0.996] | 1.05e+04 | 0.000275 | 8 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.892 1.07 1.01 0.969 1 1.16 0.946 0.848] | 1.32e+04 | 0.000139 | 3 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: trust-ncg
- Time: 0.000139 s
- Iterations: 3
- Objective: 1.32e+04

### Least Iterations (iter)
- Method: trust-ncg
- Time: 0.000139 s
- Iterations: 3
- Objective: 1.32e+04

### Best Objective (f)
- Method: BFGS
- Time: 0.00151 s
- Iterations: 49
- Objective: 0.0144
