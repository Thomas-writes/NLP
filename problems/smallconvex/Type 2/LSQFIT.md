# LSQFIT

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Convex
- **Objective Type:** sum of squares
- **# of Variables (n):** 2
- **# of Constraints (m):** 1
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.1314 -0.037096] | 0.0338 | 0.0226 | 59 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.0040955 0.0014114] | 0.0338 | 0.0233 | 63 | `gtol` termination condition is satisfied. |
| trust-constr | fail | [0 -0.29365] | 0.035 | 0.376 | 1000 | The maximum number of function evaluations is exceeded. |
| SLSQP | success | [0 -0.0073509] | 0.0338 | 0.000561 | 6 | Optimization terminated successfully |
| SLSQP | success | [0 -0.073262] | 0.0338 | 0.000518 | 6 | Optimization terminated successfully |
| SLSQP | success | [0.090228 0.02105] | 0.0338 | 0.000461 | 5 | Optimization terminated successfully |
| COBYLA | success | [0.030826 0.066431] | 0.0338 | 0.0137 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0 0.1729] | 0.0338 | 0.0128 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0 0.0039676] | 0.0338 | 0.0127 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
