# HIMMELBCLS

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.99343 1.1337] | 2.02e-16 | 0.000508 | 9 | Optimization terminated successfully. |
| CG | success | [0.91468 0.98427] | 3.41e-17 | 0.000413 | 8 | Optimization terminated successfully. |
| CG | success | [1.0421 0.83338] | 3.37e-19 | 0.000376 | 8 | Optimization terminated successfully. |
| BFGS | success | [0.90627 0.95329] | 8.8e-15 | 0.000372 | 8 | Optimization terminated successfully. |
| BFGS | success | [1.0254 1.1453] | 4.92e-14 | 0.000282 | 7 | Optimization terminated successfully. |
| BFGS | success | [0.87165 0.90843] | 1.72e-14 | 0.000329 | 8 | Optimization terminated successfully. |
| dogleg | fail | [0.93537 0.93261] | 111 | 6.05e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.97249 1.0002] | 107 | 5.55e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.83689 0.97527] | 114 | 5.45e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.97563 0.8615] | 1.05 | 0.00139 | 64 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.1311 0.92113] | 0.819 | 0.00135 | 64 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.97986 0.93578] | 1.05 | 0.00138 | 64 | A bad approximation caused failure to predict improvement. |
