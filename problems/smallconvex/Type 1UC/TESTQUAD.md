# TESTQUAD

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
- **# of Variables (n):** 10
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.0606 0.93098 0.88285 0.85285 1.0053 1.0486 1.0538 0.99489 1.1133 1.1169] | 1.11e-18 | 0.00346 | 66 | Optimization terminated successfully. |
| CG | success | [0.88569 0.9939 1.1886 0.9665 0.90175 0.97003 0.93299 0.96033 1.0999 1.0529] | 9.31e-21 | 0.00624 | 165 | Optimization terminated successfully. |
| CG | success | [1.1387 1.1064 0.96859 1.0524 0.92023 1.0395 1.06 1.0053 0.87842 1.0092] | 7.26e-12 | 0.00765 | 207 | Optimization terminated successfully. |
| BFGS | success | [0.80852 1.0441 0.98843 1.0258 1.0147 1.0599 0.98583 1.2584 1.0343 1.0166] | 1.75e-45 | 0.000791 | 15 | Optimization terminated successfully. |
| BFGS | success | [0.89452 1.0812 0.99579 1.1898 1.1194 0.91784 1.0386 0.91276 1.1305 0.9481] | 7.97e-29 | 0.000704 | 14 | Optimization terminated successfully. |
| BFGS | success | [1.0413 1.0154 0.76778 1.2307 1.0015 1.0814 1.1821 1.1209 1.0594 1.0828] | 2.27e-20 | 0.000758 | 15 | Optimization terminated successfully. |
| dogleg | success | [0.95263 1.1671 1.0544 0.99416 1.0279 1.0827 1.0853 0.9763 0.87221 0.77024] | 3.41e-29 | 0.000199 | 3 | Optimization terminated successfully. |
| dogleg | success | [0.8937 1.1185 1.0299 1.0568 0.8922 1.009 0.955 0.92726 0.87811 0.94177] | 1.83e-28 | 0.000168 | 3 | Optimization terminated successfully. |
| dogleg | success | [0.91126 0.99186 0.91384 0.94546 1.1852 0.96187 1.0919 0.98853 1.0567 0.8425] | 1.83e-28 | 0.000171 | 3 | Optimization terminated successfully. |
| trust-ncg | fail | [1.0393 0.96624 0.96682 0.80156 1.0121 0.94863 1.0309 1.1112 1.1021 0.99879] | 5.45 | 0.0686 | 2000 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.95949 1.0349 0.96686 0.89389 1.0584 1.0624 0.99097 0.87355 0.97302 1.039] | 5.99 | 0.0532 | 2000 | Maximum number of iterations has been exceeded. |
| trust-ncg | fail | [0.97904 0.84138 1.0026 1.1854 0.9621 0.9822 0.95968 0.80212 0.97724 0.94412] | 4.22 | 0.0558 | 2000 | Maximum number of iterations has been exceeded. |
