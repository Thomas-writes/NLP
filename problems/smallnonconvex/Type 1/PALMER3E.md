# PALMER3E

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
| L-BFGS-B | success | [0.98867 1.1174 1.1 1.13 1.0257 0.98474 1.1806 1.0855] | 0.029951837398860013 | 0.000880667008459568 | 45 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.91018 1.0997 1.0646 0.93345 1.0859 1.0953 0.77939 0.90479] | 0.031064168891363726 | 0.0011861249804496765 | 69 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.98146 0.94966 1.0369 0.97473 1.0244 1.0195 1.0327 1.0161] | 0.029365565973956155 | 0.0007812089752405882 | 45 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [1.0443 0.88948 0.89335 0.90946 1.1818 0.94501 0.99966 0.95223] | 280.8277432825028 | 0.00010220799595117569 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [1.0223 0.93321 1.093 0.98435 1.0501 1.0947 0.97635 1.0662] | 325.05745264267085 | 9.479199070483446e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [1.0043 0.95665 0.83981 0.94926 0.99003 0.88635 1.0617 1.1175] | 276.35341258078313 | 8.608301868662238e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [1.1037 0.94252 1.0005 0.87263 0.9707 1.0622 0.85385 0.95047] | 0.957296085121066 | 0.013283042004331946 | 13 | Optimization terminated successfully. |
| Powell | success | [1.0632 1.0032 1.03 0.89581 1.087 0.83764 1.0147 0.973] | 0.8631418127325362 | 0.0123299999977462 | 13 | Optimization terminated successfully. |
| Powell | success | [1.1735 1.005 0.98903 1.1028 0.94406 0.97852 1.223 1.1423] | 0.9375215988069749 | 0.012586208991706371 | 13 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.1142 0.96533 1.0925 0.96836 1.1713 0.83594 1.0061 1.1706] | 0.03196075351439491 | 0.012644459027796984 | 1085 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.0687 1.0002 1.0143 0.89189 1.2187 1.1245 1.0164 0.98021] | 21.108393971354452 | 0.011988374986685812 | 1081 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.1033 1.1113 1.2495 1.0381 0.95844 1.0123 1.2068 1.0242] | 40.802747316830704 | 0.012311917031183839 | 1096 | Maximum number of function evaluations has been exceeded. |
