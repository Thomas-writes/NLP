# PALMER3C

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
| CG | fail | [0.814 1.15 1.02 1.19 1.16 0.995 1.15 1] | 0.134 | 0.0695 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.21 1.05 1.01 1.06 1.02 1.26 0.938 1.08] | 16.1 | 0.0536 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.911 0.989 1 1 0.844 1.03 0.863 1.02] | 0.148 | 0.073 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [1.01 1.03 1.08 0.956 0.927 1.03 0.887 0.957] | 0.0195 | 0.0015 | 51 | Optimization terminated successfully. |
| BFGS | success | [1.12 0.873 1.03 0.993 0.857 1.07 0.934 1.15] | 0.0195 | 0.00155 | 47 | Optimization terminated successfully. |
| BFGS | success | [0.911 0.965 1.13 1.13 0.908 0.897 1.01 0.965] | 0.0195 | 0.00147 | 49 | Optimization terminated successfully. |
| dogleg | success | [0.845 1.27 0.97 1.02 1.1 0.917 0.894 0.903] | 0.0195 | 0.000391 | 7 | Optimization terminated successfully. |
| dogleg | success | [1.1 0.933 0.904 1.03 1.03 1.07 1.21 1] | 0.0195 | 0.00037 | 7 | Optimization terminated successfully. |
| dogleg | success | [1.05 1.15 1.14 1.12 0.983 0.772 1.06 0.802] | 0.0195 | 0.000361 | 7 | Optimization terminated successfully. |
| trust-ncg | fail | [0.902 1.07 0.934 1.06 1.14 1.16 1.04 1.02] | 3.42e+03 | 0.000193 | 4 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.908 1.13 0.802 1.06 1.05 1.01 0.988 0.865] | 3.23e+03 | 0.000192 | 5 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.02 0.964 1 0.986 0.997 1.07 1.08 0.943] | 2.47e+03 | 0.00101 | 36 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: trust-ncg
- Time: 0.000192 s
- Iterations: 5
- Objective: 3.23e+03

### Least Iterations (iter)
- Method: trust-ncg
- Time: 0.000193 s
- Iterations: 4
- Objective: 3.42e+03

### Best Objective (f)
- Method: BFGS
- Time: 0.0015 s
- Iterations: 51
- Objective: 0.0195
