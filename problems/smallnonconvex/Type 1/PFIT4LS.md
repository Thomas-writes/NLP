# PFIT4LS

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
| L-BFGS-B | success | [0.97435 -0.064029 1.1451] | 1.0707727062092116 | 0.022579999989829957 | 1474 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.73726 -0.029114 0.9226] | 1.225361198545225e-09 | 0.010533583001233637 | 705 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0797 -0.21761 0.96471] | 8.587433410098267e-10 | 0.00832708302186802 | 552 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.0626 0.20621 1.0396] | 113934.42809384977 | 8.870800957083702e-05 | 0 | Linear search failed |
| TNC | fail | [1.0939 -0.13239 0.97499] | 113934.42809384977 | 7.925002137199044e-05 | 1 | Unable to progress |
| TNC | fail | [0.95528 0.14214 1.0248] | 113934.42809384977 | 7.408397505059838e-05 | 0 | Linear search failed |
| Powell | success | [1.0496 -0.137 0.96435] | 11.591542925724085 | 0.012128917034715414 | 5 | Optimization terminated successfully. |
| Powell | success | [1.035 -0.018367 0.987] | 7709.803566518856 | 0.008296500018332154 | 4 | Optimization terminated successfully. |
| Powell | success | [1.1041 -0.015688 1.0601] | 3.6113464145662823e+102 | 0.002529499994125217 | 2 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.86535 0.072323 0.99978] | 73.88777102559294 | 0.00420812499942258 | 341 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.87498 0.0020149 0.97287] | 253.01063248604328 | 0.004214166023302823 | 342 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.94688 0.011202 0.86874] | 249.288490954847 | 0.0041701250011101365 | 343 | Maximum number of function evaluations has been exceeded. |
