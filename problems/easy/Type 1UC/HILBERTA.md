# HILBERTA

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-2.8 -2.61] | 9.76e-28 | 0.000172 | 2 | Optimization terminated successfully. |
| CG | success | [-2.8 -2.72] | 1.18e-28 | 0.000132 | 2 | Optimization terminated successfully. |
| CG | success | [-3.11 -2.95] | 1.61e-27 | 0.000136 | 2 | Optimization terminated successfully. |
| BFGS | success | [-2.92 -3.28] | 1.65e-10 | 0.000282 | 7 | Optimization terminated successfully. |
| BFGS | success | [-3.13 -3.67] | 2.6e-12 | 0.000269 | 7 | Optimization terminated successfully. |
| BFGS | success | [-2.69 -3.38] | 2.59e-11 | 0.000284 | 8 | Optimization terminated successfully. |
| dogleg | success | [-3.05 -3.39] | 8.22e-33 | 0.000173 | 3 | Optimization terminated successfully. |
| dogleg | success | [-3.21 -3.17] | 8.22e-33 | 0.000148 | 3 | Optimization terminated successfully. |
| dogleg | success | [-3.08 -3.05] | 1.44e-32 | 0.00016 | 3 | Optimization terminated successfully. |
| trust-ncg | success | [-3.13 -3.05] | 5.36e-08 | 0.00152 | 58 | Optimization terminated successfully. |
| trust-ncg | success | [-2.74 -3.08] | 5.56e-08 | 0.00137 | 56 | Optimization terminated successfully. |
| trust-ncg | success | [-3.26 -3.04] | 2.92e-08 | 0.00125 | 53 | Optimization terminated successfully. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: CG
- Time: 0.000132 s
- Iterations: 2
- Objective: 1.18e-28

### Least Iterations (iter)
- Method: CG
- Time: 0.000172 s
- Iterations: 2
- Objective: 9.76e-28

### Best Objective (f)
- Method: dogleg
- Time: 0.000173 s
- Iterations: 3
- Objective: 8.22e-33
