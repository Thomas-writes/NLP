# COOLHANSLS

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
- **# of Variables (n):** 9
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [-0.23284 0.05521 -0.021598 -0.068924 -0.09259 0.0059353 -0.064089 -0.08489 0.11403] | 1.53e-06 | 0.0353 | 757 | Optimization terminated successfully. |
| CG | fail | [-0.096684 -0.08489 0.18 -0.027754 -0.065412 0.14415 -0.09261 0.14192 0.14564] | 3.73e-05 | 0.0162 | 349 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [-0.0016381 0.14518 -0.056948 0.11197 0.14473 0.019986 0.065138 0.17787 0.12258] | 1.98e-05 | 0.0698 | 1800 | Maximum number of iterations has been exceeded. |
| BFGS | success | [0.085258 -0.01785 -0.072448 0.093142 0.1081 0.086622 -0.19015 0.020465 -0.025631] | 2.28e-22 | 0.0116 | 341 | Optimization terminated successfully. |
| BFGS | success | [-0.070815 -0.00094874 -0.063935 -0.018639 0.093482 -0.10722 -0.066164 -0.032258 0.087412] | 9.35e-09 | 0.00674 | 187 | Optimization terminated successfully. |
| BFGS | success | [0.019536 0.10076 -0.16495 -0.019688 0.0069882 -0.11908 -0.097791 -0.048629 0.016663] | 2.07e-17 | 0.00929 | 239 | Optimization terminated successfully. |
| dogleg | fail | [-0.13354 0.13232 0.007868 0.010294 0.071747 0.043847 -0.05762 0.0056457 0.13046] | 6.81e+05 | 7.08e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.15996 0.11848 0.014723 -0.023202 0.11456 0.033341 0.13274 0.019743 0.003943] | 5.61e+05 | 5.93e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.1875 0.16443 -0.06143 0.020165 0.023868 -0.13747 0.10025 0.083973 -0.069661] | 8.83e+05 | 5.57e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.019636 -0.045302 0.027349 0.051158 -0.071787 0.014025 0.018629 0.0009565 -0.02954] | 7.92e+05 | 0.0411 | 1800 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [-0.036205 0.033252 -0.071152 -0.095663 -0.073614 0.0099126 0.18113 -0.078544 0.061096] | 5.84e+05 | 0.0394 | 1800 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.058081 -0.0049965 0.075658 0.075414 0.058185 -0.033648 0.001747 -0.12448 -0.068031] | 5.25e+05 | 0.0407 | 1800 | Maximum number of iterations has been exceeded. |
