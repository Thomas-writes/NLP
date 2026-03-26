# POWELLSQLS

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [3.0103 0.43592] | 1.19e-10 | 0.000531 | 5 | Optimization terminated successfully. |
| CG | success | [2.8161 0.68537] | 3.3e-10 | 0.000628 | 5 | Optimization terminated successfully. |
| CG | fail | [2.7156 0.83434] | 0.000402 | 0.000419 | 3 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [3.3004 1.0475] | 4.41e-14 | 0.000529 | 9 | Optimization terminated successfully. |
| BFGS | success | [3.1025 1.5394] | 1.48e-12 | 0.000494 | 9 | Optimization terminated successfully. |
| BFGS | success | [2.5158 0.85308] | 1.02e-17 | 0.000492 | 7 | Optimization terminated successfully. |
| dogleg | fail | [3.3194 0.95887] | 71.9 | 0.000254 | 3 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [3.3318 0.75936] | 67.9 | 0.000226 | 3 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [2.5878 1.8111] | 19.6 | 0.000184 | 3 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [3.1851 0.26422] | 87.7 | 0.000917 | 32 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [3.5822 0.71307] | 97.8 | 0.000877 | 32 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [3.2459 1.276] | 97.8 | 0.000775 | 32 | A bad approximation caused failure to predict improvement. |
