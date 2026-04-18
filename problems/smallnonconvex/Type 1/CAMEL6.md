# CAMEL6

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
| L-BFGS-B | success | [1.0149 1.0322] | -1.0316284534872247 | 0.00029312499100342393 | 8 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [1.0198 1.1685] | -1.0316284534778746 | 0.00024020898854359984 | 11 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.9636 0.93005] | -1.0316284534860614 | 0.00021433300571516156 | 9 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [0.9834 0.98315] | -1.031628453489876 | 0.0002353329909965396 | 8 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [1.145 1.0204] | -1.0316284534898774 | 0.00015404197620227933 | 7 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [1.14 1.0835] | -1.0316284529259634 | 0.00014020799426361918 | 6 | Converged (|f_n-f_(n-1)| ~= 0) |
| Powell | success | [0.89929 1.1312] | -0.2154638229355086 | 0.000586083042435348 | 3 | Optimization terminated successfully. |
| Powell | success | [1.2558 0.98278] | -0.21546382293550836 | 0.000543333007954061 | 3 | Optimization terminated successfully. |
| Powell | success | [1.1101 1.1945] | -0.21546382293550925 | 0.0005350409774109721 | 3 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.1685 0.91284] | -1.0316284509896743 | 0.0006995420553721488 | 48 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.1459 1.2458] | -1.0316284500875028 | 0.0006305419956333935 | 47 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0717 1.1119] | -1.0316284496895862 | 0.0005651249666698277 | 42 | Optimization terminated successfully. |
