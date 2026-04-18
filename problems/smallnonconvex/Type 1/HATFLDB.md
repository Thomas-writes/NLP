# HATFLDB

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
- **Objective Type:** sum of squares
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1e-07 0.1003 0.050179 0.012898] | 0.00557280901673085 | 0.0005749579868279397 | 30 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.013778 0.039278 0.013616 0.15348] | 0.005572809002259008 | 0.000362291990313679 | 18 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.13976 0.078408 0.068916 1e-07] | 0.005572809000427919 | 0.0005025829887017608 | 23 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | fail | [0.11172 1e-07 0.16226 0.090372] | 1.0000000998103034 | 8.529203478246927e-05 | 0 | Linear search failed |
| TNC | fail | [0.10283 0.076511 0.072432 0.19269] | 1.0823167382044225 | 8.245802018791437e-05 | 0 | Linear search failed |
| TNC | fail | [0.083642 0.12059 0.05676 1e-07] | 1.1350561688118768 | 0.00016883399803191423 | 1 | Linear search failed |
| Powell | success | [0.057181 0.08616 0.029524 0.089098] | 0.005575893095666004 | 0.011080749973189086 | 14 | Optimization terminated successfully. |
| Powell | success | [0.09618 0.18015 0.12013 0.08151] | 0.006967632551974001 | 0.0064967499929480255 | 9 | Optimization terminated successfully. |
| Powell | success | [0.049653 0.076283 0.083006 0.13673] | 0.007320606003071526 | 0.007092542015016079 | 9 | Optimization terminated successfully. |
| Nelder-Mead | success | [1e-07 0.20418 0.21075 0.068732] | 0.9999997676137078 | 0.0005524579901248217 | 43 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.20394 0.023852 0.1052 0.012227] | 0.07785190729148188 | 0.0015427910257130861 | 131 | Optimization terminated successfully. |
| Nelder-Mead | success | [1e-07 0.2179 0.28621 1e-07] | 1.0000001823417466 | 0.00046112498966977 | 35 | Optimization terminated successfully. |
