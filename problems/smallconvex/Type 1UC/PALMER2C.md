# PALMER2C

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
| CG | fail | [0.78484 0.97196 1.0759 1.1393 0.8504 0.96108 1.051 1.049] | 0.085 | 0.0806 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.95379 0.83586 0.90546 1.0682 0.83992 1.1521 0.90444 0.92469] | 0.139 | 0.0816 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.96365 0.97971 0.99705 0.85698 0.8084 1.0535 0.89148 0.99933] | 0.132 | 0.0834 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [0.8497 0.92191 0.8136 1.028 1.0905 0.98789 0.93868 1.0926] | 0.0144 | 0.00161 | 50 | Optimization terminated successfully. |
| BFGS | success | [1.0239 1.0257 1.191 0.81592 0.94583 1.0332 0.93527 0.94895] | 0.0144 | 0.00162 | 51 | Optimization terminated successfully. |
| BFGS | success | [1.1597 1.1126 1.0924 1.1208 1.0224 1.0157 1.1583 0.97273] | 0.0144 | 0.00151 | 49 | Optimization terminated successfully. |
| dogleg | success | [1.0661 0.85729 0.95824 0.90983 0.95097 1.1402 0.8869 1.2222] | 0.0144 | 0.000782 | 15 | Optimization terminated successfully. |
| dogleg | success | [0.94443 1.0458 0.78682 1.1287 1.2697 0.90489 0.92076 0.9022] | 0.0144 | 0.000755 | 15 | Optimization terminated successfully. |
| dogleg | success | [0.84232 1.0562 1.0967 0.9856 1.2537 0.90719 1.073 1.094] | 0.0144 | 0.000751 | 15 | Optimization terminated successfully. |
| trust-ncg | fail | [0.8788 1.0862 0.97024 0.87408 0.94429 1.174 0.84167 1.2631] | 8.47e+03 | 0.00105 | 34 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.84897 1.0987 0.93804 1.2017 0.88969 0.86393 0.96232 0.98672] | 8.87e+03 | 0.000282 | 8 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.90071 1.2246 0.97496 1.0023 1.1351 1.1182 0.85823 0.94788] | 1.14e+04 | 0.000207 | 5 | A bad approximation caused failure to predict improvement. |
