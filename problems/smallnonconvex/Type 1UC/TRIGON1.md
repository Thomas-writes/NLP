# TRIGON1

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
- **# of Variables (n):** 10
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.12827 0.12883 0.22013 0.038942 0.038843 -0.033002 0.04176 0.046271 0.064256 0.16078] | 9.86e-12 | 0.0024 | 73 | Optimization terminated successfully. |
| CG | success | [0.069994 0.20191 0.20492 0.026825 0.1103 0.16248 0.1389 -0.016801 0.20823 0.1222] | 2.31e-12 | 0.0021 | 68 | Optimization terminated successfully. |
| CG | success | [0.30078 -0.1592 0.23694 0.31154 0.033572 0.21563 0.059498 -0.018978 0.26535 0.208] | 6.47e-12 | 0.00234 | 75 | Optimization terminated successfully. |
| BFGS | success | [-0.027942 0.0090804 0.27231 0.09242 0.10504 0.069615 0.14441 0.0062672 0.18322 0.027176] | 3.49e-14 | 0.000823 | 18 | Optimization terminated successfully. |
| BFGS | success | [0.18432 0.060511 0.0078702 0.20697 0.057491 0.28697 0.16498 0.12383 -0.051396 0.18706] | 3.66e-14 | 0.000724 | 17 | Optimization terminated successfully. |
| BFGS | success | [0.037944 0.18356 0.066754 0.16403 -0.032643 0.16618 0.1718 0.08603 0.047787 0.097394] | 5.26e-13 | 0.000596 | 16 | Optimization terminated successfully. |
| dogleg | fail | [0.12164 0.12771 -0.12867 0.10053 -0.018361 0.10458 0.10923 0.14924 0.064842 0.13754] | 3.9 | 7.42e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.18941 0.053634 0.15544 0.34939 0.058269 0.14688 0.063897 0.14946 0.10422 0.0039788] | 3.25 | 5.85e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.09711 0.18318 0.20538 0.23688 0.063905 0.12394 0.056904 -0.065878 0.17494 0.18224] | 5.69 | 5.55e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | success | [0.15263 0.012585 0.19095 0.18501 0.035414 0.086633 0.1968 -0.073218 0.16674 0.05163] | 2.45e-13 | 0.021 | 712 | Optimization terminated successfully. |
| trust-ncg | success | [-0.1682 0.20182 0.24452 0.1175 0.040959 -0.099477 -0.0056474 0.055327 0.20997 0.03562] | 2.37e-13 | 0.0179 | 610 | Optimization terminated successfully. |
| trust-ncg | success | [0.023187 0.028508 0.10948 0.17783 0.16719 0.13331 0.11369 0.21133 0.23986 0.18582] | 2.37e-13 | 0.0167 | 569 | Optimization terminated successfully. |
