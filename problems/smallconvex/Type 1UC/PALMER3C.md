# PALMER3C

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [1.0477 0.9826 0.85093 1.0754 1.0177 1.0675 1.018 0.97164] | 0.138 | 0.0906 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.89356 0.98809 0.97284 0.82362 0.98131 0.94207 1.1098 0.95796] | 1.44 | 0.0665 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.90843 1.0137 0.93443 0.97107 1.1332 0.75479 0.85322 0.99487] | 0.133 | 0.096 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [0.93459 1.0807 1.1155 1.0579 1.0812 0.79592 0.89975 1.0144] | 0.0195 | 0.00178 | 50 | Optimization terminated successfully. |
| BFGS | success | [0.98348 1.1404 1.0741 0.91 0.92105 0.90724 0.94039 1.1838] | 0.0195 | 0.00155 | 47 | Optimization terminated successfully. |
| BFGS | success | [0.8458 1.0385 0.9924 1.1557 1.0404 1.0308 0.98821 1.0043] | 0.0195 | 0.00153 | 48 | Optimization terminated successfully. |
| dogleg | success | [0.96591 1.1643 0.97548 1.0347 1.0905 0.92332 1.0961 0.90001] | 0.0195 | 0.000766 | 15 | Optimization terminated successfully. |
| dogleg | success | [1.217 1.1455 0.96718 0.91696 0.99858 0.90665 0.92234 0.84066] | 0.0195 | 0.000748 | 15 | Optimization terminated successfully. |
| dogleg | success | [1.0195 1.0913 0.90128 1.0198 0.89993 1.1268 0.94244 1.0204] | 0.0195 | 0.000889 | 15 | Optimization terminated successfully. |
| trust-ncg | fail | [0.99216 0.94414 1.0428 1.0133 0.8984 1.0645 0.84441 1.0271] | 1.52e+03 | 0.000921 | 35 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0474 1.0226 1.0531 0.87579 0.8884 0.91067 0.92331 0.99124] | 1.52e+03 | 0.000231 | 6 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.084 0.92081 1.1472 1.0985 0.96167 0.85412 0.86039 1.0004] | 2.85e+03 | 0.000224 | 6 | A bad approximation caused failure to predict improvement. |
