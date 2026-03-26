# BROWNDEN

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [23.496 2.6554 -3.5516 -2.6434] | 8.58e+04 | 0.00111 | 24 | Optimization terminated successfully. |
| CG | fail | [24.549 3.2457 0.78186 -3.7158] | 8.58e+04 | 0.00174 | 25 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [22.039 6.8476 -7.1499 1.182] | 8.58e+04 | 0.00125 | 30 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [25.23 9.0306 -11.756 -0.27076] | 8.58e+04 | 0.00115 | 31 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [25.214 7.6351 -3.3678 -2.1273] | 8.58e+04 | 0.000997 | 30 | Optimization terminated successfully. |
| BFGS | success | [25.09 5.1438 -5.6037 4.6902] | 8.58e+04 | 0.000901 | 27 | Optimization terminated successfully. |
| dogleg | fail | [23.867 4.7243 -2.4754 2.9118] | 8.58e+04 | 0.00049 | 10 | A bad approximation caused failure to predict improvement. |
| dogleg | success | [27.636 4.1435 -5.0177 -4.0359] | 8.58e+04 | 0.00047 | 11 | Optimization terminated successfully. |
| dogleg | fail | [26.131 2.7413 -1.9469 -1.466] | 8.58e+04 | 0.000448 | 10 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [20.003 6.3706 2.1842 -3.0491] | 2.99e+06 | 0.000926 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [26.42 5.5768 -2.5061 1.5817] | 7.13e+06 | 0.00087 | 27 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [27.162 6.0912 -7.1233 -2.6862] | 1.08e+07 | 0.000866 | 27 | A bad approximation caused failure to predict improvement. |
