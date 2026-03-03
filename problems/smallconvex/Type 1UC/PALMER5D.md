# PALMER5D

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Convex
- **Objective Type:** quadratic
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.8702 0.9133 0.90855 0.965] | 87.3 | 0.000968 | 23 | Optimization terminated successfully. |
| CG | success | [0.9987 1.1906 0.76939 1.0595] | 87.3 | 0.00249 | 60 | Optimization terminated successfully. |
| CG | success | [0.94398 1.0159 1.041 0.9936] | 87.3 | 0.00202 | 54 | Optimization terminated successfully. |
| BFGS | success | [0.90684 1.1208 1.1586 0.83582] | 87.3 | 0.000388 | 11 | Optimization terminated successfully. |
| BFGS | success | [0.93607 1.0147 0.96036 1.08] | 87.3 | 0.000367 | 11 | Optimization terminated successfully. |
| BFGS | success | [1.0152 0.88652 1.3085 1.08] | 87.3 | 0.000353 | 11 | Optimization terminated successfully. |
| dogleg | success | [1.019 1.1518 0.90949 1.0964] | 87.3 | 0.000414 | 8 | Optimization terminated successfully. |
| dogleg | success | [0.93662 1.0937 0.9694 1.0705] | 87.3 | 0.000368 | 8 | Optimization terminated successfully. |
| dogleg | success | [0.95131 1.0505 1.0128 1.0755] | 87.3 | 0.000375 | 8 | Optimization terminated successfully. |
| trust-ncg | fail | [1.0751 1.1615 0.87657 1.0091] | 1.78e+04 | 0.00021 | 6 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.1249 1.2192 1.0167 0.99237] | 1.52e+04 | 0.000328 | 11 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.95861 0.87111 0.94187 0.92686] | 1.79e+04 | 0.000199 | 6 | A bad approximation caused failure to predict improvement. |
