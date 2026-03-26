# ELATVIDU

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
- **Objective Type:** sum of squares
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.47508 4.8107] | 54.8 | 0.000621 | 11 | Optimization terminated successfully. |
| CG | success | [1.072 4.5957] | 1.71 | 0.000428 | 8 | Optimization terminated successfully. |
| CG | success | [0.63841 5.506] | 54.8 | 0.000413 | 9 | Optimization terminated successfully. |
| BFGS | success | [0.43698 5.1905] | 54.8 | 0.000746 | 20 | Optimization terminated successfully. |
| BFGS | success | [-0.15516 4.4054] | 54.8 | 0.000634 | 20 | Optimization terminated successfully. |
| BFGS | success | [1.4728 5.7881] | 54.8 | 0.000811 | 21 | Optimization terminated successfully. |
| dogleg | success | [0.93608 6.0407] | 54.8 | 0.000492 | 12 | Optimization terminated successfully. |
| dogleg | success | [1.417 5.1161] | 54.8 | 0.000412 | 11 | Optimization terminated successfully. |
| dogleg | success | [0.44249 5.1668] | 54.8 | 0.000407 | 11 | Optimization terminated successfully. |
| trust-ncg | fail | [1.7391 4.6585] | 55.4 | 0.00107 | 41 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.88783 4.2668] | 55.7 | 0.00393 | 141 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.87091 5.6144] | 56 | 0.00553 | 188 | A bad approximation caused failure to predict improvement. |
