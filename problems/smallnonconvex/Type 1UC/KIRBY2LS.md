# KIRBY2LS

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
- **# of Variables (n):** 5
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [2.1557 -0.019166 -0.33935 0.33048 -0.26534] | 2.19e+03 | 0.0309 | 452 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [1.8274 0.035368 0.20823 0.071471 0.10696] | 1.48e+03 | 0.0154 | 212 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [1.759 0.095096 0.016671 0.024809 0.1296] | 1.77e+03 | 0.0609 | 1000 | Maximum number of iterations has been exceeded. |
| BFGS | success | [2.3664 -0.042837 -0.42077 0.041026 0.14837] | 3.91 | 0.00456 | 88 | Optimization terminated successfully. |
| BFGS | fail | [2.2258 -0.15689 -0.51299 -0.12215 -0.050747] | 925 | 0.0049 | 91 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [2.039 -0.12761 -0.15551 -0.068428 0.14826] | 3.91 | 0.00618 | 84 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [1.562 0.25812 0.080529 0.30922 0.19781] | 4.84e+05 | 0.000101 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.7419 0.025957 0.19449 0.0069077 0.1103] | 4.65e+05 | 8.02e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.9789 0.16672 0.23671 -0.048727 -0.2505] | 5.04e+05 | 7.75e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.9558 -0.12054 -0.203 -0.42978 -0.11635] | 3.29e+04 | 0.000423 | 6 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.5288 -0.037056 0.12868 0.027533 -0.012852] | 9.94e+04 | 0.000371 | 6 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.9184 0.052365 -0.053551 -0.018085 0.011608] | 4.98e+05 | 0.00211 | 38 | A bad approximation caused failure to predict improvement. |
