# STANCMIN

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-25

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** other
- **# of Variables (n):** 3
- **# of Constraints (m):** 2
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | fail | [44.113 40.5 56.372] | -2.51 | 0.0631 | 225 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [46.608 42.754 46.952] | -2.15 | 0.0676 | 237 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [42.857 40.475 51.655] | -2.11 | 0.057 | 209 | Constraint violation exceeds 'gtol' |
| SLSQP | success | [44.005 42.545 51.845] | 4.25 | 0.000525 | 4 | Optimization terminated successfully |
| SLSQP | success | [37.982 41.628 41.606] | 4.25 | 0.000458 | 4 | Optimization terminated successfully |
| SLSQP | success | [40.103 48.129 42.292] | 4.25 | 0.000438 | 4 | Optimization terminated successfully |
| COBYLA | success | [35.333 43.834 42.894] | -1.08e+16 | 0.0255 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [42.666 38.796 46.165] | -5.94e+15 | 0.0235 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [46.669 40.393 53.776] | -5.07e+15 | 0.0204 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
