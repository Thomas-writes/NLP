# SIPOW2M

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
- **Objective Type:** linear
- **# of Variables (n):** 2
- **# of Constraints (m):** 2000
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.72216 0.50462] | -1 | 103 | 34 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.85636 0.38403] | -0.995 | 54.8 | 18 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.78385 0.44896] | -0.995 | 57 | 18 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0.7897 0.48642] | -1 | 0.00675 | 6 | Optimization terminated successfully |
| SLSQP | success | [0.82658 0.50323] | -1 | 0.00729 | 6 | Optimization terminated successfully |
| SLSQP | success | [0.73215 0.576] | -1 | 0.00659 | 6 | Optimization terminated successfully |
| COBYLA | success | [0.79793 0.38986] | -1 | 0.129 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.6477 0.4715] | -1 | 0.195 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.7179 0.48857] | -1 | 0.235 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
