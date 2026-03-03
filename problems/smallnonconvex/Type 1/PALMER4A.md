# PALMER4A

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
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.0317 0.84908 1.2584 0.80047 1.0308 0.9834] | 0.040606139450631996 | 0.0034121249918825924 | 128 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.93455 1.0312 1.1137 0.89784 1.0678 1.0651] | 0.0406061396262855 | 0.003538916993420571 | 89 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.86566 1.0173 0.81766 1.0014 0.93034 0.99948] | 0.04189165352052169 | 0.002593249999335967 | 57 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.011 1.0856 0.99134 1.1951 1.1634 0.90365] | 3901.9083787410054 | 0.0004769999941345304 | 1 | Linear search failed |
| TNC | fail | [1.1927 0.96057 0.7993 0.97203 1.1282 1.0695] | 5441.018934507382 | 0.0004530830046860501 | 1 | Linear search failed |
| TNC | fail | [0.85652 1.0834 1.0347 0.97006 0.99333 0.79857] | 4981.975598657492 | 0.00044041698856744915 | 1 | Linear search failed |
| Powell | success | [0.91224 1.0667 1.0454 1.0574 0.99895 1.0122] | 415.7572345771921 | 0.005225166998570785 | 7 | Optimization terminated successfully. |
| Powell | success | [1.0548 0.89396 0.91318 1.1926 0.98027 1.0422] | 122.96145532193638 | 0.01703645799716469 | 32 | Optimization terminated successfully. |
| Powell | success | [1.0879 1.0074 0.9461 1.091 0.86283 0.86364] | 411.15311103513505 | 0.005198166996706277 | 7 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.042 0.85711 1.0722 0.99929 1.1624 1.1176] | 0.27091950325309433 | 0.009239500010153279 | 788 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.041 1.0249 0.91058 1.0179 1.0647 1.0285] | 9.45828345851511 | 0.009024583006976172 | 777 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [1.0681 0.89482 0.95299 1.0669 0.89132 0.96003] | 0.258193983634682 | 0.006626041998970322 | 570 | Optimization terminated successfully. |
