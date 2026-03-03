# PALMER3B

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
| L-BFGS-B | success | [0.89742 0.99728 0.92412 0.9606] | 4.227647252567207 | 0.000642833998426795 | 28 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.95395 0.93148 0.87377 1.062] | 4.22764725256421 | 0.0006260829977691174 | 27 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.95955 0.82815 1.0647 0.94287] | 4.227647253663495 | 0.00035200000274926424 | 14 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.99005 1.1377 0.90638 1.0129] | 10559.316675197531 | 0.0004328340000938624 | 1 | Linear search failed |
| TNC | fail | [0.98109 0.84927 1.0482 1.0843] | 11468.476343533986 | 0.0004320410080254078 | 1 | Linear search failed |
| TNC | fail | [0.89279 1.1355 1.0059 0.89047] | 10686.306666882729 | 0.0004248750046826899 | 1 | Linear search failed |
| Powell | success | [1.0458 0.8863 0.96316 0.88673] | 336.16477901511695 | 0.005085458004032262 | 11 | Optimization terminated successfully. |
| Powell | success | [1.0126 0.92926 1.0159 1.0984] | 745.7016585932982 | 0.00481487499200739 | 7 | Optimization terminated successfully. |
| Powell | success | [1.1366 1.1118 0.95833 1.006] | 1192.838788886905 | 0.007153457991080359 | 14 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0882 1.0458 0.99659 1.3494] | 338.10836937764867 | 0.0029347909876378253 | 232 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.95893 1.0598 0.90326 1.0251] | 343.59798385970595 | 0.00591787499433849 | 498 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [1.0316 1.0666 0.91122 0.9376] | 678.3225446107215 | 0.0031673750054324046 | 256 | Optimization terminated successfully. |
