# PALMER8C

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
| CG | fail | [0.902 1.04 1.11 0.984 1.08 0.879 0.882 0.957] | 0.377 | 0.061 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.909 0.985 0.931 1.12 0.937 1.14 1.19 1.03] | 0.589 | 0.0563 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.05 0.776 1.2 1.11 1.07 1.02 1.09 1.11] | 0.589 | 0.0607 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [1.13 1.01 0.936 1.05 1.04 0.852 1.02 0.869] | 0.16 | 0.00157 | 53 | Optimization terminated successfully. |
| BFGS | success | [1.06 0.997 0.979 1.12 0.731 0.9 0.892 1.07] | 0.16 | 0.00156 | 51 | Optimization terminated successfully. |
| BFGS | success | [0.88 1 1.04 1.05 0.946 1.01 1.04 0.842] | 0.16 | 0.00152 | 53 | Optimization terminated successfully. |
| dogleg | success | [0.953 0.892 1.11 1.22 0.813 0.896 1.05 1.17] | 0.16 | 0.000482 | 9 | Optimization terminated successfully. |
| dogleg | success | [1.02 1.08 1 1.02 0.866 0.963 0.943 0.91] | 0.16 | 0.000443 | 9 | Optimization terminated successfully. |
| dogleg | success | [0.908 0.919 1.12 1.16 0.949 0.984 0.921 0.959] | 0.16 | 0.000429 | 9 | Optimization terminated successfully. |
| trust-ncg | fail | [1.09 1.11 0.926 1.15 0.985 1.02 0.865 1.06] | 425 | 0.000792 | 34 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.02 0.999 1.1 0.881 0.803 1.07 1.03 0.923] | 408 | 0.000179 | 5 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.897 1.08 1.2 1.13 0.898 1.02 0.94 0.882] | 378 | 0.000127 | 3 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: trust-ncg
- Time: 0.000127 s
- Iterations: 3
- Objective: 378

### Least Iterations (iter)
- Method: trust-ncg
- Time: 0.000127 s
- Iterations: 3
- Objective: 378

### Best Objective (f)
- Method: BFGS
- Time: 0.00157 s
- Iterations: 53
- Objective: 0.16
