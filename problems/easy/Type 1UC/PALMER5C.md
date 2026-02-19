# PALMER5C

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
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.08 0.931 1 1.08 1.03 0.995] | 2.13 | 0.000318 | 6 | Optimization terminated successfully. |
| CG | success | [0.905 1.06 0.961 1.06 0.792 0.957] | 2.13 | 0.000286 | 6 | Optimization terminated successfully. |
| CG | success | [1.02 1.06 0.977 0.95 1.09 1.05] | 2.13 | 0.000286 | 6 | Optimization terminated successfully. |
| BFGS | success | [1.04 1.18 1.17 0.897 0.93 1.04] | 2.13 | 0.000421 | 11 | Optimization terminated successfully. |
| BFGS | success | [1.01 0.959 1.06 0.828 0.851 0.935] | 2.13 | 0.000412 | 11 | Optimization terminated successfully. |
| BFGS | success | [1.08 0.969 1.06 1.01 1.11 1.02] | 2.13 | 0.000413 | 11 | Optimization terminated successfully. |
| dogleg | success | [1.02 0.887 1.07 1.06 1.01 1.01] | 2.13 | 0.000304 | 6 | Optimization terminated successfully. |
| dogleg | success | [1.08 1.08 1.03 1.01 1.03 0.894] | 2.13 | 0.000274 | 6 | Optimization terminated successfully. |
| dogleg | success | [1.01 0.915 0.787 1.02 0.951 1.23] | 2.13 | 0.000285 | 6 | Optimization terminated successfully. |
| trust-ncg | fail | [0.945 1 1.06 1.2 0.964 1.1] | 391 | 0.000933 | 37 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.998 1.16 0.991 1 1.08 1.13] | 386 | 0.000954 | 37 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.04 0.968 0.974 1.09 0.852 0.995] | 386 | 0.00103 | 37 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: dogleg
- Time: 0.000274 s
- Iterations: 6
- Objective: 2.13

### Least Iterations (iter)
- Method: CG
- Time: 0.000318 s
- Iterations: 6
- Objective: 2.13

### Best Objective (f)
- Method: CG
- Time: 0.000318 s
- Iterations: 6
- Objective: 2.13
