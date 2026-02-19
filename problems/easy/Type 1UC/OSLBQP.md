# OSLBQP

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [2.5 0.386 0.515 0.34 0.5 0.656 0.47 0.674] | -3 | 0.000167 | 1 | Optimization terminated successfully. |
| CG | success | [2.5 0.429 0.502 0.55 0.5 0.504 0.44 0.33] | -3 | 0.000103 | 1 | Optimization terminated successfully. |
| CG | success | [2.5 0.45 0.461 0.539 0.565 0.596 0.589 0.401] | -3 | 8.9e-05 | 1 | Optimization terminated successfully. |
| BFGS | success | [2.5 0.47 0.346 0.376 0.5 0.534 0.619 0.337] | -3 | 0.000179 | 3 | Optimization terminated successfully. |
| BFGS | success | [2.5 0.438 0.424 0.619 0.5 0.451 0.392 0.481] | -3 | 0.000134 | 3 | Optimization terminated successfully. |
| BFGS | success | [2.5 0.383 0.504 0.607 0.606 0.583 0.448 0.597] | -3 | 0.000124 | 3 | Optimization terminated successfully. |
| dogleg | success | [2.5 0.522 0.596 0.503 0.5 0.535 0.248 0.647] | -3 | 0.000317 | 3 | Optimization terminated successfully. |
| dogleg | success | [2.5 0.533 0.415 0.293 0.596 0.607 0.506 0.699] | -3 | 0.000178 | 3 | Optimization terminated successfully. |
| dogleg | success | [2.5 0.621 0.586 0.427 0.5 0.341 0.543 0.639] | -3 | 0.000167 | 3 | Optimization terminated successfully. |
| trust-ncg | fail | [2.5 0.535 0.479 0.342 0.5 0.529 0.337 0.427] | -2.95 | 0.000307 | 7 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.5 0.429 0.324 0.47 0.5 0.632 0.593 0.591] | -2.99 | 0.000293 | 8 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.5 0.395 0.6 0.443 0.506 0.431 0.481 0.8] | -2.96 | 0.000273 | 7 | A bad approximation caused failure to predict improvement. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: CG
- Time: 8.9e-05 s
- Iterations: 1
- Objective: -3

### Least Iterations (iter)
- Method: CG
- Time: 0.000167 s
- Iterations: 1
- Objective: -3

### Best Objective (f)
- Method: CG
- Time: 0.000167 s
- Iterations: 1
- Objective: -3
