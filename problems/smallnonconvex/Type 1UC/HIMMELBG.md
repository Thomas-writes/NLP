# HIMMELBG

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
- **Objective Type:** other
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.38644 0.66288] | 9.87e-20 | 0.000401 | 8 | Optimization terminated successfully. |
| CG | success | [0.52112 0.48354] | 2.5e-12 | 0.000315 | 6 | Optimization terminated successfully. |
| CG | success | [0.7639 0.38807] | 1.31e-13 | 0.000244 | 4 | Optimization terminated successfully. |
| BFGS | success | [0.50838 0.45873] | 4.96e-15 | 0.000326 | 7 | Optimization terminated successfully. |
| BFGS | success | [0.4312 0.56246] | 9.1e-14 | 0.000286 | 8 | Optimization terminated successfully. |
| BFGS | success | [0.44071 0.38841] | 2.22e-12 | 0.000254 | 6 | Optimization terminated successfully. |
| dogleg | fail | [0.50056 0.41688] | 0.409 | 6.64e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.41974 0.25774] | 0.28 | 5.27e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.41545 0.46469] | 0.412 | 4.97e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | success | [0.49406 0.429] | 8.39e-10 | 0.000507 | 18 | Optimization terminated successfully. |
| trust-ncg | success | [0.42785 0.42945] | 8.7e-10 | 0.000452 | 17 | Optimization terminated successfully. |
| trust-ncg | fail | [0.68801 0.59215] | 0.513 | 0.000779 | 30 | A bad approximation caused failure to predict improvement. |
