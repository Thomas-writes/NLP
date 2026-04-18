# PALMER4B

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
| L-BFGS-B | success | [0.9997 0.8584 0.87448 0.89862] | 6.835138602006215 | 0.0005674170097336173 | 27 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.005 0.94453 1.0667 1.0499] | 6.835138602100665 | 0.00047441700007766485 | 23 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.97558 0.94745 0.98373 1.0835] | 6.835138602226353 | 0.0005215420387685299 | 25 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.0729 0.92735 0.99411 1.0133] | 12303.293367930997 | 0.00042337505146861076 | 1 | Linear search failed |
| TNC | fail | [1.1513 1.0417 0.95055 1.0323] | 11824.642416074454 | 0.00040733302012085915 | 1 | Linear search failed |
| TNC | fail | [1.1303 0.7549 1.0303 1.0428] | 12801.455737258284 | 0.000422417011577636 | 1 | Linear search failed |
| Powell | success | [0.73073 0.88598 0.8478 0.91122] | 310.7344710760855 | 0.005187916045542806 | 8 | Optimization terminated successfully. |
| Powell | success | [1.0492 1.0271 1.1403 1.048] | 53.99465534542106 | 0.009403833013493568 | 22 | Optimization terminated successfully. |
| Powell | success | [1.1008 0.84861 1.0072 1.109] | 303.129170529085 | 0.0043547090026549995 | 7 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0316 1.0158 1.1794 1.0345] | 321.0481162860402 | 0.001597291964571923 | 130 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.036 0.92164 1.1018 1.1595] | 321.0481444278193 | 0.001813707989640534 | 146 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.1054 0.96766 1.0417 1.0957] | 191.88190378818527 | 0.0037035829736851156 | 286 | Optimization terminated successfully. |
