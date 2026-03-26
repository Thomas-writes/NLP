# DJTL

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-25

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** other
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [15.272 6.7287] | -5.26e+03 | 0.00353 | 13 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [13.303 4.8755] | -8.95e+03 | 0.00771 | 48 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [16.75 6.6427] | -8.95e+03 | 0.0114 | 55 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [13.162 5.6046] | -6.55e+03 | 0.0271 | 197 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [15.74 6.2035] | -4.78e+03 | 0.0481 | 241 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [16.665 8.1288] | -2.61e+03 | 0.0108 | 88 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [14.33 3.2477] | 9.77e+11 | 6.01e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [14.205 5.1077] | 2.33e+12 | 5.45e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [14.887 6.2851] | -2.48e+03 | 5.14e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [15.604 5.8657] | 1.48e+11 | 0.000797 | 30 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [14.992 7.2206] | 8.81e+10 | 0.000709 | 31 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [14.153 8.3245] | 2.68e+11 | 5.88e-05 | 0 | A bad approximation caused failure to predict improvement. |
