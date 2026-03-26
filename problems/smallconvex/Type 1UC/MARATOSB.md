# MARATOSB

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
- **Objective Type:** other
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [1.1008 0.16071] | -0.239 | 0.0184 | 400 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.219 0.075301] | 0.011 | 0.0174 | 400 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.99823 0.017953] | 0.139 | 0.0184 | 400 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [1.1277 0.063404] | 0.335 | 0.0131 | 400 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [1.0121 -0.038041] | 0.531 | 0.0126 | 400 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [1.1334 0.013929] | 0.385 | 0.013 | 400 | Maximum number of iterations has been exceeded. |
| dogleg | fail | [0.95368 0.041499] | 7.88e+03 | 7.08e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.0819 -0.0073715] | 1 | 0.000168 | 3 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.99366 0.1155] | -0.399 | 0.0143 | 400 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [1.0045 0.0061814] | 84.1 | 0.000796 | 34 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.2269 0.16764] | 543 | 0.000601 | 34 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.1752 0.17261] | 1.45e+04 | 0.000721 | 32 | A bad approximation caused failure to predict improvement. |
