# PALMER1D

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
- **Objective Type:** quadratic
- **# of Variables (n):** 7
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [0.85073 0.98617 0.93048 1.0735 1.097 0.97696 1.0127] | 0.702 | 0.077 | 1400 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.66965 1.123 1.1349 0.9394 1.0158 0.8092 0.99649] | 2.72 | 0.0746 | 1400 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.0566 0.9886 1.0993 0.96677 1.0616 1.0076 1.1012] | 0.906 | 0.0744 | 1400 | Maximum number of iterations has been exceeded. |
| BFGS | success | [0.99998 1.018 0.97764 1.0881 1.0895 0.98947 1.0458] | 0.653 | 0.000986 | 30 | Optimization terminated successfully. |
| BFGS | success | [0.91609 1.0887 0.93586 0.87927 0.89793 1.1317 1.0443] | 0.653 | 0.00103 | 31 | Optimization terminated successfully. |
| BFGS | success | [0.87269 1.1108 0.944 1.0927 0.99525 1.2188 0.97966] | 0.653 | 0.000943 | 30 | Optimization terminated successfully. |
| dogleg | success | [1.0159 1.0888 0.91206 1.031 0.94885 0.85358 0.94656] | 0.653 | 0.00131 | 26 | Optimization terminated successfully. |
| dogleg | success | [1.0021 1.1653 0.92492 0.87552 0.82157 0.89593 1.0146] | 0.653 | 0.00156 | 26 | Optimization terminated successfully. |
| dogleg | success | [0.89146 1.1258 0.86063 0.93892 1.1253 1.1003 1.0652] | 0.653 | 0.00131 | 26 | Optimization terminated successfully. |
| trust-ncg | fail | [1.0384 1.1689 0.85341 0.7661 1.0663 0.90795 1.0251] | 5.24e+04 | 0.000228 | 5 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0388 0.98366 1.2475 0.87938 0.98374 0.99009 0.99319] | 5.02e+04 | 0.000894 | 33 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.3451 1.0531 0.84494 1.0429 0.75817 1.242 1.0062] | 5.84e+04 | 0.0003 | 6 | A bad approximation caused failure to predict improvement. |
