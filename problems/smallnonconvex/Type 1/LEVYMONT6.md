# LEVYMONT6

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [-7.9464 7.6934 9.4626] | 12.502860200865932 | 0.00028204196132719517 | 8 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [-8.5405 7.7136 7.9428] | 9.36052596707678 | 0.00021104200277477503 | 10 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [-9.3933 7.247 7.4243] | 2.3107574971902297e-12 | 0.0005312500288709998 | 31 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [-9.4029 7.1793 8.7232] | 9.360525967578843 | 0.00024691695580258965 | 10 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [-8.3255 8.478 7.6802] | 2.8261916659233363e-18 | 0.00045958301052451134 | 25 | Local minimum reached (|pg| ~= 0) |
| TNC | success | [-7.5904 8.4832 8.22] | 12.502860201034135 | 0.0001858340110629797 | 9 | Converged (|f_n-f_(n-1)| ~= 0) |
| Powell | success | [-9.0894 7.8723 9.4675] | 3.1096420679608534 | 0.00041758298175409436 | 2 | Optimization terminated successfully. |
| Powell | success | [-9.3186 9.1446 7.2422] | 3.109642067960797 | 0.0004171250038780272 | 2 | Optimization terminated successfully. |
| Powell | success | [-8.1102 6.6181 8.6204] | 3.1096420679608534 | 0.0004059159546159208 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [-9.468 8.0741 7.4817] | 12.502860221786161 | 0.0008157499833032489 | 64 | Optimization terminated successfully. |
| Nelder-Mead | success | [-9.0886 5.9352 7.8641] | 18.347820695933468 | 0.0007180409738793969 | 58 | Optimization terminated successfully. |
| Nelder-Mead | success | [-8.3136 7.1925 8.3347] | 12.502860221940487 | 0.0009211249998770654 | 74 | Optimization terminated successfully. |
