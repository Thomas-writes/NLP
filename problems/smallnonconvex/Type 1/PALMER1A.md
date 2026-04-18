# PALMER1A

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
| L-BFGS-B | success | [1.0115 0.93725 0.87855 0.99744 1.0163 1.1038] | 0.0898836334270582 | 0.0033852090127766132 | 205 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.93046 1.0316 1.0085 1.0517 1.0025 1.0197] | 0.08988363342944451 | 0.002911709016188979 | 173 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0548 1.1074 1.0656 1.1501 1.0639 1.008] | 0.08988363337733216 | 0.002928375033661723 | 179 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.0016 0.83647 1.2098 0.94359 0.97669 1.0585] | 49951.16068252834 | 0.0004671249771490693 | 1 | Linear search failed |
| TNC | fail | [1.1961 1.1195 0.95186 0.83539 1.0175 0.89562] | 53355.46524298198 | 0.00045137503184378147 | 1 | Linear search failed |
| TNC | fail | [0.92693 1.0135 1.0289 1.0634 1.1476 0.95644] | 48355.35959152159 | 0.0004541249945759773 | 1 | Linear search failed |
| Powell | success | [1.1028 0.93994 1.176 0.99277 1.173 0.97142] | 7693.389100471171 | 0.00879158399766311 | 11 | Optimization terminated successfully. |
| Powell | success | [1.0716 0.79995 0.90437 0.91472 1.0124 1.021] | 3034.167566522142 | 0.011750624980777502 | 17 | Optimization terminated successfully. |
| Powell | success | [1.0263 1.0001 1.0526 0.99969 1.0839 1.0508] | 19826.25815497129 | 0.006666707980912179 | 9 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0943 0.98322 0.95978 1.1069 0.82494 0.97949] | 0.3426812946197042 | 0.007890375040005893 | 663 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.80676 0.94006 0.88517 1.1293 0.83951 1.0645] | 524.4051075512675 | 0.008991833019535989 | 773 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.98466 1.0777 0.96519 1.0433 0.99093 1.0998] | 124.11652726827063 | 0.008964708016719669 | 783 | Maximum number of function evaluations has been exceeded. |
