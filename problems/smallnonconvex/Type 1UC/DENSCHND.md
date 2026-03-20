# DENSCHND

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [10.505 10.974 11.306] | 1.27e-08 | 0.00101 | 24 | Optimization terminated successfully. |
| CG | success | [10.089 9.5333 9.5762] | 3.63e-09 | 0.00115 | 26 | Optimization terminated successfully. |
| CG | success | [10.189 9.6865 10.457] | 1.47e-10 | 0.000878 | 15 | Optimization terminated successfully. |
| BFGS | success | [10.167 8.3064 10.639] | 2.96e-09 | 0.00329 | 110 | Optimization terminated successfully. |
| BFGS | success | [8.128 9.2439 10.59] | 3.99e-10 | 0.00319 | 111 | Optimization terminated successfully. |
| BFGS | success | [10.14 9.6737 9.5423] | 3.7e-09 | 0.00326 | 101 | Optimization terminated successfully. |
| dogleg | fail | [10.176 8.5702 9.5951] | 6.28e+07 | 8.24e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [9.9788 9.5648 12.118] | 4.29e+08 | 5.3e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [10.114 9.5896 9.6219] | 6.1e+07 | 5.18e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | success | [9.6962 9.6157 7.6788] | 2.48e-06 | 0.0126 | 504 | Optimization terminated successfully. |
| trust-ncg | success | [9.8173 11.222 10.086] | 2.48e-06 | 0.0126 | 504 | Optimization terminated successfully. |
| trust-ncg | success | [11.992 9.3857 10.061] | 2.48e-06 | 0.0124 | 500 | Optimization terminated successfully. |
