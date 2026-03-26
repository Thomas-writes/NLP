# LANCZOS3LS

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
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.94558 -0.16236 6.6597 5.5019 6.8859 8.2779] | 8.15e-06 | 0.0309 | 619 | Optimization terminated successfully. |
| CG | success | [1.5146 1.0133 5.3579 5.8983 7.8137 7.8047] | 1.11e-06 | 0.0112 | 239 | Optimization terminated successfully. |
| CG | success | [0.22656 0.28506 5.8427 5.4168 7.3991 7.4569] | 1.72e-06 | 0.0107 | 192 | Optimization terminated successfully. |
| BFGS | success | [0.62841 0.0081807 4.9718 4.0864 5.1697 6.6335] | 1.25e-07 | 0.00232 | 69 | Optimization terminated successfully. |
| BFGS | success | [1.1432 1.2515 6.395 4.5023 7.6894 7.5568] | 1.26e-07 | 0.00347 | 99 | Optimization terminated successfully. |
| BFGS | success | [0.70283 -0.14159 5.8761 5.1764 6.4174 8.4994] | 2.34e-07 | 0.0024 | 72 | Optimization terminated successfully. |
| dogleg | fail | [1.9713 -0.8543 6.2746 5.4446 4.9699 8.1745] | 553 | 7.97e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.1422 0.5076 6.558 6.6021 6.7543 8.4632] | 285 | 6.15e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.1239 1.4451 6.2619 4.5588 7.2331 6.9278] | 348 | 6.08e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.5517 1.0787 5.5118 4.4659 7.2261 7.567] | 195 | 0.000977 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.94062 -0.34076 7.3795 5.5713 6.2193 8.4175] | 182 | 0.000799 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-0.43938 0.31638 4.5253 5.9766 6.4662 8.5391] | 108 | 0.000834 | 28 | A bad approximation caused failure to predict improvement. |
