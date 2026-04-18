# YFIT

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
| L-BFGS-B | success | [-0.91791 -1.3182 18.684] | 6.782859136595265e-13 | 0.0012840420240536332 | 77 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [2.8929 -2.0916 16.679] | 4282.251321982173 | 0.0007700840360485017 | 36 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [-0.14704 1.1187 25.087] | 7.159782849468789e-13 | 0.0012083749752491713 | 74 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.16573 -2.8187 21.027] | 5975.71650337632 | 0.00026245799381285906 | 0 | Linear search failed |
| TNC | fail | [1.5592 -2.2913 24.087] | 5975.71650337632 | 0.00025099999038502574 | 0 | Linear search failed |
| TNC | fail | [-0.023053 -2.6574 17.492] | 5975.71650337632 | 0.0002531249774619937 | 0 | Linear search failed |
| Powell | success | [-0.25096 -3.392 19.693] | 16867.68876123445 | 0.001420666987542063 | 2 | Optimization terminated successfully. |
| Powell | success | [-0.30011 -1.7616 20.181] | 12470.014025394445 | 0.0022827089997008443 | 4 | Optimization terminated successfully. |
| Powell | success | [-1.8294 -1.6601 19.631] | 22293.9581732879 | 0.0024121669703163207 | 3 | Optimization terminated successfully. |
| Nelder-Mead | success | [-1.4085 -1.4608 20.235] | 7.701669920996933e-13 | 0.0039512080256827176 | 325 | Optimization terminated successfully. |
| Nelder-Mead | success | [2.3156 1.1223 18.424] | 4541.721738738798 | 0.0016750419745221734 | 131 | Optimization terminated successfully. |
| Nelder-Mead | success | [2.8078 -2.7365 23.984] | 5975.71650337632 | 0.0006501249736174941 | 38 | Optimization terminated successfully. |
