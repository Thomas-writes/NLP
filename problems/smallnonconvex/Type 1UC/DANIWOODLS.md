# DANIWOODLS

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.55873 4.0382] | 0.00432 | 0.000533 | 10 | Optimization terminated successfully. |
| CG | success | [1.7945 5.8597] | 0.00432 | 0.000557 | 11 | Optimization terminated successfully. |
| CG | success | [0.1936 4.9468] | 0.00432 | 0.000556 | 11 | Optimization terminated successfully. |
| BFGS | success | [0.72131 4.5884] | 0.00432 | 0.000409 | 10 | Optimization terminated successfully. |
| BFGS | success | [0.63576 5.6937] | 0.00432 | 0.000522 | 14 | Optimization terminated successfully. |
| BFGS | success | [-0.014919 5.4491] | 0.00432 | 0.000508 | 15 | Optimization terminated successfully. |
| dogleg | fail | [0.95886 4.2423] | 24.5 | 6.63e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.0596 4.8558] | 145 | 5.03e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.7312 4.4739] | 409 | 4.79e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.50687 4.3374] | 0.142 | 0.000698 | 33 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.18557 5.2239] | 1.11 | 0.000784 | 30 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.5977 4.6748] | 0.257 | 0.000139 | 3 | A bad approximation caused failure to predict improvement. |
