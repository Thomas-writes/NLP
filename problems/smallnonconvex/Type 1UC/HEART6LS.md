# HEART6LS

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
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [0.17103 -0.11775 0.91455 1.0859 1.0114 0.87166] | 0.276 | 0.0449 | 1200 | Maximum number of iterations has been exceeded. |
| CG | fail | [-0.0036028 -0.13387 0.91001 1.0691 0.97765 0.94733] | 0.4 | 0.0481 | 1200 | Maximum number of iterations has been exceeded. |
| CG | fail | [-0.023644 -0.090568 1.0166 1.0255 0.94553 1.0816] | 0.341 | 0.0428 | 1200 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [-0.035211 0.041224 1.0289 0.76217 0.91395 0.81942] | 0.00261 | 0.0385 | 1200 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [-0.056548 -0.088142 0.95614 1.1656 1.1341 1.0046] | 0.42 | 0.0377 | 1200 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [-0.1575 -0.099302 1.084 1.0704 0.97166 0.88925] | 0.000817 | 0.0373 | 1200 | Maximum number of iterations has been exceeded. |
| dogleg | fail | [-0.0055287 0.065927 0.79522 0.91963 0.94701 1.0578] | 561 | 0.000113 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.16572 0.17236 1.1219 1.0223 1.0955 1.0592] | 580 | 6.28e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.05261 0.029037 0.9949 1.15 0.99571 1.056] | 598 | 5.6e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.053727 -0.13297 0.74325 1.1208 1.0709 0.85387] | 356 | 0.0245 | 1200 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [-0.15742 -0.0063218 1.1608 0.98261 1.1239 1.137] | 444 | 0.0251 | 1200 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.11732 -0.082129 1.1847 0.92478 0.83483 1.0365] | 406 | 0.0252 | 1200 | Maximum number of iterations has been exceeded. |
