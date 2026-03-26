# VIBRBEAM

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
| CG | fail | [-3.6084 1.1169 0.49572 0.14963 1.9001 -0.0071021 0.23765 0.35707] | 3.17e+04 | 0.114 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [-4.7558 1.1971 -0.31492 -0.27911 2.1289 0.040141 0.62418 0.26269] | 2.8e+03 | 0.11 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [-3.4757 0.41944 0.033981 -0.4138 1.7791 0.1406 -0.032537 -0.029112] | 9.76 | 0.094 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [-3.9183 1.2128 -0.21495 -0.17696 1.779 -1.1238 0.13388 0.083163] | 10 | 0.00807 | 163 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-3.553 1.3079 -0.31143 -0.0094307 1.4885 0.025589 0.17591 -0.22305] | 8.39 | 0.00805 | 129 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-3.742 0.95131 0.34684 0.34828 1.9193 0.18043 -0.27974 -0.069153] | 10.9 | 0.00482 | 89 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [-3.3217 1.4277 -0.29366 0.36261 1.2824 0.2248 -0.51291 -0.77574] | 5.41e+09 | 9.33e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-3.5285 1.0781 0.92167 -0.079761 1.5413 0.40865 -0.20255 -0.22284] | 1.32e+08 | 8.14e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-3.5035 0.77669 0.69458 0.35639 2.7309 -0.030436 0.20898 -0.14266] | 4.32e+09 | 7.73e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-3.1399 0.6827 0.029473 0.33377 1.9673 -0.058704 -0.54683 0.38856] | 2.28e+09 | 0.00241 | 50 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-3.5782 1.6385 -0.1748 0.32918 1.3458 -0.73448 0.43429 -0.089216] | 1.41e+09 | 0.00207 | 46 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-3.292 0.6991 0.6636 -0.17131 2.0239 0.064396 0.21857 0.43906] | 6.8e+08 | 0.00903 | 146 | A bad approximation caused failure to predict improvement. |
