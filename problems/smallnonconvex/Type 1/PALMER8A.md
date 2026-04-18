# PALMER8A

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
| L-BFGS-B | success | [0.95563 0.96693 0.91336 0.97109 1.0443 1.0179] | 0.07400969816396509 | 0.0013445419608615339 | 79 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0504 0.96879 1.0963 0.98096 0.96436 0.91206] | 0.07400969798461256 | 0.0015313330222852528 | 95 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0193 0.93156 1.2527 1.0669 0.85045 0.81956] | 0.07400969896822068 | 0.001764083979651332 | 116 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.9754 1.0446 1.1075 1.0339 0.98421 1.0514] | 9902.936350701208 | 0.0005072079948149621 | 1 | Linear search failed |
| TNC | fail | [0.93784 1.0947 0.99598 1.0403 1.0509 1.0859] | 10043.077784589808 | 0.0004244580049999058 | 1 | Linear search failed |
| TNC | fail | [0.91572 0.92304 0.96487 1.183 1.022 0.86757] | 9696.592960404967 | 0.00041499995859339833 | 1 | Linear search failed |
| Powell | fail | [0.96246 1.0425 1.1732 1.0256 0.85531 0.97314] | 15.520375252182433 | 0.02575045800767839 | 29 | Maximum number of function evaluations has been exceeded. |
| Powell | success | [1.2295 1.1774 1.0565 1.1134 1.0504 0.89339] | 37.1233072184407 | 0.011247457994613796 | 16 | Optimization terminated successfully. |
| Powell | success | [1.1806 1.0168 0.98245 1.0243 1.0494 1.1319] | 90.1822143873486 | 0.009225166984833777 | 12 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.80123 0.95457 0.90183 1.0435 0.84797 1.0109] | 4.641766353187406 | 0.005135208019055426 | 448 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.1149 0.88873 0.98926 0.98406 1.0186 1.1745] | 4.6417663527600945 | 0.005388166988268495 | 434 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.94444 1.002 1.0036 0.80211 1.0957 1.1229] | 4.6417663529436135 | 0.005091583007015288 | 438 | Optimization terminated successfully. |
