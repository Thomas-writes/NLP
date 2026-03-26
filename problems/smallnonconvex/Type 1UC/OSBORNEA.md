# OSBORNEA

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
- **# of Variables (n):** 5
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [0.37806 1.3248 -1.3044 0.061329 -0.12346] | 2.29 | 0.000278 | 1 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [0.47281 1.6522 -0.88775 -0.16099 0.036116] | 0.926 | 0.000763 | 6 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [0.53914 1.2278 -1.1139 -0.39771 -0.0061953] | 0.9 | 0.000722 | 5 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [0.54567 1.575 -0.75592 -0.08411 0.19208] | 1.11 | 0.00164 | 43 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [0.55246 1.1821 -0.92838 0.095334 0.0063382] | 0.0159 | 0.00197 | 41 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [0.61341 1.6628 -0.83881 -0.022596 -0.16396] | 1.02 | 0.00123 | 13 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [0.44393 1.3696 -0.93644 0.059675 -0.30871] | 5.6e+85 | 6.81e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.72085 1.5453 -0.71526 -0.0035266 0.34068] | 330 | 6.12e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.16902 1.5784 -0.76148 -0.046371 -0.076695] | 1.53e+21 | 5.68e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.41223 1.2637 -0.87681 0.12905 0.26553] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [0.31168 1.3986 -1.0766 -0.074883 0.11322] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [0.52968 1.2892 -0.96248 0.11927 -0.030103] | nan | nan | None | array must not contain infs or NaNs |
