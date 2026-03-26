# HEART6LS

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
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [-0.083958 0.10714 0.98889 0.88992 1.132 1.0757] | 0.219 | 0.0531 | 1200 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.095239 0.096337 0.83152 0.99111 0.91899 1.0078] | 0.0359 | 0.0511 | 1200 | Maximum number of iterations has been exceeded. |
| CG | fail | [-0.22485 -0.04822 1.0613 1.0798 0.8073 0.98003] | 0.00164 | 0.0584 | 1200 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [-0.016717 0.0181 0.8622 0.90408 1.0386 1.0087] | 0.00975 | 0.0436 | 1200 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [-0.053809 -0.15825 1.1007 1.0822 0.89559 1.0664] | 0.00806 | 0.0447 | 1200 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [0.0977 0.15134 1.1123 1.0681 1.0819 1.0414] | 0.101 | 0.0426 | 1200 | Maximum number of iterations has been exceeded. |
| dogleg | fail | [0.07887 0.03388 1.0759 1.0774 1.1159 1.0852] | 592 | 6.68e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.076892 0.0017911 1.0508 1.1503 0.90412 0.87116] | 561 | 5.82e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.1163 0.033341 1.044 0.95262 1.0932 1.0351] | 566 | 5.58e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.015269 -0.03824 0.9811 1.1051 1.1051 1.1529] | 420 | 0.0248 | 1200 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.016999 0.0098444 0.94017 1.056 1.0307 1.0885] | 433 | 0.0257 | 1200 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.013862 -0.098683 0.86909 0.91429 1.0753 1.1153] | 96.6 | 0.0458 | 1200 | Maximum number of iterations has been exceeded. |
