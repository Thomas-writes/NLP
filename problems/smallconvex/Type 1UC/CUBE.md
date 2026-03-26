# CUBE

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
| CG | success | [-1.1748 1.1718] | 2.84e-11 | 0.00152 | 31 | Optimization terminated successfully. |
| CG | success | [-1.2524 0.86068] | 1.23e-10 | 0.00106 | 24 | Optimization terminated successfully. |
| CG | success | [-1.166 1.1889] | 1.81e-19 | 0.00108 | 27 | Optimization terminated successfully. |
| BFGS | success | [-1.2214 0.82179] | 4.01e-15 | 0.0027 | 75 | Optimization terminated successfully. |
| BFGS | success | [-1.2821 0.81665] | 6.69e-18 | 0.00132 | 37 | Optimization terminated successfully. |
| BFGS | success | [-1.1581 1.0021] | 1.62e-14 | 0.00118 | 35 | Optimization terminated successfully. |
| dogleg | success | [-1.3008 1.1564] | 1e-22 | 0.00468 | 32 | Optimization terminated successfully. |
| dogleg | success | [-1.0544 1.0043] | 5e-15 | 0.00103 | 32 | Optimization terminated successfully. |
| dogleg | success | [-1.1529 1.0557] | 4.2e-16 | 0.00106 | 31 | Optimization terminated successfully. |
| trust-ncg | fail | [-1.2602 1.1069] | 0.455 | 0.00783 | 360 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-1.0689 1.0058] | 0.454 | 0.00757 | 341 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-1.1654 1.0322] | 0.454 | 0.00766 | 358 | A bad approximation caused failure to predict improvement. |
