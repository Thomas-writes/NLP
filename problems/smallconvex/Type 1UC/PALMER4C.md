# PALMER4C

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
| CG | fail | [1.1217 1.0561 1.0973 1.1109 1.0474 1.0227 1.0014 0.97139] | 0.604 | 0.0902 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.0111 0.99453 0.9794 1.0905 1.0483 1.0266 0.92023 1.1195] | 0.133 | 0.087 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.0617 1.1847 1.0449 0.89271 1.0531 0.93298 0.87732 1.1965] | 0.36 | 0.09 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [0.85645 1.0554 1.0364 0.89932 1.0549 0.84221 1.054 1.042] | 0.0503 | 0.00155 | 49 | Optimization terminated successfully. |
| BFGS | success | [1.1631 0.9727 1.0891 0.9789 1.0238 1.1895 1.2158 0.99916] | 0.0503 | 0.00148 | 48 | Optimization terminated successfully. |
| BFGS | success | [0.98225 1.0152 0.99105 1.0152 0.97116 0.68422 0.92914 0.90315] | 0.0503 | 0.00154 | 49 | Optimization terminated successfully. |
| dogleg | success | [0.96626 0.9697 0.97038 1.0472 1.0362 0.97542 0.98212 1.0407] | 0.0503 | 0.000977 | 19 | Optimization terminated successfully. |
| dogleg | success | [0.84276 1.1719 1.0041 0.98946 0.96736 0.91197 1.0915 0.9385] | 0.0503 | 0.000909 | 19 | Optimization terminated successfully. |
| dogleg | success | [0.84864 0.99116 1.0439 0.84623 1.1318 0.82398 0.94554 0.96347] | 0.0503 | 0.000919 | 19 | Optimization terminated successfully. |
| trust-ncg | fail | [0.96323 0.99648 0.96909 1.2072 1.0899 0.8877 0.88657 0.98507] | 2.39e+03 | 0.00028 | 6 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0874 1.1413 0.93942 1.01 1.0385 1.0655 0.7726 0.94726] | 1.81e+03 | 0.000237 | 5 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0145 1.0139 0.99553 1.0229 0.87451 1.0347 1.1496 1.0624] | 2e+03 | 0.00103 | 35 | A bad approximation caused failure to predict improvement. |
