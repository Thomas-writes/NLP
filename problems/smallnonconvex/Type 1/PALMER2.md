# PALMER2

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
| L-BFGS-B | success | [1.102 1.0612 0.93059 0.96273] | 3651.0975354891148 | 0.00048104103188961744 | 14 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.97268 0.94511 0.99508 0.97707] | 3651.097535493774 | 0.00031937495805323124 | 11 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.81463 1.1356 0.81674 0.95911] | 3651.0975354891825 | 0.0004581250250339508 | 17 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.1931 0.91631 0.89354 0.97063] | 14349.382940003325 | 0.0004261250142008066 | 1 | Linear search failed |
| TNC | fail | [1.1064 0.88164 0.94518 1.0989] | 14469.469185981343 | 0.000407207990065217 | 1 | Linear search failed |
| TNC | fail | [0.96182 0.97138 0.98622 1.1399] | 14671.228740721908 | 0.0004034999874420464 | 1 | Linear search failed |
| Powell | success | [0.9779 0.91298 0.82741 0.95128] | 4582.950904118699 | 0.0025771670043468475 | 2 | Optimization terminated successfully. |
| Powell | success | [0.83731 1.008 1.1626 0.95857] | 4582.8100635013525 | 0.006011041987221688 | 2 | Optimization terminated successfully. |
| Powell | success | [1.0063 0.92434 0.88448 0.93705] | 4582.870111101409 | 0.005138624983374029 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.1308 0.85202 0.93481 0.98766] | 3651.0975354891143 | 0.00535729102557525 | 435 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.97443 0.85861 0.96579 0.84109] | 3651.097535493492 | 0.0029438749770633876 | 241 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.1061 0.92723 1.0809 0.91689] | 3651.0975355667506 | 0.003284500038716942 | 265 | Optimization terminated successfully. |
