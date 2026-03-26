# SINEVAL

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
- **Objective Type:** sum of squares
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [3.8726 0.10038] | 2.45e-12 | 0.00225 | 48 | Optimization terminated successfully. |
| CG | success | [5.3883 -0.75454] | 6.84e-13 | 0.00295 | 64 | Optimization terminated successfully. |
| CG | success | [4.0262 -1.163] | 2.29e-12 | 0.00237 | 55 | Optimization terminated successfully. |
| BFGS | success | [4.8696 -1.2974] | 1.59e-18 | 0.00238 | 70 | Optimization terminated successfully. |
| BFGS | success | [4.0191 -1.3502] | 1.16e-16 | 0.00302 | 85 | Optimization terminated successfully. |
| BFGS | success | [4.8489 -0.98427] | 1.36e-16 | 0.0024 | 74 | Optimization terminated successfully. |
| dogleg | fail | [5.288 -1.028] | 2.56 | 0.0007 | 19 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [4.6793 -1.381] | 2.54 | 0.000485 | 13 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [4.714 -0.23866] | 585 | 5.02e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [5.1445 -0.1694] | 552 | 0.000736 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [4.1403 -0.589] | 67.7 | 7.75e-05 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [4.0009 -1.6754] | 27.3 | 0.000711 | 31 | A bad approximation caused failure to predict improvement. |
