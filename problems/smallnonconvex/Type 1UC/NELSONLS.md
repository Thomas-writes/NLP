# NELSONLS

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
| CG | fail | [2.0142 0.15831 -0.64741] | 3.41e+157 | 0.000276 | 0 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [2.3373 -0.29945 0.095514] | 53.6 | 0.0005 | 2 | Desired error not necessarily achieved due to precision loss. |
| CG | success | [2.049 0.21754 0.70632] | 54.4 | 0.000102 | 1 | Optimization terminated successfully. |
| BFGS | success | [2.0707 0.10232 0.45834] | 54.4 | 0.000108 | 1 | Optimization terminated successfully. |
| BFGS | success | [1.8486 -0.2788 -0.062712] | 54.4 | 0.000135 | 2 | Optimization terminated successfully. |
| BFGS | success | [2.4164 0.1328 0.30045] | 54.4 | 0.000162 | 1 | Optimization terminated successfully. |
| dogleg | fail | [2.0909 -0.055991 -0.025587] | 1.72e+08 | 9.08e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.9999 0.65317 0.096854] | 64.5 | 6.99e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [2.0968 -0.32055 -0.23679] | 1.16e+60 | 6.58e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [2.0348 0.12485 0.040087] | 62.2 | 0.000117 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.833 -0.13642 -0.31927] | 248 | 0.00512 | 114 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.0379 0.21788 -0.22943] | 99.3 | 0.00287 | 94 | A bad approximation caused failure to predict improvement. |
