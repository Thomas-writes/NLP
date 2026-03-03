# DENSCHNF

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
| CG | success | [2.0745 0.26887] | 3.04e-15 | 0.000446 | 9 | Optimization terminated successfully. |
| CG | success | [1.881 -0.02047] | 1.85e-16 | 0.000366 | 8 | Optimization terminated successfully. |
| CG | success | [2.0426 0.062775] | 5.45e-14 | 0.000417 | 10 | Optimization terminated successfully. |
| BFGS | success | [2.1206 -0.1484] | 1.03e-14 | 0.000376 | 10 | Optimization terminated successfully. |
| BFGS | success | [1.7531 0.21911] | 5.32e-15 | 0.000349 | 9 | Optimization terminated successfully. |
| BFGS | success | [2.2318 0.018695] | 3.1e-17 | 0.000351 | 10 | Optimization terminated successfully. |
| dogleg | success | [2.3205 -0.22342] | 2.85e-16 | 0.00037 | 6 | Optimization terminated successfully. |
| dogleg | success | [2.1724 -0.065342] | 1.02e-18 | 0.000269 | 6 | Optimization terminated successfully. |
| dogleg | success | [2.0305 0.037397] | 1.82e-21 | 0.000255 | 6 | Optimization terminated successfully. |
| trust-ncg | fail | [1.5969 -0.094671] | 0.116 | 0.00435 | 225 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.0533 -0.15267] | 0.528 | 0.00371 | 188 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.5705 0.13314] | 0.255 | 0.00416 | 216 | A bad approximation caused failure to predict improvement. |
