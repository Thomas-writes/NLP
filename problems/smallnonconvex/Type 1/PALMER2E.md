# PALMER2E

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-25

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.1393 0.88877 1.0081 1.1241 0.99563 1.0558 1.016 0.97751] | 0.026825163856470182 | 0.0014340829802677035 | 83 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.1152 0.95677 1.1176 1.0385 0.75492 0.96192 1.0108 1.098] | 0.03148318487779054 | 0.0008274170104414225 | 45 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0567 1.0758 1.0912 0.89548 1.2111 1.0325 0.98954 1.0932] | 0.029964939293787685 | 0.0008275000145658851 | 45 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [0.96193 0.78452 1.0463 0.98264 1.0111 0.96017 1.0993 0.91946] | 1176.9613403076753 | 9.758298983797431e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.98513 0.88143 0.84562 1.1097 1.1598 0.87979 0.93781 1.0394] | 1254.4868584875123 | 9.133398998528719e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.91463 0.93534 0.88483 0.83161 1.0902 1.0012 0.85426 0.92585] | 2650.3116330194694 | 8.954200893640518e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [1.0951 0.99292 0.88336 0.96867 1.0344 0.93808 0.9931 0.90571] | 1.2961418549140347 | 0.015943208010867238 | 22 | Optimization terminated successfully. |
| Powell | success | [1.0744 1.1808 1.0896 1.0171 0.92217 1.1065 1.1606 1.047] | 2.676210613718636 | 0.02224349998869002 | 25 | Optimization terminated successfully. |
| Powell | success | [0.90936 1.1654 0.90487 0.93877 0.86269 0.83158 0.96412 1.0336] | 1.0337238757006966 | 0.011749458033591509 | 18 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.87669 1.0374 0.9387 0.91973 0.90903 0.9268 0.95545 0.9869] | 0.7937823254049136 | 0.011369667015969753 | 967 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.99664 0.97151 1.1267 0.95509 0.93098 0.93061 1.0079 0.97294] | 0.2890429397973475 | 0.012306000047829002 | 1078 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.95331 0.95124 1.0688 0.8333 0.70391 1.132 0.89269 1.0503] | 12.374210936653922 | 0.01234512502560392 | 1068 | Maximum number of function evaluations has been exceeded. |
