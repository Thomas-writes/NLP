# HATFLDD

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
| CG | success | [1.0572 -0.89446 0.016201] | 9.51e-08 | 0.000856 | 16 | Optimization terminated successfully. |
| CG | success | [1.0401 -0.957 -0.047328] | 2.55e-07 | 0.00129 | 32 | Optimization terminated successfully. |
| CG | success | [1.0293 -1.0596 -0.037882] | 2.73e-07 | 0.00124 | 30 | Optimization terminated successfully. |
| BFGS | success | [0.81059 -1.1437 -0.020756] | 6.62e-08 | 0.00111 | 32 | Optimization terminated successfully. |
| BFGS | success | [0.9057 -0.88356 -0.034914] | 6.62e-08 | 0.00111 | 34 | Optimization terminated successfully. |
| BFGS | success | [0.92715 -0.94911 0.11049] | 6.62e-08 | 0.00128 | 35 | Optimization terminated successfully. |
| dogleg | fail | [0.89883 -0.97194 0.13115] | 29.5 | 6.31e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.1337 -0.90661 0.013704] | 22.1 | 5.85e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.0679 -0.88087 0.010672] | 23 | 5.43e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.0953 -0.73584 -0.081613] | 2.08 | 0.000109 | 1 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.91618 -1.0014 0.075925] | 6.83 | 9.73e-05 | 1 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.98027 -0.97177 0.0071351] | 5.55 | 9.13e-05 | 1 | A bad approximation caused failure to predict improvement. |
