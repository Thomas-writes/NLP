# LEVYMONT5

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [-7.5111 8.2278] | 7.7738110793971975 | 0.00034141598735004663 | 7 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [-8.1038 9.0491] | 3.1097508070618365 | 0.000208500016015023 | 8 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [-9.0245 6.3539] | 47.31308605001706 | 0.0001582079567015171 | 6 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | fail | [-6.718 8.2952] | 12.487063715454875 | 0.0001729580108076334 | 6 | Linear search failed |
| TNC | success | [-7.7359 6.8708] | 3.1097508070611752 | 0.00013958301860839128 | 6 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | fail | [-8.1311 8.536] | 12.487063715454875 | 0.00018400000408291817 | 7 | Linear search failed |
| Powell | success | [-6.7607 6.7445] | 3.1097524649339623 | 0.00032962497789412737 | 2 | Optimization terminated successfully. |
| Powell | success | [-7.2892 8.6382] | 3.109750807062488 | 0.0004878750187344849 | 3 | Optimization terminated successfully. |
| Powell | success | [-6.6948 8.2154] | 3.1097508070624045 | 0.00048474996583536267 | 3 | Optimization terminated successfully. |
| Nelder-Mead | success | [-8.9777 7.0895] | 12.48706372847823 | 0.00048691697884351015 | 34 | Optimization terminated successfully. |
| Nelder-Mead | success | [-7.1574 6.6996] | 7.773811080408647 | 0.0005796659970656037 | 42 | Optimization terminated successfully. |
| Nelder-Mead | success | [-6.8118 7.9451] | 12.487063729003752 | 0.0004719580174423754 | 34 | Optimization terminated successfully. |
