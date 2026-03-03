# PALMER3C

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
| CG | fail | [1.1966 0.99854 0.81142 0.96444 0.85073 1.0771 0.95696 1.016] | 0.141 | 0.0608 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.0622 1.0693 1.0528 0.96518 1.0447 1.0038 0.86184 0.88909] | 0.0708 | 0.0728 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.0269 0.96543 1.0072 0.91978 1.0329 0.9273 0.96014 1.0631] | 0.166 | 0.0593 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [0.90016 0.96486 1.0597 0.74351 0.93551 1.0166 1.1082 1.0761] | 0.0195 | 0.00159 | 49 | Optimization terminated successfully. |
| BFGS | success | [1.102 0.88215 1.1476 1.0173 1.0046 1.0277 1.0746 1.0292] | 0.0195 | 0.00142 | 47 | Optimization terminated successfully. |
| BFGS | success | [0.76554 1.0019 1.0994 1.1742 0.83272 0.98654 1.1815 0.85452] | 0.0195 | 0.00143 | 49 | Optimization terminated successfully. |
| dogleg | success | [1.0857 1.0048 0.99922 1.2053 1.0785 1.015 1.0585 1.0281] | 0.0195 | 0.000402 | 7 | Optimization terminated successfully. |
| dogleg | success | [0.90214 0.80672 1.0794 1.0629 1.175 1.0303 1.041 0.97453] | 0.0195 | 0.000358 | 7 | Optimization terminated successfully. |
| dogleg | success | [1.0335 1.0454 0.94288 0.9598 1.1059 1.0754 0.90509 0.94664] | 0.0195 | 0.00035 | 7 | Optimization terminated successfully. |
