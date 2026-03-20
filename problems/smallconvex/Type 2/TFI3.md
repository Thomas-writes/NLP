# TFI3

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
- **Objective Type:** other
- **# of Variables (n):** 3
- **# of Constraints (m):** 101
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [1.0273 0.41575 0.072489] | 4.3 | 0.0432 | 25 | `gtol` termination condition is satisfied. |
| trust-constr | success | [1.1437 0.51674 -0.12161] | 4.3 | 0.0332 | 20 | `gtol` termination condition is satisfied. |
| trust-constr | success | [1.0362 0.38752 0.020241] | 4.3 | 0.0364 | 22 | `gtol` termination condition is satisfied. |
| SLSQP | success | [1.0383 0.4788 -0.087989] | 4.3 | 0.000821 | 4 | Optimization terminated successfully |
| SLSQP | success | [1.0748 0.49328 0.12332] | 4.3 | 0.000885 | 4 | Optimization terminated successfully |
| SLSQP | success | [1.0321 0.49642 -0.22554] | 4.3 | 0.000744 | 4 | Optimization terminated successfully |
| COBYLA | success | [1.0422 0.4977 0.03344] | 4.3 | 0.0774 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [1.1349 0.56041 0.13606] | 4.3 | 0.0639 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [1.0033 0.40452 -0.0067418] | 4.3 | 0.0256 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
