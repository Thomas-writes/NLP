# MAKELA4

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
- **Objective Type:** linear
- **# of Variables (n):** 21
- **# of Constraints (m):** 40
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.1639 5.5774 3.1905 3.8766 4.8864 3.5428 5.257 9.2763 13.631 6.7015 -10.585 -11.857 -10.986 -14.191 -16.937 -12.136 -17.286 -16.099 -15.129 -19.711 4.8127] | 0.000328 | 0.268 | 262 | `gtol` termination condition is satisfied. |
| trust-constr | success | [2.2203 1.5079 3.1474 4.3136 5.1139 6.2706 6.4962 6.4665 7.625 10.83 -11.621 -11.53 -11.645 -14.614 -15.431 -15.037 -17.352 -17.44 -18.826 -17.395 2.5589] | 0.000355 | 0.235 | 238 | `gtol` termination condition is satisfied. |
| trust-constr | success | [0.91434 0.84295 6.536 1.9763 2.682 11.471 7.6529 7.9512 6.0245 9.5139 -11.767 -12.229 -12.046 -12.157 -15.091 -14.451 -18.939 -17.28 -15.474 -18.765 4.7488] | 0.000349 | 0.265 | 260 | `gtol` termination condition is satisfied. |
| SLSQP | success | [2.1533 6.7898 2.1133 0.44809 2.4654 6.0415 4.7886 8.11 6.5879 10.457 -10.399 -12.382 -16.428 -13.274 -13.108 -14.584 -18.139 -15.994 -18.092 -16.472 1.7101] | 3.02e-13 | 0.00472 | 18 | Optimization terminated successfully |
| SLSQP | success | [2.6593 -1.1858 3.5159 6.1468 1.7316 6.7746 7.3339 11.352 7.8798 8.5607 -15.378 -13.905 -10.809 -15.067 -17.101 -19.666 -16.609 -16.197 -18.312 -19.5 3.0021] | -6.83e-13 | 0.00508 | 19 | Optimization terminated successfully |
| SLSQP | success | [4.192 0.4404 4.8895 4.4649 5.5787 3.2854 6.1103 8.9742 10.866 5.2445 -11.411 -16.276 -14.691 -13.08 -18.484 -15.914 -19.2 -17.854 -16.9 -19.06 4.3252] | 1.15e-12 | 0.00498 | 19 | Optimization terminated successfully |
| COBYLA | success | [1.8468 3.5849 6.7475 3.7525 4.3407 5.0397 10.071 9.0546 8.5593 8.1937 -11.427 -9.8643 -16.984 -11.23 -12.705 -16.796 -15.257 -14.743 -17.384 -15.528 1.8707] | 1.57e-13 | 0.591 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [5.0766 -0.43438 1.3795 7.0458 4.2389 8.6751 9.2714 10.531 7.8929 9.0091 -12.924 -11.366 -11.788 -14.612 -13.708 -17.648 -16.882 -16.877 -19.888 -19.54 3.9059] | 5.55e-15 | 0.602 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [1.427 2.711 0.92136 4.8988 5.0179 5.4797 7.7934 7.5372 7.1332 8.7819 -10.69 -6.4774 -15.594 -15.071 -14.525 -14.454 -16.675 -17.496 -17.751 -18.732 4.1012] | 2.19e-13 | 0.604 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
