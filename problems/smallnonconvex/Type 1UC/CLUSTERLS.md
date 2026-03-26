# CLUSTERLS

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-0.050695 -0.049357] | 4.37e-09 | 0.000425 | 6 | Optimization terminated successfully. |
| CG | success | [0.18431 -0.05207] | 1.19e-10 | 0.000506 | 8 | Optimization terminated successfully. |
| CG | success | [-0.13659 -0.00046663] | 1.29e-10 | 0.000367 | 7 | Optimization terminated successfully. |
| BFGS | success | [0.17713 0.20899] | 1.07e-08 | 0.000422 | 12 | Optimization terminated successfully. |
| BFGS | success | [0.095474 -0.015779] | 7.25e-09 | 0.000512 | 14 | Optimization terminated successfully. |
| BFGS | success | [0.0020024 -0.15428] | 2.04e-08 | 0.000338 | 8 | Optimization terminated successfully. |
| dogleg | fail | [0.03183 0.18274] | 0.604 | 6.08e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.063701 -0.017221] | 1.17 | 5.72e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.018681 0.00047412] | 0.962 | 5.56e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.015059 -0.040591] | 0.0281 | 0.000196 | 3 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.113 -0.010455] | 0.00613 | 0.000398 | 7 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-0.11012 0.0201] | 0.0188 | 0.000178 | 3 | A bad approximation caused failure to predict improvement. |
