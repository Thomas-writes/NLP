# QC

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
- **# of Variables (n):** 7
- **# of Constraints (m):** 4
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.010052 0.0070661 0.27605 0.54054 0.41977 0.18581 0.43104] | -835 | 0.0249 | 119 | `xtol` termination condition is satisfied. |
| trust-constr | success | [0.010052 0.0070661 0.39259 0.3747 0.54162 0.23601 0.38109] | -823 | 0.0336 | 145 | `xtol` termination condition is satisfied. |
| trust-constr | success | [0.0039809 0.012838 0.61763 0.2948 0.56134 0.24799 0.56408] | -828 | 0.0246 | 119 | `xtol` termination condition is satisfied. |
| SLSQP | success | [0.0039809 0.012838 0.55815 0.29934 0.42942 0.14279 0.31689] | -933 | 0.000411 | 2 | Optimization terminated successfully |
| SLSQP | success | [0.010052 0.012838 0.3035 0.34819 0.65728 0.15272 0.44488] | -957 | 0.000466 | 4 | Optimization terminated successfully |
| SLSQP | success | [0.010052 0.0070661 0.47743 0.40996 0.66552 0.089432 0.22278] | -941 | 0.000354 | 2 | Optimization terminated successfully |
| COBYLA | success | [0.010052 0.012838 0.67478 0.18366 0.61848 0.27654 0.29549] | -1.43e+05 | 0.0234 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.0039809 0.012838 0.41582 0.30085 0.66156 0.31862 0.39516] | -1.29e+05 | 0.0194 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.010052 0.0070661 0.36627 0.298 0.5104 0.31549 0.55687] | -1.67e+05 | 0.023 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
