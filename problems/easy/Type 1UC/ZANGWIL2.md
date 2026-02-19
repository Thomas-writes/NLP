# ZANGWIL2

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
| CG | success | [4.66 7.93] | -18.2 | 0.00017 | 3 | Optimization terminated successfully. |
| CG | success | [2.4 7.23] | -18.2 | 0.000115 | 2 | Optimization terminated successfully. |
| CG | success | [1.69 7.66] | -18.2 | 0.000123 | 2 | Optimization terminated successfully. |
| BFGS | success | [2.03 8.57] | -18.2 | 0.000254 | 7 | Optimization terminated successfully. |
| BFGS | success | [3.92 7.22] | -18.2 | 0.000236 | 7 | Optimization terminated successfully. |
| BFGS | success | [3.6 8.33] | -18.2 | 0.000232 | 7 | Optimization terminated successfully. |
| dogleg | success | [2.41 7.83] | -18.2 | 0.000139 | 2 | Optimization terminated successfully. |
| dogleg | success | [1.43 6.96] | -18.2 | 0.000148 | 3 | Optimization terminated successfully. |
| dogleg | success | [1.87 8.51] | -18.2 | 0.000117 | 2 | Optimization terminated successfully. |
| trust-ncg | fail | [4 8.33] | -17.7 | 7.13e-05 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.45 8.78] | -17.9 | 0.000124 | 2 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.39 8.88] | -17.8 | 0.000118 | 2 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: trust-ncg
- Time: 7.13e-05 s
- Iterations: 0
- Objective: -17.7

### Least Iterations (iter)
- Method: trust-ncg
- Time: 7.13e-05 s
- Iterations: 0
- Objective: -17.7

### Best Objective (f)
- Method: CG
- Time: 0.00017 s
- Iterations: 3
- Objective: -18.2
