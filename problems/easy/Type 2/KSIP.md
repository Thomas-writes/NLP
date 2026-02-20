# KSIP

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
- **# of Variables (n):** 20
- **# of Constraints (m):** 1001
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [1.97 2.26 1.98 2.12 2.47 1.86 1.9 2.51 1.86 2.12 2.13 1.79 1.98 2.13 1.87 2.19 2.21 1.7 1.79 1.85] | 0.576 | 47.1 | 107 | `gtol` termination condition is satisfied. |
| trust-constr | success | [2.19 2.18 1.9 2.18 1.59 2.05 1.95 2.12 2.17 1.93 1.61 2.27 1.79 2.25 2.02 2.14 2.12 1.62 1.77 2.23] | 0.576 | 55.8 | 149 | `gtol` termination condition is satisfied. |
| trust-constr | success | [1.84 2.05 2.04 1.83 1.43 2.14 2.07 1.71 1.92 2.21 2.17 2.11 2.03 2.02 1.68 2.01 1.95 2.19 1.51 2.13] | 0.576 | 53.2 | 131 | `gtol` termination condition is satisfied. |
| SLSQP | success | [1.89 2.36 1.95 2.16 2.15 1.63 1.76 2.36 2.12 2.11 2.15 2.32 2.23 2.08 1.71 2.07 2.01 2.06 1.85 1.96] | 0.576 | 0.0585 | 21 | Optimization terminated successfully |
| SLSQP | success | [1.8 1.81 2.07 2.03 1.72 1.76 2.03 1.82 1.87 2.02 2.11 1.74 1.72 2.26 1.81 1.95 1.94 2 2.27 1.49] | 0.576 | 0.0664 | 23 | Optimization terminated successfully |
| SLSQP | success | [1.82 1.79 1.94 1.81 2.19 1.87 1.76 1.8 2.02 1.9 2.19 2.12 2.08 1.76 2.08 2.37 2.05 1.81 2.07 1.64] | 0.576 | 0.0597 | 21 | Optimization terminated successfully |
| COBYLA | success | [1.91 2.31 2.04 2.22 1.65 1.89 1.99 2.03 1.85 1.79 2.08 1.8 2.07 2.07 1.96 1.77 2.12 1.98 2.1 2.04] | 0.576 | 16.8 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [1.92 2.06 1.88 1.86 2.26 2.03 1.81 2.06 2.06 2.3 1.92 1.67 1.97 2.03 2.05 2.21 1.7 2.01 1.81 2.66] | 0.576 | 16.8 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [2.11 1.94 1.9 1.66 2.06 1.95 2.11 1.91 1.96 2 2.16 2 2.06 2.28 2.51 2.1 2.27 1.82 2.26 1.98] | 0.576 | 18.2 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
