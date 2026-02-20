# HILBERTA

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-2.27 -2.74] | 2.26e-30 | 0.000184 | 2 | Optimization terminated successfully. |
| CG | success | [-3.37 -2.64] | 5.84e-29 | 0.000138 | 2 | Optimization terminated successfully. |
| CG | success | [-3.27 -2.89] | 8.94e-30 | 0.000139 | 2 | Optimization terminated successfully. |
| BFGS | success | [-3.05 -3.43] | 9.6e-12 | 0.000281 | 7 | Optimization terminated successfully. |
| BFGS | success | [-2.58 -3.21] | 5.7e-13 | 0.000293 | 9 | Optimization terminated successfully. |
| BFGS | success | [-3.08 -2.76] | 1.3e-12 | 0.000257 | 7 | Optimization terminated successfully. |
| dogleg | success | [-2.79 -2.92] | 2.05e-33 | 0.000215 | 3 | Optimization terminated successfully. |
| dogleg | success | [-3.27 -2.75] | 8.22e-33 | 0.000176 | 3 | Optimization terminated successfully. |
| dogleg | success | [-2.92 -2.69] | 2.05e-33 | 0.000154 | 3 | Optimization terminated successfully. |
| trust-ncg | success | [-2.9 -3.31] | 9.05e-10 | 0.000954 | 34 | Optimization terminated successfully. |
| trust-ncg | success | [-2.52 -2.81] | 5.67e-08 | 0.00141 | 58 | Optimization terminated successfully. |
| trust-ncg | success | [-3.03 -2.69] | 3.67e-08 | 0.00138 | 58 | Optimization terminated successfully. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: CG
- Time: 0.000138 s
- Iterations: 2
- Objective: 5.84e-29

### Least Iterations (iter)
- Method: CG
- Time: 0.000184 s
- Iterations: 2
- Objective: 2.26e-30

### Best Objective (f)
- Method: dogleg
- Time: 0.000215 s
- Iterations: 3
- Objective: 2.05e-33
