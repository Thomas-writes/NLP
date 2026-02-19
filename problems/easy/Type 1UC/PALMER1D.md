# PALMER1D

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
- **# of Variables (n):** 7
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [1.09 0.933 0.98 1.08 0.978 0.944 1.03] | 0.653 | 0.0604 | 1400 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.996 1.1 0.912 0.971 0.93 1.03 0.932] | 0.653 | 0.0638 | 1400 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.1 0.903 1.04 1.08 1.12 1.12 0.867] | 0.653 | 0.00935 | 173 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [0.951 1.04 1.08 0.957 1.05 1.02 1.21] | 0.653 | 0.000871 | 20 | Optimization terminated successfully. |
| BFGS | fail | [1.08 0.965 1.17 0.855 1.01 1.25 0.98] | 0.653 | 0.00222 | 22 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [1.08 1 1.01 0.934 0.733 0.932 0.788] | 0.653 | 0.00087 | 27 | Optimization terminated successfully. |
| dogleg | success | [0.958 1.12 1.03 0.907 0.853 1.19 0.881] | 0.653 | 0.000448 | 8 | Optimization terminated successfully. |
| dogleg | success | [1.11 1.06 0.865 0.765 1.03 0.95 1.05] | 0.653 | 0.000423 | 8 | Optimization terminated successfully. |
| dogleg | success | [1.03 0.864 0.959 0.893 1.02 0.9 1.13] | 0.653 | 0.000405 | 8 | Optimization terminated successfully. |
| trust-ncg | fail | [0.854 1.04 1.25 1.03 1.07 0.838 0.951] | 5.09e+04 | 0.000947 | 33 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.02 1.07 1 1.04 0.915 1.06 1.04] | 5.08e+04 | 0.000859 | 34 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.08 0.905 0.852 1.14 1.08 0.966 1.04] | 5.15e+04 | 0.000938 | 34 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: dogleg
- Time: 0.000405 s
- Iterations: 8
- Objective: 0.653

### Least Iterations (iter)
- Method: dogleg
- Time: 0.000448 s
- Iterations: 8
- Objective: 0.653

### Best Objective (f)
- Method: CG
- Time: 0.0604 s
- Iterations: 1400
- Objective: 0.653
