# CHWIRUT1LS

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
| CG | success | [-0.058425 -0.11277 0.053104] | 3.15e+05 | 0.000185 | 2 | Optimization terminated successfully. |
| CG | fail | [0.084743 0.24629 0.18935] | 2.38e+03 | 0.00303 | 41 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [0.061182 -0.13745 0.079173] | 3.06e+05 | 0.00027 | 1 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [0.17576 0.033026 0.1246] | 2.38e+03 | 0.00132 | 20 | Optimization terminated successfully. |
| BFGS | success | [0.18467 -0.0028798 -0.069371] | 3.15e+05 | 0.000124 | 2 | Optimization terminated successfully. |
| BFGS | fail | [0.073233 0.18447 0.19969] | 2.38e+03 | 0.00203 | 16 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [0.23266 -0.093204 0.057796] | 3.02e+05 | 0.002 | 34 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.066784 0.047195 -0.0083676] | 4.8e+03 | 0.000836 | 12 | A bad approximation caused failure to predict improvement. |
| dogleg | fail | [0.021566 -0.14779 -0.19837] | 3.15e+05 | 0.000756 | 11 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.0035461 0.065515 0.16392] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [0.20887 0.050191 0.15845] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [0.032122 0.010211 -0.14097] | 3.54e+05 | 0.000201 | 1 | A bad approximation caused failure to predict improvement. |
