# PALMER1D

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
- **# of Variables (n):** 7
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [1.19 1.09 0.832 0.926 0.928 0.884 1.09] | 0.653 | 0.019 | 388 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [0.917 0.985 1.07 1.12 1.01 0.968 1.02] | 0.656 | 0.0821 | 1400 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.07 1.07 1.08 0.967 0.889 0.808 1.24] | 0.654 | 0.0564 | 1400 | Maximum number of iterations has been exceeded. |
| BFGS | success | [1.03 0.909 1.05 1.1 1.17 0.85 1.07] | 0.653 | 0.000889 | 27 | Optimization terminated successfully. |
| BFGS | success | [1.2 1.05 0.889 1.09 1.04 0.83 0.967] | 0.653 | 0.00097 | 31 | Optimization terminated successfully. |
| BFGS | success | [1.17 0.823 1.1 0.895 0.961 0.923 1.1] | 0.653 | 0.00113 | 29 | Optimization terminated successfully. |
| dogleg | success | [1.02 0.853 0.879 1.09 1.11 1.05 0.779] | 0.653 | 0.000449 | 8 | Optimization terminated successfully. |
| dogleg | success | [1.03 0.932 0.819 1.1 0.987 1.05 1.02] | 0.653 | 0.000422 | 8 | Optimization terminated successfully. |
| dogleg | success | [0.852 1.02 0.887 0.85 1.13 1.15 0.978] | 0.653 | 0.00045 | 8 | Optimization terminated successfully. |
| trust-ncg | fail | [1.08 0.983 1.1 0.907 0.896 0.756 1.02] | 4.65e+04 | 0.000161 | 3 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.92 1.04 1.07 0.806 1.12 1.06 0.867] | 5.35e+04 | 0.000935 | 32 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.962 1.03 0.968 1.02 1.1 0.937 1.01] | 5.33e+04 | 0.000199 | 5 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: trust-ncg
- Time: 0.000161 s
- Iterations: 3
- Objective: 4.65e+04

### Least Iterations (iter)
- Method: trust-ncg
- Time: 0.000161 s
- Iterations: 3
- Objective: 4.65e+04

### Best Objective (f)
- Method: CG
- Time: 0.019 s
- Iterations: 388
- Objective: 0.653
