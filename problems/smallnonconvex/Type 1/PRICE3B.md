# PRICE3B

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [-0.12186 5.5212] | 7.9545857494919595e-16 | 0.0003386670141480863 | 16 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [1.2195 5.121] | 2.492491523879072e-12 | 0.0002782499650493264 | 16 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.031 5.2423] | 7.115744866742359e-12 | 0.0002793330349959433 | 16 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [0.87185 5.5289] | 1.9220209937516634e-10 | 0.0002910839975811541 | 12 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [1.0105 5.1352] | 5.739255812182367e-12 | 0.00027895800303667784 | 12 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [-0.033221 5.3992] | 4.192870168288839e-15 | 0.00021716702030971646 | 10 | Converged (|f_n-f_(n-1)| ~= 0) |
| Powell | success | [0.59654 4.528] | 1.036705468950863e-14 | 0.0017297079903073609 | 8 | Optimization terminated successfully. |
| Powell | success | [0.92473 5.187] | 2.281441361763388e-09 | 0.0013727080076932907 | 7 | Optimization terminated successfully. |
| Powell | success | [-0.18195 5.0808] | 2.8340338833698157e-14 | 0.0017841669614426792 | 8 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.1804 4.9651] | 8.27375218704952e-08 | 0.0006972499541006982 | 51 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.73403 6.2967] | 8.998799479538786e-08 | 0.0006240829825401306 | 46 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.33266 4.6498] | 4.772870478097503e-08 | 0.000698584015481174 | 53 | Optimization terminated successfully. |
