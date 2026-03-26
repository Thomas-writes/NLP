# ALLINITU

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
- **Objective Type:** other
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.026414 0.067635 0.084026 0.081519] | 5.74 | 0.000576 | 11 | Optimization terminated successfully. |
| CG | success | [-0.1478 0.033605 0.22267 -0.047663] | 5.74 | 0.000422 | 11 | Optimization terminated successfully. |
| CG | success | [0.055555 -0.10937 0.088213 0.054676] | 5.74 | 0.000478 | 11 | Optimization terminated successfully. |
| BFGS | success | [-0.068956 -0.00029518 -0.042506 -0.010447] | 5.74 | 0.000576 | 11 | Optimization terminated successfully. |
| BFGS | success | [0.0038296 0.013104 -0.11229 -0.057234] | 5.74 | 0.000493 | 10 | Optimization terminated successfully. |
| BFGS | success | [-0.070646 -0.17225 -0.11747 0.064699] | 5.74 | 0.000554 | 11 | Optimization terminated successfully. |
| dogleg | fail | [0.0018978 0.0062707 -6.9395e-05 0.026076] | 13 | 6.61e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.080399 -0.06481 0.034183 -0.11563] | 13.7 | 5.74e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.0018638 -0.014514 0.078272 0.01669] | 13.1 | 5.97e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.21216 0.16617 -0.018687 0.20354] | 8.8 | 0.00102 | 41 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-0.014026 0.07418 -0.16699 0.010171] | 7 | 0.000158 | 3 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.035696 0.014437 -0.044338 0.069388] | 5.92 | 0.000309 | 10 | A bad approximation caused failure to predict improvement. |
