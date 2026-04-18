# PFIT2LS

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.1656 -0.12681 1.0862] | 8.401119716924893e-08 | 0.009109417034778744 | 585 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.81381 -0.092709 0.99335] | 1.2412532010500378e-09 | 0.005935374996624887 | 382 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.94309 -0.017129 0.84187] | 4817.742742378911 | 0.0001687080366536975 | 3 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.1908 -0.19904 0.96501] | 9421.432097714567 | 8.116598473861814e-05 | 1 | Unable to progress |
| TNC | fail | [0.89327 0.08983 0.86046] | 9421.432097714567 | 7.837498560547829e-05 | 0 | Linear search failed |
| TNC | fail | [0.98017 0.0096629 0.98307] | 9421.432097714567 | 7.208302849903703e-05 | 0 | Linear search failed |
| Powell | success | [0.86651 0.020593 0.90783] | 71.0238778550667 | 0.0030962080345489085 | 2 | Optimization terminated successfully. |
| Powell | success | [0.98786 0.12164 0.96182] | inf | 0.01019279204774648 | 5 | Optimization terminated successfully. |
| Powell | fail | [0.96843 -0.0049868 1.0575] | 38.43711683395054 | 0.012097416038159281 | 5 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.87656 0.040932 1.1063] | 3.3976465040003614 | 0.004042875021696091 | 339 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.0523 -0.096495 1.0835] | 1592.568469479892 | 0.00419000000692904 | 346 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.0324 0.078948 0.8496] | 4.671183017308702e-06 | 0.0041035410249605775 | 338 | Maximum number of function evaluations has been exceeded. |
