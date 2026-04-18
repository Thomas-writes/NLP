# DEVGLA1B

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
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.9022 2.1001 2.2193 2.2725] | 4.978216498021719e-12 | 0.0009264590335078537 | 38 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [2.066 1.9462 1.8272 2.0181] | 105138.82986350702 | 0.0003886250196956098 | 14 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [2.078 2.0731 1.7208 1.9876] | 105138.82986350691 | 0.0003956669825129211 | 14 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [2.0177 2.2676 2.161 1.7281] | 1.125719689545642e-09 | 0.0008732500136829913 | 22 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [1.8873 1.9237 2.1886 2.0406] | 8.147808406971833e-11 | 0.0008487079758197069 | 25 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | fail | [1.925 1.959 1.8787 2.0621] | 0.00026148618786213097 | 0.0008533339714631438 | 26 | Max. number of function evaluations reached |
| Powell | success | [1.9935 1.9674 2.0208 1.9097] | 105276.10482539554 | 0.001488707959651947 | 3 | Optimization terminated successfully. |
| Powell | success | [1.9963 2.036 2.2256 2.271] | 98064.88434430752 | 0.0011686250218190253 | 3 | Optimization terminated successfully. |
| Powell | success | [2.1986 2.287 2.4198 2.0852] | 69115.4184714872 | 0.0010971669689752162 | 3 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.8684 1.9243 1.8636 1.7814] | 3.6763966184879234e-08 | 0.0033560830052010715 | 263 | Optimization terminated successfully. |
| Nelder-Mead | success | [2.2791 2.135 2.5037 1.6453] | 3.3065925612259924e-08 | 0.004294416983611882 | 339 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.8505 2.2282 1.7993 2.085] | 9.022134721701327e-08 | 0.0031014580163173378 | 235 | Optimization terminated successfully. |
