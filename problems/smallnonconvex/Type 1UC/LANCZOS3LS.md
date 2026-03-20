# LANCZOS3LS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-03

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.4027 0.89679 7.5006 5.4666 7.2609 7.4127] | 7.38e-07 | 0.0106 | 266 | Optimization terminated successfully. |
| CG | success | [1.5412 0.39905 6.88 4.3865 6.4216 5.9697] | 4.82e-06 | 0.00618 | 160 | Optimization terminated successfully. |
| CG | success | [0.91895 -0.027902 4.6751 5.0785 7.2071 7.4008] | 9.94e-06 | 0.0142 | 380 | Optimization terminated successfully. |
| BFGS | success | [0.54444 0.52082 7.4592 5.4544 5.3477 7.8325] | 4e-08 | 0.00361 | 121 | Optimization terminated successfully. |
| BFGS | success | [0.40524 0.65679 4.9944 4.9019 8.0753 9.1221] | 9.35e-08 | 0.0028 | 90 | Optimization terminated successfully. |
| BFGS | success | [0.95803 0.61896 6.4701 4.6852 7.3169 7.3073] | 1.86e-07 | 0.003 | 92 | Optimization terminated successfully. |
| dogleg | fail | [2.0841 -0.29904 6.1614 5.8676 5.2846 8.0761] | 406 | 6.56e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.94656 -1.0314 5.6664 4.7063 6.2861 6.8077] | 355 | 5.78e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.73621 -0.44735 4.3648 6.7177 6.9614 8.0698] | 187 | 5.52e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.28985 0.55998 5.9047 6.6172 6.6133 6.7672] | 173 | 0.000865 | 28 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.2106 0.12557 4.5375 4.7211 6.9506 9.2953] | 139 | 0.000849 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.6733 0.32722 6.6001 5.0184 7.6618 8.4679] | 260 | 0.000949 | 28 | A bad approximation caused failure to predict improvement. |
