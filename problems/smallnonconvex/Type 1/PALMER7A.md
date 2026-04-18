# PALMER7A

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
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.86607 0.85392 0.94495 0.90365 1.0226 0.96845] | 10.374601228921687 | 0.029491291963495314 | 1925 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0462 1.0141 1.0032 1.0107 1.0995 0.84116] | 10.39237696304434 | 0.024746207986027002 | 1649 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.92466 0.97697 1.0059 1.0582 0.74564 0.76715] | 10.374434740038911 | 0.029923541995231062 | 1977 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.1094 1.0759 0.97538 0.93391 0.8557 1.1331] | 11873.889892179948 | 0.000460083014331758 | 1 | Linear search failed |
| TNC | fail | [1.0369 1.178 1.0273 1.0764 1.0311 1.0666] | 10985.287533851297 | 0.00044249999336898327 | 1 | Linear search failed |
| TNC | fail | [1.0279 0.94167 1.0334 0.9751 0.94035 1.107] | 11691.213581209027 | 0.00042812502942979336 | 1 | Linear search failed |
| Powell | success | [0.91638 1.1616 0.93483 1.0362 0.8984 0.96265] | 119.66899770542867 | 0.007146582996938378 | 9 | Optimization terminated successfully. |
| Powell | success | [0.99276 0.82399 1.0608 0.9075 0.96643 1.0353] | 122.39137835351701 | 0.012357375002466142 | 19 | Optimization terminated successfully. |
| Powell | success | [0.99991 0.83867 1.1021 0.95339 1.1755 0.79653] | 132.17180323191894 | 0.009355457965284586 | 12 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.90587 1.0119 0.87487 1.1756 1.2133 1.1344] | 25.762916307174812 | 0.004751667031086981 | 390 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.80813 1.2111 1.1987 1.2226 1.0261 1.1158] | 25.762916306733484 | 0.00483300001360476 | 421 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.1233 0.96263 1.0349 0.98421 1.2606 1.0187] | 25.76291630656891 | 0.005187707953155041 | 444 | Optimization terminated successfully. |
