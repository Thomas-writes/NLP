# SIMBQP

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
| CG | success | [10.2 0.5] | -0.139 | 0.000151 | 2 | Optimization terminated successfully. |
| CG | success | [10 0.5] | -0.139 | 0.000134 | 2 | Optimization terminated successfully. |
| CG | success | [10.4 0] | -0.139 | 0.000134 | 2 | Optimization terminated successfully. |
| BFGS | success | [8.03 0] | -0.139 | 0.000306 | 9 | Optimization terminated successfully. |
| BFGS | success | [10.6 0] | -0.139 | 0.000222 | 5 | Optimization terminated successfully. |
| BFGS | success | [11.7 0.5] | -0.139 | 0.00021 | 5 | Optimization terminated successfully. |
| dogleg | success | [9.92 0.0826] | -0.139 | 0.000213 | 4 | Optimization terminated successfully. |
| dogleg | success | [10.7 0.5] | -0.139 | 0.000187 | 4 | Optimization terminated successfully. |
| dogleg | success | [11.1 0.5] | -0.139 | 0.000181 | 4 | Optimization terminated successfully. |
| trust-ncg | fail | [9.17 0.137] | -0.137 | 0.00096 | 40 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [8.08 0.476] | -0.138 | 0.000838 | 38 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [11.3 0.5] | -0.139 | 0.000893 | 40 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: CG
- Time: 0.000134 s
- Iterations: 2
- Objective: -0.139

### Least Iterations (iter)
- Method: CG
- Time: 0.000151 s
- Iterations: 2
- Objective: -0.139

### Best Objective (f)
- Method: CG
- Time: 0.000151 s
- Iterations: 2
- Objective: -0.139
