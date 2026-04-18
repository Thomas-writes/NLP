# WEEDS

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
| L-BFGS-B | success | [0.94042 1.0367 0.96532] | 2.587277395284234 | 0.0007524589891545475 | 35 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0407 1.0107 0.91004] | 2.5872773953039454 | 0.0005992079968564212 | 33 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0171 0.93572 0.95928] | 2.587277395284236 | 0.0009482920286245644 | 39 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | fail | [0.91408 0.96361 0.95273] | 24355.782551 | 0.00012883299496024847 | 0 | Linear search failed |
| TNC | fail | [0.89426 1.0669 1.0319] | 24355.782551 | 0.00014141702558845282 | 0 | Linear search failed |
| TNC | fail | [1.1038 1.2104 0.88987] | 24355.782551 | 9.183300426229835e-05 | 0 | Linear search failed |
| Powell | success | [0.85459 0.97768 1.2052] | 24355.78255099936 | 0.0018480829894542694 | 3 | Optimization terminated successfully. |
| Powell | success | [1.1746 1.0329 1.0167] | 24355.78255099981 | 0.0013431659899652004 | 2 | Optimization terminated successfully. |
| Powell | success | [0.82646 1.0845 0.8268] | 24355.461500297388 | 0.0008049579919315875 | 1 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.91685 1.1249 1.1274] | 9205.435198928952 | 0.0009187919786199927 | 68 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0739 1.1673 0.92652] | 9205.435198927695 | 0.000967165979091078 | 70 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0427 1.0218 0.97321] | 9205.435198928357 | 0.0009400840499438345 | 69 | Optimization terminated successfully. |
