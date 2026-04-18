# EXPFITB

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
- **# of Constraints (m):** 102
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [1.1868 1.2576 5.9603 -0.27979 -0.085128] | 0.00502 | 0.133 | 70 | `gtol` termination condition is satisfied. |
| trust-constr | success | [1.0612 1.3986 6.1204 -0.24766 -0.084779] | 0.00502 | 0.165 | 81 | `gtol` termination condition is satisfied. |
| trust-constr | success | [2.2972 0.30902 6.462 -0.46082 -0.12823] | 0.00502 | 0.151 | 79 | `gtol` termination condition is satisfied. |
| SLSQP | success | [1.3432 0.96521 5.9591 0.21143 0.028707] | 0.00502 | 0.00422 | 22 | Optimization terminated successfully |
| SLSQP | success | [1.5032 1.2035 5.8298 -0.3111 -0.080159] | 0.00502 | 0.00378 | 20 | Optimization terminated successfully |
| SLSQP | success | [1.2404 1.0319 6.0112 0.60517 0.094671] | 1.05e+05 | 0.00117 | 5 | Optimization terminated successfully |
| COBYLA | success | [1.0987 1.1197 6.2166 0.5315 0.078765] | 0.00502 | 0.439 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.81599 0.86236 5.9984 -0.11683 -0.05333] | 0.00502 | 0.197 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.85612 0.48222 6.3361 -0.37206 -0.095781] | 93.2 | 0.089 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
