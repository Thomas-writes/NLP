# VESUVIOLS

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [0.14977 -0.048334 0.10121 -0.017152 0.024019 0.16195 0.080189 -0.17023] | 3.46e+03 | 0.0122 | 43 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [-0.0010669 -0.035317 0.10287 0.099011 -0.15264 0.14529 0.13571 -0.046785] | 3.46e+03 | 0.0191 | 93 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [0.011553 0.01455 0.021732 0.11051 -0.11952 0.17602 0.027635 -0.041799] | 3.46e+03 | 0.0104 | 41 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [0.00098728 0.099869 0.0064463 -0.036921 0.095003 0.14418 -0.20065 -0.011786] | 3.46e+03 | 0.0048 | 14 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [0.044331 -0.034002 -0.068859 0.0022958 -0.0095397 0.18123 -0.10837 -0.086205] | 1.46e+03 | 0.0877 | 782 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-0.051232 -0.11412 0.16308 -0.038036 0.020641 -0.10298 0.0062595 -0.002245] | 1.5e+03 | 0.154 | 1496 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [0.03827 -0.068048 0.16205 0.1683 -0.0072412 -0.12532 -0.046345 0.11843] | 2.57e+04 | 0.000509 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.028246 -0.0021703 -0.10356 -0.081072 0.16701 0.044887 0.011023 0.19434] | 7.79e+03 | 0.000324 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [-0.065271 0.027952 0.036965 -0.13885 0.038129 -0.012502 0.1211 0.040167] | 2.07e+04 | 0.000321 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.19706 0.010836 0.029709 0.09726 0.034895 0.099098 0.11041 -0.1038] | 1.57e+04 | 0.000904 | 3 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-0.014889 -0.099714 0.041689 -0.098739 0.041595 0.062042 0.073864 0.12534] | 4.88e+03 | 0.00324 | 8 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-0.15608 0.049562 -0.014646 -0.031786 0.051763 0.27726 0.037561 -0.085009] | 1.26e+04 | 0.000278 | 0 | A bad approximation caused failure to predict improvement. |
