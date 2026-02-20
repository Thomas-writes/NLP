# PALMER2C

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
| CG | fail | [1.22 1.05 0.935 1.25 1.08 0.929 0.893 0.995] | 0.14 | 0.0675 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.866 0.954 1.09 1.09 1.04 0.946 1.1 1.03] | 0.136 | 0.0727 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.06 1.06 1.09 1.04 0.879 0.879 0.932 0.903] | 0.0178 | 0.0749 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [0.958 1.21 1.23 0.981 0.946 0.811 0.967 0.885] | 0.0144 | 0.00138 | 44 | Optimization terminated successfully. |
| BFGS | success | [0.963 0.81 0.867 0.907 0.975 0.912 1.08 0.998] | 0.0144 | 0.00144 | 49 | Optimization terminated successfully. |
| BFGS | success | [1.04 1.04 1.05 0.97 0.962 0.98 1.03 1.08] | 0.0144 | 0.00159 | 51 | Optimization terminated successfully. |
| dogleg | success | [0.926 0.87 1.1 0.872 0.95 0.914 0.93 0.977] | 0.0144 | 0.000396 | 7 | Optimization terminated successfully. |
| dogleg | success | [0.952 0.827 0.979 0.923 1.02 1.06 0.8 0.943] | 0.0144 | 0.000361 | 7 | Optimization terminated successfully. |
| dogleg | success | [0.775 1.09 1.04 1.04 0.807 1.08 1.05 1.02] | 0.0144 | 0.00036 | 7 | Optimization terminated successfully. |
| trust-ncg | fail | [0.935 1.04 0.923 1.06 0.954 0.969 0.953 0.973] | 9.72e+03 | 0.000933 | 35 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.869 0.836 0.95 0.866 1.13 1.09 0.917 0.987] | 1.06e+04 | 0.000256 | 7 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.984 1.03 1.05 1.03 0.872 1.1 0.931 1.03] | 9.92e+03 | 0.000831 | 34 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: trust-ncg
- Time: 0.000256 s
- Iterations: 7
- Objective: 1.06e+04

### Least Iterations (iter)
- Method: dogleg
- Time: 0.000396 s
- Iterations: 7
- Objective: 0.0144

### Best Objective (f)
- Method: BFGS
- Time: 0.00138 s
- Iterations: 44
- Objective: 0.0144
