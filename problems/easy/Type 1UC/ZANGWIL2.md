# ZANGWIL2

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
| CG | success | [2.73 7.98] | -18.2 | 0.000183 | 3 | Optimization terminated successfully. |
| CG | success | [2.23 6.62] | -18.2 | 0.000129 | 2 | Optimization terminated successfully. |
| CG | success | [2.85 8.27] | -18.2 | 0.000134 | 3 | Optimization terminated successfully. |
| BFGS | success | [2.9 6.53] | -18.2 | 0.000252 | 7 | Optimization terminated successfully. |
| BFGS | success | [3.55 9.04] | -18.2 | 0.00017 | 4 | Optimization terminated successfully. |
| BFGS | success | [2.86 7.58] | -18.2 | 0.000196 | 5 | Optimization terminated successfully. |
| dogleg | success | [2.6 8.03] | -18.2 | 0.000138 | 2 | Optimization terminated successfully. |
| dogleg | success | [3.79 8.25] | -18.2 | 7.47e-05 | 1 | Optimization terminated successfully. |
| dogleg | success | [2.16 9.08] | -18.2 | 0.000111 | 2 | Optimization terminated successfully. |
| trust-ncg | fail | [1.63 7.75] | -17.3 | 0.000167 | 3 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [3.86 7.78] | -16.7 | 5.11e-05 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [3.68 7.43] | -15.7 | 5.14e-05 | 0 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: trust-ncg
- Time: 5.11e-05 s
- Iterations: 0
- Objective: -16.7

### Least Iterations (iter)
- Method: trust-ncg
- Time: 5.11e-05 s
- Iterations: 0
- Objective: -16.7

### Best Objective (f)
- Method: CG
- Time: 0.000183 s
- Iterations: 3
- Objective: -18.2
