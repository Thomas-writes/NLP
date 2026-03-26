# DANIWOODLS

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
| CG | success | [0.095561 4.8008] | 0.00432 | 0.000877 | 14 | Optimization terminated successfully. |
| CG | success | [0.99647 5.0701] | 0.00432 | 0.000765 | 16 | Optimization terminated successfully. |
| CG | success | [1.6901 4.2549] | 0.00432 | 0.000468 | 10 | Optimization terminated successfully. |
| BFGS | success | [1.6697 4.1517] | 0.00432 | 0.000456 | 13 | Optimization terminated successfully. |
| BFGS | success | [1.102 5.4629] | 0.00432 | 0.000765 | 17 | Optimization terminated successfully. |
| BFGS | success | [0.72299 4.9278] | 0.00432 | 0.000489 | 14 | Optimization terminated successfully. |
| dogleg | fail | [0.35413 5.7115] | 2.05 | 7.2e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.1285 4.5604] | 109 | 5.5e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | success | [0.54739 4.6006] | 0.00432 | 0.000313 | 7 | Optimization terminated successfully. |
| trust-ncg | fail | [0.30195 5.069] | 0.583 | 0.000807 | 32 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.70028 4.6759] | 0.232 | 0.000779 | 33 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.8581 5.2403] | 0.233 | 0.000843 | 34 | A bad approximation caused failure to predict improvement. |
