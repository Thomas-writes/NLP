# PALMER6C

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [1.1066 0.91967 0.99856 0.91165 1.119 0.93494 0.88177 0.98633] | 0.0921 | 0.0657 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.88525 1.0779 1.0126 1.0864 1.1649 0.9543 0.97372 1.1369] | 0.0926 | 0.0699 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.98716 0.81737 0.96733 1.188 0.88706 1.14 1.0518 0.99015] | 0.0933 | 0.0602 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [0.97843 0.81688 1.0878 1.032 1.0488 0.82291 0.91501 0.99221] | 0.0164 | 0.00178 | 60 | Optimization terminated successfully. |
| BFGS | success | [0.81617 1.026 1.0711 0.9667 1.0449 1.2299 0.97847 1.1646] | 0.0164 | 0.00185 | 59 | Optimization terminated successfully. |
| BFGS | success | [1.1408 1.1953 0.90333 1.094 0.99803 1.0052 1.0004 0.95958] | 0.0164 | 0.0018 | 60 | Optimization terminated successfully. |
| dogleg | success | [0.89183 1.0667 1.2086 1.0296 1.0806 1.1814 0.97076 0.85192] | 0.0164 | 0.00138 | 30 | Optimization terminated successfully. |
| dogleg | success | [1.1474 0.96913 0.82708 0.93194 0.91553 0.92049 0.90786 0.83115] | 0.0164 | 0.00134 | 30 | Optimization terminated successfully. |
| dogleg | success | [1.1151 1.0653 1.1545 0.951 1.0799 0.99974 0.96157 1.1681] | 0.0164 | 0.00136 | 30 | Optimization terminated successfully. |
| trust-ncg | fail | [1.1852 1.0116 0.85646 1.1168 1.0528 1.065 1.1551 0.96907] | 902 | 0.000219 | 4 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.84086 1.0136 0.9692 1.0474 0.85381 1.1522 1.002 1.214] | 615 | 0.000268 | 7 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.91182 0.87601 1.0218 0.97791 0.8925 1.0747 0.90912 0.92279] | 204 | 0.000225 | 5 | A bad approximation caused failure to predict improvement. |
