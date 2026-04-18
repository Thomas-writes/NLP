# PALMER2A

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
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.87592 1.0453 0.98229 1.0366 0.92103 0.95728] | 0.0187231541803613 | 0.0010137499775737524 | 55 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.93391 0.93716 0.83115 1.0235 0.85642 0.9697] | 0.019757109903838298 | 0.001047917001415044 | 60 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0691 1.0829 1.0378 1.0187 0.96718 0.92243] | 0.017109717121016315 | 0.0020316250156611204 | 126 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.99739 1.0159 0.97835 0.89719 0.91384 1.2528] | 4305.768691079098 | 0.00044779200106859207 | 1 | Linear search failed |
| TNC | fail | [0.99336 0.95963 1.0603 0.90384 0.98483 0.94396] | 4167.839764282849 | 0.0004255829844623804 | 1 | Linear search failed |
| TNC | fail | [1.0494 1.0161 0.8783 0.96974 0.97023 1.0353] | 4099.494239313354 | 0.00042320898501202464 | 1 | Linear search failed |
| Powell | success | [0.87343 1.2058 0.98492 1.1951 1.0359 0.93429] | 503.75255798342357 | 0.006509916041977704 | 9 | Optimization terminated successfully. |
| Powell | success | [1.2176 0.888 0.94821 1.0538 0.9371 0.92246] | 851.8751667882896 | 0.005142292007803917 | 8 | Optimization terminated successfully. |
| Powell | success | [1.0275 0.96196 1.0065 1.0251 0.85051 1.1625] | 190.64327648845116 | 0.006853916973341256 | 11 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.77074 0.97556 0.85062 0.93587 1.0729 1.0222] | 0.0790330812642016 | 0.00897383299889043 | 773 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [1.1384 1.0895 0.91975 0.90926 0.93165 0.92884] | 0.017672865625557744 | 0.00720349996117875 | 630 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.98022 1.1517 1.0076 1.0974 0.94482 1.114] | 28.18712736001571 | 0.008929874980822206 | 780 | Maximum number of function evaluations has been exceeded. |
