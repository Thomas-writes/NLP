# PALMER5D

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.1403 0.94457 0.93936 1.0072] | 87.3 | 0.0016 | 34 | Optimization terminated successfully. |
| CG | success | [1.1326 1.0207 1.0173 1.0257] | 87.3 | 0.000497 | 10 | Optimization terminated successfully. |
| CG | success | [0.96575 1.1966 0.97314 0.95543] | 87.3 | 0.00098 | 22 | Optimization terminated successfully. |
| BFGS | success | [1.0009 0.86533 1.0599 0.8744] | 87.3 | 0.000393 | 11 | Optimization terminated successfully. |
| BFGS | success | [1.0316 0.98742 1.1152 0.70962] | 87.3 | 0.000369 | 11 | Optimization terminated successfully. |
| BFGS | success | [1.0746 0.89434 1.0126 1.0244] | 87.3 | 0.000361 | 11 | Optimization terminated successfully. |
| dogleg | success | [0.97171 1.0324 1.0417 0.96289] | 87.3 | 0.000925 | 20 | Optimization terminated successfully. |
| dogleg | success | [0.92364 0.86039 0.94955 0.92238] | 87.3 | 0.000884 | 20 | Optimization terminated successfully. |
| dogleg | success | [1.1157 0.95878 0.94736 0.94208] | 87.3 | 0.000852 | 20 | Optimization terminated successfully. |
| trust-ncg | fail | [0.87131 1.0547 1.0181 0.9708] | 1.79e+04 | 0.000245 | 6 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0788 0.85313 1.1147 1.0153] | 1.78e+04 | 0.000216 | 6 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0476 1.138 1.1215 0.94998] | 1.79e+04 | 0.000207 | 6 | A bad approximation caused failure to predict improvement. |
