# MDHOLE

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
- **Objective Type:** other
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [8.6915 2.0538] | 4.137965785899868e-33 | 0.0009604170336388052 | 49 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [9.0243 1.7815] | 2.0812195835417778e-34 | 0.0010105829569511116 | 58 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [10.262 1.9997] | 3.998724312315072e-39 | 0.0010900420020334423 | 68 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [10.848 0.49949] | 97.846354708792 | 8.224998600780964e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | fail | [9.171 0.58897] | 6.304117668772598 | 9.941600728780031e-05 | 1 | Linear search failed |
| TNC | success | [9.624 2.2633] | 3.916921962523628 | 7.079198257997632e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [9.1643 1.0027] | 730.212323192118 | 0.0005337090115062892 | 1 | Optimization terminated successfully. |
| Powell | success | [10.596 0.8658] | 641.9126137473338 | 0.0005186250200495124 | 1 | Optimization terminated successfully. |
| Powell | success | [10.952 1.52] | 282.9820198938079 | 0.001285624981392175 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [8.2994 2.25] | 6.503458242028088e-08 | 0.0017154999659396708 | 134 | Optimization terminated successfully. |
| Nelder-Mead | success | [8.8982 3.3475] | 5.6117070918671594e-08 | 0.0018934590043500066 | 155 | Optimization terminated successfully. |
| Nelder-Mead | success | [8.7448 2.1591] | 1.108644138166377e-08 | 0.00181124999653548 | 145 | Optimization terminated successfully. |
