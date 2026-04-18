# QCNEW

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
| trust-constr | success | [0.0081608 0.010649 0.45939 0.48649 0.52112 0.30882 0.25194] | -805 | 0.0225 | 112 | `xtol` termination condition is satisfied. |
| trust-constr | success | [0.0079618 0.010649 0.45 0.48649 0.51471 0.39217 0.088982] | -806 | 0.0258 | 121 | `xtol` termination condition is satisfied. |
| trust-constr | success | [0.0079618 0.01045 0.41253 0.51034 0.51471 0.44681 0.15793] | -809 | 0.024 | 116 | `xtol` termination condition is satisfied. |
| SLSQP | success | [0.0081608 0.010649 0.40541 0.5267 0.51471 0.30882 0.083333] | -807 | 0.000414 | 3 | Optimization terminated successfully |
| SLSQP | success | [0.0079618 0.01045 0.46835 0.48649 0.51471 0.44367 0.12701] | -852 | 0.00177 | 19 | Optimization terminated successfully |
| SLSQP | success | [0.0079618 0.010649 0.40541 0.48649 0.51471 0.37117 0.083333] | -881 | 0.000519 | 7 | Optimization terminated successfully |
| COBYLA | success | [0.0081608 0.01045 0.40541 0.48649 0.53949 0.30882 0.083333] | -1.09e+05 | 0.019 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.0079618 0.01045 0.45434 0.48649 0.66699 0.30882 0.083333] | -1.12e+05 | 0.0215 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.0081608 0.010649 0.40541 0.50722 0.51471 0.30882 0.087816] | -1.38e+05 | 0.0214 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
