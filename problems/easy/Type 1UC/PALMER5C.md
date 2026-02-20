# PALMER5C

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
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.916 0.949 1.04 0.981 1.01 0.828] | 2.13 | 0.000336 | 6 | Optimization terminated successfully. |
| CG | success | [0.8 1.14 0.947 1.03 0.85 0.989] | 2.13 | 0.00035 | 6 | Optimization terminated successfully. |
| CG | success | [1.03 0.849 1.02 0.878 1.01 0.926] | 2.13 | 0.000303 | 6 | Optimization terminated successfully. |
| BFGS | success | [0.978 0.961 0.947 0.979 1.05 0.965] | 2.13 | 0.000454 | 11 | Optimization terminated successfully. |
| BFGS | success | [0.963 1.14 0.934 1.14 0.853 1.1] | 2.13 | 0.000389 | 10 | Optimization terminated successfully. |
| BFGS | success | [0.912 1.32 1.03 0.983 0.867 1.02] | 2.13 | 0.000428 | 11 | Optimization terminated successfully. |
| dogleg | success | [0.944 0.996 1.04 1.06 1.12 0.896] | 2.13 | 0.000303 | 6 | Optimization terminated successfully. |
| dogleg | success | [0.958 1.05 1.05 0.867 0.982 0.972] | 2.13 | 0.000276 | 6 | Optimization terminated successfully. |
| dogleg | success | [1.05 1.1 1.25 1.01 0.938 1.15] | 2.13 | 0.000273 | 6 | Optimization terminated successfully. |
| trust-ncg | fail | [1.26 0.987 1.05 1.11 1.01 0.984] | 389 | 0.00104 | 37 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.11 1.09 1 1.12 1.13 1.03] | 387 | 0.000978 | 37 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.03 1.05 1.02 0.887 1.06 1.06] | 387 | 0.000937 | 37 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: dogleg
- Time: 0.000273 s
- Iterations: 6
- Objective: 2.13

### Least Iterations (iter)
- Method: CG
- Time: 0.000336 s
- Iterations: 6
- Objective: 2.13

### Best Objective (f)
- Method: CG
- Time: 0.000336 s
- Iterations: 6
- Objective: 2.13
