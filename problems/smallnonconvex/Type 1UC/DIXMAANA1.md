# DIXMAANA1

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.8208 1.9041 2.072] | 1 | 0.000305 | 5 | Optimization terminated successfully. |
| CG | success | [2.0558 2.1276 2.2279] | 1 | 0.000296 | 6 | Optimization terminated successfully. |
| CG | success | [1.9088 2.1837 1.9137] | 1 | 0.000233 | 5 | Optimization terminated successfully. |
| BFGS | success | [1.9056 1.8018 2.1499] | 1 | 0.000447 | 12 | Optimization terminated successfully. |
| BFGS | success | [2.3438 1.9894 2.0737] | 1 | 0.0005 | 15 | Optimization terminated successfully. |
| BFGS | success | [1.6055 1.971 1.8969] | 1 | 0.000345 | 11 | Optimization terminated successfully. |
| dogleg | fail | [2.1299 2.0717 2.0629] | 34.8 | 5.93e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [2.142 2.1501 1.9904] | 36 | 5.58e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [2.3092 2.1768 2.2187] | 46 | 5.15e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | success | [1.9857 1.927 2.2178] | 1 | 0.000581 | 21 | Optimization terminated successfully. |
| trust-ncg | success | [2.0858 2.1559 2.0564] | 1 | 0.000575 | 21 | Optimization terminated successfully. |
| trust-ncg | success | [2.0119 2.2124 2.0966] | 1 | 0.000478 | 18 | Optimization terminated successfully. |
