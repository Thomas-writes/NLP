# PALMER5D

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.969 0.973 1.02 1.01] | 87.3 | 0.00109 | 24 | Optimization terminated successfully. |
| CG | success | [0.996 1.02 0.931 0.994] | 87.3 | 0.000932 | 25 | Optimization terminated successfully. |
| CG | success | [1.24 1.06 1.22 0.971] | 87.3 | 0.000502 | 11 | Optimization terminated successfully. |
| BFGS | success | [1.05 1.05 1.06 0.905] | 87.3 | 0.000391 | 11 | Optimization terminated successfully. |
| BFGS | success | [1.1 1.11 0.958 0.97] | 87.3 | 0.000353 | 11 | Optimization terminated successfully. |
| BFGS | success | [0.966 0.945 0.906 1.07] | 87.3 | 0.000361 | 11 | Optimization terminated successfully. |
| dogleg | success | [0.93 1.1 0.837 0.861] | 87.3 | 0.000411 | 8 | Optimization terminated successfully. |
| dogleg | success | [0.78 0.857 1.03 0.821] | 87.3 | 0.000372 | 8 | Optimization terminated successfully. |
| dogleg | success | [0.97 1.02 0.936 0.925] | 87.3 | 0.000365 | 8 | Optimization terminated successfully. |
| trust-ncg | fail | [1.07 1.05 0.918 1.13] | 1.52e+04 | 0.000308 | 11 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.04 0.908 1.04 0.879] | 1.79e+04 | 0.000212 | 6 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.851 0.945 1.04 1.08] | 1.79e+04 | 0.000207 | 6 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: trust-ncg
- Time: 0.000207 s
- Iterations: 6
- Objective: 1.79e+04

### Least Iterations (iter)
- Method: trust-ncg
- Time: 0.000212 s
- Iterations: 6
- Objective: 1.79e+04

### Best Objective (f)
- Method: CG
- Time: 0.00109 s
- Iterations: 24
- Objective: 87.3
