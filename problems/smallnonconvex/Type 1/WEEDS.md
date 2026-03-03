# WEEDS

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.0362 0.92861 1.0711] | 2.587277395287108 | 0.0007107080018613487 | 34 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.95948 0.87022 0.85724] | 2.587277395284345 | 0.0005327089893398806 | 32 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.2251 1.0724 1.0256] | 2.587277395284369 | 0.0005255420110188425 | 30 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.0154 1.0107 0.85807] | 24355.782551 | 0.00010654199286364019 | 0 | Linear search failed |
| TNC | fail | [1.1868 0.91681 0.99684] | 24355.782551 | 7.883300713729113e-05 | 0 | Linear search failed |
| TNC | fail | [0.96491 0.9691 1.0535] | 24355.782551 | 7.650000043213367e-05 | 0 | Linear search failed |
| Powell | success | [0.88753 0.9513 1.0162] | 24355.782550999807 | 0.0012910000077681616 | 2 | Optimization terminated successfully. |
| Powell | success | [0.99953 0.78259 0.97561] | 24355.782550999895 | 0.0012193750008009374 | 2 | Optimization terminated successfully. |
| Powell | success | [1.0462 1.0253 0.8649] | 23743.691466732533 | 0.0013698749971808866 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0625 0.90202 0.9716] | 9205.435198925428 | 0.00096674999804236 | 70 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0881 0.92547 1.0676] | 9205.435198924311 | 0.0009557080047670752 | 70 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.86509 1.1428 1.0299] | 9205.43519892481 | 0.0009720000089146197 | 71 | Optimization terminated successfully. |
