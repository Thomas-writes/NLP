# YFITU

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
| CG | fail | [2.7552 -2.3854 22.91] | 5.24e+03 | 0.00513 | 113 | Desired error not necessarily achieved due to precision loss. |
| CG | success | [-0.15486 -1.8456 22.001] | 6.01e-08 | 0.00764 | 191 | Optimization terminated successfully. |
| CG | success | [-2.7904 0.08125 22.095] | 6.03e-10 | 0.0109 | 243 | Optimization terminated successfully. |
| BFGS | success | [1.8769 -2.0752 18.971] | 5.02e+03 | 0.00214 | 53 | Optimization terminated successfully. |
| BFGS | success | [1.5799 0.084628 18.955] | 4.75e+03 | 0.0023 | 61 | Optimization terminated successfully. |
| BFGS | fail | [-0.33277 -2.925 20.421] | 5.61e+03 | 0.00343 | 58 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [-0.17926 0.7206 17.833] | 1.16e+04 | 7.33e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-1.0221 0.809 22.557] | 1.95e+04 | 6.27e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [2.7884 0.62204 20.242] | 4.27e+08 | 5.52e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [4.1781 0.72579 19.819] | 7.94e+04 | 0.0151 | 600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [-3.1557 -0.99667 22.596] | 9.4e+04 | 0.0161 | 503 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-1.207 -1.2201 19.453] | 250 | 0.000922 | 36 | A bad approximation caused failure to predict improvement. |
