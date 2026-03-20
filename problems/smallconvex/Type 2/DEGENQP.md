# DEGENQP

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
- **Objective Type:** quadratic
- **# of Variables (n):** 10
- **# of Constraints (m):** 125
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [1 1 1 1 1 1 1 1 1 1] | 0.00402 | 0.0446 | 16 | `gtol` termination condition is satisfied. |
| trust-constr | success | [1 1 1 1 1 1 1 1 1 1] | 0.00402 | 0.0417 | 16 | `gtol` termination condition is satisfied. |
| trust-constr | success | [1 1 1 1 1 1 1 1 1 1] | 0.00402 | 0.0427 | 16 | `gtol` termination condition is satisfied. |
| SLSQP | success | [1 1 1 1 1 1 1 1 1 1] | 5.77e-15 | 0.0015 | 2 | Optimization terminated successfully |
| SLSQP | success | [1 1 1 1 1 1 1 1 1 1] | 5.77e-15 | 0.000839 | 2 | Optimization terminated successfully |
| SLSQP | success | [1 1 1 1 1 1 1 1 1 1] | 5.77e-15 | 0.000896 | 2 | Optimization terminated successfully |
| COBYLA | fail | [1 1 1 1 1 1 1 1 1 1] | 12.6 | 0.228 | None | Did not converge to a solution satisfying the constraints. See `maxcv` for the magnitude of the violation. |
| COBYLA | fail | [1 1 1 1 1 1 1 1 1 1] | 12.6 | 0.226 | None | Did not converge to a solution satisfying the constraints. See `maxcv` for the magnitude of the violation. |
| COBYLA | fail | [1 1 1 1 1 1 1 1 1 1] | 12.6 | 0.23 | None | Did not converge to a solution satisfying the constraints. See `maxcv` for the magnitude of the violation. |
