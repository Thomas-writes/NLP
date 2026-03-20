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
| CG | success | [0.93068 0.98991 1.14 0.85194 1.1657 0.87467 0.95706 0.89236 1.1432 0.87709] | 9.06e-11 | 0.00861 | 246 | Optimization terminated successfully. |
| CG | success | [0.98976 1.188 0.9816 1.1274 0.83939 0.88923 1.006 1.0529 0.92899 0.93723] | 3.75e-11 | 0.00564 | 165 | Optimization terminated successfully. |
| CG | success | [1.0421 0.97182 0.97226 0.87372 1.1105 0.84381 0.98236 0.96296 1.0942 1.0743] | 4.24e-20 | 0.000849 | 15 | Optimization terminated successfully. |
| BFGS | success | [0.98609 0.93447 1.0411 1.1684 0.85872 0.90431 0.91886 1.0522 1.1793 1.0314] | 9.67e-26 | 0.000763 | 15 | Optimization terminated successfully. |
| BFGS | success | [1.0829 0.84266 0.96241 1.0424 0.96071 1.0012 1.0426 0.96286 0.89742 0.81035] | 3.82e-16 | 0.00072 | 15 | Optimization terminated successfully. |
| BFGS | success | [0.98983 1.0638 0.85228 0.9951 1.0128 1.002 0.92724 1.0867 1.0782 0.92658] | 5.22e-40 | 0.000726 | 15 | Optimization terminated successfully. |
| dogleg | success | [1.1729 0.98466 0.97187 1.1601 0.92082 0.97055 0.9495 0.87291 0.92082 0.98625] | 7.62e-29 | 0.000203 | 3 | Optimization terminated successfully. |
| dogleg | success | [1.0028 1.0179 0.99099 1.1011 0.87024 0.79849 0.9849 0.96173 1.1088 0.99998] | 1.28e-28 | 0.000163 | 3 | Optimization terminated successfully. |
| dogleg | success | [1.1195 1.0756 0.9364 1.0953 0.99689 0.97644 0.94226 1.066 1.1241 1.0379] | 5.78e-28 | 0.000165 | 3 | Optimization terminated successfully. |
| trust-ncg | fail | [0.86392 1.064 1.0176 1.0681 0.86744 0.90295 1.018 1.1647 1.0059 1.1019] | 6.23 | 0.0507 | 2000 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.93196 1.0316 1.0013 1.0261 0.89742 0.92489 0.99088 1.0499 1.0078 1.1275] | 5.93 | 0.0492 | 2000 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.95349 0.91802 0.95053 1.0662 0.96655 0.98037 1.0364 0.91387 0.88942 1.0386] | 4.93 | 0.0504 | 2000 | Maximum number of iterations has been exceeded. |
