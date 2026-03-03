# CUBE

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
- **Objective Type:** sum of squares
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-1.1696 0.87175] | 2.23e-15 | 0.00139 | 27 | Optimization terminated successfully. |
| CG | success | [-1.1625 0.90132] | 3.39e-12 | 0.00111 | 29 | Optimization terminated successfully. |
| CG | success | [-1.3723 0.98733] | 8.13e-11 | 0.00124 | 30 | Optimization terminated successfully. |
| BFGS | success | [-1.0156 1.0361] | 4.53e-16 | 0.00122 | 37 | Optimization terminated successfully. |
| BFGS | success | [-1.0621 0.88354] | 3.6e-15 | 0.00102 | 34 | Optimization terminated successfully. |
| BFGS | success | [-1.1713 1.266] | 6.75e-15 | 0.00119 | 38 | Optimization terminated successfully. |
| dogleg | success | [-1.1214 0.94277] | 1.19e-18 | 0.00295 | 31 | Optimization terminated successfully. |
| dogleg | success | [-1.2951 1.0113] | 1.18e-12 | 0.00099 | 31 | Optimization terminated successfully. |
| dogleg | success | [-1.382 0.90725] | 1.4e-12 | 0.000998 | 32 | Optimization terminated successfully. |
| trust-ncg | fail | [-1.043 0.96871] | 0.454 | 0.00718 | 367 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-1.3988 0.95271] | 0.455 | 0.00695 | 316 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-1.4121 0.81103] | 0.454 | 0.00627 | 330 | A bad approximation caused failure to predict improvement. |
