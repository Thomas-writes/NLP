# HS21MOD

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
- **Objective Type:** sum of squares
- **# of Variables (n):** 7
- **# of Constraints (m):** 1
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | fail | [2.2688 -1.0638 0.39066 2 -0.12746 0 0] | -95.9 | 0.397 | 1000 | The maximum number of function evaluations is exceeded. |
| trust-constr | fail | [2.195 -0.96357 0.13518 2 0.28843 0 0] | -95.9 | 0.406 | 1000 | The maximum number of function evaluations is exceeded. |
| trust-constr | fail | [2.0471 -1.1562 0.036804 2 0.24079 0 0] | -95.8 | 0.405 | 1000 | The maximum number of function evaluations is exceeded. |
| SLSQP | success | [2.0049 -0.93609 0.0028089 2.2432 0.2337 -0.1841 0] | -96 | 0.00115 | 10 | Optimization terminated successfully |
| SLSQP | success | [2.1723 -0.90821 0.078361 2 -0.054734 -0.0065452 0.15708] | -96 | 0.00101 | 9 | Optimization terminated successfully |
| SLSQP | success | [2.1134 -0.93243 0.015688 2.0088 -0.029773 0 0.32865] | -96 | 0.000655 | 5 | Optimization terminated successfully |
| COBYLA | fail | [2.2035 -0.9763 -0.10699 2 -0.20011 0 0] | -100 | 0.553 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [2.4316 -0.79303 -0.18181 2 -0.13216 -0.2627 0.15391] | -100 | 0.573 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [2 -1.3683 -0.096036 2 0.028453 0 0.0633] | -100 | 0.566 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
