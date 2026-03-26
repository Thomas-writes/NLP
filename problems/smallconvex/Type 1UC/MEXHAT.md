# MEXHAT

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
- **Objective Type:** other
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.95452 0.78917] | -0.04 | 0.00337 | 56 | Optimization terminated successfully. |
| CG | fail | [0.87964 0.70573] | 4.22e+07 | 0.000387 | 1 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [0.74779 0.6376] | 3.79e+08 | 0.000279 | 0 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [0.69259 0.76579] | -0.04 | 0.00219 | 72 | Optimization terminated successfully. |
| BFGS | success | [1.1026 0.70206] | -0.04 | 0.00254 | 68 | Optimization terminated successfully. |
| BFGS | success | [0.92548 0.54588] | -0.04 | 0.00388 | 128 | Optimization terminated successfully. |
| dogleg | success | [0.99852 0.73535] | -0.04 | 0.00808 | 233 | Optimization terminated successfully. |
| dogleg | fail | [0.65958 0.72255] | 6.83e+10 | 7.9e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | success | [0.89607 0.69467] | -0.04 | 0.00198 | 62 | Optimization terminated successfully. |
| trust-ncg | fail | [0.84821 0.49607] | 9.41e+05 | 0.00125 | 36 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.77391 0.81172] | 1.86e+06 | 0.0135 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.73567 0.83007] | 1.25e+06 | 0.00163 | 37 | A bad approximation caused failure to predict improvement. |
