# LOGROS

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
- **Objective Type:** other
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0 0.87201] | 5.684341886079186e-13 | 0.0013871660339646041 | 82 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0 1.221] | 1.4033219031260994e-13 | 0.001296832982916385 | 80 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0 0.9149] | 3.885780586187972e-14 | 0.001330958039034158 | 83 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | fail | [0 1.1213] | 0.6931471805599453 | 0.00010229198960587382 | 0 | Linear search failed |
| TNC | fail | [0 0.99799] | 0.6931471805599453 | 9.362504351884127e-05 | 0 | Linear search failed |
| TNC | fail | [0 0.99624] | 0.6931471805599453 | 8.762499783188105e-05 | 0 | Linear search failed |
| Powell | fail | [0 0.87546] | 0.00024211078682103432 | 0.007974584004841745 | 7 | Maximum number of function evaluations has been exceeded. |
| Powell | fail | [0 0.79769] | 0.0019590976563956205 | 0.007843125029467046 | 7 | Maximum number of function evaluations has been exceeded. |
| Powell | success | [0 0.97482] | 0.00016106382331061714 | 0.0016905419761314988 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [0 0.99983] | 0.6658171862314017 | 0.00034016702556982636 | 23 | Optimization terminated successfully. |
| Nelder-Mead | success | [0 0.90547] | 0.6658171862314017 | 0.0003444169997237623 | 23 | Optimization terminated successfully. |
| Nelder-Mead | success | [0 0.93243] | 0.6658171862314017 | 0.0003487500362098217 | 23 | Optimization terminated successfully. |
