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
| CG | fail | [0.95232 1.0803 1.0746 1.0176 1.0701 0.87273 0.73232 0.81879] | 0.301 | 0.0771 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.9179 1.0701 0.92836 0.87127 0.89698 1.1345 0.87746 1.09] | 0.307 | 0.0641 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [1.1478 1.1227 1.1775 1.1565 1.2832 0.99567 0.96508 1.0597] | 0.54 | 0.0647 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [1.1504 0.8587 1.0645 0.95207 0.94762 0.90755 1.0233 1.0769] | 0.16 | 0.00172 | 54 | Optimization terminated successfully. |
| BFGS | success | [0.80605 1.0959 1.2256 0.97229 0.88981 0.83311 0.79941 0.9751] | 0.16 | 0.00153 | 51 | Optimization terminated successfully. |
| BFGS | success | [1.0546 0.97382 1.0136 1.0292 1.0256 0.80723 0.88188 1.0014] | 0.16 | 0.00164 | 53 | Optimization terminated successfully. |
| dogleg | success | [0.90426 0.94195 1.0354 0.94726 0.91541 1.0937 0.91644 0.86851] | 0.16 | 0.000499 | 9 | Optimization terminated successfully. |
| dogleg | success | [0.92362 1.0167 1.0307 0.82692 0.99667 0.92185 1.3302 0.90575] | 0.16 | 0.000447 | 9 | Optimization terminated successfully. |
| dogleg | success | [0.99393 0.89285 0.99646 1.0693 1.0155 0.92162 0.87898 0.74985] | 0.16 | 0.000443 | 9 | Optimization terminated successfully. |
| trust-ncg | fail | [1.0328 1.2411 0.88153 1.1631 1.0746 0.97436 0.97363 1.0762] | 364 | 0.00021 | 5 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.9674 1.0709 1.1085 0.92731 0.82208 1.1091 1.0126 1.0491] | 546 | 0.000958 | 36 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.0124 1.0289 0.96682 1.0737 1.1468 0.97718 1.0855 0.92796] | 452 | 0.000809 | 34 | A bad approximation caused failure to predict improvement. |
