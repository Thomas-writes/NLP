# KOWOSB

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [0.35015 0.50119 0.42139 0.48268] | 0.000308 | 0.00252 | 57 | Optimization terminated successfully. |
| CG | success | [0.30549 0.46343 0.35234 0.24061] | 0.000308 | 0.00203 | 56 | Optimization terminated successfully. |
| CG | success | [0.37376 0.45271 0.5983 0.2736] | 0.000308 | 0.00223 | 53 | Optimization terminated successfully. |
| BFGS | success | [0.31485 0.40665 0.44451 0.50702] | 0.000308 | 0.00102 | 33 | Optimization terminated successfully. |
| BFGS | success | [0.21299 0.5096 0.44961 0.47453] | 0.000308 | 0.000969 | 32 | Optimization terminated successfully. |
| BFGS | success | [0.0491 0.36903 0.33506 0.55217] | 0.000308 | 0.000995 | 34 | Optimization terminated successfully. |
| dogleg | fail | [0.17839 0.35866 0.35256 0.43133] | 0.0118 | 6.83e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.12537 0.24792 0.42916 0.21869] | 0.0324 | 5.34e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.089873 0.41727 0.35823 0.40647] | 0.0541 | 5.07e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.23466 0.39473 0.25298 0.42268] | 0.00515 | 0.000742 | 33 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.35752 0.25493 0.31326 0.54942] | 0.0417 | 0.000569 | 32 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.17616 0.35746 0.48239 0.5899] | 0.0209 | 0.0007 | 32 | A bad approximation caused failure to predict improvement. |
