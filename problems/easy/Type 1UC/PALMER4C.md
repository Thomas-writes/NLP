# PALMER4C

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
| CG | fail | [1.01 0.907 0.834 1.04 0.857 1.1 0.831 0.909] | 0.359 | 0.062 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.04 0.982 1.13 1.18 0.964 0.92 0.973 1.01] | 0.373 | 0.0548 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.13 1.01 1.11 1.05 1.01 1.04 1.01 0.972] | 0.358 | 0.0625 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [0.998 0.805 1.11 1.14 1.13 0.918 0.971 1.07] | 0.0503 | 0.00153 | 50 | Optimization terminated successfully. |
| BFGS | success | [0.92 1.02 1.17 0.999 1.14 1.08 1.03 0.885] | 0.0503 | 0.00158 | 49 | Optimization terminated successfully. |
| BFGS | success | [1.16 0.987 1.04 0.96 1.16 0.963 1.18 1.01] | 0.0503 | 0.00148 | 48 | Optimization terminated successfully. |
| dogleg | success | [1.06 0.915 1.06 0.929 1 0.99 0.914 1.04] | 0.0503 | 0.000426 | 8 | Optimization terminated successfully. |
| dogleg | success | [1.08 1.01 1.18 1.12 0.959 1.11 1.02 0.9] | 0.0503 | 0.000409 | 8 | Optimization terminated successfully. |
| dogleg | success | [1.05 0.887 0.843 1.11 1.19 0.811 1.04 1.2] | 0.0503 | 0.000407 | 8 | Optimization terminated successfully. |
| trust-ncg | fail | [1.15 0.946 1.1 0.988 0.965 1.15 0.897 1.04] | 1.64e+03 | 0.000805 | 34 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.956 1.09 0.888 0.965 0.98 1.15 0.953 1.08] | 1.98e+03 | 0.000167 | 4 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.977 0.933 0.961 1.03 0.958 1.04 0.853 0.899] | 1.69e+03 | 0.000892 | 34 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: trust-ncg
- Time: 0.000167 s
- Iterations: 4
- Objective: 1.98e+03

### Least Iterations (iter)
- Method: trust-ncg
- Time: 0.000167 s
- Iterations: 4
- Objective: 1.98e+03

### Best Objective (f)
- Method: BFGS
- Time: 0.00153 s
- Iterations: 50
- Objective: 0.0503
