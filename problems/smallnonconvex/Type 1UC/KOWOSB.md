# KOWOSB

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.29423 0.55199 0.39851 0.37469] | 0.000308 | 0.00314 | 64 | Optimization terminated successfully. |
| CG | success | [0.23817 0.37964 0.41883 0.47848] | 0.000308 | 0.0021 | 50 | Optimization terminated successfully. |
| CG | success | [0.38695 0.53497 0.42771 0.3781] | 0.000308 | 0.00637 | 75 | Optimization terminated successfully. |
| BFGS | success | [0.27941 0.50393 0.37013 0.48429] | 0.000308 | 0.00107 | 33 | Optimization terminated successfully. |
| BFGS | success | [0.17688 0.35487 0.66813 0.24953] | 0.000308 | 0.000935 | 28 | Optimization terminated successfully. |
| BFGS | success | [0.29163 0.28567 0.34282 0.46217] | 0.000308 | 0.00108 | 32 | Optimization terminated successfully. |
| dogleg | fail | [0.14604 0.4903 0.45929 0.49313] | 0.0226 | 7.86e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.22753 0.5362 0.53864 0.39311] | 0.00228 | 6.3e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.39171 0.35974 0.43361 0.39586] | 0.0729 | 5.56e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.13539 0.32909 0.48378 0.3582] | 0.0309 | 0.000791 | 31 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.24232 0.35413 0.37065 0.58289] | 0.00893 | 0.000775 | 32 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.30336 0.42654 0.20345 0.38415] | 0.00315 | 0.000776 | 32 | A bad approximation caused failure to predict improvement. |
