# BQP1VAR

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-02-05

## Classification
- **Convexity:** Convex
- **Degree:** Quadratic
- **# of Variables (n):** 1
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 
## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.28589406] | -0.25 | 0.00018404200091026723 | 1 | Optimization terminated successfully. |
| CG | success | [0.29227435] | -0.25 | 0.00012216600589454174 | 1 | Optimization terminated successfully. |
| CG | success | [0.33410751] | -0.25 | 0.00010933401063084602 | 1 | Optimization terminated successfully. |
| BFGS | success | [0.05959445] | -0.25 | 0.00016041702474467456 | 3 | Optimization terminated successfully. |
| BFGS | success | [0.46450091] | -0.25 | 9.72909911070019e-05 | 2 | Optimization terminated successfully. |
| BFGS | success | [0.19708066] | -0.25 | 8.895801147446036e-05 | 2 | Optimization terminated successfully. |
| dogleg | success | [0.20608066] | -0.25 | 0.00010854197898879647 | 1 | Optimization terminated successfully. |
| dogleg | success | [0.47193455] | -0.25 | 8.283299393951893e-05 | 1 | Optimization terminated successfully. |
| dogleg | success | [0.18778766] | -0.25 | 7.654100772924721e-05 | 1 | Optimization terminated successfully. |
| trust-ncg | fail | [0.17257799] | -0.24679772168449166 | 0.0007690410129725933 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.39963108] | -0.248565945205946 | 0.0006585419760085642 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.24970025] | -0.24999991014876122 | 0.0007862089842092246 | 29 | A bad approximation caused failure to predict improvement. |
