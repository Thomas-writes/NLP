# PALMER2B

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.1171 1.0874 1.0205 0.88353] | 0.6232669721739978 | 0.0006156669987831265 | 31 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0137 1.0491 1.1965 0.90157] | 0.6232669721662355 | 0.0006615419988520443 | 37 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.99066 0.94 0.86217 0.89455] | 0.6232669721646108 | 0.0006471250089816749 | 34 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.90904 0.92989 1.1777 0.83079] | 11439.397126147987 | 0.00044337500003166497 | 1 | Linear search failed |
| TNC | fail | [0.84704 1.031 0.82342 0.98204] | 11183.061477423933 | 0.0004253750084899366 | 1 | Linear search failed |
| TNC | fail | [1.0577 0.81001 0.99063 0.87906] | 11656.538697919745 | 0.000426958009484224 | 1 | Linear search failed |
| Powell | success | [0.92531 1.0096 1.0713 1.2051] | 1407.3808961582963 | 0.0034993750014109537 | 7 | Optimization terminated successfully. |
| Powell | success | [0.87604 0.94128 1.0894 0.83499] | 1404.4528892115848 | 0.004567915995721705 | 8 | Optimization terminated successfully. |
| Powell | success | [0.89371 0.8727 1.091 1.0891] | 1493.3545882368962 | 0.004383292005513795 | 8 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.88168 0.94919 1.0303 0.98671] | 0.6232669784539594 | 0.005151250006747432 | 418 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.1201 1.0462 0.99081 0.96938] | 0.6232669747780668 | 0.003015707989106886 | 250 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0861 0.9804 0.99155 1.0501] | 0.6232669742909629 | 0.004117124990443699 | 328 | Optimization terminated successfully. |
