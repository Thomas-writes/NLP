# AVGASB

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
| trust-constr | success | [0.516 0.513 0.396 0.59 0.443 0.128 0.411 0.526] | -4.48 | 0.0177 | 34 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.476 0.493 0.651 0.435 0.435 0.337 0.483 0.507] | -4.48 | 0.0152 | 29 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.406 0.399 0.624 0.489 0.507 0.604 0.53 0.489] | -4.48 | 0.0191 | 38 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0.556 0.47 0.477 0.603 0.382 0.565 0.4 0.473] | -4.48 | 0.000811 | 5 | Optimization terminated successfully |
| SLSQP | success | [0.377 0.645 0.585 0.486 0.703 0.702 0.41 0.641] | -4.48 | 0.00114 | 9 | Optimization terminated successfully |
| SLSQP | success | [0.619 0.437 0.569 0.507 0.442 0.454 0.529 0.517] | -4.48 | 0.000751 | 5 | Optimization terminated successfully |
| COBYLA | success | [0.584 0.654 0.384 0.401 0.505 0.585 0.521 0.439] | -4.67 | 0.0949 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.505 0.544 0.496 0.555 0.494 0.625 0.556 0.522] | -4.67 | 0.109 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.431 0.576 0.576 0.459 0.374 0.549 0.562 0.386] | -4.67 | 0.106 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
