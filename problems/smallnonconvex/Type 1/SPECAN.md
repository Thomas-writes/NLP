# SPECAN

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
- **# of Variables (n):** 9
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [29.515 6.3 3.7 8.5333 2.2 2.6 10.75 1.7784 2.4848] | 4.0511867822712753e-10 | 0.045280416001332924 | 78 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [25.888 4.2191 2.7557 8.9428 3.3066 5.6831 9.7682 1.2 2.8] | 9.544900427830616e-09 | 0.03188241699535865 | 56 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [23.627 3.5 1.3964 8.3061 3.0865 6.2 12.92 1.2 1.3] | 6.038678441734995e-09 | 0.03705991599417757 | 65 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [25.44 4.2188 0.3 9.2645 4.74 4.7364 9.8167 1.2 2.8] | 3.5874259536757034e-10 | 0.03400979199795984 | 17 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [23.998 4.6053 2.2527 5 2.2 5.4538 11.004 1.2 2.8] | 3.133875490751222e-10 | 0.040894833000493236 | 18 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [23.867 3.5 3.1008 7.0653 2.2 2.6945 12.396 3.3 1.5604] | 1.216496226448412e-08 | 0.035550040993257426 | 14 | Converged (|f_n-f_(n-1)| ~= 0) |
| Powell | success | [29.225 5.0361 2.1091 5 5.3 4.8151 12.78 1.2 1.3] | 7.0350133593715115e-06 | 0.15552949999982957 | 17 | Optimization terminated successfully. |
| Powell | success | [26.121 6.3 1.7307 7.9118 5.3 4.0447 10.355 1.8393 2.1495] | 6.374462438633977e-06 | 0.14337304199580103 | 17 | Optimization terminated successfully. |
| Powell | success | [27.431 5.5319 0.3 5.6626 2.2 5.9351 12.369 3.3 1.3] | 6.282845469060057e-06 | 0.11643433400604408 | 14 | Optimization terminated successfully. |
| Nelder-Mead | success | [22.509 3.5 0.3 8.557 4.8123 3.522 8.6712 3.3 2.8] | 2.089936842592001e-05 | 0.15134825000131968 | 1049 | Optimization terminated successfully. |
| Nelder-Mead | fail | [30.289 4.9359 2.5885 6.9947 4.4136 2.6 9.6666 2.6638 2.8] | 0.0002894203982766963 | 0.17962758400244638 | 1266 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [21.398 3.5 2.7483 7.6119 2.5031 5.4762 9.0299 1.2499 1.3] | 6.678059803519181 | 0.1797122499992838 | 1267 | Maximum number of function evaluations has been exceeded. |
