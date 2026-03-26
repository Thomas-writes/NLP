# THURBERLS

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
- **# of Variables (n):** 7
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [869.18 891.56 387.2 86.141 -6.9584 0.19287 -122.05] | 7.79e+05 | 0.0714 | 1400 | Maximum number of iterations has been exceeded. |
| CG | fail | [1160 1088.8 362.72 -73.912 135.01 126.48 -39.38] | 1.7e+07 | 0.0697 | 1400 | Maximum number of iterations has been exceeded. |
| CG | fail | [1021.4 998.23 249.81 2.5738 146.84 -129.05 148.04] | 4.34e+06 | 0.0753 | 1400 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [827.17 1140.1 549.14 -58.546 -26.132 188.41 38.278] | 5.64e+03 | 0.00399 | 59 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [1031.4 1012.7 338.95 148.94 0.17966 -197.41 69.135] | 4.91e+05 | 0.00432 | 105 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [1024.6 1036.7 589.59 127.48 52.409 69.542 24.695] | 1.55e+04 | 0.00506 | 88 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [1243.8 827.08 404.99 88.083 -20.807 -24.194 176.22] | 2.37e+08 | 7.94e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [882.07 1065.8 274.03 71.643 262.87 -5.4095 -78.632] | 3.41e+07 | 6.62e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [981.99 1004.5 374.92 233.95 172.9 116.93 65.029] | 3.34e+07 | 6.31e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1111 932.69 214.65 -71.976 139.75 -32.97 -48.047] | 3.33e+07 | 0.000979 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1101 1023.4 478.63 -10.06 172.38 -24.694 -141.64] | 3.21e+07 | 0.00103 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [943.47 983.08 513.25 31.665 -84.376 -61.429 13.474] | 5.79e+07 | 0.000114 | 2 | A bad approximation caused failure to predict improvement. |
