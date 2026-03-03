# PALMER5E

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [26.618 -0.81267 46.684 2.1424 0.74728 -0.59233 14.84 7.8751] | 0.024551703804243773 | 0.0319526249950286 | 2066 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [17.493 1.3032 43.547 5.2692 6.4852 -3.9419 6.6183 -3.6593] | 0.023776904293531968 | 0.03182283299975097 | 2037 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [17.567 -6.6183 32.759 -2.8715 5.3769 0.13006 8.6019 5.7324] | 0.024161309180704024 | 0.03332087499438785 | 2154 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [15.051 -5.7999 39.848 -2.4062 -1.0497 10.05 12.01 -2.473] | 542.7598984193527 | 9.308301378041506e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | fail | [19.516 -8.7323 43.248 3.0539 -1.0379 -2.747 6.4036 5.2676] | 2691.4240666108294 | 0.00010616699000820518 | 0 | Linear search failed |
| TNC | fail | [24.038 0.046796 34.356 0.91287 7.3831 -7.4661 1.4366 9.4003] | 976.7182309635907 | 0.00010416700388304889 | 0 | Linear search failed |
| Powell | success | [19.994 -0.8766 40.464 -5.4882 3.4378 -8.56 5.8359 4.3008] | 5.427300127399782 | 0.004666125008952804 | 6 | Optimization terminated successfully. |
| Powell | success | [24.374 -13.083 43.246 4.2815 7.7779 1.8108 12.995 3.3793] | 75.2117443604236 | 0.006399708014214411 | 6 | Optimization terminated successfully. |
| Powell | success | [21.639 -4.9407 42.662 2.644 -6.1862 -5.8122 13.032 7.1107] | 3.564384821663361 | 0.005308042003889568 | 6 | Optimization terminated successfully. |
| Nelder-Mead | fail | [17.562 3.9076 41.37 4.1583 -3.3181 0.78728 9.3284 -1.3441] | 2.12914586125983 | 0.01254904200322926 | 1085 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [20.628 -0.57141 46.934 7.2768 5.2256 4.9539 5.4183 -3.3753] | 0.7491927092523314 | 0.011604041996179149 | 1031 | Optimization terminated successfully. |
| Nelder-Mead | fail | [19.401 2.2947 34.519 2.3864 6.1614 -1.6552 7.562 1.2044] | 1.65253636833232 | 0.012446667009498924 | 1113 | Maximum number of function evaluations has been exceeded. |
