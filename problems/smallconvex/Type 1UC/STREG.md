# STREG

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-25

## Classification
- **Convexity:** Convex
- **Objective Type:** sum of squares
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [1.7936e+08 6.582e+08 1.0146e+10 8.6757e+09] | 6.27e+33 | 0.000597 | 1 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [-9.7879e+08 1.5305e+08 9.4326e+09 1.0015e+10] | 1.93e+34 | 0.000614 | 2 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [-5.0598e+08 1.462e+09 1.0938e+10 1.0213e+10] | 4.36e+34 | 0.000558 | 1 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [1.4008e+08 -1.2048e+09 9.1298e+09 1.0319e+10] | 2.28e+16 | 0.0015 | 8 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [1.6864e+09 -6.4164e+08 8.7255e+09 9.8297e+09] | 3.37e+18 | 0.00139 | 8 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-4.8583e+08 9.0571e+08 9.6875e+09 9.6262e+09] | 2.77e+17 | 0.00161 | 7 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [2.0121e+09 -1.1592e+09 9.9892e+09 8.9513e+09] | 1.64e+39 | 0.0303 | 800 | Maximum number of iterations has been exceeded. |
| dogleg | fail | [2.397e+08 -2.708e+09 1.033e+10 8.0934e+09] | 3.3e+35 | 0.0298 | 800 | Maximum number of iterations has been exceeded. |
| dogleg | fail | [-3.9117e+07 -2.9514e+08 1.0549e+10 9.8064e+09] | 2.34e+32 | 0.0312 | 800 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [9.1031e+08 -5.6696e+08 1.0298e+10 1.0291e+10] | 6.87e+37 | 0.0237 | 800 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [-1.5479e+09 -5.7694e+08 9.8366e+09 8.1977e+09] | 5.74e+38 | 0.0249 | 800 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [-7.5422e+08 -3.3596e+08 8.1794e+09 1.1513e+10] | 3.24e+37 | 0.0234 | 800 | Maximum number of iterations has been exceeded. |
