# PALMER5D

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.01 0.819 1.11 0.979] | 87.3 | 0.00261 | 77 | Optimization terminated successfully. |
| CG | success | [0.767 1.11 0.898 0.978] | 87.3 | 0.00242 | 68 | Optimization terminated successfully. |
| CG | success | [1.05 1.14 1.11 1.06] | 87.3 | 0.00371 | 97 | Optimization terminated successfully. |
| BFGS | success | [1.15 0.915 0.91 0.986] | 87.3 | 0.000367 | 11 | Optimization terminated successfully. |
| BFGS | success | [1.15 1.03 0.933 0.932] | 87.3 | 0.000358 | 11 | Optimization terminated successfully. |
| BFGS | success | [1.1 0.986 1.12 1.18] | 87.3 | 0.000358 | 11 | Optimization terminated successfully. |
| dogleg | success | [0.785 0.83 0.988 0.807] | 87.3 | 0.00039 | 8 | Optimization terminated successfully. |
| dogleg | success | [1.01 1.09 0.942 0.846] | 87.3 | 0.000376 | 8 | Optimization terminated successfully. |
| dogleg | success | [1.09 1.07 1.19 1.23] | 87.3 | 0.000371 | 8 | Optimization terminated successfully. |
| trust-ncg | fail | [1.1 0.84 0.973 0.851] | 1.78e+04 | 0.000206 | 6 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.01 0.951 1.15 1.06] | 1.52e+04 | 0.000289 | 11 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.926 1.05 0.98 1.05] | 1.79e+04 | 0.000198 | 6 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: trust-ncg
- Time: 0.000198 s
- Iterations: 6
- Objective: 1.79e+04

### Least Iterations (iter)
- Method: trust-ncg
- Time: 0.000206 s
- Iterations: 6
- Objective: 1.78e+04

### Best Objective (f)
- Method: CG
- Time: 0.00261 s
- Iterations: 77
- Objective: 87.3
