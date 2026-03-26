# BIGGS6

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
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.1404 2.1858 1.034 0.7551 0.88113 0.94473] | 2e-08 | 0.00469 | 116 | Optimization terminated successfully. |
| CG | success | [0.78056 2.2241 1.2962 0.75272 1.0391 0.77019] | 5.49e-06 | 0.0165 | 406 | Optimization terminated successfully. |
| CG | success | [0.81812 1.8199 0.93026 0.89515 0.9756 1.2057] | 1.6e-06 | 0.0195 | 499 | Optimization terminated successfully. |
| BFGS | success | [1.0534 2.144 1.2394 0.69031 0.8469 1.1001] | 3.64e-11 | 0.00284 | 88 | Optimization terminated successfully. |
| BFGS | success | [0.70554 1.9193 1.1025 1.092 1.1963 1.0081] | 5.23e-12 | 0.00331 | 98 | Optimization terminated successfully. |
| BFGS | success | [0.97684 1.6495 0.88116 0.87831 0.70824 0.92403] | 2.39e-06 | 0.00171 | 55 | Optimization terminated successfully. |
| dogleg | fail | [0.866 1.8624 1.128 0.99842 1.0122 0.83494] | 0.889 | 6.71e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.1376 2.0467 0.72807 1.1524 1.0531 1.0058] | 2.11 | 5.9e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [1.4909 1.8269 0.79691 0.82459 0.88813 1.0384] | 0.987 | 5.55e-05 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [0.93386 2.4195 1.1223 1.0331 1.0578 1.2388] | 0.714 | 0.000799 | 29 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.5002 1.9773 1.0442 0.96597 0.64307 1.0662] | 1.4 | 0.000807 | 30 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0826 1.8044 1.3746 0.95479 1.0883 1.1466] | 0.615 | 0.000914 | 30 | A bad approximation caused failure to predict improvement. |
