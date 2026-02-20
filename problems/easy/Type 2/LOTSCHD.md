# LOTSCHD

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-02-19

## Classification
- **Convexity:** Convex
- **Degree:** Quadratic
- **# of Variables (n):** 12
- **# of Constraints (m):** 7
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| SLSQP | success | [-0.0155 0.00275 0.0507 0.0536 0.241 0.0357 -0.0313 0.0371 0.0765 -0.0546 -0.172 -0.112] | 2.4e+03 | 0.000903 | 6 | Optimization terminated successfully |
| SLSQP | success | [0.122 0.236 -0.102 -0.0444 0.0356 0.125 -0.0782 0.0618 -0.0809 0.0759 -0.0942 0.286] | 2.4e+03 | 0.000869 | 6 | Optimization terminated successfully |
| SLSQP | success | [0.0352 0.0593 -0.0545 -0.0774 0.0897 -0.0847 -0.138 -0.0861 -0.324 -0.014 -0.116 0.0707] | 2.4e+03 | 0.000865 | 6 | Optimization terminated successfully |
| COBYLA | fail | [-0.0989 -0.0732 -0.0384 -0.0408 0.119 0.0638 -0.0816 0.163 -0.111 -0.103 0.0841 -0.145] | 168 | 2.77 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [-0.065 0.062 -0.0264 0.0496 -0.0666 0.0258 -0.203 -0.0747 -0.00254 -0.155 0.159 0.131] | 167 | 2.88 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [-0.00678 -0.0494 0.0489 -0.141 -0.0407 -0.0524 -0.118 0.13 -0.0834 -0.044 -0.0257 -0.194] | 169 | 2.76 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
