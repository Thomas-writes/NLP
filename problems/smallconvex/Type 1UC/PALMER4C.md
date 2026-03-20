# PALMER4C

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Convex
- **Objective Type:** quadratic
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [0.9604 1.1934 1.1852 1.0067 1.193 1.0668 1.1034 0.97132] | 0.178 | 0.0783 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.96748 0.98828 0.81693 1.1027 1.1076 1.1451 0.99006 1.0104] | 0.0503 | 0.041 | 922 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [0.88447 0.972 0.98828 0.89874 1.0023 1.1186 1.0273 1.0441] | 0.373 | 0.0568 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [1.1546 0.73104 0.99128 0.94165 0.98317 0.9147 0.95221 0.91651] | 0.0503 | 0.00144 | 49 | Optimization terminated successfully. |
| BFGS | success | [0.88027 0.97052 0.93445 0.9144 1.0462 1.051 0.86897 0.90532] | 0.0503 | 0.00159 | 52 | Optimization terminated successfully. |
| BFGS | success | [0.9831 0.89533 1.0892 0.81207 0.96644 0.89871 0.87181 1.0738] | 0.0503 | 0.00156 | 49 | Optimization terminated successfully. |
| dogleg | success | [0.88494 1.1517 0.92248 1.2083 0.85417 0.951 1.0989 1.0911] | 0.0503 | 0.000455 | 8 | Optimization terminated successfully. |
| dogleg | success | [1.0488 1.136 0.98472 0.87742 0.98341 1.0462 0.95274 1.0724] | 0.0503 | 0.000414 | 8 | Optimization terminated successfully. |
| dogleg | success | [0.90684 1.0836 1.0286 1.1144 1.1988 1.0354 0.99653 0.9429] | 0.0503 | 0.000408 | 8 | Optimization terminated successfully. |
| CG | fail | [0.94551 1.056 1.2606 1.0835 1.1546 0.99119 1.1335 1.0247] | 0.353 | 0.0681 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.1591 0.8865 1.0793 1.2093 0.82392 0.97606 1.0611 0.9011] | 4.34 | 0.057 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.92376 0.87246 1.2984 1.1622 0.96512 0.97997 0.96364 0.97759] | 0.371 | 0.0674 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [1.113 1.0617 0.99418 1.0488 0.8994 1.0757 0.95939 1.0669] | 0.0503 | 0.00156 | 50 | Optimization terminated successfully. |
| BFGS | success | [0.82833 0.97146 1.0641 0.90042 1.0922 1.0909 1.0991 1.1444] | 0.0503 | 0.0015 | 49 | Optimization terminated successfully. |
| BFGS | success | [1.1319 0.84855 0.72713 0.8971 0.99424 1.0622 0.91431 0.93901] | 0.0503 | 0.00157 | 49 | Optimization terminated successfully. |
| dogleg | success | [1.0636 0.99697 0.9992 0.96736 1.0063 1.0717 1.1525 1.0577] | 0.0503 | 0.000448 | 8 | Optimization terminated successfully. |
| dogleg | success | [0.90683 1.1922 1.01 1.1386 0.96479 0.96928 1.0241 1.0227] | 0.0503 | 0.000414 | 8 | Optimization terminated successfully. |
| dogleg | success | [0.91851 0.94867 1.0406 1.0312 1.0093 0.90932 1.0419 0.98226] | 0.0503 | 0.000413 | 8 | Optimization terminated successfully. |
| trust-ncg | fail | [1.0651 1.0724 0.9734 1.0343 0.86682 1.1699 0.98665 0.80798] | 2.1e+03 | 0.000812 | 32 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.1527 1.2202 1.071 1.1324 0.85833 0.77488 1.0963 0.98236] | 1.66e+03 | 0.00103 | 36 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0185 0.87952 0.92375 1.0593 0.97685 1.0334 0.96359 1.0785] | 2.65e+03 | 0.000168 | 4 | A bad approximation caused failure to predict improvement. |
