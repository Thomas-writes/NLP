# PALMER3C

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
| CG | fail | [0.915 0.841 1.03 1.15 0.99 1.05 1.01 0.916] | 0.0196 | 0.0677 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.11 0.87 1.03 0.972 1.08 1.01 0.882 1.16] | 0.16 | 0.0633 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.843 0.974 1.13 1.01 0.877 1.16 1.08 0.999] | 0.0204 | 0.0599 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [1.07 1.09 0.977 0.903 1.06 0.922 0.947 0.9] | 0.0195 | 0.00148 | 49 | Optimization terminated successfully. |
| BFGS | success | [1.09 0.986 1.13 1 1.05 0.975 1.16 1.01] | 0.0195 | 0.00151 | 49 | Optimization terminated successfully. |
| BFGS | success | [1.03 0.838 1.03 1.12 1.01 1.05 1 1.19] | 0.0195 | 0.00162 | 49 | Optimization terminated successfully. |
| dogleg | success | [0.934 1.03 1.09 1.06 0.82 0.987 0.88 0.922] | 0.0195 | 0.000385 | 7 | Optimization terminated successfully. |
| dogleg | success | [0.968 0.974 1.01 0.957 0.992 1.16 0.968 1.12] | 0.0195 | 0.000369 | 7 | Optimization terminated successfully. |
| dogleg | success | [1.04 0.862 0.935 1.02 1.02 0.899 1.09 1.01] | 0.0195 | 0.00052 | 7 | Optimization terminated successfully. |
| trust-ncg | fail | [0.974 1.15 0.937 1.13 0.976 0.94 1.04 0.849] | 2.27e+03 | 0.000856 | 34 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.13 0.806 1.02 1.22 0.988 0.815 1.06 1.01] | 1.86e+03 | 0.000203 | 5 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.956 1.05 0.942 0.878 1.01 0.98 1.08 0.847] | 2.52e+03 | 0.000189 | 5 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: trust-ncg
- Time: 0.000189 s
- Iterations: 5
- Objective: 2.52e+03

### Least Iterations (iter)
- Method: trust-ncg
- Time: 0.000203 s
- Iterations: 5
- Objective: 1.86e+03

### Best Objective (f)
- Method: BFGS
- Time: 0.00148 s
- Iterations: 49
- Objective: 0.0195
