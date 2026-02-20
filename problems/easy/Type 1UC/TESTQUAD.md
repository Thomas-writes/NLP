# TESTQUAD

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
- **# of Variables (n):** 10
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.945 1.11 0.928 1.1 0.949 0.92 0.97 1.08 0.92 0.949] | 3.85e-12 | 0.00925 | 264 | Optimization terminated successfully. |
| CG | success | [0.843 1.04 1.13 0.898 0.932 0.798 0.97 0.984 1.03 0.979] | 7.48e-23 | 0.00202 | 52 | Optimization terminated successfully. |
| CG | success | [0.973 0.964 0.784 1.2 1.01 1.09 0.822 0.928 1.02 1.07] | 6.65e-11 | 0.0118 | 364 | Optimization terminated successfully. |
| BFGS | success | [1.02 1.05 1.03 1.06 0.762 1.09 0.754 1.14 0.973 0.932] | 3.96e-23 | 0.000794 | 15 | Optimization terminated successfully. |
| BFGS | success | [0.896 0.928 1 1.05 0.939 1.1 1.23 0.882 0.982 0.98] | 6.3e-18 | 0.000716 | 13 | Optimization terminated successfully. |
| BFGS | success | [1.07 0.875 1.11 0.998 1.04 0.874 0.898 1.1 1.25 0.953] | 6.37e-18 | 0.000828 | 14 | Optimization terminated successfully. |
| dogleg | success | [0.788 1.1 1.11 0.865 1.05 0.948 0.964 1.05 1.04 0.915] | 1.77e-28 | 0.000865 | 3 | Optimization terminated successfully. |
| dogleg | success | [0.838 0.961 0.849 0.961 1.17 1.15 1.19 0.81 0.909 0.971] | 2.47e-28 | 0.000188 | 3 | Optimization terminated successfully. |
| dogleg | success | [1.23 0.872 1.14 0.907 0.966 0.963 0.971 1.16 0.952 0.79] | 2.29e-28 | 0.000168 | 3 | Optimization terminated successfully. |
| trust-ncg | fail | [1.07 0.995 1.14 1.01 1.14 0.914 1.19 0.987 0.919 0.913] | 5.92 | 0.0472 | 2000 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [1 0.918 1.04 1.09 1.14 1 1.05 0.969 1.1 0.868] | 5 | 0.047 | 2000 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.996 1.1 1.07 1.03 1.07 1.09 0.937 0.907 1.12 1.07] | 6.62 | 0.0474 | 2000 | Maximum number of iterations has been exceeded. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: dogleg
- Time: 0.000168 s
- Iterations: 3
- Objective: 2.29e-28

### Least Iterations (iter)
- Method: dogleg
- Time: 0.000865 s
- Iterations: 3
- Objective: 1.77e-28

### Best Objective (f)
- Method: dogleg
- Time: 0.000865 s
- Iterations: 3
- Objective: 1.77e-28
