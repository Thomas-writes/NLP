# PALMER7C

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
| CG | fail | [1.1457 1.1039 0.88252 0.95334 1.2175 1.0139 1.0312 1.1352] | 3.27 | 0.103 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.0746 0.93774 0.95776 1.1067 0.84755 1.0068 0.99053 0.97008] | 3.44 | 0.0844 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.97584 0.86996 1.0262 0.85891 0.96444 0.82681 0.86662 1.0221] | 4.02 | 0.0898 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [1.0075 0.93826 0.95213 1.0697 0.94279 1.1726 1.0033 0.88917] | 0.602 | 0.00157 | 50 | Optimization terminated successfully. |
| BFGS | success | [0.98554 1.136 1.187 0.91721 1.0154 1.1268 0.93604 0.94402] | 0.602 | 0.00153 | 49 | Optimization terminated successfully. |
| BFGS | success | [0.87155 1.0418 1.0235 1.0486 0.99547 0.8679 0.99722 1.1432] | 0.602 | 0.00167 | 50 | Optimization terminated successfully. |
| dogleg | success | [1.1959 0.94644 0.94961 0.95771 0.87509 1.062 1.0302 0.93552] | 0.602 | 0.00485 | 110 | Optimization terminated successfully. |
| dogleg | success | [0.85317 0.76233 1.0104 0.92723 1.0781 1.0109 1.0446 1.0612] | 0.602 | 0.00498 | 110 | Optimization terminated successfully. |
| dogleg | success | [1.1126 1.0381 1.2552 0.99639 0.8101 0.97754 1.1138 1.222] | 0.602 | 0.00484 | 110 | Optimization terminated successfully. |
| trust-ncg | fail | [0.91583 1.0595 1.0015 0.9728 1.1493 1.1819 0.99092 0.93578] | 372 | 0.000982 | 35 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.1787 1.1233 0.8705 0.95445 0.89507 1.026 0.95324 0.97742] | 363 | 0.000892 | 35 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.1524 0.94791 0.94623 1.0757 1.0847 0.86873 0.8473 0.75758] | 355 | 0.000842 | 34 | A bad approximation caused failure to predict improvement. |
