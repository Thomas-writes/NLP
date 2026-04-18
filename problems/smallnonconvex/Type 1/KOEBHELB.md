# KOEBHELB

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [9.6243 0.79198 0.58087] | 77.51634735582567 | 0.0009298340301029384 | 31 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [10.668 -0.05603 0.25112] | 112.91943412226469 | 0.0007374169654212892 | 15 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [10.461 0.9823 1.6428] | 114.17234411325983 | 0.00010370800737291574 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | fail | [10.159 -0.79802 0.001] | 114.17234411325983 | 9.629200212657452e-05 | 0 | Linear search failed |
| TNC | fail | [6.9641 1.4606 0.43723] | 114.17234411325983 | 9.158399188891053e-05 | 0 | Linear search failed |
| TNC | fail | [8.6849 1.6639 0.20704] | 114.17234411325983 | 8.55830148793757e-05 | 0 | Linear search failed |
| Powell | success | [9.9589 -1.776 0.001] | 114.17234411325983 | 0.0017577080288901925 | 2 | Optimization terminated successfully. |
| Powell | success | [10.244 -1.3233 0.001] | 114.17234411325983 | 0.001841624965891242 | 2 | Optimization terminated successfully. |
| Powell | success | [10.478 -1.6258 0.99412] | 114.17234411325983 | 0.0018062920426018536 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [10.566 0.23643 0.22739] | 77.51634736290441 | 0.0018087910139001906 | 129 | Optimization terminated successfully. |
| Nelder-Mead | success | [12.072 0.79916 0.001] | 114.17234411325983 | 0.00044704199535772204 | 14 | Optimization terminated successfully. |
| Nelder-Mead | success | [11.048 -0.17631 0.001] | 112.22441304633759 | 0.001176042016595602 | 75 | Optimization terminated successfully. |
