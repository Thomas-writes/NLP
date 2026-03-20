# LOGHAIRY

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
| CG | success | [-565.73 -731.43] | 0.182 | 0.0048 | 46 | Optimization terminated successfully. |
| CG | success | [-517.41 -638.19] | 0.182 | 0.00809 | 97 | Optimization terminated successfully. |
| CG | success | [-598 -766.07] | 0.182 | 0.0118 | 148 | Optimization terminated successfully. |
| BFGS | success | [-486.12 -577.96] | 0.182 | 0.00242 | 36 | Optimization terminated successfully. |
| BFGS | success | [-491.49 -789.7] | 0.182 | 0.00509 | 86 | Optimization terminated successfully. |
| BFGS | success | [-507.39 -793.81] | 0.182 | 0.00857 | 146 | Optimization terminated successfully. |
| dogleg | fail | [-558.2 -767.87] | 6.65 | 6.7e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-476.41 -659.86] | 6.49 | 5.36e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-481.79 -707.99] | 6.56 | 4.51e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-438.19 -655.47] | 6.49 | 0.000701 | 31 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-549.47 -662.45] | 6.5 | 0.000708 | 33 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-505.24 -690.36] | 6.54 | 0.000354 | 10 | A bad approximation caused failure to predict improvement. |
