# HATFLDA

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
| L-BFGS-B | success | [0.14816 1e-07 0.21359 0.12518] | 2.5435157497713322e-12 | 0.0007667499594390392 | 36 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.13054 0.085794 0.17322 0.13369] | 9.835735430167519e-13 | 0.0004307079943828285 | 25 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.024093 0.13936 1e-07 1e-07] | 2.2387984364966057e-11 | 0.0007857079617679119 | 40 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | fail | [0.20851 0.033754 1e-07 0.0671] | 1.0000000998103034 | 0.00039183400804176927 | 1 | Linear search failed |
| TNC | success | [0.076742 0.073129 0.12877 0.30267] | 1.0000000998103034 | 9.362498531118035e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.032747 0.0091299 0.20123 0.12856] | 1.0000000998103034 | 9.354203939437866e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | fail | [1e-07 0.051311 0.02317 0.02053] | 2.2162526644976274e-08 | 0.01572370796930045 | 10 | Maximum number of function evaluations has been exceeded. |
| Powell | success | [1e-07 0.21183 0.19301 0.11333] | 2.5878610329549746e-12 | 0.014535207999870181 | 11 | Optimization terminated successfully. |
| Powell | fail | [0.070108 0.2425 0.076124 1e-07] | 2.819217096764603e-05 | 0.014910625002812594 | 8 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [0.18363 1e-07 0.2252 0.15141] | 0.18734203768019334 | 0.002064333006273955 | 175 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.091664 0.060797 0.14991 0.11129] | 0.18734203896789117 | 0.0010195419890806079 | 84 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.2263 1e-07 0.0097729 0.16737] | 0.18734203779809575 | 0.003187082998920232 | 268 | Optimization terminated successfully. |
