# EXPFITC

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
- **# of Variables (n):** 5
- **# of Constraints (m):** 502
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [1.4366 1.4059 6.0602 0.124 0.036079] | 0.0233 | 4.61 | 90 | `gtol` termination condition is satisfied. |
| trust-constr | success | [1.1458 1.084 6.1345 -0.13434 -0.053954] | 0.0233 | 4.05 | 80 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.83076 1.1512 5.9573 -0.8763 -0.2095] | 0.0233 | 4.93 | 101 | `gtol` termination condition is satisfied. |
| SLSQP | success | [1.3143 0.71631 5.9532 -0.1707 -0.025119] | 0.0233 | 0.0102 | 15 | Optimization terminated successfully |
| SLSQP | success | [1.006 1.3603 5.655 -0.24131 -0.076178] | 0.0233 | 0.0117 | 19 | Optimization terminated successfully |
| SLSQP | success | [1.0101 1.1674 5.8881 0.11548 0.0029155] | 0.0233 | 0.0139 | 23 | Optimization terminated successfully |
| COBYLA | success | [1.9804 1.7315 6.9339 -0.98835 -0.20453] | 0.0233 | 0.946 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.90113 1.0104 6.0069 -0.13096 -0.041896] | 785 | 0.28 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.096462 1.5701 6.3787 0.1872 -0.0012778] | 1.22e+04 | 0.926 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
