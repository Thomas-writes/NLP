# PALMER5A

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.2383 0.93674 1.1702 0.89838 0.87763 1.1392 1.0328 1.0203] | 0.07320742886348232 | 0.04143391700927168 | 2403 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.95369 1.3417 1.0916 1.039 1.0897 1.0092 1.1116 0.95139] | 0.06758298944629867 | 0.043365917008486576 | 2814 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0313 1.0451 0.92591 1.0997 0.9543 0.92356 1.0864 0.99281] | 0.07577250576370113 | 0.03572945800260641 | 2331 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.1027 0.7412 1.2365 0.91935 0.88771 0.83843 1.2124 0.88403] | 25232.344778515002 | 0.00043008300417568535 | 1 | Linear search failed |
| TNC | fail | [1.0981 0.96155 0.91893 1.0616 1.0137 1.1544 1.0443 0.99792] | 25434.727880853432 | 0.00042137500713579357 | 1 | Linear search failed |
| TNC | fail | [0.92249 1.1191 0.89155 1.0538 1.0696 1.0035 1.0163 1.0038] | 25644.294534321212 | 0.0004254160012351349 | 1 | Linear search failed |
| Powell | success | [1.1978 1.0736 1.0568 0.93582 0.87585 1.0289 0.89221 1.1177] | 124.72325862461989 | 0.006929416005732492 | 9 | Optimization terminated successfully. |
| Powell | success | [0.97611 1.0528 0.91541 0.87044 0.99931 0.73311 1.1388 0.92725] | 122.52506864689784 | 0.006997459000558592 | 9 | Optimization terminated successfully. |
| Powell | success | [0.98651 0.8582 1.108 0.94472 0.95706 0.97771 0.97596 1.2037] | 124.60995728100116 | 0.00663416700263042 | 9 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.91579 1.0641 1.0799 1.0186 1.0289 0.85644 1.2483 1.1176] | 5327.951587192469 | 0.012108333001378924 | 1088 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.99542 0.9278 0.8447 1.0363 0.99924 0.95655 0.90785 0.82332] | 4065.158311670857 | 0.012221832992509007 | 1073 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.1333 1.0279 0.98762 0.96965 1.0351 0.87876 0.75387 0.92314] | 3605.6522275283364 | 0.012102541993954219 | 1087 | Maximum number of function evaluations has been exceeded. |
