# LSC2LS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [116.05 39.298 267.21] | 13.3 | 0.00546 | 112 | Optimization terminated successfully. |
| CG | success | [123.6 39.524 243.35] | 13.4 | 0.0162 | 311 | Optimization terminated successfully. |
| CG | fail | [130.79 52.697 241.07] | 13.3 | 0.00197 | 43 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [132.4 29.828 272.36] | 13.4 | 0.00177 | 55 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [118.76 31.611 271.47] | 13.4 | 0.00175 | 53 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [110.44 -14.223 273.66] | 13.5 | 0.00228 | 64 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [62.793 15.83 249.37] | 2.74e+05 | 6.93e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [62.69 25.129 269.86] | 3.29e+05 | 5.28e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [117.52 81.102 235.58] | 9.73e+04 | 5.06e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [105.68 -14.056 292.38] | 596 | 0.000505 | 17 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [71.932 37.505 321.76] | 126 | 0.000357 | 11 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [118.07 59.072 237.18] | 107 | 0.000362 | 12 | A bad approximation caused failure to predict improvement. |
