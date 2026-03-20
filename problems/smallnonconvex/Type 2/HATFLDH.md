# HATFLDH

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
| trust-constr | fail | [1 5 5 1] | -12.7 | 0.0241 | 121 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [1 5 5 1] | -12.7 | 0.0242 | 121 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [1 5 5 1] | -12.7 | 0.0239 | 121 | Constraint violation exceeds 'gtol' |
| SLSQP | success | [1 5 5 1] | -24.4 | 0.000486 | 2 | Optimization terminated successfully |
| SLSQP | success | [1 5 5 1] | -24.4 | 0.000331 | 2 | Optimization terminated successfully |
| SLSQP | success | [1 5 5 1] | -24.4 | 0.000312 | 2 | Optimization terminated successfully |
| COBYLA | success | [1 5 5 1] | -24.2 | 0.0228 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [1 5 5 1] | -24.2 | 0.0227 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [1 5 5 1] | -24.2 | 0.0226 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
