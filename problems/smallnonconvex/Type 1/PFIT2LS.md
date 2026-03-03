# PFIT2LS

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
| L-BFGS-B | success | [0.92831 0.021947 1.0105] | 7.84193850225993e-09 | 0.00493895799445454 | 301 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.90735 -0.1435 1.0855] | 2.381085607605925e-09 | 0.00497712500509806 | 321 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0465 0.18675 0.95545] | 5.1872747081771455e-06 | 0.00045729200064670295 | 20 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.99166 -0.062291 0.89162] | 9421.432097714567 | 7.991699385456741e-05 | 1 | Unable to progress |
| TNC | fail | [1.0489 0.23052 1.0374] | 9421.432097714567 | 7.404200732707977e-05 | 0 | Linear search failed |
| TNC | fail | [0.89715 -0.25258 0.8728] | 9421.432097714567 | 6.887500057928264e-05 | 1 | Unable to progress |
| Powell | fail | [1.0623 -0.14261 0.88889] | 20.66489982828771 | 0.012039291992550716 | 4 | Maximum number of function evaluations has been exceeded. |
| Powell | success | [1.0308 0.090536 0.86329] | inf | 0.004516083994531073 | 3 | Optimization terminated successfully. |
| Powell | fail | [0.93424 -0.053976 0.93465] | 226.11535644832236 | 0.012115332996472716 | 4 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.0044 0.090266 0.93171] | 0.0010153450318283795 | 0.004413375005242415 | 341 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.91302 -0.037333 0.94495] | 1593.5428544480487 | 0.00406791600107681 | 339 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.95018 0.046462 0.97046] | 2.963125993781336 | 0.00430120799865108 | 338 | Maximum number of function evaluations has been exceeded. |
