# AVGASA

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 10
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.526 0.474 0.397 0.422 0.487 0.517 0.5 0.513] | -4.63 | 0.0157 | 31 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.572 0.502 0.601 0.576 0.464 0.381 0.568 0.453] | -4.63 | 0.0176 | 32 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.572 0.623 0.422 0.495 0.429 0.551 0.694 0.393] | -4.63 | 0.0163 | 32 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0.39 0.536 0.323 0.528 0.453 0.451 0.334 0.351] | -4.63 | 0.000777 | 5 | Optimization terminated successfully |
| SLSQP | success | [0.411 0.491 0.623 0.397 0.327 0.394 0.377 0.586] | -4.63 | 0.000962 | 7 | Optimization terminated successfully |
| SLSQP | success | [0.56 0.606 0.553 0.444 0.473 0.571 0.475 0.49] | -4.63 | 0.000749 | 5 | Optimization terminated successfully |
| COBYLA | success | [0.544 0.5 0.443 0.554 0.441 0.636 0.59 0.659] | -4.79 | 0.105 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.414 0.443 0.279 0.562 0.5 0.476 0.626 0.599] | -4.79 | 0.109 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.453 0.588 0.484 0.663 0.523 0.596 0.597 0.46] | -4.79 | 0.114 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
