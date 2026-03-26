# POWERSUM

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
- **Objective Type:** sum of squares
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [2.0715 1.6119 2.1109 2.1192] | 7.14e-06 | 0.0452 | 800 | Maximum number of iterations has been exceeded. |
| CG | fail | [2.1708 2.1995 2.1557 2.2469] | 7.27e-06 | 0.0368 | 800 | Maximum number of iterations has been exceeded. |
| CG | success | [2.1126 2.2292 2.1609 1.9303] | 2.83e-07 | 0.0319 | 720 | Optimization terminated successfully. |
| BFGS | success | [2.0681 1.806 1.542 1.9217] | 6.48e-12 | 0.0166 | 447 | Optimization terminated successfully. |
| BFGS | success | [1.8949 1.7987 1.9829 1.9997] | 2.87e-12 | 0.0276 | 626 | Optimization terminated successfully. |
| BFGS | success | [2.0742 1.9478 1.8175 2.0876] | 5.07e-12 | 0.0168 | 408 | Optimization terminated successfully. |
| dogleg | fail | [1.9507 1.9585 2.2395 2.4269] | 636 | 6.24e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.9325 1.6048 1.8579 2.2093] | 3.58e+03 | 5.83e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [2.173 1.8167 1.6858 2.2543] | 2.34e+03 | 5.38e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.9005 2.0089 1.6689 1.8918] | 4.44e+03 | 6.77e-05 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.1015 1.7543 2.2733 2.3614] | 761 | 0.000453 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.4881 1.9066 1.8671 1.9175] | 1.42e+03 | 0.000436 | 28 | A bad approximation caused failure to predict improvement. |
