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
| CG | fail | [0.91238 1.0654 1.0195 0.79751 1.0677 1.069 0.9692 1.0119] | 0.152 | 0.0691 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.0316 1.0647 0.87862 0.87876 1.0404 0.9959 0.78364 1.0254] | 0.157 | 0.0669 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.0317 0.99122 0.96329 0.90762 0.84997 1.0274 1.0689 0.90993] | 0.0277 | 0.0786 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [1.053 1.0863 1.0379 0.91141 0.9433 0.87661 1.1446 0.99952] | 0.0195 | 0.00164 | 49 | Optimization terminated successfully. |
| BFGS | success | [1.0842 0.93056 1.0945 0.88339 1.0098 0.99228 0.97416 0.87465] | 0.0195 | 0.00146 | 50 | Optimization terminated successfully. |
| BFGS | success | [1.239 1.0083 1.0673 1.009 1.0444 0.87525 0.84932 1.1302] | 0.0195 | 0.00145 | 47 | Optimization terminated successfully. |
| dogleg | success | [0.97906 1.064 1.1367 0.99483 1.0441 0.94628 0.93484 1.147] | 0.0195 | 0.000406 | 7 | Optimization terminated successfully. |
| dogleg | success | [0.94502 1.0504 1.022 1.0305 0.93912 1.0019 1.066 0.91266] | 0.0195 | 0.000367 | 7 | Optimization terminated successfully. |
| dogleg | success | [1.0471 1.0451 0.93689 0.94837 1.0199 0.92514 0.9622 0.84088] | 0.0195 | 0.000367 | 7 | Optimization terminated successfully. |
| trust-ncg | fail | [0.82854 0.81859 0.92982 1.1185 1.1635 0.94743 1.0429 1.0348] | 2.83e+03 | 0.000251 | 7 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.168 0.88148 1.047 1.1863 1.0583 1.0156 1.0686 0.89517] | 2.76e+03 | 0.000988 | 36 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.1195 0.83454 0.94968 1.1834 1.1536 0.91513 1.1398 0.97727] | 2.56e+03 | 0.000858 | 33 | A bad approximation caused failure to predict improvement. |
