# DIAGIQB

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
- **Objective Type:** quadratic
- **# of Variables (n):** 10
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.89691 1.0032 1.0582 0.84911 1.1644 0.91254 0.93301 0.94304 0.87967 1.0797] | -10149994100000.588 | 0.0003652090090326965 | 15 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.99816 0.84964 1.1815 0.98908 1.0129 1.0505 0.91379 1.156 0.944 1.0012] | -10149994100000.588 | 0.0003340410185046494 | 15 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.89516 1.1789 0.99268 1.1446 1.0785 0.82023 1.0587 1.0551 1.0632 0.9155] | -10149994099792.367 | 0.0002997079864144325 | 13 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [0.95661 1.0018 0.89529 1.0284 1.0749 0.98946 1.0173 1.017 0.96962 1.1384] | -10149994100000.586 | 0.000453916029073298 | 13 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [1.2408 0.89811 0.97481 0.96785 0.94289 0.98325 1.1344 0.83554 1.0985 1.0124] | -10149994100000.586 | 0.00036041700514033437 | 12 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [0.89398 1.136 1.0001 1.1155 0.92807 0.89476 1.0534 1.0401 0.98794 1.1303] | -10149994100000.59 | 0.0006605410017073154 | 13 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [1.0502 1.1733 0.78317 0.99704 0.83077 0.96623 1.0701 0.89883 1.0745 0.86278] | -10149994098716.797 | 0.003546583990100771 | 2 | Optimization terminated successfully. |
| Powell | success | [1.0945 1.0518 0.82586 0.86396 0.98128 1.0009 0.96644 0.85972 1.0521 1.1336] | -10149994098716.799 | 0.0034522920032031834 | 2 | Optimization terminated successfully. |
| Powell | success | [0.87594 1.1162 1.0304 0.97071 1.0436 0.94526 1.1237 1.0962 1.0321 1.1411] | -10149994098716.795 | 0.003446000046096742 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0869 0.94876 0.82533 1.128 0.92335 0.88207 1.1312 0.9945 1.1862 0.98485] | -9457495500000.0 | 0.003410833014640957 | 317 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.92466 0.98525 0.98028 1.222 1.0087 1.0537 1.1938 0.78089 0.8212 0.97773] | -8912994400000.0 | 0.0035260419826954603 | 336 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.1203 0.91779 0.89848 0.98064 0.96138 1.2875 1.1412 1.0002 1.1221 1.0321] | -8912995500000.0 | 0.0032785419607535005 | 312 | Optimization terminated successfully. |
