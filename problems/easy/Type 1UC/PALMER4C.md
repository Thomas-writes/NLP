# PALMER4C

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
| CG | fail | [0.817 1.04 1.01 1.06 0.927 1.03 0.935 0.777] | 0.255 | 0.0723 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.04 0.935 1.21 1.04 0.884 0.837 0.929 0.966] | 0.242 | 0.0731 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.954 1.05 0.988 1.12 0.952 0.973 0.983 1.05] | 0.307 | 0.0806 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [0.956 1.05 0.956 0.935 0.874 1.18 0.935 1.15] | 0.0503 | 0.00156 | 50 | Optimization terminated successfully. |
| BFGS | success | [1.23 0.956 1.03 0.832 0.903 1.01 1.14 0.975] | 0.0503 | 0.00151 | 49 | Optimization terminated successfully. |
| BFGS | success | [1.01 1.07 0.795 1.13 1.03 0.867 0.719 1.1] | 0.0503 | 0.00143 | 49 | Optimization terminated successfully. |
| dogleg | success | [0.97 0.942 1.05 0.88 1.06 0.978 0.869 1.09] | 0.0503 | 0.000434 | 8 | Optimization terminated successfully. |
| dogleg | success | [0.963 0.96 0.86 0.994 1.06 0.862 0.908 0.889] | 0.0503 | 0.000417 | 8 | Optimization terminated successfully. |
| dogleg | success | [0.917 0.927 0.828 0.958 0.97 0.91 0.893 0.893] | 0.0503 | 0.000408 | 8 | Optimization terminated successfully. |
| trust-ncg | fail | [0.891 1.01 1.03 1.12 0.937 0.925 1.08 1.18] | 1.57e+03 | 0.000936 | 37 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.18 1.16 0.939 1.02 0.974 0.951 0.888 0.997] | 1.36e+03 | 0.00023 | 6 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.923 1.05 1.04 1.09 0.938 0.945 1.09 1.2] | 1.58e+03 | 0.000873 | 36 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: trust-ncg
- Time: 0.00023 s
- Iterations: 6
- Objective: 1.36e+03

### Least Iterations (iter)
- Method: trust-ncg
- Time: 0.00023 s
- Iterations: 6
- Objective: 1.36e+03

### Best Objective (f)
- Method: BFGS
- Time: 0.00156 s
- Iterations: 50
- Objective: 0.0503
