# HS44NEW

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-25

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** quadratic
- **# of Variables (n):** 4
- **# of Constraints (m):** 6
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [1.1422 1.0668 1.1146 0.85198] | -15 | 0.009 | 22 | `gtol` termination condition is satisfied. |
| trust-constr | success | [1.0513 0.97443 1.17 0.96729] | -15 | 0.00922 | 23 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.90743 1.2506 0.97441 0.84461] | -15 | 0.00862 | 21 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0.9103 1.0566 0.97109 0.87018] | -15 | 0.000548 | 5 | Optimization terminated successfully |
| SLSQP | success | [0.80963 1.006 1.0086 0.9762] | -15 | 0.000557 | 5 | Optimization terminated successfully |
| SLSQP | success | [0.90925 0.87327 1.0069 1.078] | -15 | 0.000534 | 5 | Optimization terminated successfully |
| COBYLA | fail | [0.63969 1.022 0.86608 0.9329] | -1.27 | 0.52 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [0.97602 0.98799 0.81727 1.2679] | -0.835 | 0.518 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [0.94397 0.91579 1.0274 1.1387] | -0.996 | 0.52 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
