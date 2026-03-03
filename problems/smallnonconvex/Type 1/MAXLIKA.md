# MAXLIKA

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
- **Objective Type:** other
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.001 0.499 121.62 138.73 170 10.173 25 22.405] | 1136.307304784654 | 0.005300250006257556 | 129 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.28158 0.001 120.66 134.78 200.63 25 5 25] | 1136.3072969924497 | 0.0050712090014712885 | 120 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.499 0.499 101.24 139.6 170 5 23.403 25] | 1149.3463965576068 | 0.0017874580080388114 | 44 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [0.001 0.499 146.95 142.87 170 7.5711 25 21.494] | 1136.3072968973843 | 0.002422165998723358 | 20 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | fail | [0.499 0.499 115.88 152.78 188.62 25 5 8.6042] | 1136.371176753943 | 0.002523208997445181 | 20 | Max. number of function evaluations reached |
| TNC | fail | [0.001 0.001 100 130 171.62 5 25 5] | 1136.3079008998523 | 0.002409667009487748 | 21 | Max. number of function evaluations reached |
| Powell | success | [0.499 0.001 100 130 170 25 5 11.316] | 1138.711718355951 | 0.004639791994122788 | 4 | Optimization terminated successfully. |
| Powell | success | [0.499 0.499 100 130 189.78 25 25 8.7073] | 1136.7729518761173 | 0.004982250000466593 | 5 | Optimization terminated successfully. |
| Powell | success | [0.001 0.499 100 138.43 171.77 25 11.708 20.051] | 1137.4433010116397 | 0.00724537500354927 | 6 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.499 0.001 100 130 170 25 5 21.409] | 1140.331879420885 | 0.01967383398732636 | 1126 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [0.001 0.001 100 144.32 204.05 22.634 13.291 21.686] | 1168.883981013741 | 0.010667458001989871 | 579 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.499 0.001 100 130 206.8 5 19.75 5] | 1162.6657075125363 | 0.010552499996265396 | 583 | Optimization terminated successfully. |
