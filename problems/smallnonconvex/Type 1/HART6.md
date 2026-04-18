# HART6

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
- **Objective Type:** other
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.24841 0.18973 0.3134 0.27109 0.13885 0.28584] | -3.3228868912294196 | 0.00027241697534918785 | 10 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.1333 0.24216 0.18795 0.11622 0.23296 0.11333] | -3.3228868915771224 | 0.0002842079848051071 | 14 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.17592 0 0.079168 0.1087 0.15218 0.082653] | -3.3228868915893126 | 0.00031629198929294944 | 15 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [0.15127 0.26113 0.1087 0.037414 0.18983 0.2116] | -3.322886891320845 | 0.00030516699189320207 | 7 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [0.12642 0.43247 0.015487 0.21526 0.15375 0.10156] | -3.3228868915893104 | 0.0004450420383363962 | 11 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [0.097562 0.32637 0.31477 0.14324 0.29122 0.025485] | -3.322886891587392 | 0.0002721250057220459 | 7 | Converged (|f_n-f_(n-1)| ~= 0) |
| Powell | success | [0.24389 0.020142 0.23601 0.13711 0.23955 0.28983] | -3.322886651717658 | 0.000972250010818243 | 3 | Optimization terminated successfully. |
| Powell | success | [0.26778 0.23856 0.31129 0.23142 0.2911 0.3356] | -3.3228867288912642 | 0.001000499993097037 | 3 | Optimization terminated successfully. |
| Powell | success | [0.2992 0.41721 0.23752 0.24815 0.07503 0.12573] | -3.204521667750213 | 0.00168599997414276 | 4 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.18011 0.28567 0.22619 0.062715 0.27636 0.17084] | -2.8412145241514626 | 0.0027619170141406357 | 230 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.23845 0.28502 0.31538 0.076259 0.34189 0.27162] | -3.322886766271996 | 0.003108792006969452 | 270 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.23649 0.12325 0.32636 0.26846 0.019193 0.28487] | -2.841214500815571 | 0.004735749971587211 | 416 | Optimization terminated successfully. |
