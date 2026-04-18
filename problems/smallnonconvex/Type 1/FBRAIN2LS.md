# FBRAIN2LS

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [-4.2131 -0.10403 4.8204 0.047461] | 0.3683881757404004 | 0.012156333948951215 | 32 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [-3.9755 -0.35514 4.0618 0.36] | 0.36838817574108157 | 0.014017249981407076 | 40 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [-3.2592 -0.41428 3.8805 -0.1257] | 0.3683881757429378 | 0.014484250044915825 | 40 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [-3.8467 0.32936 4.6411 0.38161] | 0.36838817574057797 | 0.01678558299317956 | 17 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [-4.3163 -0.1877 4.3119 0.078137] | 0.3683881757427858 | 0.023214499989990145 | 21 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | fail | [-4.0664 -0.30747 3.6367 -0.56537] | 0.3683883677101865 | 0.029690583993215114 | 30 | Max. number of function evaluations reached |
| Powell | success | [-3.9236 0.080224 3.8196 -0.078684] | 5.012085419901146 | 0.04033049999270588 | 5 | Optimization terminated successfully. |
| Powell | success | [-4.1871 0.42616 4.3438 0.083801] | 3.103060278385198 | 0.04579050000756979 | 12 | Optimization terminated successfully. |
| Powell | success | [-4.2039 0.58881 3.7464 0.77825] | 0.6279239336531616 | 0.11635775002650917 | 25 | Optimization terminated successfully. |
| Nelder-Mead | fail | [-3.5835 0.51566 3.6663 0.38734] | 1.9025228243137589 | 0.0707711250288412 | 486 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [-3.8292 -0.55645 3.9342 -0.70184] | 0.4143048434304413 | 0.0707289160345681 | 484 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [-3.8207 -0.22282 4.1651 0.2364] | 0.41635506526232763 | 0.03198666695971042 | 212 | Optimization terminated successfully. |
