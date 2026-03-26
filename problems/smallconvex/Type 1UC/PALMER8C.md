# PALMER8C

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-25

## Classification
- **Convexity:** Convex
- **Objective Type:** quadratic
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [0.84373 0.97532 0.87355 1.0261 0.844 1.0219 1.1357 0.96172] | 0.504 | 0.0686 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.94134 1.1021 1.0137 0.90823 1.1345 0.96075 0.94997 0.98527] | 0.342 | 0.0656 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.94195 0.87894 1.0401 1.0613 0.95083 0.92188 1.0025 0.95964] | 0.415 | 0.0695 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [1.088 1.0057 0.97472 0.80594 1.0737 1.0165 0.83261 0.98948] | 0.16 | 0.00163 | 54 | Optimization terminated successfully. |
| BFGS | success | [0.896 1.0749 0.97611 1.0944 0.9354 1.0771 1.2178 1.022] | 0.16 | 0.00162 | 51 | Optimization terminated successfully. |
| BFGS | success | [0.97925 0.84631 1.03 1.1682 1.1361 1.0479 0.95829 0.95052] | 0.16 | 0.00173 | 51 | Optimization terminated successfully. |
| dogleg | success | [1.0726 0.94182 0.95538 0.98789 1.0423 1.0779 0.93492 0.6811] | 0.16 | 0.0019 | 42 | Optimization terminated successfully. |
| dogleg | success | [0.8444 0.91646 0.95068 1.0337 0.95419 0.97552 1.1295 1.0917] | 0.16 | 0.00201 | 42 | Optimization terminated successfully. |
| dogleg | success | [1.0113 0.96057 1.0193 0.87381 1.1027 1.1344 0.91807 1.1184] | 0.16 | 0.00193 | 42 | Optimization terminated successfully. |
| trust-ncg | fail | [1.0726 0.96186 1.0621 0.84128 1.0383 0.86126 1.0911 0.93465] | 452 | 0.000885 | 33 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.1154 0.95736 0.99661 0.95927 0.95991 1.1211 0.9899 1.0005] | 395 | 0.000883 | 34 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0853 0.9042 0.88733 1.1367 0.91065 0.82007 1.1214 0.99941] | 465 | 0.000881 | 34 | A bad approximation caused failure to predict improvement. |
