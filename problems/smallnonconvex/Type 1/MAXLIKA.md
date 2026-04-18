# MAXLIKA

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.499 0.001 107.19 130 170 12.513 19.57 11.493] | 1149.3177799922544 | 0.0014961250126361847 | 35 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.499 0.499 113.19 144.25 199.45 12.181 9.7171 5] | 1136.3074278618844 | 0.0032987080048769712 | 87 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.499 0.499 100 130 170 5 18.301 5] | 1149.3242100852872 | 0.0019572500023059547 | 53 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [0.499 0.001 112.85 145.36 170 6.234 5 25] | 1136.3072968980775 | 0.0024444159935228527 | 21 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [0.499 0.499 119.02 141.65 170 5 17.328 14.796] | 1136.3072968973784 | 0.0019225000287406147 | 17 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [0.001 0.001 100 167.32 170 25 6.9977 15.372] | 1149.345591564082 | 0.0017652499955147505 | 17 | Converged (|f_n-f_(n-1)| ~= 0) |
| Powell | success | [0.001 0.001 100 136.29 196.86 5 24.368 25] | 1136.329693299539 | 0.013119042036123574 | 10 | Optimization terminated successfully. |
| Powell | success | [0.001 0.001 102.45 136.31 170 5 25 25] | 1136.3707246944177 | 0.01103270798921585 | 11 | Optimization terminated successfully. |
| Powell | success | [0.499 0.001 114.42 140.22 174.86 5 5.7722 5] | 1138.7461328651411 | 0.006846583972219378 | 5 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.499 0.499 103.07 161.94 170 25 5 25] | 1137.3633452245049 | 0.018952791986521333 | 1097 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [0.499 0.499 100 130 172.29 9.5566 25 5] | 1148.0706478580764 | 0.014958582993131131 | 874 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.001 0.499 100 130 171.64 11.387 23.316 15.251] | 1137.1604979886313 | 0.017561000015120953 | 1008 | Optimization terminated successfully. |
