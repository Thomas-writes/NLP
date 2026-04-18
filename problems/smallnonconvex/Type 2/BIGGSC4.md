# BIGGSC4

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
| trust-constr | fail | [0.2218 0 0.1115 0.22328] | -0.0247 | 0.0218 | 108 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [0.25855 0.12458 0.065193 0] | -0.0169 | 0.0208 | 108 | Constraint violation exceeds 'gtol' |
| trust-constr | success | [0.17905 0.083694 0.098638 0] | -24.5 | 0.0181 | 53 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0.078818 0.084815 0.0719 0.16993] | -24.5 | 0.000578 | 5 | Optimization terminated successfully |
| SLSQP | success | [0.086092 0.1301 0.2334 0] | -24.5 | 0.000464 | 4 | Optimization terminated successfully |
| SLSQP | success | [0 0.31028 0.085603 0.018096] | -24.5 | 0.000537 | 5 | Optimization terminated successfully |
| COBYLA | success | [0.026315 0.091294 0.072772 0.27727] | -24.4 | 0.0172 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.12447 0.25839 0.07039 0.044542] | -24.4 | 0.0219 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.11721 0 0.18656 0.10963] | -24.5 | 0.0154 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
