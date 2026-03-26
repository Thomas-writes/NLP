# PALMER5C

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
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.1211 1.1355 0.84921 1.2032 1.0659 0.93993] | 2.13 | 0.000417 | 6 | Optimization terminated successfully. |
| CG | success | [0.91497 0.86722 0.95784 0.95465 1.1025 0.95453] | 2.13 | 0.000314 | 6 | Optimization terminated successfully. |
| CG | success | [1.052 1.0035 0.97973 0.87199 1.1346 1.1885] | 2.13 | 0.000463 | 6 | Optimization terminated successfully. |
| BFGS | success | [0.92817 1.0947 0.82802 0.9898 1.0685 1.0822] | 2.13 | 0.00044 | 11 | Optimization terminated successfully. |
| BFGS | success | [0.96849 1.1189 0.95703 1.1314 1.0794 1.061] | 2.13 | 0.000417 | 11 | Optimization terminated successfully. |
| BFGS | success | [1.1498 1.1384 0.95643 0.84224 1.2605 1.0404] | 2.13 | 0.000417 | 11 | Optimization terminated successfully. |
| dogleg | success | [0.89414 0.9814 1.129 1.114 1.0198 1.1192] | 2.13 | 0.00073 | 10 | Optimization terminated successfully. |
| dogleg | success | [0.97486 0.87028 1.112 0.95515 0.85128 0.87109] | 2.13 | 0.000451 | 10 | Optimization terminated successfully. |
| dogleg | success | [0.9225 1.0658 0.92814 1.0823 1.0769 1.1361] | 2.13 | 0.000446 | 10 | Optimization terminated successfully. |
| trust-ncg | fail | [1.0085 1.0014 0.84439 1.0661 1.1426 1.1324] | 2.82e+03 | 0.00022 | 6 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.1218 1.1922 1.0086 1.0792 1.0401 0.92086] | 2.79e+03 | 0.000202 | 6 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.95024 0.84565 0.95156 0.80606 1.102 1.2022] | 2.8e+03 | 0.000199 | 6 | A bad approximation caused failure to predict improvement. |
