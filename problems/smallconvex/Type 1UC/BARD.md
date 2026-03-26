# BARD

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.0542 0.82606 0.90353] | 0.00821 | 0.00105 | 20 | Optimization terminated successfully. |
| CG | success | [1.0584 0.9094 1.0782] | 0.00821 | 0.000905 | 19 | Optimization terminated successfully. |
| CG | success | [0.88618 1.1283 1.089] | 0.00821 | 0.00102 | 22 | Optimization terminated successfully. |
| BFGS | success | [0.86676 1.1169 1.072] | 0.00821 | 0.000657 | 19 | Optimization terminated successfully. |
| BFGS | success | [1.0878 1.0701 0.98248] | 0.00821 | 0.000675 | 20 | Optimization terminated successfully. |
| BFGS | success | [0.99655 0.95993 1.1022] | 0.00821 | 0.000618 | 20 | Optimization terminated successfully. |
| dogleg | success | [0.98859 1.1587 0.8486] | 0.00821 | 0.00044 | 10 | Optimization terminated successfully. |
| dogleg | success | [0.96273 1.2593 1.0502] | 0.00821 | 0.00034 | 8 | Optimization terminated successfully. |
| dogleg | fail | [1.0463 1.0201 1.0163] | 0.174 | 0.000191 | 3 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.0883 0.98194 0.85673] | 55.5 | 0.0137 | 600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [1.0731 1.032 1.095] | 39 | 0.0156 | 600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [1.0134 1.1613 0.94147] | 37.3 | 0.0144 | 600 | Maximum number of iterations has been exceeded. |
