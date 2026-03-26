# PRICE3

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.4632 5.6438] | 2.42e-17 | 0.000652 | 13 | Optimization terminated successfully. |
| CG | success | [1.6466 5.4747] | 0.00742 | 0.000681 | 15 | Optimization terminated successfully. |
| CG | success | [1.6531 4.8681] | 6.45e-17 | 0.000541 | 12 | Optimization terminated successfully. |
| BFGS | success | [1.2586 3.4452] | 2.77e-16 | 0.000736 | 17 | Optimization terminated successfully. |
| BFGS | success | [1.0523 4.8285] | 2.36e-14 | 0.0007 | 19 | Optimization terminated successfully. |
| BFGS | success | [1.3729 4.5814] | 6.27e-14 | 0.000741 | 18 | Optimization terminated successfully. |
| dogleg | fail | [0.7828 5.6171] | 3.01e+04 | 5.94e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | success | [1.7078 5.1469] | 3.34e-15 | 0.000395 | 10 | Optimization terminated successfully. |
| dogleg | fail | [1.3178 6.3167] | 4.82e+04 | 5.08e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [1.3868 5.275] | 4.88 | 0.000921 | 34 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.657 4.4744] | 5.79 | 0.000901 | 34 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.097611 4.7039] | 1.8 | 0.000822 | 33 | A bad approximation caused failure to predict improvement. |
