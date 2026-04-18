# PALMER1E

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
| L-BFGS-B | success | [0.92915 0.94633 0.81484 0.93972 0.93428 0.94237 1.1135 0.84559] | 0.5048895365940759 | 0.001188291993457824 | 60 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.97619 0.7708 1.1016 1.1497 0.96662 0.99107 1.1912 0.91014] | 0.11134157210871065 | 0.0028592090238817036 | 160 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0349 1.0722 1.0142 1.0836 0.98778 1.0668 1.0048 1.0103] | 0.10565265858350495 | 0.003218041965737939 | 181 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [1.0696 0.9924 0.90368 0.96715 0.92492 0.9055 1.0476 1.0152] | 37052.53732596351 | 0.00013995799235999584 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.94233 1.0075 0.84746 0.89947 0.98658 0.94553 0.96779 0.96187] | 37266.47269636113 | 0.00010283297160640359 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.91902 0.97527 0.88298 1.0726 0.84059 1.0733 1.0572 1.1287] | 37089.468457612944 | 9.741599205881357e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [0.94889 1.0191 1.1229 1.1017 0.9665 0.90704 1.0346 0.86553] | 22066.650966245645 | 0.006016500003170222 | 5 | Optimization terminated successfully. |
| Powell | success | [0.81497 0.94384 0.97766 1.0405 0.92085 1.0337 1.1564 1.1431] | 21996.082702325544 | 0.0059552909806370735 | 5 | Optimization terminated successfully. |
| Powell | success | [1.0361 0.96219 1.1026 0.99391 1.1315 0.89942 0.89136 0.82072] | 22289.80493118683 | 0.005887540988624096 | 5 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.1259 0.90846 0.94087 1.0509 1.0223 0.90634 0.98567 1.0457] | 23.677976688129863 | 0.01066304201958701 | 903 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.87902 1.0382 0.90274 1.0698 1.0492 1.1232 1.0481 1.0357] | 5287.996397073761 | 0.01239870797144249 | 1068 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.1806 0.77938 1.0268 1.0166 0.89015 0.98432 0.89786 1.0255] | 342.9225324152222 | 0.01229391701053828 | 1075 | Maximum number of function evaluations has been exceeded. |
