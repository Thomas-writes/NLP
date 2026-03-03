# PALMER4B

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.87799 1.062 0.9651 1.0729] | 6.835138602015042 | 0.0006398340046871454 | 26 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.87785 0.9439 1.0509 1.0809] | 6.8351386067421425 | 0.0004233750078128651 | 16 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.1246 1.0533 1.0448 1.0948] | 6.835138602007319 | 0.0005307079991325736 | 24 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.99094 0.83695 0.74023 1.1485] | 12716.078348440595 | 0.00043470899981912225 | 1 | Linear search failed |
| TNC | fail | [1.1401 1.0847 1.0672 1.1081] | 11700.186060088985 | 0.0004224169970257208 | 1 | Linear search failed |
| TNC | fail | [0.96784 0.88648 1.2735 1.0488] | 12581.418002773331 | 0.00042795798799488693 | 1 | Linear search failed |
| Powell | success | [0.87248 1.0482 0.99508 0.90932] | 178.54104890096355 | 0.005632125001284294 | 12 | Optimization terminated successfully. |
| Powell | success | [1.1204 0.96424 0.89546 1.0259] | 861.2318530402544 | 0.006303083006059751 | 10 | Optimization terminated successfully. |
| Powell | success | [0.96485 0.93527 1.1665 0.96795] | 498.6583110576329 | 0.004633667005691677 | 7 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.92767 0.87591 0.95831 0.91877] | 302.4257177518621 | 0.0019509170087985694 | 155 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.73132 0.91625 0.97362 0.98768] | 321.04797057491993 | 0.0021437079994939268 | 158 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.0669 1.0797 0.88984 0.94708] | 315.583332311626 | 0.005800957995234057 | 488 | Maximum number of function evaluations has been exceeded. |
