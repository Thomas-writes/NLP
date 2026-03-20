# DEVGLA2

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
- **Objective Type:** sum of squares
- **# of Variables (n):** 5
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [18.505 4.1414 0.21376 1.3995 -2.8373] | nan | 0.00164 | 2 | NaN result encountered. |
| CG | fail | [18.17 -1.2287 0.49856 3.4551 0.8895] | nan | 4.57e-05 | 0 | NaN result encountered. |
| CG | fail | [21.48 -2.4821 -0.2213 4.7482 -1.6593] | nan | 3.71e-05 | 0 | NaN result encountered. |
| BFGS | fail | [21.207 3.0436 4.2031 0.36656 -1.0876] | nan | 0.00709 | 5 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [17.14 2.0513 2.093 -0.57029 -2.1025] | nan | 0.0016 | 2 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [17.592 1.1301 2.4042 1.827 -0.74886] | 0.0267 | 0.00197 | 51 | Optimization terminated successfully. |
| dogleg | fail | [19.75 1.9603 3.9729 3.4924 0.14501] | 1.21e+04 | 8.23e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [21.828 0.67804 0.23516 2.5707 -1.2023] | 1.43e+04 | 5.95e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [20.497 -2.1731 2.2833 2.852 3.8606] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [19.446 2.0771 2.9349 0.43414 1.201] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [19.411 3.2691 1.9575 3.7056 0.88108] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [20.425 3.9632 3.6034 4.1875 -0.35521] | nan | nan | None | array must not contain infs or NaNs |
