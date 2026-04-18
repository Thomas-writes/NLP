# PALMER5A

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
| L-BFGS-B | success | [0.90686 1.0007 1.0656 1.0603 1.1274 1.1288 0.98275 1.0354] | 0.07713164831434002 | 0.033691124990582466 | 2236 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.1226 0.92187 0.91533 1.0583 1.0954 0.9126 1.0248 1.0691] | 0.3164062387902672 | 0.0020759589970111847 | 131 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.1095 1.0618 0.83663 1.084 0.94873 1.0476 1.0434 0.97939] | 0.07667298567439783 | 0.036652499984484166 | 2425 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.1623 1.0306 0.83038 1.2724 1.0675 1.0226 1.036 1.1553] | 25473.638399919597 | 0.0004189170431345701 | 1 | Linear search failed |
| TNC | fail | [1.0393 1.0706 0.92923 1.0935 0.98004 0.97876 0.87028 0.92622] | 25540.77259212075 | 0.0004219159600324929 | 1 | Linear search failed |
| TNC | fail | [0.97695 0.77582 0.86026 0.86763 1.0105 1.1053 0.99209 0.96633] | 25478.446191054514 | 0.00041274999966844916 | 1 | Linear search failed |
| Powell | success | [0.84315 0.97709 0.87798 0.82081 1.101 1.1241 0.94557 0.95229] | 126.47095382254895 | 0.006625874957535416 | 9 | Optimization terminated successfully. |
| Powell | success | [1.0472 1.0001 0.88627 0.94366 0.94713 1.0519 0.95313 0.93845] | 125.47793375697516 | 0.006674958043731749 | 9 | Optimization terminated successfully. |
| Powell | success | [1.1211 1.0491 0.98116 1.0705 0.89682 1.0788 0.93282 0.99895] | 125.36333454205624 | 0.006636334001086652 | 9 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.89947 1.0197 1.0527 1.1166 1.0064 0.92681 1.0502 0.87597] | 3451.9230508791256 | 0.012128874950576574 | 1076 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.99503 1.0361 0.95307 0.88955 0.98535 0.99914 0.96024 1.0289] | 5048.933813583754 | 0.011824292014352977 | 1087 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.89522 0.99802 1.0281 0.84589 0.98269 1.1024 1.0402 0.9015] | 3836.4557335141185 | 0.012099832994863391 | 1092 | Maximum number of function evaluations has been exceeded. |
