# STANCMIN

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
- **Objective Type:** other
- **# of Variables (n):** 3
- **# of Constraints (m):** 2
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | fail | [50 50 50] | -2.15 | 0.0677 | 237 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [50 50 50] | -2.15 | 0.0672 | 237 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [50 50 50] | -2.15 | 0.0678 | 237 | Constraint violation exceeds 'gtol' |
| SLSQP | success | [50 50 50] | 4.25 | 0.000295 | 2 | Optimization terminated successfully |
| SLSQP | success | [50 50 50] | 4.25 | 0.000284 | 2 | Optimization terminated successfully |
| SLSQP | success | [50 50 50] | 4.25 | 0.000291 | 2 | Optimization terminated successfully |
| COBYLA | success | [50 50 50] | -7.7e+06 | 0.0206 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [50 50 50] | -7.7e+06 | 0.0206 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [50 50 50] | -7.7e+06 | 0.0206 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
