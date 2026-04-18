# PALMER6E

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
| L-BFGS-B | success | [0.88363 1.0056 1.0299 1.0084 1.0087 0.91789 1.0083 1.235] | 0.0264001045015071 | 0.0016743330052122474 | 102 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0395 0.93644 0.96578 0.83077 1.0525 1.15 1.0892 0.97499] | 0.02645175374754148 | 0.0021634160075336695 | 138 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0502 1.2119 0.73672 0.88813 1.1336 1.1849 1.0456 0.87071] | 0.026272283661888038 | 0.0019664160208776593 | 112 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [0.99223 0.85838 1.1683 0.94874 0.92459 0.94431 1.0905 1.0022] | 211.9210087533262 | 9.462499292567372e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.93969 1.0061 0.86455 1.0764 0.97695 1.0659 0.94577 0.88274] | 208.70760753350567 | 8.633302059024572e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.92834 0.92326 0.95937 1.0099 1.0354 0.96099 1.0239 1.1484] | 211.4896144220574 | 8.416699711233377e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [1.1178 1.0091 1.0536 0.97261 1.0464 0.98537 1.1112 0.85417] | 57.46370247978736 | 0.019154708017595112 | 18 | Optimization terminated successfully. |
| Powell | success | [0.96321 0.9501 0.91101 1.2403 0.87626 1.0026 1.0612 1.0401] | 57.415482061463244 | 0.01898804196389392 | 18 | Optimization terminated successfully. |
| Powell | success | [0.99822 1.0467 1.003 1.0096 0.91714 1.0379 0.92444 0.98891] | 57.69533199408014 | 0.019025999994482845 | 18 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.0881 0.95141 0.92639 0.98903 0.96673 1.0244 1.1571 1.1813] | 0.06488732338694965 | 0.012593791005201638 | 1099 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [0.88273 1.0786 0.90871 0.98235 0.94586 0.96671 1.002 1.0705] | 0.35267922436637816 | 0.009024082974065095 | 795 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.9598 1.0227 1.1317 1.0302 1.0952 1.1498 1.0872 1.0314] | 0.08046892833635212 | 0.011995124979875982 | 1095 | Maximum number of function evaluations has been exceeded. |
