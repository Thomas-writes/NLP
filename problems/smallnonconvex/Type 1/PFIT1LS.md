# PFIT1LS

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
| L-BFGS-B | success | [1.0715 0.023403 1.015] | 1.7673833531057464e-05 | 0.0005322079960023984 | 25 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0123 0.05593 1.1147] | 4.702419795085004e-05 | 0.0004378750018076971 | 21 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.055 0.0214 0.97501] | 2.399400225285546e-05 | 0.0006077910074964166 | 35 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.029 -0.13886 1.0771] | 946.567900934321 | 9.779199899639934e-05 | 1 | Unable to progress |
| TNC | fail | [0.94489 -0.035824 1.0367] | 946.567900934321 | 0.00014995899982750416 | 1 | Unable to progress |
| TNC | fail | [0.94266 -0.042344 0.89201] | 946.567900934321 | 8.704200445208699e-05 | 1 | Unable to progress |
| Powell | success | [0.89694 0.046071 1.1925] | inf | 0.00439170899335295 | 3 | Optimization terminated successfully. |
| Powell | fail | [1.0171 -0.13643 0.97624] | 4.088075343565842 | 0.01190995798970107 | 4 | Maximum number of function evaluations has been exceeded. |
| Powell | success | [0.95833 -0.023243 1.1416] | 9.382679875424625 | 0.010931500000879169 | 5 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.0998 -0.00028876 0.87513] | 148.27302111041988 | 0.004088166999281384 | 343 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.0845 -0.037503 1.0605] | 92.29225511773127 | 0.0043015000119339675 | 340 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.99838 0.025161 0.99343] | 2.628401794190335 | 0.004078833007952198 | 340 | Maximum number of function evaluations has been exceeded. |
