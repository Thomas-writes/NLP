# PALMER1C

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
| CG | fail | [0.89 0.846 1 0.929 0.786 1.03 1.02 1.06] | 5.24 | 0.0717 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.05 1.03 1.07 0.987 1.22 0.767 1.07 0.833] | 4.95 | 0.0674 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.937 0.991 1.03 1.09 0.994 0.878 1.14 0.961] | 5.91 | 0.078 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [1.02 1.1 0.871 0.995 1.05 0.897 1.1 1.03] | 0.0976 | 0.00118 | 37 | Optimization terminated successfully. |
| BFGS | success | [0.941 1.18 1.09 0.98 0.933 1 0.976 0.95] | 0.0976 | 0.00111 | 37 | Optimization terminated successfully. |
| BFGS | success | [0.911 0.91 0.93 1.16 0.995 0.877 1.09 1.08] | 0.0976 | 0.00111 | 37 | Optimization terminated successfully. |
| dogleg | success | [0.861 1.07 0.904 1.01 1.06 1.02 1.15 0.904] | 0.0976 | 0.00052 | 9 | Optimization terminated successfully. |
| dogleg | success | [1.05 1.17 1.12 0.763 1.06 0.918 1.13 1.02] | 0.0976 | 0.00049 | 9 | Optimization terminated successfully. |
| dogleg | success | [1.04 0.978 1.05 1.12 0.999 1.14 1.06 1.08] | 0.0976 | 0.000481 | 9 | Optimization terminated successfully. |
| trust-ncg | fail | [0.964 0.838 1.08 1.01 1.05 1.04 0.971 0.98] | 1.67e+05 | 0.000861 | 32 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.16 1.07 0.887 1 1.05 1.21 0.929 0.926] | 1.82e+05 | 0.000942 | 32 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.19 0.955 1.01 0.886 1.07 1.17 1.18 1.01] | 2.14e+05 | 0.000247 | 7 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: trust-ncg
- Time: 0.000247 s
- Iterations: 7
- Objective: 2.14e+05

### Least Iterations (iter)
- Method: trust-ncg
- Time: 0.000247 s
- Iterations: 7
- Objective: 2.14e+05

### Best Objective (f)
- Method: BFGS
- Time: 0.00118 s
- Iterations: 37
- Objective: 0.0976
