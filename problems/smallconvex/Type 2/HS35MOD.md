# HS35MOD

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 1
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.53791 0.75268] | 0.25 | 0.0498 | 121 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.63823 0.54018] | 0.25 | 0.0537 | 142 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.36671 0.31106] | 0.25 | 0.0478 | 120 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0.56767 0.60739] | 0.25 | 0.000459 | 4 | Optimization terminated successfully |
| SLSQP | success | [0.47266 0.60047] | 0.25 | 0.000404 | 4 | Optimization terminated successfully |
| SLSQP | success | [0.62105 0.71214] | 0.25 | 0.000408 | 4 | Optimization terminated successfully |
| COBYLA | success | [0.46865 0.46972] | 0.25 | 0.0114 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.44362 0.53271] | 0.25 | 0.0135 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.58257 0.45229] | 0.25 | 0.0108 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
