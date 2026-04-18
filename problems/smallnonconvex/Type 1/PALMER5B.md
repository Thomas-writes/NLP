# PALMER5B

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
- **# of Variables (n):** 9
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.90906 1.013 0.98296 0.9613 1.0683 1.114 0.88449 1.1042 0.99794] | 0.07355715813334468 | 0.002333166019525379 | 147 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0844 0.81609 1.0443 0.99565 0.85358 0.91249 0.90638 0.70875 1.0288] | 0.07412085937305427 | 0.002145208010915667 | 137 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0443 1.0316 0.97851 0.76721 0.97773 0.83764 0.98687 0.99987 0.96902] | 0.07318495668865954 | 0.002759292023256421 | 172 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.1343 1.0776 1.0206 0.93808 1.0414 0.97623 0.99378 0.95021 0.98499] | 118167.54911253724 | 0.0004272499936632812 | 1 | Linear search failed |
| TNC | fail | [0.95607 1.1189 1.0287 1.03 0.96634 0.85478 1.0189 1.0393 0.88024] | 113592.47062862627 | 0.00041320803575217724 | 1 | Linear search failed |
| TNC | fail | [0.95938 1.1536 1.1313 1.1096 0.93211 1.0048 0.84768 1.0217 1.1124] | 99191.25866822404 | 0.0004163749981671572 | 1 | Linear search failed |
| Powell | success | [0.78449 1.0707 1.0684 0.92936 0.96623 0.94054 1.04 0.90195 1.0387] | 97.08007692299374 | 0.022522374987602234 | 19 | Optimization terminated successfully. |
| Powell | success | [0.9998 1.0902 1.0098 0.88928 1.0486 1.0008 0.83968 1.0447 1.0165] | 121.49070588902364 | 0.03119712503394112 | 22 | Optimization terminated successfully. |
| Powell | success | [0.94058 0.97766 1.1453 1.1368 1.0287 0.95754 0.99355 0.93056 1.0431] | 340.1565062212597 | 0.01767475000815466 | 17 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.2149 0.98494 1.0526 1.0242 1.0146 1.0607 0.99143 1.0145 0.83497] | 938.7588278471213 | 0.01368608302436769 | 1206 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.72785 1.0329 0.96988 0.96031 0.91863 0.95254 1.2174 0.89409 0.90169] | 9.084626017894896 | 0.01359958399552852 | 1240 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [1.064 1.1072 0.87543 1.1438 1.0039 1.0191 1.0085 1.0869 1.0236] | 47.40985024951723 | 0.0131150420056656 | 1181 | Optimization terminated successfully. |
