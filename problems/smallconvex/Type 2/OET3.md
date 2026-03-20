# OET3

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 1002
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0 0 0 0] | 0.00533 | 260 | 719 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0 0 0 0] | 0.00533 | 254 | 719 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0 0 0 0] | 0.00533 | 253 | 719 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0 0 0 0] | 0.00451 | 0.00613 | 6 | Optimization terminated successfully |
| SLSQP | success | [0 0 0 0] | 0.00451 | 0.00567 | 6 | Optimization terminated successfully |
| SLSQP | success | [0 0 0 0] | 0.00451 | 0.00594 | 6 | Optimization terminated successfully |
| COBYLA | success | [0 0 0 0] | 0.00451 | 4.33 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0 0 0 0] | 0.00451 | 4.29 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0 0 0 0] | 0.00451 | 4.62 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
