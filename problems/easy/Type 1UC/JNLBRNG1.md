# JNLBRNG1

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
| CG | success | [0.813 0.958 0 0] | -0.317 | 0.000302 | 6 | Optimization terminated successfully. |
| CG | success | [0.937 0.835 0 0] | -0.317 | 0.000273 | 6 | Optimization terminated successfully. |
| CG | success | [0.893 0.876 0 0] | -0.317 | 0.000264 | 6 | Optimization terminated successfully. |
| BFGS | success | [0.673 1.01 0 0] | -0.317 | 0.000327 | 7 | Optimization terminated successfully. |
| BFGS | success | [0.702 0.82 0 0] | -0.317 | 0.00033 | 8 | Optimization terminated successfully. |
| BFGS | success | [0.936 0.705 0 0] | -0.317 | 0.000314 | 8 | Optimization terminated successfully. |
| dogleg | success | [0.86 0.919 0 0] | -0.317 | 0.000154 | 2 | Optimization terminated successfully. |
| dogleg | success | [0.8 0.854 0 0] | -0.317 | 0.00014 | 2 | Optimization terminated successfully. |
| dogleg | success | [0.841 0.788 0 0] | -0.317 | 7.85e-05 | 1 | Optimization terminated successfully. |
| trust-ncg | fail | [0.857 1.01 0 0] | -0.315 | 0.000925 | 31 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.819 0.782 0 0] | -0.315 | 0.000856 | 31 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.857 0.945 0 0] | -0.313 | 0.000922 | 31 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: dogleg
- Time: 7.85e-05 s
- Iterations: 1
- Objective: -0.317

### Least Iterations (iter)
- Method: dogleg
- Time: 7.85e-05 s
- Iterations: 1
- Objective: -0.317

### Best Objective (f)
- Method: CG
- Time: 0.000302 s
- Iterations: 6
- Objective: -0.317
