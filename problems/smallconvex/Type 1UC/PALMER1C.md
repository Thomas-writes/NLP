# PALMER1C

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
| CG | fail | [0.96421 1.0512 0.85221 1.0761 0.93181 0.87329 1.0699 1.0835] | 2.12 | 0.0893 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.0628 1.028 0.91102 1.2039 1.1108 1.0425 0.98077 1.0708] | 4.76 | 0.0965 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.96052 0.94696 0.86951 1.1269 0.87804 1.0735 1.0322 0.97914] | 65.3 | 0.0812 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [0.8308 1.0941 0.87461 0.95836 1.0103 1.2263 1.2032 0.91683] | 0.0976 | 0.00116 | 37 | Optimization terminated successfully. |
| BFGS | success | [0.89154 1.0986 1.0453 1.0777 1.0418 0.95672 0.93359 1.105] | 0.0976 | 0.00121 | 37 | Optimization terminated successfully. |
| BFGS | success | [1.0659 1.0386 1.1141 0.84114 1.1643 0.71943 1.0176 0.81769] | 0.0976 | 0.0014 | 37 | Optimization terminated successfully. |
| dogleg | success | [0.94991 0.96501 0.99104 0.84978 0.88193 0.96427 1.1006 1.1248] | 0.0976 | 0.0016 | 30 | Optimization terminated successfully. |
| dogleg | success | [1.2081 1.0626 1.0157 0.9018 0.93886 0.99133 0.84599 1.124] | 0.0976 | 0.00149 | 30 | Optimization terminated successfully. |
| dogleg | success | [1.0425 0.97903 1.0082 0.94611 0.96878 1.0191 0.84531 0.91755] | 0.0976 | 0.0015 | 30 | Optimization terminated successfully. |
| trust-ncg | fail | [0.76031 1.0294 0.8397 0.79543 1.0264 1.0255 1.0096 1.1398] | 1.57e+05 | 0.000321 | 9 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0922 1.0308 1.062 1.0819 0.89006 1.0633 1.2556 0.81902] | 2.23e+05 | 0.000231 | 7 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.84673 1.2042 1.0048 1.0002 0.91031 0.95103 1.0464 0.97045] | 1.63e+05 | 0.00122 | 33 | A bad approximation caused failure to predict improvement. |
