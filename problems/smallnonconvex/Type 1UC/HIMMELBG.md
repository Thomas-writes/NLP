# HIMMELBG

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
| CG | success | [0.54533 0.33928] | 6.22e-12 | 0.000305 | 5 | Optimization terminated successfully. |
| CG | success | [0.63918 0.43035] | 1.05e-12 | 0.000272 | 5 | Optimization terminated successfully. |
| CG | success | [0.60122 0.44734] | 3.88e-13 | 0.000259 | 6 | Optimization terminated successfully. |
| BFGS | success | [0.29099 0.71203] | 2.31e-13 | 0.000536 | 9 | Optimization terminated successfully. |
| BFGS | success | [0.57413 0.38448] | 2.32e-16 | 0.000291 | 7 | Optimization terminated successfully. |
| BFGS | success | [0.39977 0.73658] | 1.57e-13 | 0.000247 | 6 | Optimization terminated successfully. |
| dogleg | fail | [0.59887 0.47352] | 0.476 | 5.85e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.54662 0.45009] | 0.445 | 5.72e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.47005 0.50434] | 0.455 | 5.37e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | success | [0.46031 0.552] | 6.63e-14 | 0.000966 | 34 | Optimization terminated successfully. |
| trust-ncg | success | [0.46792 0.4993] | 1.09e-14 | 0.000995 | 37 | Optimization terminated successfully. |
| trust-ncg | success | [0.56381 0.51852] | 1.18e-14 | 0.000981 | 37 | Optimization terminated successfully. |
