# PALMER5E

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
| L-BFGS-B | success | [24.727 0.81634 39.584 0.49217 7.5999 0.032337 13.181 2.1215] | 0.02499584370219065 | 0.03291533299488947 | 1534 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [24.049 -1.8734 41.76 -7.8271 0.39266 0.55043 9.2666 5.2288] | 0.02335149582864415 | 0.03914712503319606 | 2515 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [17.638 7.1237 42.355 -2.5025 2.7033 -0.11872 10.964 -1.3394] | 0.023804959796281815 | 0.0357509590103291 | 2359 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [17.123 -8.3121 40.875 7.4353 2.8702 -4.1173 11.871 8.2738] | 2416.3547875887957 | 0.00012375001097097993 | 0 | Linear search failed |
| TNC | success | [27.367 -8.9301 40.632 0.46359 6.866 -3.7384 8.4615 -2.8814] | 102.33573024463452 | 9.179103653877974e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | fail | [23.583 -4.6933 37.096 1.2705 2.2257 -0.58614 15.496 1.0067] | 1965.0421155247236 | 0.00010341696906834841 | 0 | Linear search failed |
| Powell | success | [13.688 -4.574 39.438 2.1035 2.8995 3.3863 16.972 -2.7444] | 5.880885358874374 | 0.008394042029976845 | 9 | Optimization terminated successfully. |
| Powell | success | [17.5 -0.98202 40.303 -2.5936 8.8718 -0.35738 8.7898 7.388] | 39.73418664126868 | 0.00900937500409782 | 8 | Optimization terminated successfully. |
| Powell | success | [13.561 -5.7657 44.063 -3.1352 2.1704 -0.1182 9.5146 6.5219] | 18.08052864687724 | 0.008944583008997142 | 8 | Optimization terminated successfully. |
| Nelder-Mead | fail | [19.601 -7.8351 44.909 -4.977 4.1736 4.094 8.1261 8.9847] | 0.3788910976601771 | 0.012370541982818395 | 1115 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [19.415 -1.4847 36.88 4.2865 8.4421 2.7541 19.616 3.2595] | 0.36541376760527583 | 0.012173082970548421 | 1096 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [21.191 2.1452 44.719 -2.6012 -2.2152 1.4061 9.5582 -4.8141] | 1.5121206713145903 | 0.011958457995206118 | 1083 | Maximum number of function evaluations has been exceeded. |
