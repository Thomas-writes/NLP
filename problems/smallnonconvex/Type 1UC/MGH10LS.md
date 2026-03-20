# MGH10LS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-03

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-31446 4.105e+05 -30736] | 3.89e+09 | 0.00134 | 8 | Optimization terminated successfully. |
| CG | success | [-8113 3.8779e+05 -6360.2] | 3.89e+09 | 4.64e-05 | 0 | Optimization terminated successfully. |
| CG | fail | [2789.7 4.2228e+05 69759] | 1.27e+09 | 0.0127 | 242 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-86705 3.8028e+05 53295] | 6.47e+05 | 0.0194 | 600 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [16980 3.7924e+05 34486] | 7.27e+05 | 0.00875 | 221 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [30249 3.5088e+05 42487] | 6.55e+05 | 0.0196 | 600 | Maximum number of iterations has been exceeded. |
| dogleg | fail | [9393.1 4.6774e+05 35683] | 3.22e+20 | 6.05e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-34001 4.053e+05 -20217] | 3.89e+09 | 5.39e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-27602 3.7729e+05 38580] | 3.64e+18 | 5.02e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [42163 4.4335e+05 14071] | 1.57e+11 | 0.00359 | 142 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [23017 3.9396e+05 2546.7] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-39510 3.3656e+05 -22340] | 3.89e+09 | 0.000601 | 24 | A bad approximation caused failure to predict improvement. |
