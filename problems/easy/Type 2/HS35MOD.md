# HS35MOD

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-02-19

## Classification
- **Convexity:** Convex
- **Degree:** Quadratic
- **# of Variables (n):** 2
- **# of Constraints (m):** 1
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.482 0.436] | 0.25 | 0.0481 | 120 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.35 0.515] | 0.25 | 0.0484 | 123 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.549 0.634] | 0.25 | 0.0551 | 142 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0.528 0.501] | 0.25 | 0.000449 | 4 | Optimization terminated successfully |
| SLSQP | success | [0.488 0.434] | 0.25 | 0.000389 | 4 | Optimization terminated successfully |
| SLSQP | success | [0.657 0.658] | 0.25 | 0.000386 | 4 | Optimization terminated successfully |
| COBYLA | success | [0.367 0.426] | 0.25 | 0.00905 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.504 0.61] | 0.25 | 0.0135 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.554 0.443] | 0.25 | 0.0193 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
