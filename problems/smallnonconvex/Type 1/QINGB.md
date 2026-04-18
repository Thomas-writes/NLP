# QINGB

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
- **# of Variables (n):** 5
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.0279 0.91171 0.87593 0.98384 0.98411] | 3.669343112483387e-12 | 0.00027458404656499624 | 10 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0831 0.93941 1.0267 0.88261 0.98546] | 3.914105230882346e-12 | 0.00022883398924022913 | 10 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.037 0.86504 1.18 1.1879 0.87215] | 8.861042426867598e-16 | 0.0002240000176243484 | 11 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [0.9282 1.1606 0.96961 0.90242 1.1785] | 1.0778191158210457e-10 | 0.00022262497805058956 | 7 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [0.97495 1.1048 1.002 0.84147 0.87265] | 9.748942777194663e-13 | 0.0002262920024804771 | 8 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [1.0462 1.0214 0.95103 1.0876 1.1107] | 1.2920156364057126e-12 | 0.0002424580161459744 | 8 | Converged (|f_n-f_(n-1)| ~= 0) |
| Powell | success | [0.70894 1.0515 1.1956 1.0868 1.1334] | 9.619364155561583e-10 | 0.0021597500308416784 | 4 | Optimization terminated successfully. |
| Powell | success | [0.92553 1.1823 1.0376 0.89762 1.0984] | 9.619370350616928e-10 | 0.002128334017470479 | 4 | Optimization terminated successfully. |
| Powell | success | [0.86071 1.0189 0.99343 1.1162 1.139] | 9.619364326002901e-10 | 0.002068416972178966 | 4 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.87194 0.88679 1.0236 0.82018 1.1073] | 3.0849142115309864e-08 | 0.0023049580049701035 | 178 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0124 0.96437 1.0088 0.94311 0.97276] | 5.6010932063755815e-08 | 0.0036163339973427355 | 321 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.99886 0.94943 1.0722 0.88993 1.1368] | 3.578493031603142e-08 | 0.0025284579605795443 | 217 | Optimization terminated successfully. |
