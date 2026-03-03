# GAUSS1LS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Convex
- **Objective Type:** sum of squares
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [104.22 23.331 67.164 53.902 -2.0758 53.384 168.04 31.931] | 5.29e+04 | 0.00404 | 40 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [106.52 13.106 104.53 46.827 17.765 69.803 162.75 38.955] | 4.26e+04 | 0.00464 | 59 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [81.686 19.203 125.76 63.939 37.085 58.482 212.88 -6.6743] | 5.29e+04 | 0.00282 | 43 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [100.49 0.40596 92.715 61.429 28.949 66.006 165.48 38.156] | 1.32e+03 | 0.003 | 29 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [83.943 0.76762 115.78 55.346 2.8362 77.921 164.31 48.379] | 5.02e+04 | 0.00322 | 39 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [131.18 5.4898 129.02 39.663 55.097 97.147 202.32 36.37] | 1.32e+03 | 0.00381 | 43 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [97.457 20.613 121.31 85.614 16.123 89.201 154.42 34.585] | 8.74e+05 | 0.0002 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [96.906 11.899 137.43 41.975 -12.444 86.228 188.11 2.7002] | 1.02e+06 | 0.000133 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [88.453 1.3093 133.37 76.752 3.9641 65.781 163.29 -4.505] | 1.16e+06 | 0.000133 | 0 | A linalg error occurred, such as a non-psd Hessian. |
