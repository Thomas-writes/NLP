# TRIGON1B

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
- **# of Variables (n):** 10
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0 0.10918 0.073208 0.15627 0.069703 0.16067 0.0053489 0.014302 0.27425 0.06052] | 8.796179405156061e-13 | 0.00041458301711827517 | 17 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.13312 0.095453 0 0.0046295 0.13298 0.11786 0 0.042865 0 0] | 2.1111166210606955e-10 | 0.0003129590186290443 | 15 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.11772 0.10839 0.20513 0 0.056485 0 0.018286 0.045717 0.31549 0.15089] | 0.0 | 0.00037466600770130754 | 20 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [0.054986 0.14433 0.088842 0.14678 0.14758 0.041593 0.21043 0.088029 0.0012562 0.035964] | 3.8000422396412087e-22 | 0.00029079202795401216 | 9 | Local minimum reached (|pg| ~= 0) |
| TNC | success | [0.1919 0.0057121 0.29053 0 0.18387 0 0.092062 0.035311 0.014971 0.076414] | 0.0 | 0.00035620899870991707 | 10 | Local minimum reached (|pg| ~= 0) |
| TNC | success | [0 0.12196 0.16645 0.015844 0.15852 0.35165 0.071566 0 0.023752 0.017733] | 1.0261031310724052e-24 | 0.0002815419575199485 | 9 | Local minimum reached (|pg| ~= 0) |
| Powell | success | [0 0.12411 0.084068 0 0.023981 0.17946 0.15095 0 0.044897 0.086406] | 9.253322826335276 | 0.0007418750319629908 | 1 | Optimization terminated successfully. |
| Powell | success | [0.08348 0.072272 0.11137 0.07186 0.056938 0.36052 0.19496 0.20352 0.13095 0.090642] | 9.304547435013738 | 0.0013527090195566416 | 2 | Optimization terminated successfully. |
| Powell | success | [0.13463 0.10317 0.24791 0.028373 0.23393 0.26128 0.0073359 0.11221 0.26908 0.19094] | 9.214800164242407 | 0.0014409160357899964 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.10036 0.053646 0 0.075897 0.16185 0.12726 0.15312 0.03821 0.11083 0.015551] | 2.6340878357382544e-06 | 0.012494499969761819 | 1150 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.12254 0.027624 0.13864 0.13982 0.11819 0.050701 0.24732 0.15242 0 0.0064247] | 0.04269309275761931 | 0.015535750018898398 | 1426 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [0 0.28195 0.20348 0 0 0 0.25962 0.14685 0.056043 0.1886] | 1.2454304010556847e-05 | 0.0074728750041686 | 694 | Optimization terminated successfully. |
