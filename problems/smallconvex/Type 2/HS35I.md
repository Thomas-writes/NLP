# HS35I

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 1
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.58874 0.64364 0.33744] | 0.111 | 0.0192 | 46 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.59572 0.62554 0.53923] | 0.111 | 0.0178 | 45 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.54389 0.48313 0.63198] | 0.111 | 0.00853 | 22 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0.47093 0.46975 0.56015] | 0.111 | 0.000604 | 6 | Optimization terminated successfully |
| SLSQP | success | [0.46673 0.47855 0.51624] | 0.111 | 0.000597 | 6 | Optimization terminated successfully |
| SLSQP | success | [0.53472 0.48331 0.53512] | 0.111 | 0.000563 | 6 | Optimization terminated successfully |
| COBYLA | success | [0.5397 0.47452 0.4306] | 0.111 | 0.0217 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.55418 0.33203 0.51085] | 0.111 | 0.02 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.44377 0.51156 0.40821] | 0.111 | 0.0204 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
