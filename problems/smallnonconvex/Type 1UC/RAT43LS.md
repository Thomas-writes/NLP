# RAT43LS

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [84.961 25.926 16.088 2.0443] | 9.06e+05 | 0.000356 | 1 | Desired error not necessarily achieved due to precision loss. |
| CG | success | [93.573 11.509 -10.956 19.23] | 1.08e+06 | 0.00018 | 3 | Optimization terminated successfully. |
| CG | fail | [109.68 -3.0718 7.173 -17.235] | 1.08e+06 | 0.000816 | 15 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [95.868 7.3291 15.62 8.4036] | 9.58e+05 | 0.00061 | 3 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [104.26 20.9 -8.5414 -16.055] | 1.08e+06 | 0.000155 | 3 | Optimization terminated successfully. |
| BFGS | success | [85.863 13.385 -13.105 2.8439] | 1.08e+06 | 0.00023 | 1 | Optimization terminated successfully. |
| dogleg | fail | [92.271 -5.512 -6.0579 -4.0325] | 2.18e+22 | 6.65e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [95.732 7.7071 5.8986 23.978] | 2.68e+06 | 6.04e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [95.96 -4.8568 -1.0844 -28.959] | 2.41e+06 | 5.66e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [88.851 22.403 -10.072 14.723] | 2.73e+06 | 0.0151 | 800 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [95.594 20.172 -4.477 -19.484] | 3.75e+05 | 0.000218 | 4 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [105.93 24.6 18.874 10.505] | nan | nan | None | array must not contain infs or NaNs |
