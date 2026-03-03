# OSLBQP

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
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [2.5 0.35664 0.55944 0.58509 0.5 0.47606 0.45988 0.47654] | 6.25 | 0.0005244579951977357 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [2.5 0.47305 0.49368 0.45704 0.56405 0.36062 0.46444 0.31366] | 6.25 | 0.00014362500223796815 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [2.5 0.42611 0.58852 0.54228 0.5 0.47474 0.50973 0.45139] | 6.25 | 0.00011504199937917292 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [2.5 0.38955 0.50813 0.50246 0.5 0.68141 0.53381 0.40661] | 6.25 | 0.00016941700596362352 | 1 | Local minimum reached (|pg| ~= 0) |
| TNC | success | [2.5 0.50614 0.36716 0.65966 0.50462 0.50993 0.5262 0.41482] | 6.25 | 0.00025683299463707954 | 2 | Local minimum reached (|pg| ~= 0) |
| TNC | success | [2.5 0.47565 0.44569 0.45009 0.58011 0.33743 0.42682 0.47653] | 6.25 | 0.00024574999406468123 | 2 | Local minimum reached (|pg| ~= 0) |
| Powell | success | [2.5 0.42151 0.59716 0.38864 0.5 0.40655 0.46554 0.65103] | 6.250336779296088 | 0.005768749993876554 | 2 | Optimization terminated successfully. |
| Powell | success | [2.5 0.3726 0.23399 0.70221 0.5 0.45866 0.33927 0.46552] | 6.250336779296088 | 0.005127790995175019 | 2 | Optimization terminated successfully. |
| Powell | success | [2.5 0.70136 0.4452 0.53237 0.55408 0.49044 0.63486 0.51485] | 6.250336779296088 | 0.005171374999918044 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [2.5 0.52165 0.54532 0.45692 0.5 0.57625 0.57731 0.47504] | 6.250000000480297 | 0.004845458999625407 | 412 | Optimization terminated successfully. |
| Nelder-Mead | success | [2.5 0.47702 0.55987 0.55677 0.5 0.57544 0.4981 0.44029] | 6.250000001731524 | 0.002911874995334074 | 232 | Optimization terminated successfully. |
| Nelder-Mead | success | [2.5 0.29914 0.50821 0.40701 0.5 0.41113 0.58927 0.55426] | 6.250000002076106 | 0.0042967920016963035 | 378 | Optimization terminated successfully. |
