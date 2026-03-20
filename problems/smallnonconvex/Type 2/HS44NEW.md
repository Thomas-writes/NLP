# HS44NEW

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-03

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** quadratic
- **# of Variables (n):** 4
- **# of Constraints (m):** 6
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.74271 1.2002 0.94758 1.1046] | -15 | 0.0575 | 130 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.96971 0.88899 1.2673 1.011] | -15 | 0.00831 | 19 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.99101 1.0762 1.0147 1.0981] | -15 | 0.00849 | 20 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0.98763 0.95409 1.1785 0.88407] | -15 | 0.000592 | 5 | Optimization terminated successfully |
| SLSQP | success | [1.1485 0.89473 1.1484 1.0668] | -15 | 0.000512 | 5 | Optimization terminated successfully |
| SLSQP | success | [1.1752 0.99247 1.1845 1.0192] | -15 | 0.000526 | 5 | Optimization terminated successfully |
| COBYLA | fail | [1.0128 0.74793 1.0734 1.0071] | -2e+10 | 0.687 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [1.0896 0.91366 1.2627 0.91995] | -2.04e+10 | 0.682 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [1.1688 1.2002 1.2189 1.0254] | -2.05e+10 | 0.669 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
