# PALMER4E

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.0307 1.0427 1.1351 0.90266 1.1189 0.99394 0.99038 0.81157] | 0.06907290856827064 | 0.000756290988647379 | 34 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.91561 0.94524 0.92159 0.97294 1.0023 0.96458 1.3139 0.97398] | 0.06381176650092589 | 0.0013944590027676895 | 78 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.145 1.041 0.99207 0.90185 0.99504 1.1173 1.1213 1.045] | 0.06341770634097826 | 0.0014604160096496344 | 87 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [0.96227 1.0103 0.8564 1.1288 0.97875 0.95512 1.0796 1.055] | 253.21670150555894 | 9.854200470726937e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.94821 0.84238 0.95773 1.0232 0.8683 0.85689 1.0128 0.86122] | 245.1446590610344 | 8.870899910107255e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [1.0312 0.93796 1.1615 1.0869 1.0071 0.98388 1.0773 1.0245] | 256.3390931249857 | 8.550001075491309e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [1.0673 1.0214 0.95055 1.011 1.0708 0.90097 1.0817 1.0811] | 1.5816288776566267 | 0.009267583009204827 | 9 | Optimization terminated successfully. |
| Powell | success | [0.95292 0.9374 1.0355 0.95774 0.79313 1.0458 1.1356 1.1845] | 1.4744507043053632 | 0.015128166996873915 | 20 | Optimization terminated successfully. |
| Powell | success | [1.039 1.1098 0.91543 0.83032 1.065 0.97388 1.1098 1.0492] | 1.47803565801629 | 0.012763708000420593 | 13 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0801 1.0445 1.0518 0.84334 1.0109 1.1914 1.0365 1.0208] | 76.3165209642864 | 0.01030916700256057 | 899 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.1018 1.0623 1.0132 0.96899 1.1585 0.9745 1.0856 0.9627] | 1.739988205355324 | 0.01234716598992236 | 1073 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.87829 0.97793 1.1689 0.97074 1.1958 0.9303 0.92679 1.0114] | 1.29071326285929 | 0.012396250007441267 | 1105 | Maximum number of function evaluations has been exceeded. |
