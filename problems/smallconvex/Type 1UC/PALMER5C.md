# PALMER5C

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-03

## Classification
- **Convexity:** Convex
- **Objective Type:** quadratic
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.91491 1.0303 1.0206 1.1901 1.1258 0.90888] | 2.13 | 0.000411 | 6 | Optimization terminated successfully. |
| CG | success | [0.96932 0.89869 1.0725 0.95837 1.2284 1.0156] | 2.13 | 0.000421 | 6 | Optimization terminated successfully. |
| CG | success | [0.90179 0.89499 1.0975 1.0762 1.0864 0.94573] | 2.13 | 0.000331 | 6 | Optimization terminated successfully. |
| BFGS | success | [1.0451 1.0782 0.8683 0.79999 0.90261 0.98584] | 2.13 | 0.000426 | 10 | Optimization terminated successfully. |
| BFGS | success | [0.87131 1.0772 0.9504 0.86351 0.91277 1.0717] | 2.13 | 0.000423 | 11 | Optimization terminated successfully. |
| BFGS | success | [0.83875 0.98338 0.88965 0.99029 1.2014 1.0979] | 2.13 | 0.000417 | 11 | Optimization terminated successfully. |
| dogleg | success | [0.90945 1.0441 0.93564 1.0683 1.13 1.0162] | 2.13 | 0.000302 | 6 | Optimization terminated successfully. |
| dogleg | success | [0.81892 1.0468 0.99376 1.141 0.98947 1.0057] | 2.13 | 0.000292 | 6 | Optimization terminated successfully. |
| dogleg | success | [1.0054 1.0338 0.93958 1.0186 0.95032 0.96915] | 2.13 | 0.000283 | 6 | Optimization terminated successfully. |
| trust-ncg | fail | [1.0312 0.94251 0.98745 0.68279 0.92683 1.1142] | 387 | 0.000986 | 37 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.90825 1.0831 0.97133 1.0443 1.1916 0.98508] | 385 | 0.000977 | 37 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.98335 0.93347 0.9374 1.1071 1.1308 1.0141] | 388 | 0.00111 | 37 | A bad approximation caused failure to predict improvement. |
