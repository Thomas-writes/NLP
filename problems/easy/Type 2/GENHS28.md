# GENHS28

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
- **# of Variables (n):** 10
- **# of Constraints (m):** 8
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [-3.66 1.54 0.474 0.842 1.08 1.4 0.905 1.32 1.05 0.746] | 0.927 | 0.00872 | 24 | `gtol` termination condition is satisfied. |
| trust-constr | success | [-4.64 1.21 1.11 0.889 1.06 0.792 0.983 0.907 0.841 0.799] | 0.927 | 0.00758 | 21 | `gtol` termination condition is satisfied. |
| trust-constr | success | [-4.06 0.943 1.24 1.46 0.938 1.1 1.09 0.912 0.811 1.17] | 0.927 | 0.00756 | 22 | `gtol` termination condition is satisfied. |
| SLSQP | success | [-4.08 1.16 1.23 1.24 0.864 0.905 0.931 1.2 1.24 1.03] | 0.927 | 0.00082 | 7 | Optimization terminated successfully |
| SLSQP | success | [-3.92 0.439 0.781 0.78 0.872 0.66 1.23 1.45 0.51 0.885] | 0.927 | 0.00082 | 7 | Optimization terminated successfully |
| SLSQP | success | [-3.84 0.968 0.947 0.925 1.52 0.927 0.487 0.343 1.28 0.623] | 0.927 | 0.000824 | 7 | Optimization terminated successfully |
| COBYLA | success | [-3.87 1.08 0.0529 1.26 1.04 0.849 0.829 1.09 1.13 0.483] | 0.928 | 0.238 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [-4.28 1.36 0.928 1.32 0.648 0.722 1.53 0.796 0.302 1.22] | 0.927 | 0.204 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [-4 0.976 1.7 1.54 0.612 1.88 0.793 0.52 1.16 0.915] | 0.927 | 0.289 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
