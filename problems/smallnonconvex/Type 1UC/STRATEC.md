# STRATEC

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
- **Objective Type:** other
- **# of Variables (n):** 10
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [-0.01128 -0.049082 0.022924 0.080204 -0.05245 -0.14529 -0.071932 0.074111 0.070177 0.81885] | 2.21e+03 | 15.6 | 2000 | Maximum number of iterations has been exceeded. |
| CG | fail | [-0.24016 -0.11302 0.022384 0.021477 0.094876 -0.10294 0.037984 0.017054 -0.050059 0.72653] | 2.21e+03 | 14.6 | 2000 | Maximum number of iterations has been exceeded. |
| CG | fail | [-0.1276 -0.015745 0.15546 -0.049807 0.019025 -0.15635 -0.10477 0.24374 -0.14844 0.91996] | 2.21e+03 | 15 | 2000 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [0.05779 0.019144 -0.054881 0.088896 -0.024493 0.042604 -0.035993 -0.14732 -0.021795 1.0468] | 2.21e+03 | 0.382 | 53 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-0.071842 0.043271 0.073195 -0.042723 -0.08821 -0.13862 -0.013184 -0.1791 -0.052826 1.1467] | 2.21e+03 | 0.312 | 55 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [0.022516 -0.080942 0.055153 0.033088 -0.021491 -0.13309 -0.050688 0.04389 0.20002 0.88874] | 2.21e+03 | 0.281 | 42 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [-0.029431 -0.06077 -0.17127 0.026701 -0.0059685 -0.042182 -0.033203 0.12482 0.012725 1.0265] | 3.65e+03 | 0.117 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.10997 -0.088011 -0.2389 0.069529 0.02343 -0.090273 -0.0053862 -0.16638 -0.040753 0.94425] | 8.69e+03 | 0.101 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.00057366 -0.088302 0.016988 -0.18727 -0.078512 0.018267 0.14101 0.07642 0.075917 1.0879] | 2.87e+04 | 0.0979 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.3111 -0.094128 -0.019221 -0.081569 -0.10271 -0.031705 0.12655 0.13953 -0.1266 1.0683] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [0.0017674 -0.088887 -0.089708 0.061507 -0.087192 -0.055292 -0.026565 -0.12006 -0.09322 0.93337] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [0.023055 0.023371 -0.13566 -0.089493 -0.11761 -0.013096 0.054231 -0.00076031 -0.066626 0.93832] | nan | nan | None | array must not contain infs or NaNs |
