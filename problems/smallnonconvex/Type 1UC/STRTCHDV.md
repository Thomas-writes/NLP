# STRTCHDV

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
- **# of Variables (n):** 10
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.0742 -0.96721 -1.0672 -0.8375 -1.0526 -1.0972 -0.88441 -1.1897 -0.82579 -1.0661] | 4.63e-08 | 0.00185 | 30 | Optimization terminated successfully. |
| CG | success | [0.76142 -0.92902 -1.0853 -0.97106 -1.0921 -0.86783 -1.1303 -0.86371 -0.94604 -1.0811] | 4.26e-08 | 0.00138 | 31 | Optimization terminated successfully. |
| CG | success | [1.1324 -0.98374 -1.1107 -1.0041 -1.0752 -0.9019 -1.1412 -0.96056 -0.8867 -0.87677] | 1.86e-08 | 0.000734 | 13 | Optimization terminated successfully. |
| BFGS | success | [0.97852 -0.94189 -1.1468 -0.89348 -0.91566 -1.0556 -1.1631 -1.1727 -1.001 -0.90297] | 1.19e-08 | 0.0019 | 61 | Optimization terminated successfully. |
| BFGS | success | [1.0655 -0.93037 -1.0331 -1.0332 -1.0545 -1.1392 -1.0415 -1.0765 -0.94435 -1.1166] | 6.19e-09 | 0.00197 | 62 | Optimization terminated successfully. |
| BFGS | success | [1.0095 -0.90237 -0.98925 -0.94472 -0.88853 -1.1595 -0.96666 -1.0408 -0.91766 -0.90849] | 1.11e-08 | 0.0016 | 49 | Optimization terminated successfully. |
| dogleg | fail | [0.77236 -0.98777 -1.0616 -1.024 -1.2626 -0.90581 -1.0896 -1.1654 -0.97599 -1.0748] | 5.75 | 6.93e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.95366 -1.0173 -1.1756 -0.97474 -0.99729 -1.1355 -1.0169 -1.0803 -0.98288 -1.006] | 3.71 | 5.33e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.0249 -0.97949 -0.85716 -0.93269 -1.0703 -0.92825 -0.87873 -0.96352 -1.1955 -1.0541] | 15.7 | 5.14e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.0566 -1.0627 -0.96093 -1.0454 -0.96554 -1.0437 -0.9014 -1.1975 -1.1354 -0.93381] | 4.46 | 0.0409 | 2000 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.97588 -1.1412 -1.1021 -1.1005 -0.9006 -0.92974 -1.0738 -1.1913 -0.99445 -1.054] | 5.14 | 0.000114 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.95653 -0.90027 -0.98521 -1.0264 -0.95709 -0.95193 -1.0816 -1.0149 -1.1665 -1.1084] | 9.43 | 0.0436 | 2000 | Maximum number of iterations has been exceeded. |
