# HS3

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
| CG | fail | [10.1 0.306] | -2.37e+35 | 0.00228 | 4 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [9.92 1.23] | -7.73e+34 | 0.00197 | 3 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [9.38 1.27] | -1.58e+35 | 0.0021 | 5 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [10.5 2.37] | nan | 0.0241 | 114 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [10.1 1.58] | -2.39e+26 | 0.0047 | 73 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [9.83 1.51] | -1.2e+19 | 0.00226 | 71 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [10.3 1.52] | -2.8e+05 | 0.0137 | 400 | Maximum number of iterations has been exceeded. |
| dogleg | fail | [9.26 1.1] | -2.8e+05 | 0.0134 | 400 | Maximum number of iterations has been exceeded. |
| dogleg | fail | [8.5 0.561] | -2.8e+05 | 0.0138 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [11.2 1.14] | -2.79e+05 | 0.0115 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [11.1 2.2] | -2.79e+05 | 0.0113 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [10.2 0.697] | -2.79e+05 | 0.0116 | 400 | Maximum number of iterations has been exceeded. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: CG
- Time: 0.00197 s
- Iterations: 3
- Objective: -7.73e+34

### Least Iterations (iter)
- Method: CG
- Time: 0.00197 s
- Iterations: 3
- Objective: -7.73e+34

### Best Objective (f)
- Method: CG
- Time: 0.00228 s
- Iterations: 4
- Objective: -2.37e+35
