# BQP1VAR

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
| CG | success | [0.0421] | -0.25 | 0.000134 | 1 | Optimization terminated successfully. |
| CG | success | [0.221] | -0.25 | 0.000123 | 1 | Optimization terminated successfully. |
| CG | success | [0.412] | -0.25 | 0.000127 | 1 | Optimization terminated successfully. |
| BFGS | success | [0.239] | -0.25 | 0.000108 | 2 | Optimization terminated successfully. |
| BFGS | success | [0.5] | -0.25 | 9.05e-05 | 2 | Optimization terminated successfully. |
| BFGS | success | [0.173] | -0.25 | 9.13e-05 | 2 | Optimization terminated successfully. |
| dogleg | success | [0.416] | -0.25 | 0.000114 | 1 | Optimization terminated successfully. |
| dogleg | success | [0.195] | -0.25 | 8.55e-05 | 1 | Optimization terminated successfully. |
| dogleg | success | [0.137] | -0.25 | 8.21e-05 | 1 | Optimization terminated successfully. |
| trust-ncg | fail | [0.384] | -0.248 | 0.000708 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.186] | -0.248 | 0.000663 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.145] | -0.248 | 0.000811 | 29 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: dogleg
- Time: 8.21e-05 s
- Iterations: 1
- Objective: -0.25

### Least Iterations (iter)
- Method: CG
- Time: 0.000134 s
- Iterations: 1
- Objective: -0.25

### Best Objective (f)
- Method: CG
- Time: 0.000134 s
- Iterations: 1
- Objective: -0.25
