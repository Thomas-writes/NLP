# PALMER4C

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
| CG | fail | [0.9604 1.1934 1.1852 1.0067 1.193 1.0668 1.1034 0.97132] | 0.178 | 0.0783 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.96748 0.98828 0.81693 1.1027 1.1076 1.1451 0.99006 1.0104] | 0.0503 | 0.041 | 922 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [0.88447 0.972 0.98828 0.89874 1.0023 1.1186 1.0273 1.0441] | 0.373 | 0.0568 | 1600 | Maximum number of iterations has been exceeded. |
| BFGS | success | [1.1546 0.73104 0.99128 0.94165 0.98317 0.9147 0.95221 0.91651] | 0.0503 | 0.00144 | 49 | Optimization terminated successfully. |
| BFGS | success | [0.88027 0.97052 0.93445 0.9144 1.0462 1.051 0.86897 0.90532] | 0.0503 | 0.00159 | 52 | Optimization terminated successfully. |
| BFGS | success | [0.9831 0.89533 1.0892 0.81207 0.96644 0.89871 0.87181 1.0738] | 0.0503 | 0.00156 | 49 | Optimization terminated successfully. |
| dogleg | success | [0.88494 1.1517 0.92248 1.2083 0.85417 0.951 1.0989 1.0911] | 0.0503 | 0.000455 | 8 | Optimization terminated successfully. |
| dogleg | success | [1.0488 1.136 0.98472 0.87742 0.98341 1.0462 0.95274 1.0724] | 0.0503 | 0.000414 | 8 | Optimization terminated successfully. |
| dogleg | success | [0.90684 1.0836 1.0286 1.1144 1.1988 1.0354 0.99653 0.9429] | 0.0503 | 0.000408 | 8 | Optimization terminated successfully. |
