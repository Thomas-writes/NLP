# PALMER8C

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [0.98103 0.98182 1.052 0.99124 0.90416 1.1109 0.93861 0.89605] | 0.224 | 0.054 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.0972 1.0413 1.0553 1.1747 0.9211 1.1547 0.92708 1.0664] | 0.569 | 0.0606 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.0797 1.0436 0.88453 0.90315 0.93745 0.86674 1.0857 1.0826] | 0.552 | 0.0575 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [0.99813 1.2086 0.98502 0.88257 0.91045 0.93536 1.0517 0.91406] | 0.16 | 0.00149 | 51 | Optimization terminated successfully. |
| BFGS | success | [0.9146 1.0699 1.0464 1.0517 1.0676 1.0768 1.0236 1.013] | 0.16 | 0.00185 | 53 | Optimization terminated successfully. |
| BFGS | success | [1.1996 0.98107 1.1038 0.96414 0.94016 0.82754 0.98936 1.1022] | 0.16 | 0.00166 | 57 | Optimization terminated successfully. |
| dogleg | success | [1.0023 1.0797 1.0722 1.2343 0.89644 0.98684 0.94332 1.0637] | 0.16 | 0.000528 | 9 | Optimization terminated successfully. |
| dogleg | success | [0.98796 1.0095 0.97138 1.1206 1.0317 1.1284 0.93298 1.1389] | 0.16 | 0.000456 | 9 | Optimization terminated successfully. |
| dogleg | success | [0.99325 0.92036 0.85416 1.0578 0.98015 0.9073 1.045 1.1423] | 0.16 | 0.000436 | 9 | Optimization terminated successfully. |
| trust-ncg | fail | [0.96935 1.2443 0.97008 1.045 1.0907 1.0059 0.88903 0.80634] | 469 | 0.000763 | 34 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.71777 0.97277 1.0829 0.97058 1.1046 0.89963 1.1221 1.0404] | 1.8e+03 | 0.000169 | 4 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.1349 0.9831 1.046 0.88977 0.97035 0.94801 0.92013 0.86129] | 1.45e+03 | 0.000126 | 3 | A bad approximation caused failure to predict improvement. |
