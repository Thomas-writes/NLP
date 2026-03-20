# PORTSNQP

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** quadratic
- **# of Variables (n):** 10
- **# of Constraints (m):** 2
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | 1.94 | 0.00936 | 22 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | 1.94 | 0.00883 | 22 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | 1.94 | 0.00883 | 22 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | 1.94 | 0.000502 | 3 | Optimization terminated successfully |
| SLSQP | success | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | 1.94 | 0.000483 | 3 | Optimization terminated successfully |
| SLSQP | success | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | 1.94 | 0.000479 | 3 | Optimization terminated successfully |
| COBYLA | fail | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | -1.04e+10 | 1.28 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | -1.04e+10 | 1.28 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | -1.04e+10 | 1.28 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
