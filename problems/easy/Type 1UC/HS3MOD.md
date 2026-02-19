# HS3MOD

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
| CG | fail | [8.66 0.069] | -6.39e+30 | 0.00123 | 3 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [10.4 0] | -9.12e+30 | 0.00476 | 17 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [9.23 0.103] | -1.81e+34 | 0.00272 | 4 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [8.97 2.25] | -1.95e+14 | 0.00165 | 56 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [9.73 0] | -3.98e+21 | 0.0044 | 63 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [10.6 1.04] | -5.25e+14 | 0.00188 | 54 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [9.72 2.04] | -2.76e+05 | 0.016 | 400 | Maximum number of iterations has been exceeded. |
| dogleg | fail | [13.3 0.41] | -2.76e+05 | 0.0158 | 400 | Maximum number of iterations has been exceeded. |
| dogleg | fail | [9.65 0] | -2.76e+05 | 0.0158 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [11.1 1.46] | -92.4 | 0.00937 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [10.8 3.84] | -92.9 | 0.00907 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [9.09 0.615] | -94 | 0.00938 | 400 | Maximum number of iterations has been exceeded. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: CG
- Time: 0.00123 s
- Iterations: 3
- Objective: -6.39e+30

### Least Iterations (iter)
- Method: CG
- Time: 0.00123 s
- Iterations: 3
- Objective: -6.39e+30

### Best Objective (f)
- Method: CG
- Time: 0.00272 s
- Iterations: 4
- Objective: -1.81e+34
