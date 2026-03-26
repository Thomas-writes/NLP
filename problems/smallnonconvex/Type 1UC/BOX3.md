# BOX3

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.4865 7.8035 1.2155] | 4.67e-09 | 0.000957 | 18 | Optimization terminated successfully. |
| CG | success | [0.7231 8.2825 0.17505] | 2.86e-11 | 0.000728 | 13 | Optimization terminated successfully. |
| CG | success | [-0.26222 10.423 -0.29694] | 1.67e-12 | 0.000777 | 15 | Optimization terminated successfully. |
| BFGS | success | [-0.604 11.071 0.069495] | 3.43e-12 | 0.000796 | 25 | Optimization terminated successfully. |
| BFGS | success | [-2.0483 10.884 1.6749] | 2.82e-12 | 0.000926 | 30 | Optimization terminated successfully. |
| BFGS | success | [0.57125 11.141 2.8536] | 6.95e-14 | 0.000634 | 20 | Optimization terminated successfully. |
| dogleg | success | [0.92123 9.9779 1.1154] | 2.25e-14 | 0.000223 | 4 | Optimization terminated successfully. |
| dogleg | fail | [1.3547 8.3189 1.4478] | 1.26 | 4.83e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.41014 10.718 0.50488] | 9.48 | 5.48e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.33069 9.414 1.3015] | 0.87 | 0.000779 | 30 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.1638 10.723 -1.057] | 1.1 | 0.00085 | 30 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.36159 9.7899 0.19863] | 1.88 | 0.000893 | 31 | A bad approximation caused failure to predict improvement. |
