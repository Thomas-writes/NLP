# GAUSSIAN

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.3795 0.90937 -0.043336] | 1.14e-08 | 0.000457 | 9 | Optimization terminated successfully. |
| CG | success | [0.37574 1.0989 -0.065963] | 1.13e-08 | 0.000517 | 13 | Optimization terminated successfully. |
| CG | success | [0.32089 1.0148 -0.012711] | 1.13e-08 | 0.000329 | 7 | Optimization terminated successfully. |
| BFGS | success | [0.52707 0.97741 0.015237] | 1.13e-08 | 0.000283 | 7 | Optimization terminated successfully. |
| BFGS | success | [0.42809 1.1176 0.0079333] | 1.13e-08 | 0.000298 | 8 | Optimization terminated successfully. |
| BFGS | success | [0.45061 1.0723 0.17733] | 1.13e-08 | 0.000294 | 8 | Optimization terminated successfully. |
| dogleg | success | [0.38657 1.1704 -0.054777] | 1.13e-08 | 0.000219 | 4 | Optimization terminated successfully. |
| dogleg | success | [0.46887 0.92708 -0.01575] | 1.13e-08 | 0.000191 | 4 | Optimization terminated successfully. |
| dogleg | success | [0.49695 0.92169 0.021387] | 1.13e-08 | 0.000188 | 4 | Optimization terminated successfully. |
| trust-ncg | fail | [0.42949 0.95646 -0.0078292] | 0.0046 | 0.000901 | 32 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.31511 1.1349 -0.011151] | 0.032 | 0.000796 | 31 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.44327 1.0092 0.13979] | 0.0128 | 0.000816 | 32 | A bad approximation caused failure to predict improvement. |
