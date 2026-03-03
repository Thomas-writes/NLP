# PFIT4LS

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.99132 -0.05733 1.0475] | 8.534315720279773e-10 | 0.011081333999754861 | 718 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.149 -0.030444 1.1245] | 3.2778528242407334e-10 | 0.010673125012544915 | 705 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.9165 0.17408 1.0593] | 6.620213230005812e-09 | 0.0075158330000704154 | 486 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.99442 -0.055266 1.0382] | 113934.42809384977 | 8.516699017491192e-05 | 1 | Unable to progress |
| TNC | fail | [0.93782 -0.029585 1.0023] | 113934.42809384977 | 7.529200229328126e-05 | 1 | Unable to progress |
| TNC | fail | [1.1374 -0.1428 1.0063] | 113934.42809384977 | 7.095900946296751e-05 | 1 | Unable to progress |
| Powell | success | [0.87275 -0.10505 1.1188] | 5171.462220601192 | 0.013378124989685602 | 5 | Optimization terminated successfully. |
| Powell | success | [0.90024 -0.016699 1.1106] | 7514.693160310071 | 0.006386541994288564 | 3 | Optimization terminated successfully. |
| Powell | success | [0.96589 -0.037586 1.0308] | 7650.243263984916 | 0.006378749996656552 | 3 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.89747 0.026858 0.94083] | 283.0619829306916 | 0.004164167010458186 | 335 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.0424 0.056914 0.99753] | 71.39833808496616 | 0.004059958999278024 | 333 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.92709 0.11657 0.99385] | 98.01080873737244 | 0.004201500007184222 | 336 | Maximum number of function evaluations has been exceeded. |
