# PALMER2E

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
| L-BFGS-B | success | [1.1402 0.99606 0.98259 1.1305 0.96101 0.96711 0.86899 0.72324] | 0.026816683021689273 | 0.0015417089889524505 | 75 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0442 0.95862 1.1724 1.0359 1.0029 0.69897 1.0898 0.97724] | 0.030652466945917774 | 0.0009593750000931323 | 53 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0433 0.98846 0.92234 1.0673 0.96238 0.8666 1.1625 0.83619] | 0.030700639854025182 | 0.0007112080056685954 | 38 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [0.89396 0.96945 1.0172 1.1319 0.97051 0.9665 1.134 0.88092] | 1217.6940857500206 | 0.00010016700252890587 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.94125 0.75857 1.0469 0.98245 1.0547 0.93287 0.83406 1.1447] | 1883.039502836689 | 8.787499973550439e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [1.1572 0.90085 0.94388 0.96997 1.072 1.1676 0.76853 0.98962] | 5728.871363761236 | 8.770899148657918e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [0.81781 1.015 0.93939 0.99235 1.0168 0.86603 0.80665 1.0518] | 1.0749138547270167 | 0.012531791988294572 | 18 | Optimization terminated successfully. |
| Powell | success | [1.0478 0.8669 1.0799 1.0139 0.85088 0.97184 0.94773 0.78523] | 1.5254617976378462 | 0.025787541002500802 | 28 | Optimization terminated successfully. |
| Powell | fail | [0.98132 1.0631 1.0291 0.97617 1.1407 1.1149 0.76984 1.0141] | 1.7464007849792988 | 0.03527133299212437 | 32 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.97294 1.1048 0.99744 1.0487 1.0466 1.0121 1.0087 0.93586] | 37.695662859047985 | 0.012445999993360601 | 1088 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [1.0518 0.94192 0.94658 0.93442 0.9976 0.97896 1.1041 1.0114] | 0.9046197406217663 | 0.01115012499212753 | 963 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.1454 1.1695 0.90432 1.2008 0.97713 1.0194 1.0336 0.74748] | 20.17940575149533 | 0.012528207997092977 | 1105 | Maximum number of function evaluations has been exceeded. |
