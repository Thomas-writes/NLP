# PALMER3

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
| L-BFGS-B | success | [0.95891 1.0898 1.1214 0.91355] | 2416.980393365019 | 0.00037745898589491844 | 10 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [1.0008 0.92989 0.84931 0.9606] | 2416.9805086919805 | 0.00025595800252631307 | 8 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.9473 0.8327 1.0128 1.0026] | 2265.958218263063 | 0.0008185409824363887 | 25 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.93316 1.0726 0.84914 1.0419] | 14406.106602949141 | 0.00044445903040468693 | 1 | Linear search failed |
| TNC | fail | [0.92977 0.80461 0.92421 0.93331] | 14411.042358149542 | 0.0004111669841222465 | 1 | Linear search failed |
| TNC | fail | [0.79397 0.94775 1.0224 0.8597] | 14609.910874277242 | 0.00040729204192757607 | 1 | Linear search failed |
| Powell | success | [0.90089 1.1688 0.9818 0.94704] | 2419.6237651983624 | 0.0018701659864746034 | 2 | Optimization terminated successfully. |
| Powell | success | [1.0467 1.0029 1.0691 1.0806] | 2419.063056663246 | 0.0018769589951261878 | 2 | Optimization terminated successfully. |
| Powell | success | [0.98616 0.96664 0.96501 1.1625] | 2419.2814528764625 | 0.0021469590137712657 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.95899 0.87949 1.0619 1.131] | 2416.9802568007804 | 0.0013576250057667494 | 108 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.94459 1.0387 0.92707 0.89683] | 2319.100089277592 | 0.001622250012587756 | 123 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.95425 1.0029 1.0281 0.99342] | 2416.9793431549506 | 0.0014234160189516842 | 112 | Optimization terminated successfully. |
