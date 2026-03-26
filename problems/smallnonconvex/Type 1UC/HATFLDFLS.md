# HATFLDFLS

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
| CG | success | [0.17075 0.0027308 0.086497] | 9.41e-08 | 0.00264 | 46 | Optimization terminated successfully. |
| CG | success | [0.16856 0.14588 0.13351] | 6.07e-08 | 0.00325 | 66 | Optimization terminated successfully. |
| CG | success | [0.063142 -0.17156 0.09615] | 6.72e-05 | 0.00518 | 111 | Optimization terminated successfully. |
| BFGS | success | [0.057059 0.062813 0.35067] | 7.36e-14 | 0.00136 | 40 | Optimization terminated successfully. |
| BFGS | success | [0.10777 0.15851 0.07185] | 7.56e-13 | 0.00187 | 52 | Optimization terminated successfully. |
| BFGS | success | [-0.0035056 0.19535 0.050114] | 3.53e-13 | 0.00188 | 57 | Optimization terminated successfully. |
| dogleg | fail | [0.19147 -0.043407 0.060314] | 0.022 | 6.85e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.015031 0.08615 0.13424] | 0.0138 | 5.54e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.047789 0.12709 -0.043726] | 0.0342 | 5.57e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.077449 0.18262 0.018465] | 0.00259 | 0.000891 | 30 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.072956 0.39997 0.0059965] | 0.00636 | 0.000924 | 33 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.064541 0.11192 0.068692] | 0.00196 | 0.000721 | 31 | A bad approximation caused failure to predict improvement. |
