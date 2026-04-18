# PALMER1

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
| L-BFGS-B | success | [0.89292 1.0609 1.1238 1.0619] | 11754.602545362091 | 0.000448125007096678 | 13 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0041 1.0315 1.276 1.1418] | 11754.602545363057 | 0.0003494999837130308 | 11 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0022 0.95729 0.99982 0.91065] | 11754.60254536212 | 0.0003475829726085067 | 12 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.1886 1.0767 0.88911 0.9772] | 63213.67075807292 | 0.00044370803516358137 | 1 | Linear search failed |
| TNC | fail | [0.89952 0.89881 0.91465 1.0478] | 64017.24903933354 | 0.0004258750122971833 | 1 | Linear search failed |
| TNC | fail | [1.0673 1.0079 1.1419 1.1188] | 63548.775247185025 | 0.00041791703552007675 | 1 | Linear search failed |
| Powell | success | [1.0059 1.1176 0.96888 1.0179] | 38662.00565253505 | 0.003192083036992699 | 5 | Optimization terminated successfully. |
| Powell | success | [0.95529 1.1352 0.90589 0.99015] | 38655.64250155215 | 0.003312167013064027 | 5 | Optimization terminated successfully. |
| Powell | success | [1.0154 0.99338 1.1101 1.0901] | 38683.77879147344 | 0.0032569169998168945 | 5 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.94146 0.98917 1.0847 0.96335] | 11754.602545363115 | 0.0035533749614842236 | 290 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.108 1.0912 1.066 1.0735] | 11754.602545365724 | 0.004148916981648654 | 328 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0975 1.0002 0.94505 0.98648] | 11754.602545362699 | 0.0047391250263899565 | 386 | Optimization terminated successfully. |
