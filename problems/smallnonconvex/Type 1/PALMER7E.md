# PALMER7E

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
| L-BFGS-B | success | [1.1817 0.92148 0.93754 0.89326 0.79104 1.1894 1.08 0.86629] | 10.153971151260995 | 0.009405541990417987 | 609 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.1655 1.0758 0.90912 0.94808 0.92985 1.0447 1.0905 1.1754] | 10.153927954236167 | 0.010549374972470105 | 698 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.93869 0.80717 1.0619 0.92504 1.127 0.87791 1.1516 1.1165] | 10.153928064942892 | 0.014690332987811416 | 971 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [0.87091 1.1013 0.87476 1.0628 0.90974 1.0085 0.94834 0.95057] | 93.63392580176264 | 9.470799705013633e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.97676 0.80999 0.93527 1.2341 1.0979 1.0131 0.91385 0.89998] | 91.52735761256004 | 8.770800195634365e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.91421 1.0047 0.91726 0.66284 1.0676 0.92709 1.0546 1.1626] | 102.39151646938674 | 8.520903065800667e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [1.0684 0.99883 1.0478 1.0314 1.0893 0.914 0.98031 0.91272] | 11.748858591342001 | 0.015984041034244 | 20 | Optimization terminated successfully. |
| Powell | success | [1.0529 1.0155 0.97342 1.1163 1.0528 0.95389 0.97532 0.84388] | 15.166023941172979 | 0.017070917005185038 | 20 | Optimization terminated successfully. |
| Powell | success | [0.76632 1.1412 1.0066 0.95693 1.0102 0.9991 1.0425 1.0904] | 14.795380725698001 | 0.01671458297641948 | 20 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.1469 1.0376 0.93151 0.96273 1.0691 1.0024 0.90527 0.88603] | 22.137512103951263 | 0.012217291980050504 | 1077 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.0172 0.83813 1.1096 1.1043 0.94884 0.96202 0.99233 0.96614] | 15.982041024901644 | 0.012192249996587634 | 1104 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.0202 1.0153 1.1706 0.91373 0.88903 1.1948 1.3017 1.0915] | 21.460417638334505 | 0.012049166951328516 | 1090 | Maximum number of function evaluations has been exceeded. |
