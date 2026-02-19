# HILBERTB

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
| CG | success | [-3.58 -3.04 -3.11 -3.27 -3.02 -2.97 -3.27 -2.61 -3.26 -3.26] | 1.02e-17 | 0.000228 | 4 | Optimization terminated successfully. |
| CG | success | [-2.97 -2.85 -2.96 -3.04 -3.26 -3.43 -2.75 -2.87 -2.74 -2.77] | 2.59e-14 | 0.000267 | 5 | Optimization terminated successfully. |
| CG | success | [-2.98 -3.06 -3.09 -3.03 -2.95 -3.16 -3.41 -2.59 -3.31 -2.63] | 7.22e-18 | 0.000225 | 4 | Optimization terminated successfully. |
| BFGS | success | [-3.16 -2.71 -3.46 -2.75 -2.99 -2.74 -2.85 -2.58 -3.14 -2.97] | 2.85e-12 | 0.000501 | 10 | Optimization terminated successfully. |
| BFGS | success | [-2.77 -3.11 -2.87 -2.83 -3.46 -3.06 -3.46 -3.47 -3.19 -3.34] | 1.4e-16 | 0.000467 | 11 | Optimization terminated successfully. |
| BFGS | success | [-2.98 -3.51 -2.9 -3.25 -2.62 -2.53 -2.67 -3.11 -3.11 -3.44] | 6.59e-16 | 0.000457 | 11 | Optimization terminated successfully. |
| dogleg | success | [-2.32 -3.38 -2.85 -2.5 -3.4 -2.89 -3.65 -2.91 -2.55 -3.39] | 1.88e-30 | 0.000236 | 4 | Optimization terminated successfully. |
| dogleg | success | [-3.17 -2.87 -2.45 -3.43 -3.14 -3.1 -2.87 -2.46 -3.02 -2.71] | 7.44e-31 | 0.000217 | 4 | Optimization terminated successfully. |
| dogleg | success | [-3.17 -3.25 -3 -2.98 -2.45 -2.76 -3.12 -2.86 -3.47 -3.13] | 1.34e-30 | 0.000213 | 4 | Optimization terminated successfully. |
| trust-ncg | success | [-2.76 -2.68 -2.74 -2.84 -2.66 -2.94 -2.97 -2.67 -3.14 -2.81] | 4.38e-10 | 0.000651 | 20 | Optimization terminated successfully. |
| trust-ncg | success | [-2.67 -3.11 -2.91 -2.76 -3 -3 -3.31 -2.92 -2.63 -3.23] | 1.22e-10 | 0.000758 | 25 | Optimization terminated successfully. |
| trust-ncg | success | [-3.09 -2.85 -2.74 -2.72 -3.1 -3.39 -2.78 -2.77 -3.04 -3.28] | 2.8e-11 | 0.000877 | 27 | Optimization terminated successfully. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: dogleg
- Time: 0.000213 s
- Iterations: 4
- Objective: 1.34e-30

### Least Iterations (iter)
- Method: CG
- Time: 0.000228 s
- Iterations: 4
- Objective: 1.02e-17

### Best Objective (f)
- Method: dogleg
- Time: 0.000217 s
- Iterations: 4
- Objective: 7.44e-31
