# SIM2BQP

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
| CG | success | [0.11526396] | -0.125 | 0.0001272080116905272 | 1 | Optimization terminated successfully. |
| CG | success | [0.31383131] | -0.125 | 9.549999958835542e-05 | 1 | Optimization terminated successfully. |
| CG | success | [0.02182235] | -0.125 | 8.13750084489584e-05 | 1 | Optimization terminated successfully. |
| BFGS | success | [0.38008577] | -0.125 | 0.0001087500131689012 | 2 | Optimization terminated successfully. |
| BFGS | success | [0.27531619] | -0.125 | 7.845801883377135e-05 | 1 | Optimization terminated successfully. |
| BFGS | success | [0.23133885] | -0.125 | 7.554201874881983e-05 | 1 | Optimization terminated successfully. |
| dogleg | success | [0.3617081] | -0.125 | 0.00012500002048909664 | 1 | Optimization terminated successfully. |
| dogleg | success | [0.01653531] | -0.125 | 8.212501415982842e-05 | 1 | Optimization terminated successfully. |
| dogleg | success | [0.35978467] | -0.125 | 7.554100011475384e-05 | 1 | Optimization terminated successfully. |
| trust-ncg | fail | [0.12964364] | -0.11598346423939601 | 0.0001974170154426247 | 4 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.3588] | -0.1207126206893636 | 0.0001830830005928874 | 5 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.13482107] | -0.1145393244922421 | 0.00014483300037682056 | 4 | A bad approximation caused failure to predict improvement. |
