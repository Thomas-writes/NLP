# OSBORNEB

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
- **# of Variables (n):** 11
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.2822 0.72877 1.1352 1.3141 -0.18919 2.0846 4.93 6.8075 2.905 4.0798 5.377] | 0.0401 | 0.0137 | 331 | Optimization terminated successfully. |
| CG | success | [1.4587 -0.0030317 0.93736 0.83481 1.3353 2.5849 4.7489 7.0973 1.6925 5.1484 4.6073] | 0.0401 | 0.0179 | 435 | Optimization terminated successfully. |
| CG | success | [0.96962 1.246 0.77631 0.59279 1.0615 3.9396 4.6932 6.9746 1.5366 4.7562 3.985] | 0.0401 | 0.0203 | 500 | Optimization terminated successfully. |
| BFGS | success | [1.3866 0.87422 0.33756 0.81058 0.83279 2.7234 5.8975 7.3642 1.0418 4.037 4.6202] | 0.0876 | 0.00292 | 71 | Optimization terminated successfully. |
| BFGS | success | [2.1263 1.1777 1.1636 -0.97536 1.5314 2.8024 5.2128 7.51 2.0576 3.5273 5.0334] | 0.0401 | 0.00228 | 56 | Optimization terminated successfully. |
| BFGS | success | [1.9922 0.48167 0.27364 0.93367 0.7369 2.6323 4.8801 6.3022 1.4599 4.0455 5.0746] | 0.0401 | 0.00207 | 54 | Optimization terminated successfully. |
| dogleg | fail | [2.0814 0.55972 -0.31586 0.28003 0.38672 1.969 4.3256 7.9446 0.5666 4.8626 5.8067] | 20.3 | 0.000119 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.1442 0.30746 1.5104 0.79713 0.011346 3.2465 5.036 5.8984 2.6624 3.9742 6.2175] | 59.9 | 9.11e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.8458 -0.53405 -0.9806 0.19086 0.1887 3.7632 4.4181 6.3619 2.9667 4.1163 5.6822] | 13 | 8.37e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.5618 1.2952 0.22136 0.47988 0.75632 2.1883 4.6018 8.3958 1.2294 4.7792 4.7113] | 18.5 | 0.00167 | 30 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [3.2373 0.84647 0.24492 0.68064 1.7569 3.5519 5.248 7.2606 1.9708 5.1945 4.9386] | 8.26 | 0.00171 | 31 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.7358 0.55518 0.084565 0.35385 1.2294 1.7949 3.5515 7.6309 3.2086 4.653 6.4403] | 9.84 | 0.00172 | 31 | A bad approximation caused failure to predict improvement. |
