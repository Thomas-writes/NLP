# MISRA1BLS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-25

## Classification
- **Convexity:** Convex
- **Objective Type:** sum of squares
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [559.28 -58.061] | 4.77e+03 | 0.000776 | 4 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [496.26 34.795] | 4.77e+03 | 0.000658 | 4 | Desired error not necessarily achieved due to precision loss. |
| CG | success | [523.5 94.123] | 6.76e+03 | 0.000182 | 2 | Optimization terminated successfully. |
| BFGS | success | [482.54 -92.765] | 6.76e+03 | 0.000203 | 3 | Optimization terminated successfully. |
| BFGS | fail | [477.03 -39.411] | 4.84e+03 | 0.00071 | 5 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [506.95 -36.976] | 4.83e+03 | 0.00133 | 4 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [525.88 -89.228] | 3.27e+06 | 6.84e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [521.12 64.743] | 3.2e+06 | 6.26e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [469.16 0.37214] | 2.54e+06 | 5.88e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [629.33 3.8381] | 4.81e+06 | 0.000654 | 26 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [537.82 46.799] | 3.43e+06 | 0.000676 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [437.66 28.481] | 2.18e+06 | 0.000748 | 28 | A bad approximation caused failure to predict improvement. |
