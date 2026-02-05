# TAME

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-02-05

## Classification
- **Convexity:** Convex
- **Degree:** Quadratic
- **# of Variables (n):** 2
- **# of Constraints (m):** 1
- **Bounds type: Type 1** 
## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [9.32961575e+19 7.52241958e+19] | 0.0 | 0.00022774998797103763 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [6.76180267e+19 1.05179751e+19] | 0.0 | 9.279098594561219e-05 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [4.53166678e+19 8.69489201e+19] | 0.0 | 0.00010516599286347628 | 2 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | fail | [2.40161953e+19 5.99502676e+19] | 67108864.0 | 0.00010316699626855552 | 1 | Linear search failed |
| TNC | fail | [3.79322724e+19 4.79532844e+19] | 67108864.0 | 9.270801092498004e-05 | 1 | Linear search failed |
| TNC | success | [9.24601567e+19 2.74784777e+19] | 0.0 | 9.291697642765939e-05 | 2 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [2.78423846e+19 7.99877512e+19] | 0.0 | 0.0006524159980472177 | 2 | Optimization terminated successfully. |
| Powell | success | [1.28418536e+19 5.91892868e+19] | 0.0 | 0.0010586249991320074 | 3 | Optimization terminated successfully. |
| Powell | success | [5.91549875e+19 6.04750435e+19] | 0.0 | 0.0005900409887544811 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [5.12253104e+19 5.00865489e+19] | 0.0 | 0.0016909580153878778 | 119 | Optimization terminated successfully. |
| Nelder-Mead | success | [4.04287538e+19 2.34796230e+19] | 0.0 | 0.0016818339936435223 | 122 | Optimization terminated successfully. |
| Nelder-Mead | success | [8.24712869e+19 6.16903256e+18] | 0.0 | 0.001964791998034343 | 129 | Optimization terminated successfully. |
