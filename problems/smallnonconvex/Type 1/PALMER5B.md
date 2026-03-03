# PALMER5B

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
- **# of Variables (n):** 9
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.2692 1.1312 1.0968 0.9659 0.99615 1.1603 0.87544 0.94039 0.89846] | 0.13118478599217506 | 0.0021284160029608756 | 124 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.79155 0.95681 1.0443 0.90733 1.1314 0.93946 1.0412 0.82414 0.99587] | 0.07368452156325732 | 0.002499167007044889 | 158 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.85839 1.0633 0.96681 0.9596 1.057 1.0569 1.0374 0.89466 0.95332] | 0.07314731051190214 | 0.002776499997708015 | 176 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.8405 0.97219 1.2116 0.82133 1.0097 0.93552 0.9369 1.1057 1.0779] | 106195.68837423426 | 0.00048520800191909075 | 1 | Linear search failed |
| TNC | fail | [0.93044 1.0274 1.0767 1.0797 0.97421 1.2054 1.1418 1.0723 0.84552] | 157031.53230750634 | 0.00044333400728646666 | 1 | Linear search failed |
| TNC | fail | [1.028 1.268 0.91018 0.87012 0.89834 1.167 0.92643 1.0138 1.0316] | 115370.99708244142 | 0.0004268339980626479 | 1 | Linear search failed |
| Powell | success | [0.8903 0.99254 0.90935 1.1723 0.97895 0.95536 0.91622 1.0194 1.1181] | 247.9424693951883 | 0.028104249999159947 | 22 | Optimization terminated successfully. |
| Powell | success | [0.99881 1.1734 0.96696 1.0704 1.0246 0.93574 1.0946 0.90345 1.0806] | 4.429956494729728 | 0.026498084000195377 | 25 | Optimization terminated successfully. |
| Powell | success | [1.0484 0.95595 1.1268 0.83092 0.81353 0.99694 1.0194 0.83624 0.94509] | 50.95475790670607 | 0.02771641699655447 | 22 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.0592 1.1047 0.82929 0.97305 0.84152 0.99489 0.94475 0.99919 1.0522] | 315.86741568926806 | 0.013600582999060862 | 1205 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [0.91991 1.0457 0.97324 0.90367 1.1569 0.94296 1.0466 0.85772 1.0646] | 83.26730977148075 | 0.012470749992644414 | 1109 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.98068 1.0122 0.97931 1.0641 0.98804 0.88393 0.98299 0.85927 1.0259] | 680.4605193390853 | 0.013693250002688728 | 1230 | Maximum number of function evaluations has been exceeded. |
