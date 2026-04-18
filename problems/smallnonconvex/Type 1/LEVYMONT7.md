# LEVYMONT7

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
| L-BFGS-B | success | [-8.7003 9.3459 6.1499 7.5083] | 3.8934127314953533 | 0.00041024998063221574 | 17 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [-6.6386 8.0704 7.086 8.5968] | 12.510759059489496 | 0.00025687500601634383 | 12 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [-9.1673 8.8645 9.4344 9.0959] | 19.27120065172968 | 0.00022358301794156432 | 9 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [-7.8772 6.9698 8.8369 8.6887] | 7.797738631811866 | 0.00026470900047570467 | 8 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [-9.0205 8.9873 7.2601 9.2435] | 12.510759059487219 | 0.00025812495732679963 | 8 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [-8.2518 8.8449 9.2034 8.4878] | 12.510759059487112 | 0.00018441601423546672 | 6 | Converged (|f_n-f_(n-1)| ~= 0) |
| Powell | success | [-9.0245 8.216 9.4166 7.6349] | 3.1095966938621804 | 0.000676875002682209 | 2 | Optimization terminated successfully. |
| Powell | success | [-9.501 8.8456 8.3761 7.5379] | 3.109653274321257 | 0.0005590840009972453 | 2 | Optimization terminated successfully. |
| Powell | success | [-8.3182 8.1896 7.7662 8.5147] | 3.109586802556249 | 0.0005543330335058272 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [-8.1446 7.6821 8.9728 8.79] | 12.510759081556893 | 0.001102791982702911 | 86 | Optimization terminated successfully. |
| Nelder-Mead | success | [-6.8321 7.6312 8.1441 8.6174] | 12.510759069824386 | 0.0012491249945014715 | 104 | Optimization terminated successfully. |
| Nelder-Mead | success | [-7.9919 6.9299 7.9717 7.4539] | 7.797738655998136 | 0.0012608749675564468 | 103 | Optimization terminated successfully. |
