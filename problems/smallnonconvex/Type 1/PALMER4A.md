# PALMER4A

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
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.91489 1.111 0.881 1.4606 1.0551 1.1348] | 0.04060613955780311 | 0.0017255410202778876 | 100 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.17 1.0049 0.9019 1.0615 0.97043 1.0352] | 0.041617193872931696 | 0.0009908330393955112 | 57 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.98929 1.0756 0.9748 0.99866 0.86825 1.0181] | 0.04060614033893988 | 0.001850707980338484 | 102 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.0163 1.0246 1.0065 0.94126 1.1426 0.89232] | 5179.397899372742 | 0.0004460419877432287 | 1 | Linear search failed |
| TNC | fail | [1.0893 1.0634 1.0996 1.1493 1.0129 0.93755] | 3904.359594313638 | 0.0004236250533722341 | 1 | Linear search failed |
| TNC | fail | [0.92542 0.91835 0.99957 1.2549 0.88265 0.81337] | 3765.682015276305 | 0.00042462500277906656 | 1 | Linear search failed |
| Powell | success | [1.1295 0.99864 0.96819 0.94673 0.86342 1.0431] | 399.75012983563073 | 0.00704029097687453 | 9 | Optimization terminated successfully. |
| Powell | success | [1.007 1.1738 0.90471 1.1106 0.94493 0.95441] | 141.35647048641573 | 0.010543040989432484 | 16 | Optimization terminated successfully. |
| Powell | success | [0.96654 0.96308 1.1704 0.94033 0.9389 0.91868] | 6.890344418283565 | 0.012205625011119992 | 16 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.1384 0.88227 1.0677 0.97928 0.87978 1.0799] | 45.0284158527434 | 0.008960999955888838 | 777 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.0787 1.1301 1.0892 1.0182 0.94909 1.2026] | 0.15036667047887783 | 0.008900874992832541 | 780 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [1.0964 1.1113 0.88433 0.96874 0.96778 0.97194] | 0.08073807819987112 | 0.00561116699827835 | 476 | Optimization terminated successfully. |
