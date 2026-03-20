# DUALC8

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
- **# of Constraints (m):** 503
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | fail | [0 0 0 0 0 0 0 0] | 0 | 2.24 | 120 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [0 0 0 0 0 0 0 0] | 0 | 2.22 | 120 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [0 0 0 0 0 0 0 0] | 0 | 2.22 | 120 | Constraint violation exceeds 'gtol' |
| SLSQP | fail | [0 0 0 0 0 0 0 0] | 0 | 0.00637 | 5 | Positive directional derivative for linesearch |
| SLSQP | fail | [0 0 0 0 0 0 0 0] | 0 | 0.00596 | 5 | Positive directional derivative for linesearch |
| SLSQP | fail | [0 0 0 0 0 0 0 0] | 0 | 0.00604 | 5 | Positive directional derivative for linesearch |
| COBYLA | fail | [0 0 0 0 0 0 0 0] | 1.33e+04 | 3.41 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [0 0 0 0 0 0 0 0] | 1.33e+04 | 3.27 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [0 0 0 0 0 0 0 0] | 1.33e+04 | 3.2 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
