# PFIT3LS

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.93804 -0.13585 1.1631] | 0.38339630894416715 | 0.0012210829881951213 | 72 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.1654 -0.023127 0.86894] | 0.3723915639907634 | 0.02495729200018104 | 1617 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.76111 -0.084164 1.067] | 8.605004610823262e-10 | 0.006391832997906022 | 411 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.9178 0.087376 1.146] | 39734.07955229674 | 8.308399992529303e-05 | 0 | Linear search failed |
| TNC | fail | [0.91879 -0.17691 1.0574] | 39734.07955229674 | 7.329200161620975e-05 | 1 | Unable to progress |
| TNC | fail | [0.89335 -0.22088 1.0902] | 39734.07955229674 | 7.108399586286396e-05 | 1 | Unable to progress |
| Powell | success | [0.76333 0.040191 0.98749] | 180.11710452905933 | 0.0030352499888977036 | 2 | Optimization terminated successfully. |
| Powell | fail | [1.0454 -0.0021275 1.0944] | 508.51196241829575 | 0.012443250001524575 | 4 | Maximum number of function evaluations has been exceeded. |
| Powell | success | [0.80659 0.03936 0.97756] | 180.73516687262605 | 0.0029660410073120147 | 2 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.83299 -0.15045 1.0521] | 7310.6663929985 | 0.004318000006605871 | 341 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.0472 -0.11156 1.1342] | 7299.836721214087 | 0.004291542005375959 | 343 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.1565 0.16235 0.91031] | 72.64226938941006 | 0.004287874995497987 | 343 | Maximum number of function evaluations has been exceeded. |
