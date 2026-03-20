# BOX3

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-03

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-0.76175 10.039 0.54372] | 3.4e-09 | 0.000818 | 17 | Optimization terminated successfully. |
| CG | success | [0.58099 8.3853 0.37927] | 1.97e-08 | 0.00112 | 24 | Optimization terminated successfully. |
| CG | success | [-0.97703 9.1987 3.0253] | 7.28e-10 | 0.00104 | 24 | Optimization terminated successfully. |
| BFGS | success | [0.97959 11.399 1.625] | 2.38e-14 | 0.000622 | 19 | Optimization terminated successfully. |
| BFGS | success | [-0.13403 10.381 0.604] | 6.35e-13 | 0.000691 | 23 | Optimization terminated successfully. |
| BFGS | success | [0.65046 9.5162 0.28416] | 2.94e-12 | 0.00063 | 22 | Optimization terminated successfully. |
| dogleg | fail | [-2.7751 11.185 1.5883] | 516 | 5.73e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-1.027 10.004 0.72623] | 23.8 | 4.92e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.37721 9.7292 0.97427] | 0.59 | 4.8e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.73942 10.934 1.3241] | 0.103 | 9.55e-05 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-0.25851 9.3103 0.86085] | 2.04 | 0.000714 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0719 10.948 1.9139] | 2.66 | 0.000716 | 29 | A bad approximation caused failure to predict improvement. |
