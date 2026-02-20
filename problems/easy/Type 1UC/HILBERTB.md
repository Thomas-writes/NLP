# HILBERTB

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
- **# of Variables (n):** 10
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-3.03 -2.6 -3.41 -3.15 -2.71 -3.09 -2.99 -2.36 -3.16 -2.13] | 8.39e-13 | 0.000325 | 5 | Optimization terminated successfully. |
| CG | success | [-2.9 -2.62 -2.8 -2.82 -2.75 -2.69 -3.5 -3.2 -3.12 -2.69] | 5.22e-13 | 0.000308 | 5 | Optimization terminated successfully. |
| CG | success | [-2.98 -3.16 -2.54 -3.66 -2.64 -2.86 -2.65 -3.07 -2.79 -3.47] | 2.6e-17 | 0.000299 | 5 | Optimization terminated successfully. |
| BFGS | success | [-2.76 -3.59 -3 -2.53 -3.25 -3.26 -2.8 -3.1 -3.54 -2.48] | 1.93e-12 | 0.000472 | 12 | Optimization terminated successfully. |
| BFGS | success | [-2.51 -3.3 -3.17 -3.05 -2.1 -3.15 -2.73 -3.07 -2.8 -2.8] | 2.17e-16 | 0.000451 | 11 | Optimization terminated successfully. |
| BFGS | success | [-3.02 -3.44 -3.34 -2.79 -2.96 -2.77 -3.4 -3.02 -3.29 -2.65] | 5.01e-14 | 0.000454 | 12 | Optimization terminated successfully. |
| dogleg | success | [-3.51 -3.2 -2.97 -3.18 -3 -2.96 -3.33 -3.62 -2.69 -2.78] | 2.91e-30 | 0.000242 | 4 | Optimization terminated successfully. |
| dogleg | success | [-2.89 -2.98 -3.02 -3.52 -3.33 -2.76 -2.81 -2.83 -2.69 -2.92] | 2.16e-30 | 0.000214 | 4 | Optimization terminated successfully. |
| dogleg | success | [-2.76 -2.22 -2.78 -3.25 -3.27 -2.68 -2.5 -2.9 -3.64 -3.22] | 1.45e-30 | 0.000212 | 4 | Optimization terminated successfully. |
| trust-ncg | success | [-2.36 -2.64 -2.52 -3.53 -3.4 -3.43 -2.8 -2.56 -2.84 -3.28] | 6.29e-11 | 0.000991 | 28 | Optimization terminated successfully. |
| trust-ncg | success | [-2.81 -2.76 -2.17 -3.07 -3.3 -2.66 -3.46 -2.89 -2.21 -3.03] | 9.32e-11 | 0.000721 | 23 | Optimization terminated successfully. |
| trust-ncg | success | [-2.73 -2.67 -2.8 -2.91 -3.13 -2.85 -3.16 -2.86 -2.74 -2.73] | 1.3e-10 | 0.000829 | 26 | Optimization terminated successfully. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: dogleg
- Time: 0.000212 s
- Iterations: 4
- Objective: 1.45e-30

### Least Iterations (iter)
- Method: dogleg
- Time: 0.000242 s
- Iterations: 4
- Objective: 2.91e-30

### Best Objective (f)
- Method: dogleg
- Time: 0.000212 s
- Iterations: 4
- Objective: 1.45e-30
