# DENSCHNF

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-25

## Classification
- **Convexity:** Convex
- **Objective Type:** sum of squares
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.8602 -0.10071] | 7.72e-15 | 0.000489 | 8 | Optimization terminated successfully. |
| CG | success | [1.7157 0.081141] | 1.28e-14 | 0.000403 | 8 | Optimization terminated successfully. |
| CG | success | [2.4304 -0.076577] | 2.14e-16 | 0.000603 | 10 | Optimization terminated successfully. |
| BFGS | success | [2.0242 -0.11323] | 2.35e-16 | 0.000431 | 12 | Optimization terminated successfully. |
| BFGS | success | [2.2389 0.086631] | 3.53e-14 | 0.000327 | 9 | Optimization terminated successfully. |
| BFGS | success | [2.0344 0.52232] | 7.95e-16 | 0.000328 | 9 | Optimization terminated successfully. |
| dogleg | success | [1.7951 -0.20099] | 4.04e-25 | 0.00028 | 6 | Optimization terminated successfully. |
| dogleg | success | [2.172 0.1682] | 2.52e-19 | 0.000233 | 6 | Optimization terminated successfully. |
| dogleg | success | [2.2634 0.051184] | 1.17e-17 | 0.000242 | 6 | Optimization terminated successfully. |
| trust-ncg | fail | [1.8844 -0.10012] | 5.4 | 0.00226 | 102 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.8584 0.11096] | 1.1 | 0.00321 | 135 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.0223 -0.074754] | 0.493 | 0.0034 | 149 | A bad approximation caused failure to predict improvement. |
