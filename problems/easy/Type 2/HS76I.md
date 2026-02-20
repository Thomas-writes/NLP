# HS76I

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 3
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.55 0.362 0.572 0.385] | -4.68 | 0.00753 | 20 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.331 0.635 0.507 0.633] | -4.68 | 0.015 | 39 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.489 0.389 0.614 0.54] | -4.68 | 0.0152 | 40 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0.591 0.536 0.532 0.581] | -4.68 | 0.000636 | 6 | Optimization terminated successfully |
| SLSQP | success | [0.592 0.432 0.534 0.485] | -4.68 | 0.000612 | 6 | Optimization terminated successfully |
| SLSQP | success | [0.555 0.588 0.527 0.548] | -4.68 | 0.000529 | 5 | Optimization terminated successfully |
| COBYLA | success | [0.574 0.575 0.655 0.36] | -4.97 | 0.0297 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.424 0.553 0.479 0.695] | -4.97 | 0.0262 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.576 0.588 0.412 0.503] | -4.97 | 0.0277 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
