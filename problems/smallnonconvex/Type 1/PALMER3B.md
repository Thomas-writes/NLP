# PALMER3B

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
| L-BFGS-B | success | [1.0979 1.1083 1.1069 1.0462] | 4.227647252563337 | 0.0006687499699182808 | 33 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.146 0.73778 1.0308 1.075] | 4.227647252562908 | 0.0004898330080322921 | 24 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [1.0403 0.99471 0.86319 0.9952] | 4.227647252568668 | 0.0004614590434357524 | 22 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.81927 0.9195 0.95042 0.99596] | 11453.694478512634 | 0.0004226660239510238 | 1 | Linear search failed |
| TNC | fail | [1.0123 0.99799 0.92149 1.0915] | 10961.345687507222 | 0.0004085840191692114 | 1 | Linear search failed |
| TNC | fail | [1.1561 0.928 0.97775 0.98453] | 10997.956379883652 | 0.000408249965403229 | 1 | Linear search failed |
| Powell | success | [0.99218 1.0433 1.1818 0.89379] | 281.5401276479191 | 0.005366625031456351 | 10 | Optimization terminated successfully. |
| Powell | success | [0.91371 0.91387 0.96168 0.95018] | 478.654369867104 | 0.006368250004015863 | 12 | Optimization terminated successfully. |
| Powell | success | [0.95484 1.0649 0.93228 0.83001] | 40.35592866967574 | 0.006327665993012488 | 14 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.99079 0.90175 0.91993 0.96041] | 356.90603176194804 | 0.001894167042337358 | 154 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.0692 0.98964 0.86618 1.0057] | 356.82454636115904 | 0.005822792008984834 | 489 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [1.0437 0.97436 1.0391 0.92257] | 4.2276472574755415 | 0.0037026249920018017 | 302 | Optimization terminated successfully. |
