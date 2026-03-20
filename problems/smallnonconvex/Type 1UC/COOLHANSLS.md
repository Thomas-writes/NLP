# COOLHANSLS

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
- **# of Variables (n):** 9
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [0.14033 -0.027785 0.11544 0.055486 0.18067 0.13882 -0.064747 -0.026784 0.13206] | 5.98e-05 | 0.0756 | 1800 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.040758 -0.064181 0.13701 0.026503 0.091578 -0.22412 -0.023521 -0.038884 -0.01179] | 3.29e-05 | 0.0685 | 1800 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.085517 -0.15463 -0.022966 -0.048178 -0.096779 -0.059463 -0.068563 0.016307 -0.10175] | 4.57e-05 | 0.0134 | 338 | Desired error not necessarily achieved due to precision loss. |
| BFGS | success | [0.010333 -0.23845 -0.14518 0.18423 -0.28016 0.0015643 -0.050957 0.14555 0.073262] | 9.89e-17 | 0.0102 | 328 | Optimization terminated successfully. |
| BFGS | success | [0.016059 0.080977 -0.18391 -0.032186 -0.022064 0.13145 0.02232 -0.077148 0.024949] | 1.97e-14 | 0.00601 | 190 | Optimization terminated successfully. |
| BFGS | fail | [-0.035985 0.15545 0.061145 -0.091333 -0.089497 -0.091455 0.12858 0.051645 0.01124] | 0.00814 | 0.0124 | 400 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [-0.023354 0.22862 0.075941 -0.14382 -0.079645 -0.026671 -0.13175 -0.036468 -0.049922] | 1.24e+06 | 7.87e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.01362 -0.19167 -0.078271 -0.1774 0.023482 0.14462 0.012378 -0.043613 -0.074864] | 1.05e+06 | 5.7e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.0077116 -0.018284 -0.097774 0.0075096 0.02643 0.00771 -0.076275 0.014234 -0.20643] | 8.14e+05 | 5.58e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.07234 0.018723 0.17185 -0.016086 -0.025885 0.05699 0.035133 -0.035533 0.029001] | 142 | 0.000451 | 10 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-0.049943 -0.030106 -0.095644 -0.26237 0.091754 -0.041869 -0.041337 -0.0038027 0.01651] | 7.82e+04 | 0.0646 | 1800 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [-0.09949 -0.11875 -0.10818 0.096558 0.029244 -0.094406 0.051946 -0.035757 -0.015346] | 1.44e+05 | 0.0386 | 1800 | Maximum number of iterations has been exceeded. |
