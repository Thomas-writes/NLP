# SPECAN

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
- **# of Variables (n):** 9
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [22.71 3.5 3.7 7.0675 2.2 6.2 13.908 3.3 2.8] | 5.324899474337185e-09 | 0.03156170801958069 | 50 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [28.559 6.3 2.7098 10.074 4.0636 4.4171 10.528 3.3 1.3] | 6.508854638447136e-10 | 0.03676074999384582 | 64 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [25.726 6.3 3.7 9.702 5.1133 4.4552 10.167 1.3225 2.8] | 2.3594664852795964e-09 | 0.03984541702084243 | 72 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [17.154 6.3 3.7 7.9056 5.1706 3.3403 10.396 2.6267 1.3] | 9.962590161161704e-11 | 0.04875445901416242 | 24 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [23.858 3.9172 1.9253 6.7198 3.979 4.8978 13.747 1.6554 1.3] | 2.1349627977031026e-09 | 0.03751687495969236 | 18 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [27.662 6.1392 3.7 9.7401 2.2 4.0183 14 1.8848 2.8] | 6.394790659573186e-09 | 0.034933958027977496 | 16 | Converged (|f_n-f_(n-1)| ~= 0) |
| Powell | success | [26.983 5.0672 1.5365 5.3433 5.2068 6.2 12.83 1.2 1.3] | 3.0922624355391397e-07 | 0.2374717919738032 | 26 | Optimization terminated successfully. |
| Powell | success | [26.41 3.5286 3.7 7.2629 5.1352 2.7263 11.505 3.3 1.3] | 5.995432216669998e-06 | 0.17993470799410716 | 21 | Optimization terminated successfully. |
| Powell | success | [23.376 4.137 2.7365 9.5978 2.2 4.6082 10.757 3.0008 1.3] | 403.2756561569259 | 0.08566995902219787 | 7 | Optimization terminated successfully. |
| Nelder-Mead | fail | [24.636 3.5 0.3 7.5188 2.2 4.5712 9.4186 2.5961 2.8] | 0.0925184145225641 | 0.18485975003568456 | 1276 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [23.179 3.5 0.31115 6.5178 2.296 2.6 8.9909 3.3 1.3] | 1.4802682047941589 | 0.18486387497978285 | 1262 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [22.244 6.3 3.7 5 2.9389 5.1573 9.8265 3.3 2.6411] | 1721.9929486875717 | 0.1646956250187941 | 1114 | Optimization terminated successfully. |
