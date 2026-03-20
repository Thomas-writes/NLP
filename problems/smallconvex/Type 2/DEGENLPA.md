# DEGENLPA

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
- **# of Variables (n):** 20
- **# of Constraints (m):** 15
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | fail | [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] | 533 | 0.0528 | 120 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] | 533 | 0.0421 | 120 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] | 533 | 0.0421 | 120 | Constraint violation exceeds 'gtol' |
| SLSQP | success | [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] | 3.06 | 0.00132 | 3 | Optimization terminated successfully |
| SLSQP | success | [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] | 3.06 | 0.000802 | 3 | Optimization terminated successfully |
| SLSQP | success | [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] | 3.06 | 0.000772 | 3 | Optimization terminated successfully |
| COBYLA | success | [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] | -6.96e+07 | 1.1 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] | -6.96e+07 | 1.1 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] | -6.96e+07 | 1.1 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
