# DENSCHND

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
| CG | success | [10.907 9.7696 11.625] | 2.83e-08 | 0.00105 | 18 | Optimization terminated successfully. |
| CG | success | [9.8063 10.943 9.4524] | 8.44e-08 | 0.00205 | 41 | Optimization terminated successfully. |
| CG | success | [9.4552 8.783 8.1882] | 7.11e-08 | 0.0012 | 22 | Optimization terminated successfully. |
| BFGS | success | [9.9835 11.955 9.1449] | 3.41e-09 | 0.00317 | 104 | Optimization terminated successfully. |
| BFGS | success | [10.221 9.4336 9.1107] | 1.36e-08 | 0.00303 | 92 | Optimization terminated successfully. |
| BFGS | success | [10.353 10.899 9.3991] | 1.18e-09 | 0.00287 | 93 | Optimization terminated successfully. |
| dogleg | fail | [11.901 10.724 8.1944] | 1.42e+07 | 7.99e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [7.5638 8.7186 10.48] | 1.31e+08 | 5.41e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [9.6103 10.286 11.427] | 2.57e+08 | 5.09e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [12.114 9.6475 9.7309] | 1.72e-06 | 0.0152 | 600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [9.4267 9.4388 10.319] | 1.76e-06 | 0.0152 | 600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [11.855 8.7826 9.5231] | 1.69e-06 | 0.0153 | 600 | Maximum number of iterations has been exceeded. |
