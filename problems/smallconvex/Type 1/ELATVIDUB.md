# ELATVIDUB

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Convex
- **Objective Type:** sum of squares
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.4931 4.0225] | 26.975430973218977 | 0.00023600000713486224 | 10 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.3669 5.53] | 26.975430973215843 | 0.0002732919965637848 | 15 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [1.4845 5.0856] | 26.975430973273475 | 0.000251750010647811 | 13 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [0.38639 4.4374] | 54.751118642231134 | 0.00027150000096298754 | 8 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [0.84265 4.7358] | 1.7127803548623417 | 0.00023666700872126967 | 8 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [0.76147 5.8989] | 1.7127803548622045 | 0.00024529200163669884 | 9 | Converged (|f_n-f_(n-1)| ~= 0) |
| Powell | success | [1.755 4.5225] | 1.7127806566274482 | 0.0011251249961787835 | 5 | Optimization terminated successfully. |
| Powell | success | [0.94325 4.3587] | 54.75120153161242 | 0.0011092920030932873 | 5 | Optimization terminated successfully. |
| Powell | success | [1.6997 5.8574] | 54.75111864251212 | 0.0013801250024698675 | 6 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.3021 4.0821] | 54.7511186835538 | 0.0008709159883437678 | 59 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.2562 4.7413] | 54.751118668426805 | 0.0012124999921070412 | 81 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0358 5.0426] | 54.75111865816208 | 0.0007555830088676885 | 50 | Optimization terminated successfully. |
