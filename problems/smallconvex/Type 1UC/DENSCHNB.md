# DENSCHNB

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
| CG | success | [1.1 1.1154] | 1.94e-11 | 0.000268 | 4 | Optimization terminated successfully. |
| CG | success | [1.0893 1.0316] | 1.29e-13 | 0.000247 | 6 | Optimization terminated successfully. |
| CG | success | [0.99642 1.0458] | 5.15e-13 | 0.000251 | 6 | Optimization terminated successfully. |
| BFGS | success | [0.88251 1.1577] | 1.87e-13 | 0.000332 | 9 | Optimization terminated successfully. |
| BFGS | success | [0.79172 1.091] | 4.04e-15 | 0.000346 | 11 | Optimization terminated successfully. |
| BFGS | success | [1.0801 0.9436] | 1.52e-15 | 0.000342 | 11 | Optimization terminated successfully. |
| dogleg | success | [0.97982 0.86682] | 1.27e-17 | 0.000261 | 5 | Optimization terminated successfully. |
| dogleg | fail | [1.0314 1.0765] | 6.34 | 4.86e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.90434 1.0267] | 6.57 | 5.48e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.97397 0.9826] | 0.0837 | 0.000188 | 3 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0241 0.96094] | 0.0447 | 0.000113 | 2 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0183 1.0653] | 0.0986 | 0.00072 | 31 | A bad approximation caused failure to predict improvement. |
