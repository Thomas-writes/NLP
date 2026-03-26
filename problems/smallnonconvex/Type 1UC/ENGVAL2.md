# ENGVAL2

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
| CG | success | [0.83004 1.7195 -0.19551] | 112 | 0.00132 | 23 | Optimization terminated successfully. |
| CG | success | [1.1378 1.8358 -0.066209] | 112 | 0.00244 | 50 | Optimization terminated successfully. |
| CG | success | [0.82802 2.1227 -0.33722] | 112 | 0.00146 | 33 | Optimization terminated successfully. |
| BFGS | success | [0.84367 1.7764 -0.26815] | 112 | 0.000913 | 17 | Optimization terminated successfully. |
| BFGS | success | [1.0408 2.4999 0.11215] | 3.94e-17 | 0.00139 | 30 | Optimization terminated successfully. |
| BFGS | success | [0.70443 1.6503 -0.083165] | 1.52e-16 | 0.00122 | 30 | Optimization terminated successfully. |
| dogleg | fail | [1.3517 1.7911 -0.027042] | 665 | 6.47e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.0789 1.8282 -0.13301] | 681 | 5.82e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.91466 1.7597 -0.077585] | 746 | 5.63e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.86201 2.143 0.22142] | 263 | 0.000253 | 2 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.55885 2.3878 0.2039] | 205 | 0.0167 | 600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [1.0053 1.9675 -0.28687] | 290 | 0.000862 | 29 | A bad approximation caused failure to predict improvement. |
