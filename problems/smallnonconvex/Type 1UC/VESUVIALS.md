# VESUVIALS

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [609.74 2184.2 -31.678 -6229.8 1.1433e+05 4411.9 -17359 1.0131e+05] | 3.46e+03 | 0.00151 | 3 | Optimization terminated successfully. |
| CG | success | [-13777 3429.3 12403 -5096.9 1.0378e+05 -2815.8 6178.6 96330] | 3.46e+03 | 0.000957 | 3 | Optimization terminated successfully. |
| CG | success | [-13368 -3386.8 -8229.1 -8482.3 1.0201e+05 -205 13095 1.0112e+05] | 3.46e+03 | 0.000951 | 3 | Optimization terminated successfully. |
| BFGS | success | [90.349 3967.2 304.04 -10445 88244 -150.98 5603.6 1.0912e+05] | 3.46e+03 | 0.000943 | 7 | Optimization terminated successfully. |
| BFGS | success | [10680 1539.9 -7312.8 -10825 1.1038e+05 9351.4 223.78 89958] | 3.46e+03 | 0.000899 | 5 | Optimization terminated successfully. |
| BFGS | success | [2137.1 15114 16047 -4292.8 95295 3817.5 4320.1 1.0415e+05] | 3.46e+03 | 0.000927 | 6 | Optimization terminated successfully. |
| dogleg | fail | [6529.1 -5797.7 4193.6 -8380.3 1.0014e+05 -8748 11025 89842] | 9.28e+13 | 0.000508 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [3473.9 1051.2 16640 3441 1.0415e+05 12189 -2565.6 1.0513e+05] | 2.63e+13 | 0.000399 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [4920.6 775.68 8990.1 7389.9 89568 -2383.6 -24120 82928] | 5.27e+13 | 0.000402 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [7493.2 18375 -140.04 2248 1.0503e+05 2930.9 -9169.9 99318] | 7.58e+13 | 0.632 | 1600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [-7464.1 11655 -13333 -738.17 96446 -7577.3 26432 98105] | 7.48e+13 | 0.68 | 1600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [-12943 -15871 -272.47 14622 1.0099e+05 -3851.2 23261 75110] | 2.81e+14 | 0.685 | 1600 | Maximum number of iterations has been exceeded. |
