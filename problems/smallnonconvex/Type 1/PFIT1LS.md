# PFIT1LS

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
| L-BFGS-B | success | [1.1501 -0.038128 0.99933] | 0.004445013172166339 | 0.0013979169889353216 | 79 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.134 0.017874 0.9274] | 8.656902541023135e-08 | 0.003535499970894307 | 231 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0941 -0.055618 0.97216] | 3.7688730872223728e-06 | 0.0006939999875612557 | 37 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.0035 -0.059647 0.8743] | 946.567900934321 | 8.087500464171171e-05 | 1 | Unable to progress |
| TNC | fail | [0.89306 0.10513 0.88839] | 946.567900934321 | 7.287500193342566e-05 | 0 | Linear search failed |
| TNC | fail | [1.119 -0.16565 0.86046] | 946.567900934321 | 7.00420350767672e-05 | 1 | Unable to progress |
| Powell | fail | [0.92861 -0.055671 1.0765] | 12.795051050556836 | 0.017442415992263705 | 4 | Maximum number of function evaluations has been exceeded. |
| Powell | success | [0.98871 0.063218 1.2169] | inf | 0.004444457998033613 | 3 | Optimization terminated successfully. |
| Powell | success | [1.0391 -0.11978 1.051] | 13.121436336992542 | 0.008334083016961813 | 4 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.0703 -0.0008032 1.0278] | 143.77242592002034 | 0.003975124971475452 | 341 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.1022 0.13924 1.0051] | 0.33974892352497543 | 0.004030500014778227 | 336 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.88401 -0.088506 1.0148] | 140.15822321855038 | 0.0040398340206593275 | 347 | Maximum number of function evaluations has been exceeded. |
