# EQC

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
- **Objective Type:** other
- **# of Variables (n):** 7
- **# of Constraints (m):** 3
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.0081608 0.010649 0.40541 0.48649 0.51471 0.30882 0.25456] | -828 | 0.0278 | 132 | `xtol` termination condition is satisfied. |
| trust-constr | fail | [0.0081608 0.010649 0.40541 0.57091 0.51471 0.31029 0.11774] | -828 | 0.0293 | 136 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [0.0081608 0.010649 0.40541 0.58095 0.51471 0.30882 0.087445] | -829 | 0.0266 | 129 | Constraint violation exceeds 'gtol' |
| SLSQP | success | [0.0079618 0.01045 0.40541 0.58571 0.51471 0.30882 0.36261] | -867 | 0.00154 | 8 | Optimization terminated successfully |
| SLSQP | success | [0.0079618 0.010649 0.40541 0.48649 0.51782 0.30882 0.083333] | -830 | 0.000363 | 2 | Optimization terminated successfully |
| SLSQP | fail | [0.0079618 0.01045 0.40541 0.51975 0.56518 0.30882 0.16377] | -946 | 0.000456 | 2 | Inequality constraints incompatible |
| COBYLA | success | [0.0079618 0.010649 0.42493 0.56173 0.51471 0.34959 0.10364] | -1.68e+05 | 0.0182 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.0079618 0.010649 0.40541 0.48649 0.51471 0.36433 0.083333] | -1.75e+05 | 0.0198 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.0079618 0.010649 0.44347 0.48649 0.51471 0.44029 0.083333] | -1.95e+05 | 0.0327 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
