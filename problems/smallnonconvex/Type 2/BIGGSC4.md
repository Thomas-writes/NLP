# BIGGSC4

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 7
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | fail | [0 0 0 0] | 0 | 0.0251 | 120 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [0 0 0 0] | 0 | 0.0238 | 120 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [0 0 0 0] | 0 | 0.0237 | 120 | Constraint violation exceeds 'gtol' |
| SLSQP | success | [0 0 0 0] | -24.4 | 0.000397 | 3 | Optimization terminated successfully |
| SLSQP | success | [0 0 0 0] | -24.4 | 0.000386 | 3 | Optimization terminated successfully |
| SLSQP | success | [0 0 0 0] | -24.4 | 0.000381 | 3 | Optimization terminated successfully |
| COBYLA | success | [0 0 0 0] | -24.4 | 0.0238 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0 0 0 0] | -24.4 | 0.024 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0 0 0 0] | -24.4 | 0.0239 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
