# PALMER4E

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.0529 0.97128 0.9429 1.0806 0.97066 0.88273 0.8955 1.0323] | 0.06439667128014491 | 0.0012760829995386302 | 72 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.9795 1.2402 1.1115 0.88386 1.1032 1.0156 0.91919 0.72105] | 0.06471694284514538 | 0.0013702500145882368 | 79 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.1161 1.0509 0.99495 1.0781 0.88681 1.0093 0.98808 0.95734] | 0.06425191094943784 | 0.0011801249929703772 | 62 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [1.1237 0.94524 1.1589 0.75565 0.90677 0.84164 1.035 1.1207] | 256.2828768179356 | 0.00016558298375457525 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.97568 0.88004 0.90767 0.85037 1.1024 1.1653 0.95631 0.92729] | 261.8998497082591 | 0.00012291601160541177 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.95585 0.88298 1.0613 1.0781 0.89314 0.90001 1.0517 0.9055] | 248.301785451104 | 9.887502528727055e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [0.87266 1.0561 0.95302 0.99245 1.0832 0.89131 0.96923 0.94207] | 1.7877484350167714 | 0.009825916029512882 | 16 | Optimization terminated successfully. |
| Powell | success | [0.80346 1.1168 0.90894 1.0437 1.1551 1.0753 1.1385 1.0037] | 1.5058015915722687 | 0.012517958006355911 | 13 | Optimization terminated successfully. |
| Powell | success | [0.88718 0.84086 0.99691 1.1587 1.0393 0.85075 1.0413 1.0686] | 2.1354581027069304 | 0.009521375002805144 | 16 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.1414 1.0071 1.1244 1.1315 0.82341 0.95 1.0924 1.0249] | 5.660222157313886 | 0.012192416994366795 | 1082 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.94775 0.94566 0.98598 1.018 1.0602 0.8318 0.99251 0.96841] | 23.813000332632637 | 0.012254500004928559 | 1103 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.0966 0.95934 0.92638 0.75562 0.68988 1.0871 0.92592 1.0499] | 1.79947781944469 | 0.012009916012175381 | 1063 | Maximum number of function evaluations has been exceeded. |
