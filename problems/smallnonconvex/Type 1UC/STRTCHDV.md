# STRTCHDV

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
- **# of Variables (n):** 10
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.9715 -0.97869 -1.1792 -1.0041 -0.98142 -1.0831 -0.96995 -1.0392 -1.0196 -0.81824] | 1.36e-08 | 0.0013 | 24 | Optimization terminated successfully. |
| CG | success | [0.95189 -1.1027 -1.0064 -1.076 -0.83929 -1.0988 -0.95237 -0.95717 -0.90384 -1.0846] | 2.85e-08 | 0.00121 | 20 | Optimization terminated successfully. |
| CG | success | [1.046 -0.87542 -1.1349 -0.98073 -0.92002 -1.1346 -1.1812 -0.80687 -0.9968 -0.973] | 2.62e-08 | 0.000934 | 17 | Optimization terminated successfully. |
| BFGS | success | [1.1397 -0.97311 -1.1302 -1.1492 -0.94796 -1.1156 -0.891 -1.0713 -1.0597 -1.0988] | 7.36e-09 | 0.00165 | 50 | Optimization terminated successfully. |
| BFGS | success | [1.0933 -1.0945 -0.87654 -0.84272 -1.0229 -0.9464 -0.95004 -1.0395 -1.0807 -0.91357] | 9.08e-09 | 0.00227 | 70 | Optimization terminated successfully. |
| BFGS | success | [1.0782 -0.77837 -1.0071 -0.97082 -1.0309 -0.88134 -1.0834 -0.97444 -0.95646 -1.0233] | 9.67e-09 | 0.00186 | 59 | Optimization terminated successfully. |
| dogleg | fail | [0.82993 -1.0237 -0.94111 -1.0222 -1.1218 -1.0236 -1.1399 -1.0508 -0.93143 -0.95026] | 8.59 | 7.52e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.1754 -1.0147 -1.0384 -0.88833 -0.87225 -0.9081 -1.0308 -1.1057 -0.8308 -1.1014] | 14.3 | 6.32e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.0324 -0.92709 -0.99088 -1.0291 -1.1114 -1.0626 -1.0388 -0.96367 -0.87943 -1.0214] | 9.71 | 5.33e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.82446 -0.93914 -0.81231 -0.89715 -0.99941 -0.9197 -0.83964 -1.0463 -1.1291 -0.97231] | 23 | 0.0466 | 2000 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.9881 -1.0696 -0.89915 -1.14 -1.0066 -0.8283 -1.0161 -0.81631 -0.97414 -0.98244] | 15.8 | 0.0418 | 2000 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.95314 -1.048 -1.0974 -1.1404 -0.96528 -0.87129 -1.057 -1.2447 -1.068 -1.0768] | 5.65 | 0.000125 | 0 | A bad approximation caused failure to predict improvement. |
