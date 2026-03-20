# DENSCHNE

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
| CG | success | [2.298 2.5989 -7.5465] | 6.9e-16 | 0.000834 | 11 | Optimization terminated successfully. |
| CG | success | [1.0962 3.9088 -7.8614] | 4.39e-17 | 0.000851 | 10 | Optimization terminated successfully. |
| CG | success | [2.2814 2.9917 -6.5442] | 1.05e-13 | 0.000821 | 14 | Optimization terminated successfully. |
| BFGS | success | [2.9047 2.8337 -8.4727] | 2.17e-12 | 0.00116 | 30 | Optimization terminated successfully. |
| BFGS | success | [1.7837 2.1942 -7.8049] | 5.68e-13 | 0.00104 | 25 | Optimization terminated successfully. |
| BFGS | success | [3.5023 1.4223 -7.9644] | 1.87e-11 | 0.00104 | 24 | Optimization terminated successfully. |
| dogleg | fail | [1.9808 3.1575 -6.8997] | 177 | 6.5e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [2.064 3.7104 -8.4241] | 311 | 4.98e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [2.0247 3.4216 -9.5246] | 234 | 4.92e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [2.2729 3.2736 -7.1785] | 0.999 | 0.000762 | 32 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.0213 2.3724 -10.012] | 1 | 0.000686 | 31 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.5036 3.0541 -7.1326] | 0.999 | 0.00071 | 32 | A bad approximation caused failure to predict improvement. |
