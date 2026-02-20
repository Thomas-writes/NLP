# DEGENQPC

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
- **# of Variables (n):** 50
- **# of Constraints (m):** 19625
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| SLSQP | success | [2.13 2.07 1.95 2.07 1.96 1.86 1.85 1.42 1.85 2.18 2.21 1.83 2.03 1.59 2.2 1.99 1.96 2.17 2.24 1.84 2.09 2.2 1.99 1.68 1.82 1.72 1.92 2.2 2.28 1.61 1.36 2.14 1.84 2.29 1.94 1.84 2.06 2.26 1.93 1.9 1.88 2.31 2.27 2.01 1.99 2.22 2.14 1.89 1.97 1.95] | 0 | 0.898 | 2 | Optimization terminated successfully |
| SLSQP | success | [2.36 1.9 2.07 2.04 2.52 1.96 2.18 1.83 1.7 2.1 1.78 1.88 2.24 2.04 2.35 1.99 2.25 2.22 2.04 2.24 2.12 1.93 1.91 2.24 2.16 2.1 1.92 2.19 1.86 1.92 1.58 1.92 1.86 1.61 2.34 1.81 2.09 1.83 1.95 2.16 2.16 1.86 1.68 2.34 1.99 2.29 2.09 2.25 1.91 1.84] | 0 | 0.909 | 2 | Optimization terminated successfully |
| SLSQP | success | [2.06 1.8 2.24 1.77 2.13 1.88 2.07 1.44 2.31 1.84 2.32 2.04 2.02 2.19 2.11 1.97 1.58 1.78 2.1 2.38 2.29 2.39 1.42 2.21 1.87 1.63 1.74 1.95 1.77 2.14 2.32 1.75 2.12 1.93 2.07 2.1 1.76 2.22 2.04 2.2 2.47 2.06 2.02 2.11 2.2 1.77 1.85 1.9 2.24 1.92] | 0 | 0.894 | 2 | Optimization terminated successfully |
| COBYLA | success | [2.27 1.86 1.96 1.75 1.87 1.77 1.89 2.19 1.97 2.46 1.7 2.07 1.64 1.95 1.97 1.77 2.15 1.99 1.95 2.18 2.17 2.07 1.68 1.81 2.11 1.88 2.11 1.98 1.94 2.15 1.82 2.06 2.15 1.89 2.04 1.89 1.79 2.08 1.48 1.89 2.27 2.18 1.78 2.27 2.23 2.47 1.77 2.24 1.95 1.87] | 13.8 | 735 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | fail | [1.66 1.77 2.1 2.15 1.69 1.67 2 2.13 2.39 2.39 2.07 2.1 1.92 2 1.98 1.85 1.82 2.13 1.77 1.81 1.83 1.85 1.55 2.45 1.73 2.16 1.84 2.24 1.81 1.85 1.91 1.89 2.05 2.09 2.32 1.78 1.98 2.12 2.25 1.86 2.2 1.98 1.99 1.69 1.91 1.86 2.07 1.8 1.69 2.06] | 100 | 234 | None | Did not converge to a solution satisfying the constraints. See `maxcv` for the magnitude of the violation. |
| COBYLA | fail | [1.63 1.91 2.11 2.38 1.99 2.09 1.79 1.96 2.03 2.13 2.04 1.91 2.15 2.1 1.94 1.84 1.84 2.09 1.94 1.66 1.89 1.81 1.88 1.98 1.68 1.76 2.1 2.01 1.97 2.39 2.2 1.55 1.73 2.12 2.14 2 2.11 1.85 2.44 1.88 2.22 2.06 1.99 2.34 2.13 1.84 1.7 1.99 1.9 2.13] | 135 | 138 | None | Did not converge to a solution satisfying the constraints. See `maxcv` for the magnitude of the violation. |
