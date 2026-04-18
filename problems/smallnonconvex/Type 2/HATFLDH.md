# HATFLDH

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
- **Objective Type:** quadratic
- **# of Variables (n):** 4
- **# of Constraints (m):** 7
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [1.5916 4.3801 3.8937 1.1955] | -24.5 | 0.0103 | 26 | `gtol` termination condition is satisfied. |
| trust-constr | success | [1.5631 3.4448 4.4487 0.89309] | -24.5 | 0.00897 | 23 | `gtol` termination condition is satisfied. |
| trust-constr | success | [1.2451 3.7957 4.567 1.9299] | -24.5 | 0.00785 | 20 | `gtol` termination condition is satisfied. |
| SLSQP | success | [1.4357 4.9817 4.1883 1.4648] | -24.4 | 0.000335 | 2 | Optimization terminated successfully |
| SLSQP | success | [0.64514 4.0117 3.7281 0.96543] | -24.4 | 0.000316 | 2 | Optimization terminated successfully |
| SLSQP | success | [1.6816 4.5309 4.2822 1.3928] | -24.5 | 0.000537 | 5 | Optimization terminated successfully |
| COBYLA | success | [1.5457 4.1062 4.9333 2.1671] | -24.5 | 0.0161 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [1.1773 4.4075 4.4472 1.1648] | -24.5 | 0.0126 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [1.5606 4.355 4.3551 0.60842] | -24.4 | 0.019 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
