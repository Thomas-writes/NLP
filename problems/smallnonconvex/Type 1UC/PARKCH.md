# PARKCH

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
- **Objective Type:** other
- **# of Variables (n):** 15
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [-0.18897 -0.094269 -0.1878 0.082019 0.015181 0.12288 -0.099772 -0.13651 0.098048 -0.12081 -0.087135 0.02027 0.066305 0.0066583 0.78573] | 1.62e+03 | 19.2 | 2100 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [0.070766 0.0050752 0.011016 0.028982 0.049406 0.053623 0.10878 0.11677 -0.16325 0.090842 0.099577 0.049415 -0.099493 0.031377 0.94265] | 4.4e+03 | 0.356 | 1 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [-0.064924 0.026608 -0.066014 0.056562 0.044808 0.065231 0.02032 -0.0053309 -0.15241 -0.092058 -0.055505 0.02676 0.087354 -0.064214 0.8903] | 1.62e+03 | 18.2 | 2048 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [0.042938 -0.0020156 0.051248 0.077208 -0.075764 -0.016038 0.01188 -0.083859 -0.066446 -0.10431 0.030265 -0.031817 0.077172 0.099033 0.9772] | 1.62e+03 | 0.362 | 39 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-0.044133 -0.03516 0.088812 0.15127 -0.062869 0.055005 0.10511 -0.085962 0.078774 -0.094547 -0.12089 0.059211 0.1185 -0.040121 0.99125] | 1.62e+03 | 0.419 | 47 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-0.020455 -0.047955 0.12596 -0.12146 -0.17156 -0.13882 0.1254 0.12177 0.063671 -0.0022239 -0.11962 0.10972 0.085261 0.012293 1.0586] | 1.62e+03 | 0.319 | 52 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [0.04898 0.090864 -0.092036 -0.13416 0.10985 0.061964 0.0075537 0.0035665 0.025486 -0.059423 -0.012923 0.11099 0.048304 -0.16527 1.0787] | 1.18e+04 | 0.232 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.0092321 -0.12201 0.078897 -0.0048971 0.13091 -0.051759 -0.086179 0.16539 -0.14269 0.07321 0.1127 -0.1274 0.071228 -0.17442 0.919] | 3.34e+03 | 0.241 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.084455 0.096435 0.060004 -0.0065014 0.087425 0.18416 -0.051204 -0.064942 -0.12147 -0.099629 0.0050263 0.083046 0.30567 -0.009817 0.92371] | 1.4e+04 | 0.253 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.03809 -0.082791 -0.11386 -0.0076794 -0.10349 -0.068327 0.078102 -0.027835 0.028176 0.0015417 0.071122 -0.12456 -0.023442 0.039103 1.0121] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [0.10814 -0.035188 -0.048286 0.053151 -0.12868 0.16997 -0.0015886 0.16251 0.1166 0.082702 0.018881 -0.020838 0.031667 0.0060085 1.0412] | nan | nan | None | array must not contain infs or NaNs |
| trust-ncg | fail | [-0.14247 -0.015009 -0.005935 -0.086349 0.042214 0.17047 -0.0030755 0.13407 -0.020296 -0.082387 0.044866 0.12539 0.23809 -0.056269 0.89583] | nan | nan | None | array must not contain infs or NaNs |
