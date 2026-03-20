# OET1

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
- **# of Constraints (m):** 1002
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0 0 0] | 0.538 | 150 | 372 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0 0 0] | 0.538 | 159 | 372 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0 0 0] | 0.538 | 144 | 372 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0 0 0] | 0.538 | 0.00444 | 5 | Optimization terminated successfully |
| SLSQP | success | [0 0 0] | 0.538 | 0.00414 | 5 | Optimization terminated successfully |
| SLSQP | success | [0 0 0] | 0.538 | 0.00404 | 5 | Optimization terminated successfully |
| COBYLA | success | [0 0 0] | 0.538 | 0.21 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0 0 0] | 0.538 | 0.204 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0 0 0] | 0.538 | 0.209 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
