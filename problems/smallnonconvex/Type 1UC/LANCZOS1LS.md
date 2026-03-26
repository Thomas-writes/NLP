# LANCZOS1LS

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
| CG | success | [1.2812 0.16698 6.4273 5.0375 5.2542 6.5351] | 7.45e-07 | 0.0131 | 261 | Optimization terminated successfully. |
| CG | success | [1.3659 -0.38021 5.2912 5.293 6.6981 8.3881] | 1.15e-06 | 0.0163 | 307 | Optimization terminated successfully. |
| CG | success | [1.9996 -1.372 5.5995 5.3341 6.3522 7.7145] | 8.47e-06 | 0.0268 | 519 | Optimization terminated successfully. |
| BFGS | success | [2.0659 1.4549 5.1954 4.4926 7.7115 7.8553] | 2.57e-07 | 0.00207 | 63 | Optimization terminated successfully. |
| BFGS | success | [1.4053 0.10874 5.261 5.8186 6.6758 8.5321] | 4.29e-06 | 0.0038 | 110 | Optimization terminated successfully. |
| BFGS | success | [1.9281 0.61471 7.2304 5.6 6.1799 7.7859] | 1.23e-07 | 0.00252 | 76 | Optimization terminated successfully. |
| dogleg | fail | [0.01039 0.48531 6.4251 6.3752 7.1332 7.0892] | 231 | 7.98e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.22207 1.2555 5.9393 6.077 6.0503 8.9079] | 146 | 6.17e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.19646 -0.50322 6.1835 5.1892 6.6651 7.6365] | 227 | 5.97e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.23057 -1.1344 4.6515 4.5896 6.0983 5.6514] | 145 | 0.000835 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.31778 -1.311 4.9828 4.5656 6.7444 8.4369] | 156 | 0.000824 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-0.40956 -0.41493 5.5479 6.2085 7.5726 7.0583] | 188 | 0.00101 | 29 | A bad approximation caused failure to predict improvement. |
