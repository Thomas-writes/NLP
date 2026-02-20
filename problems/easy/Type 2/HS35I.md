# HS35I

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 1
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.25 0.521 0.411] | 0.111 | 0.0182 | 46 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.621 0.444 0.49] | 0.111 | 0.017 | 45 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.622 0.513 0.588] | 0.111 | 0.0166 | 44 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0.55 0.594 0.573] | 0.111 | 0.00061 | 6 | Optimization terminated successfully |
| SLSQP | success | [0.568 0.369 0.528] | 0.111 | 0.000659 | 6 | Optimization terminated successfully |
| SLSQP | success | [0.45 0.324 0.42] | 0.111 | 0.000582 | 6 | Optimization terminated successfully |
| COBYLA | success | [0.517 0.491 0.42] | 0.111 | 0.0243 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.583 0.532 0.511] | 0.111 | 0.026 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.39 0.576 0.665] | 0.111 | 0.0222 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
