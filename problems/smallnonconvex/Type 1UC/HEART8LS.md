# HEART8LS

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-0.12845 1.0425 0.045754 0.93853 0.86775 0.96951 1.0542 1.1231] | 1.75e-11 | 0.0135 | 375 | Optimization terminated successfully. |
| CG | success | [0.1588 0.91663 0.046085 0.91932 0.96695 1.1271 0.90493 0.89646] | 4.55e-12 | 0.0126 | 349 | Optimization terminated successfully. |
| CG | success | [0.17667 1.0787 0.10016 0.83633 0.90517 1.042 1.0699 1.1155] | 1.47e-10 | 0.0167 | 454 | Optimization terminated successfully. |
| BFGS | success | [-0.15073 0.87872 -0.15891 1.0216 1.0723 0.95544 0.94058 0.80086] | 8.22e-13 | 0.00817 | 258 | Optimization terminated successfully. |
| BFGS | fail | [-0.0013873 1.0616 0.064536 0.94269 1.0919 1.0168 1.1462 1.0593] | 1.14 | 0.0634 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [0.16025 1.0483 -0.0014515 0.90731 1.1263 0.99274 0.81579 1.1841] | 1.14 | 0.0593 | 1600 | Maximum number of iterations has been exceeded. |
| dogleg | fail | [-0.064557 0.8498 -0.167 0.93749 0.73283 1.0157 1.0579 1.0616] | 186 | 6.82e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.060217 1.1179 -0.11828 0.93661 1.2579 1.1739 1.0876 1.0337] | 135 | 5.73e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.10314 1.0375 -0.17581 0.92502 0.98628 0.78943 1.0936 1.1418] | 233 | 5.34e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.058785 1.0072 -0.082634 0.8788 0.90147 0.94291 0.93802 0.76218] | 203 | 0.0773 | 1600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [-0.16121 1.0315 0.19288 1.092 1.0298 1.1254 0.89581 0.91222] | 82.4 | 0.0513 | 1600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [-0.012838 1.2048 -0.12163 0.97861 1.1183 1.0153 0.91438 1.0427] | 161 | 0.0759 | 1600 | Maximum number of iterations has been exceeded. |
