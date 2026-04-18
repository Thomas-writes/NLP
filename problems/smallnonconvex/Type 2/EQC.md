# EQC

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
- **# of Constraints (m):** 3
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.0081608 0.010649 0.46137 0.48828 0.51471 0.30882 0.083333] | -830 | 0.0293 | 132 | `xtol` termination condition is satisfied. |
| trust-constr | success | [0.0079618 0.010649 0.4352 0.52468 0.54119 0.30882 0.083333] | -829 | 0.0236 | 117 | `xtol` termination condition is satisfied. |
| trust-constr | success | [0.0081608 0.01045 0.40541 0.48649 0.58744 0.30882 0.083333] | -831 | 0.027 | 125 | `xtol` termination condition is satisfied. |
| SLSQP | success | [0.0079618 0.01045 0.41281 0.48649 0.53832 0.31025 0.083738] | -830 | 0.000374 | 2 | Optimization terminated successfully |
| SLSQP | fail | [0.0079618 0.01045 0.47387 0.48649 0.51471 0.30882 0.20457] | -855 | 0.000435 | 2 | Inequality constraints incompatible |
| SLSQP | success | [0.0079618 0.01045 0.47163 0.52391 0.51471 0.30882 0.13492] | -864 | 0.000782 | 4 | Optimization terminated successfully |
| COBYLA | success | [0.0081608 0.010649 0.40541 0.48649 0.51471 0.39174 0.083333] | -1.45e+05 | 0.0195 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.0081608 0.010649 0.40541 0.501 0.51471 0.31527 0.083333] | -1.53e+05 | 0.0224 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.0081608 0.01045 0.40541 0.48649 0.57123 0.30882 0.083333] | -1.83e+05 | 0.0214 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
