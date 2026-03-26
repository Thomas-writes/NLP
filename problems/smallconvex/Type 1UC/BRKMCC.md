# BRKMCC

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
- **Objective Type:** other
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [2.1448 1.6322] | 0.169 | 0.000366 | 5 | Optimization terminated successfully. |
| CG | success | [2.4909 2.0229] | 0.169 | 0.000296 | 6 | Optimization terminated successfully. |
| CG | success | [2.1908 1.9835] | 0.169 | 0.000211 | 4 | Optimization terminated successfully. |
| BFGS | success | [2.0815 2.2523] | 0.169 | 0.00026 | 7 | Optimization terminated successfully. |
| BFGS | success | [2.3801 1.9048] | 0.169 | 0.000305 | 8 | Optimization terminated successfully. |
| BFGS | success | [2.0227 1.6547] | 0.169 | 0.000162 | 3 | Optimization terminated successfully. |
| dogleg | success | [1.6538 2.3064] | 0.169 | 0.000177 | 3 | Optimization terminated successfully. |
| dogleg | success | [2.0395 1.7379] | 0.169 | 0.000158 | 3 | Optimization terminated successfully. |
| dogleg | success | [1.967 1.794] | 0.169 | 0.000154 | 3 | Optimization terminated successfully. |
| trust-ncg | fail | [1.9446 2.3625] | 0.416 | 0.000976 | 37 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.8683 2.2843] | 0.353 | 0.000851 | 32 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.1731 1.9928] | 0.565 | 0.000877 | 30 | A bad approximation caused failure to predict improvement. |
