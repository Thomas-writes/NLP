# MGH10LS

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
- **Objective Type:** sum of squares
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [6054.9 4.709e+05 25396] | 1.42e+09 | 0.042 | 561 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [5143.4 3.7626e+05 -66836] | 1.3e+09 | 0.00274 | 42 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [-2130.8 4.2889e+05 -47536] | 3.94e+07 | 0.0054 | 76 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [222.07 3.9105e+05 -5841.1] | 3.89e+09 | 6.96e-05 | 0 | Optimization terminated successfully. |
| BFGS | fail | [-454.95 3.5492e+05 37216] | 3.22e+05 | 0.0206 | 600 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [-93366 3.4155e+05 17978] | 1.36e+24 | 0.000419 | 3 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [-18689 4.2383e+05 28229] | 5.59e+22 | 7.36e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-39126 4.1103e+05 -20330] | 3.89e+09 | 5.59e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-34254 3.7533e+05 12502] | 1.49e+36 | 5.3e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [53072 3.1676e+05 49437] | 3.92e+15 | 0.0154 | 600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [-8876.9 4.1442e+05 35044] | 4.87e+17 | 0.014 | 600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [13510 3.9737e+05 31133] | 4.86e+18 | 0.014 | 600 | Maximum number of iterations has been exceeded. |
