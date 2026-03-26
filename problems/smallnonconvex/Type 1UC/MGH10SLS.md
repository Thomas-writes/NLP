# MGH10SLS

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
| CG | fail | [195.43 414.52 223.9] | 8.25e+08 | 0.0116 | 205 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [173.78 343.57 210.24] | 5.3e+08 | 0.0139 | 264 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [139.21 486.91 239.07] | 1.15e+09 | 0.0146 | 279 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [223 465.46 216.84] | 1.69e+14 | 0.000432 | 3 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [221.09 391.46 162.42] | 1.3e+21 | 0.000333 | 3 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [201.11 402.13 266.45] | 87.9 | 0.0256 | 574 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [147.25 365.1 222.27] | 5.64e+15 | 6.37e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [186.93 374.38 214.27] | 7.28e+16 | 5.82e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [170.87 459.23 234.6] | 4.07e+18 | 5.39e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [192.07 353.26 227.51] | 1.4e+09 | 0.0014 | 45 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [263.6 380.43 242.7] | 1.4e+09 | 0.00386 | 143 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [197.65 377.17 251.65] | 1.4e+09 | 0.00383 | 130 | A bad approximation caused failure to predict improvement. |
