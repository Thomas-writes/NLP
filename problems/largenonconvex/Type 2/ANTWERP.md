# ANTWERP

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
- **Objective Type:** sum of squares
- **# of Variables (n):** 27
- **# of Constraints (m):** 10
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | fail | [0 0 0 1 1 0 1 1 1 0 0 0 1 1 1 1 0 1 1 0 38854 15801 8088.3 0 61929 0 32321] | 2.07e+11 | 0.0383 | 120 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [0 1 1 0 0 1 0 1 1 1 1 0 1 0 0 1 1 1 0 0 42831 19182 3492.5 0 61929 0 32321] | 4.88e+10 | 0.0381 | 120 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [1 0 1 0 0 1 0 0 1 1 0 0 1 0 0 1 1 0 1 0 39688 18185 4661.4 0 61929 0 32321] | 1.67e+10 | 0.0388 | 120 | Constraint violation exceeds 'gtol' |
| SLSQP | fail | [0 0 1 0 1 1 0 0 1 0 0 0 0 1 1 0 0 0 1 0 40032 17749 6468.3 0 61929 0 32321] | 9.03e+10 | 0.00169 | 1 | Inequality constraints incompatible |
| SLSQP | fail | [0 1 1 0 0 1 0 0 1 1 0 0 0 1 1 0 0 1 1 0 48199 17822 0 0 61929 0 32321] | 5.85e+08 | 0.00292 | 4 | Inequality constraints incompatible |
| SLSQP | fail | [0 0 0 1 0 1 0 0 0 0 1 0 1 1 0 0 1 1 0 1 42926 5294.3 17871 0 61929 0 32321] | 9.34e+07 | 0.00813 | 12 | Inequality constraints incompatible |
| COBYLA | fail | [0 0 0 0 1 0 1 0 0 1 1 1 0 0 1 0 0 1 1 0 40982 17240 6824.3 0 61929 0 32321] | 1.17e+09 | 5.69 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [0 0 1 0 1 1 0 1 1 1 0 1 1 1 0 0 1 0 1 1 35948 19176 8393.4 0 61929 0 32321] | 5.91e+09 | 5.71 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | success | [0 0 0 0 1 0 1 0 0 0 0 1 0 0 0 1 0 0 1 0 43422 18739 3185.2 0 61929 0 32321] | 1.43e+10 | 2.74 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
