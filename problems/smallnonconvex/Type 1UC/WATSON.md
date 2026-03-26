# WATSON

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
- **# of Variables (n):** 12
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.11508 -0.12311 -0.1423 -0.081776 -0.1627 -0.010821 0.2125 0.10403 0.021307 0.034714 0.009344 -0.046668] | 4.33e-07 | 0.0311 | 746 | Optimization terminated successfully. |
| CG | success | [0.095682 0.017492 0.018067 0.041873 0.1586 -0.0059541 -0.035931 0.12482 0.12416 -0.053213 -0.14467 0.14009] | 3.84e-07 | 0.0384 | 918 | Optimization terminated successfully. |
| CG | success | [0.047488 -0.11807 -0.01918 -0.063464 -0.039848 -0.037552 -0.13098 0.052053 0.095217 -0.053052 0.021293 0.11889] | 1.46e-07 | 0.0349 | 750 | Optimization terminated successfully. |
| BFGS | success | [-0.064322 0.17429 -0.040381 -0.030543 -0.055794 0.0038579 -0.050673 -0.3665 0.061631 -0.11484 -0.044368 0.01993] | 2.3e-07 | 0.00163 | 45 | Optimization terminated successfully. |
| BFGS | success | [0.045985 0.025386 -0.065678 0.070675 0.15545 0.026064 -0.053299 0.024283 0.1777 0.086394 -0.13321 0.012728] | 1.62e-07 | 0.00153 | 43 | Optimization terminated successfully. |
| BFGS | success | [0.0512 -0.045104 0.075769 0.065968 -0.022791 -0.12768 -0.03115 -0.10545 0.096571 -0.10146 0.013968 -0.099679] | 1.41e-07 | 0.00156 | 45 | Optimization terminated successfully. |
| dogleg | fail | [-0.03973 -0.18641 -0.036249 0.0067373 0.15629 0.044394 -0.089564 -0.068469 -0.22685 -0.043748 0.034658 0.073428] | 61.3 | 9.36e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.023321 0.058537 -0.028537 -0.094481 -0.027 0.095815 0.047869 0.076813 0.17943 -0.10013 -0.082187 -0.065176] | 26.9 | 7.52e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.069805 0.027561 0.1968 0.089064 -0.17549 0.11999 0.019196 -0.026562 0.095083 0.093841 -0.026614 0.046217] | 17.1 | 6.52e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.079784 -0.037622 0.11283 -0.013736 -0.2501 0.059479 -0.10399 0.1347 0.11587 -0.090726 0.10811 -0.050052] | 12 | 0.000512 | 8 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.040832 0.15149 -0.25639 -0.031494 -0.0053459 -0.15478 -0.042841 0.02451 0.066603 -0.050304 0.18655 -0.028323] | 8.33 | 0.000568 | 10 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-0.03305 0.03055 -0.076999 0.024261 0.014974 0.02502 -0.090633 0.085411 -0.03284 0.021347 -0.1705 0.16378] | 8.95 | 0.000432 | 7 | A bad approximation caused failure to predict improvement. |
