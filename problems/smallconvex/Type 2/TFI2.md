# TFI2

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 101
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0 0 0] | 0.649 | 0.182 | 106 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0 0 0] | 0.649 | 0.181 | 106 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0 0 0] | 0.649 | 0.18 | 106 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0 0 0] | 0.649 | 0.00109 | 7 | Optimization terminated successfully |
| SLSQP | success | [0 0 0] | 0.649 | 0.00106 | 7 | Optimization terminated successfully |
| SLSQP | success | [0 0 0] | 0.649 | 0.00109 | 7 | Optimization terminated successfully |
| COBYLA | success | [0 0 0] | 0.649 | 0.017 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0 0 0] | 0.649 | 0.017 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0 0 0] | 0.649 | 0.0168 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
