# DEGENQP

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
- **# of Constraints (m):** 125
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| SLSQP | success | [2.37 2.46 2.04 2.34 1.96 1.92 2.07 1.92 2.27 1.76] | 5.77e-15 | 0.00102 | 2 | Optimization terminated successfully |
| SLSQP | success | [2.14 1.68 2.15 1.93 2.06 2.12 2.3 2.29 2.07 2.01] | 5.77e-15 | 0.00106 | 2 | Optimization terminated successfully |
| SLSQP | success | [2.38 1.91 1.95 2.08 1.78 1.88 1.85 1.85 1.99 2.21] | 5.77e-15 | 0.000906 | 2 | Optimization terminated successfully |
| COBYLA | fail | [2.1 2.13 1.98 1.84 2 2.27 1.95 1.89 2 2.11] | 23.3 | 0.214 | None | Did not converge to a solution satisfying the constraints. See `maxcv` for the magnitude of the violation. |
| COBYLA | fail | [1.93 2.06 1.83 1.98 2.13 2.21 1.97 1.97 1.94 2.12] | 16 | 0.647 | None | Did not converge to a solution satisfying the constraints. See `maxcv` for the magnitude of the violation. |
| COBYLA | success | [1.87 2.12 1.91 2.02 1.87 1.69 1.69 1.8 1.95 1.84] | -1.2e-15 | 0.266 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
