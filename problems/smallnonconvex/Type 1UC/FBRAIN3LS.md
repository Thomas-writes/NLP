# FBRAIN3LS

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
| CG | fail | [-3.7807 0.41567 4.8809 -0.17867 -1.947 -0.31498] | 0.259 | 1.45 | 1200 | Maximum number of iterations has been exceeded. |
| CG | fail | [-4.437 0.0012904 3.1769 0.26379 -1.9768 -0.095752] | 0.254 | 1.41 | 1200 | Maximum number of iterations has been exceeded. |
| CG | fail | [-2.8533 -0.37501 3.8912 0.47609 -2.263 -0.62996] | 0.255 | 1.46 | 1200 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [-4.7547 0.18404 4.13 0.38699 -1.319 -0.080846] | 0.241 | 0.792 | 1155 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-3.562 -1.2811 4.2681 1.3128 -1.7924 0.19858] | 0.241 | 0.617 | 1077 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-4.3099 -0.50507 4.055 0.11659 -2.0863 -0.58306] | 0.241 | 0.574 | 959 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [-3.8399 0.10908 4.2039 -0.17921 -2.1041 0.31865] | 274 | 0.00158 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-4.4938 -0.069948 4.1149 -0.2938 -1.309 -0.36043] | 52.1 | 0.00125 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-3.8164 0.07806 3.5638 0.17607 -2.2055 0.16192] | 32.4 | 0.00125 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-3.7781 -0.44897 4.0569 1.1429 -1.2165 0.14524] | 2.19 | 0.0794 | 37 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-4.3114 -0.38865 4.4788 -0.19271 -1.8147 -0.66784] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-3.9743 0.092797 4.3778 0.36887 -1.5311 -0.16672] | 0.433 | 0.0961 | 42 | A bad approximation caused failure to predict improvement. |
