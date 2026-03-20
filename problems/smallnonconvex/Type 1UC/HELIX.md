# HELIX

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-1.1568 -0.10261 -0.081461] | 8.83e-15 | 0.00142 | 34 | Optimization terminated successfully. |
| CG | success | [-0.89989 0.041683 -0.17164] | 2.63e-11 | 0.00207 | 58 | Optimization terminated successfully. |
| CG | success | [-1.1322 -0.015507 0.0029903] | 1.29e-11 | 0.00129 | 33 | Optimization terminated successfully. |
| BFGS | success | [-0.99262 0.04452 0.037513] | 7.28e-15 | 0.00102 | 31 | Optimization terminated successfully. |
| BFGS | success | [-0.82958 -0.13942 -0.15836] | 6.77e-16 | 0.00109 | 32 | Optimization terminated successfully. |
| BFGS | success | [-0.94418 -0.2192 0.050438] | 8.03e-15 | 0.000943 | 28 | Optimization terminated successfully. |
| dogleg | fail | [-1.0088 -0.0047651 -0.073749] | 2.42e+03 | 6.56e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-1.001 0.027325 0.048026] | 2.41e+03 | 4.91e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.83915 -0.059505 0.023816] | 2.41e+03 | 4.63e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-1.046 0.10075 0.023027] | 31.3 | 0.000151 | 3 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-1.1257 0.026366 0.08925] | 40 | 0.000131 | 3 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-0.89268 -0.12166 -0.065175] | 22.9 | 0.0105 | 600 | Maximum number of iterations has been exceeded. |
