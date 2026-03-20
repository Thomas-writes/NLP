# MGH17SLS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 5
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [81.581 176.68 -84.295 121.55 201.73] | 1.02 | 0.000711 | 3 | Desired error not necessarily achieved due to precision loss. |
| CG | success | [17.299 181.27 -95.107 137.33 219.5] | 1.11 | 0.000164 | 2 | Optimization terminated successfully. |
| CG | success | [25.506 164.94 -101.8 87.581 200.65] | 1.02 | 0.0015 | 28 | Optimization terminated successfully. |
| BFGS | success | [63.852 148.24 -72.602 92.962 182.44] | 1.02 | 0.001 | 24 | Optimization terminated successfully. |
| BFGS | success | [71.643 163.32 -90.58 109.71 217.6] | 1.02 | 0.000915 | 11 | Optimization terminated successfully. |
| BFGS | success | [45.623 159.11 -92.24 105.99 204.54] | 1.02 | 0.000942 | 20 | Optimization terminated successfully. |
| dogleg | fail | [64.406 170.76 -101.8 118.54 202.57] | 1.48e+05 | 7.78e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [64.938 165.59 -61.618 124.8 197.03] | 1.61e+05 | 5.58e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [61.992 145.72 -102.6 98.795 221.31] | 1.31e+05 | 5.59e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [37.715 150.32 -89.319 99.284 196.07] | 1.62e+04 | 0.024 | 735 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [52.756 172.93 -93.254 118.38 188.93] | 2.51e+04 | 0.0254 | 790 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [46.468 160.84 -74.9 107.38 186.16] | 2.9e+04 | 0.026 | 785 | A bad approximation caused failure to predict improvement. |
