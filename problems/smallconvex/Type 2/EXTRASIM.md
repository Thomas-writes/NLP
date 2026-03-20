# EXTRASIM

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
- **Objective Type:** linear
- **# of Variables (n):** 2
- **# of Constraints (m):** 1
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0 0] | 1 | 0.00452 | 12 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0 0] | 1 | 0.00422 | 12 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0 0] | 1 | 0.0044 | 12 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0 0] | 1 | 0.000242 | 1 | Optimization terminated successfully |
| SLSQP | success | [0 0] | 1 | 0.000205 | 1 | Optimization terminated successfully |
| SLSQP | success | [0 0] | 1 | 0.000204 | 1 | Optimization terminated successfully |
| COBYLA | fail | [0 0] | -2.09e+10 | 0.518 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [0 0] | -2.09e+10 | 0.5 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [0 0] | -2.09e+10 | 0.498 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
