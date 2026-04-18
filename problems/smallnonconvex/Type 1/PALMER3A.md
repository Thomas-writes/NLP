# PALMER3A

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
| L-BFGS-B | success | [1.071 1.1013 0.94319 1.0263 0.95609 0.9465] | 0.02043142309452698 | 0.002026124973781407 | 119 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0428 1.0308 1.1065 1.0185 1.2043 1.0148] | 0.02448967701706997 | 0.0009552499977871776 | 55 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.87272 1.0242 0.90925 0.98643 0.96367 1.0233] | 0.020502561291083517 | 0.0009162090136669576 | 53 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.79701 1.0406 0.95016 0.86083 1.0201 1.0074] | 5022.190402706074 | 0.0004452909925021231 | 1 | Linear search failed |
| TNC | fail | [1.0235 0.93607 0.88286 0.97137 0.9386 0.92471] | 4588.914334201332 | 0.00042679201578721404 | 1 | Linear search failed |
| TNC | fail | [0.95601 0.99049 0.96135 0.93538 1.0732 0.82568] | 4596.68127473186 | 0.00042441702680662274 | 1 | Linear search failed |
| Powell | success | [0.8578 1.0621 1.0608 1.0587 0.98741 1.1452] | 194.3131081296573 | 0.01298362499801442 | 24 | Optimization terminated successfully. |
| Powell | success | [1.1253 0.86546 0.82381 0.77479 1.0409 0.99163] | 5.518164591285743 | 0.009455957973841578 | 12 | Optimization terminated successfully. |
| Powell | success | [1.0404 1.1245 0.85357 0.88977 0.95736 1.0137] | 127.02415453792746 | 0.017544667003676295 | 26 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.2203 0.93825 1.0505 0.9402 1.0257 0.81775] | 0.03572778838591418 | 0.009101084026042372 | 779 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.2266 0.8447 1.1066 0.95751 0.99814 1.1246] | 6.909081850089735 | 0.008950332994572818 | 780 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [1.125 1.1997 0.74638 1.0258 1.0922 1.0711] | 0.07233551452815933 | 0.006933833006769419 | 598 | Optimization terminated successfully. |
