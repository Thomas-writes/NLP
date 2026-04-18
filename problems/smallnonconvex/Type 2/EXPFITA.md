# EXPFITA

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
- **# of Constraints (m):** 22
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [1.4619 1.336 6.117 0.23361 0.018171] | 0.00114 | 0.031 | 53 | `gtol` termination condition is satisfied. |
| trust-constr | success | [1.2444 1.6555 5.6352 0.21212 0.020883] | 0.00114 | 0.0314 | 55 | `gtol` termination condition is satisfied. |
| trust-constr | success | [1.2984 -0.41331 6.2235 -0.30861 -0.095875] | 0.00114 | 0.0342 | 59 | `gtol` termination condition is satisfied. |
| SLSQP | success | [2.0977 1.3638 6.4347 0.19832 0.011899] | 0.00114 | 0.00276 | 28 | Optimization terminated successfully |
| SLSQP | success | [1.6631 0.58708 6.1032 0.38752 0.058212] | 0.00114 | 0.00272 | 28 | Optimization terminated successfully |
| SLSQP | success | [1.2189 0.96771 6.407 0.53263 0.098759] | 0.0013 | 0.00461 | 49 | Optimization terminated successfully |
| COBYLA | success | [0.66651 0.92072 5.8065 -0.23041 -0.075357] | 35 | 0.0523 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [1.3262 0.8367 6.4457 -0.41953 -0.10528] | 0.00114 | 0.137 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.87646 0.38884 6.2411 -0.58736 -0.1524] | 51.4 | 0.0501 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
