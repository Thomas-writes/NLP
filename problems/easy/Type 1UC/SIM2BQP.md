# SIM2BQP

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
- **# of Variables (n):** 1
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.5] | -0.125 | 0.000126 | 1 | Optimization terminated successfully. |
| CG | success | [0.5] | -0.125 | 0.000106 | 1 | Optimization terminated successfully. |
| CG | success | [0.5] | -0.125 | 0.000103 | 1 | Optimization terminated successfully. |
| BFGS | success | [0.5] | -0.125 | 0.000112 | 2 | Optimization terminated successfully. |
| BFGS | success | [0.5] | -0.125 | 9.23e-05 | 2 | Optimization terminated successfully. |
| BFGS | success | [0.5] | -0.125 | 8.65e-05 | 2 | Optimization terminated successfully. |
| dogleg | success | [0.5] | -0.125 | 0.000106 | 1 | Optimization terminated successfully. |
| dogleg | success | [0.5] | -0.125 | 8.08e-05 | 1 | Optimization terminated successfully. |
| dogleg | success | [0.5] | -0.125 | 7.22e-05 | 1 | Optimization terminated successfully. |
| trust-ncg | success | [0.5] | -0.125 | 0.000128 | 3 | Optimization terminated successfully. |
| trust-ncg | success | [0.5] | -0.125 | 0.000111 | 3 | Optimization terminated successfully. |
| trust-ncg | success | [0.5] | -0.125 | 0.000108 | 3 | Optimization terminated successfully. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: dogleg
- Time: 7.22e-05 s
- Iterations: 1
- Objective: -0.125

### Least Iterations (iter)
- Method: CG
- Time: 0.000126 s
- Iterations: 1
- Objective: -0.125

### Best Objective (f)
- Method: CG
- Time: 0.000126 s
- Iterations: 1
- Objective: -0.125
