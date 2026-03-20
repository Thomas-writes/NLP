# AVGASB

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 10
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | -4.48 | 0.0269 | 56 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | -4.48 | 0.0262 | 56 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | -4.48 | 0.0269 | 56 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | -4.48 | 0.000784 | 5 | Optimization terminated successfully |
| SLSQP | success | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | -4.48 | 0.000781 | 5 | Optimization terminated successfully |
| SLSQP | success | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | -4.48 | 0.000954 | 5 | Optimization terminated successfully |
| COBYLA | success | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | -4.67 | 0.0984 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | -4.67 | 0.0974 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] | -4.67 | 0.0978 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
