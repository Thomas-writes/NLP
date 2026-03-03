# TESTQUAD

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
- **Objective Type:** quadratic
- **# of Variables (n):** 10
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.0469 0.87317 0.91002 0.9907 1.0515 0.8725 0.99315 0.9947 0.97888 0.94695] | 9.19e-13 | 0.0102 | 312 | Optimization terminated successfully. |
| CG | success | [1.1033 0.98065 0.96103 0.98565 1.002 0.86861 0.99746 0.89949 1.0407 0.89967] | 2.65e-19 | 0.000935 | 15 | Optimization terminated successfully. |
| CG | success | [0.94073 0.91552 1.0296 0.98709 1.0471 1.0195 1.0476 0.99008 1.0304 0.92065] | 2.01e-20 | 0.00511 | 155 | Optimization terminated successfully. |
| BFGS | success | [0.96076 1.0002 0.91033 1.0579 0.94082 1.0368 0.73796 0.90141 0.99441 0.99128] | 5.57e-29 | 0.000691 | 14 | Optimization terminated successfully. |
| BFGS | success | [1.0046 0.96493 0.92155 1.0036 0.91686 1.1574 0.7876 0.86786 0.99176 1.0185] | 3.53e-35 | 0.000766 | 15 | Optimization terminated successfully. |
| BFGS | success | [1.0659 1.0626 1.1176 1.0033 1.0369 0.86492 1.0281 0.97234 1.0094 0.89583] | 2.36e-26 | 0.000725 | 15 | Optimization terminated successfully. |
| dogleg | success | [1.0142 1.0592 1.0926 1.0197 1.0741 1.0479 0.96873 0.9765 1.1169 0.92747] | 3.61e-28 | 0.000214 | 3 | Optimization terminated successfully. |
| dogleg | success | [1.1278 0.88966 1.1561 0.74828 1.1364 1.1674 1.0134 0.90977 1.1447 1.048] | 5.86e-28 | 0.000165 | 3 | Optimization terminated successfully. |
| dogleg | success | [0.85662 0.97971 1.2498 1.0485 0.97916 0.87549 1.0149 0.96337 1.0274 0.98043] | 2.01e-28 | 0.000169 | 3 | Optimization terminated successfully. |
| trust-ncg | fail | [1.0675 0.97443 1.1123 0.97546 0.98034 0.99431 0.90397 1.0374 0.9498 1.0292] | 5.43 | 0.0479 | 2000 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [1.0632 1.1045 1.0242 1.023 1.0301 0.9006 1.1309 1.0967 0.88041 1.0682] | 6.97 | 0.0474 | 2000 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.94497 0.97987 1.0853 1.0857 1.2096 1.0924 1.031 0.93743 1.0479 1.0134] | 5.48 | 0.0473 | 2000 | Maximum number of iterations has been exceeded. |
