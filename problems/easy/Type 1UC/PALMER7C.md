# PALMER7C

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [0.879 0.992 0.918 0.72 0.903 1 1.09 0.886] | 4.12 | 0.0682 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.13 1.09 1.12 1.08 1.16 1.12 1.14 1.02] | 3.55 | 0.0736 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.02 0.95 0.952 1.01 1.02 1.16 1 1.02] | 4.15 | 0.0692 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [0.944 0.932 1 0.855 1.2 0.87 0.88 0.829] | 0.602 | 0.00156 | 49 | Optimization terminated successfully. |
| BFGS | success | [0.927 0.897 1.05 1.02 1.06 1.04 1.08 0.812] | 0.602 | 0.00155 | 54 | Optimization terminated successfully. |
| BFGS | success | [1.12 1.04 1.1 1.12 1.15 0.995 0.926 1.17] | 0.602 | 0.00156 | 52 | Optimization terminated successfully. |
| dogleg | success | [0.944 0.853 1.1 1.02 1.06 0.947 0.887 1.11] | 0.602 | 0.000634 | 11 | Optimization terminated successfully. |
| dogleg | success | [1.09 1.01 1.03 1.04 0.997 0.798 0.955 0.899] | 0.602 | 0.000543 | 11 | Optimization terminated successfully. |
| dogleg | success | [1.09 0.892 0.874 0.938 0.838 0.929 1.07 0.929] | 0.602 | 0.000525 | 11 | Optimization terminated successfully. |
| trust-ncg | fail | [0.862 1.02 0.894 1.03 1.03 1.07 0.953 1.17] | 393 | 0.000805 | 35 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.04 1.09 1.04 1.06 1.03 0.943 0.975 1.01] | 470 | 0.000218 | 6 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.872 0.989 1.11 1.07 1.1 1.11 1.02 1.06] | 469 | 0.000886 | 35 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: trust-ncg
- Time: 0.000218 s
- Iterations: 6
- Objective: 470

### Least Iterations (iter)
- Method: trust-ncg
- Time: 0.000218 s
- Iterations: 6
- Objective: 470

### Best Objective (f)
- Method: BFGS
- Time: 0.00156 s
- Iterations: 49
- Objective: 0.602
