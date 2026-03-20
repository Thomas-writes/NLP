# RECIPELS

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
- **Objective Type:** sum of squares
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [2.1984 4.5853 0.45539] | 1.96e-09 | 0.000523 | 10 | Optimization terminated successfully. |
| CG | success | [1.5351 4.565 1.8372] | 1.75e-09 | 0.000596 | 16 | Optimization terminated successfully. |
| CG | success | [1.7434 5.6949 0.97238] | 1.05e-09 | 0.000711 | 17 | Optimization terminated successfully. |
| BFGS | success | [1.3815 5.6004 0.95442] | 1.82e-09 | 0.000785 | 28 | Optimization terminated successfully. |
| BFGS | success | [2.0047 4.8725 0.71236] | 2.92e-10 | 0.000822 | 30 | Optimization terminated successfully. |
| BFGS | success | [2.3829 5.4101 0.44604] | 1.87e-10 | 0.000653 | 23 | Optimization terminated successfully. |
| dogleg | success | [2.6089 4.8693 1.2228] | 1.59e-07 | 0.000544 | 14 | Optimization terminated successfully. |
| dogleg | fail | [2.0835 5.8677 0.13874] | 240 | 0.000136 | 2 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [2.5918 4.3403 1.3853] | 134 | 9.19e-05 | 1 | A linalg error occurred, such as a non-psd Hessian. |
| CG | success | [2.3607 5.212 2.0977] | 9.27e-09 | 0.000701 | 14 | Optimization terminated successfully. |
| CG | success | [1.7935 4.9497 1.3959] | 2.12e-08 | 0.000846 | 17 | Optimization terminated successfully. |
| CG | success | [2.4573 5.3392 0.82965] | 1.72e-10 | 0.000617 | 13 | Optimization terminated successfully. |
| BFGS | success | [1.9407 4.5634 0.84165] | 6.57e-09 | 0.000695 | 25 | Optimization terminated successfully. |
| BFGS | success | [0.77934 5.3373 0.21489] | 2.4e-10 | 0.000675 | 24 | Optimization terminated successfully. |
| BFGS | success | [1.822 5.0931 -0.20329] | 5.18e-09 | 0.000747 | 27 | Optimization terminated successfully. |
| dogleg | fail | [1.4503 4.9797 1.9527] | 59.4 | 0.000229 | 2 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [2.1944 4.9917 1.6117] | 62.7 | 0.000156 | 2 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | success | [2.4263 4.7798 0.54265] | 1.49e-07 | 0.00054 | 14 | Optimization terminated successfully. |
| trust-ncg | fail | [1.9347 4.2595 0.0034949] | 1.71 | 0.000205 | 5 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.4421 5.2939 1.5312] | 37.3 | 0.0109 | 600 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [2.5456 5.0222 0.51407] | 2.38 | 0.000204 | 5 | A bad approximation caused failure to predict improvement. |
