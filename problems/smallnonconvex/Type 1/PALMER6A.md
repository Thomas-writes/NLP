# PALMER6A

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
| L-BFGS-B | success | [1.1434 0.83114 1.0921 1.0505 0.91267 0.98099] | 0.06682190684183263 | 0.0012374999932944775 | 69 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.96836 0.98722 1.1183 1.0701 0.92743 0.91313] | 0.05594883926659244 | 0.0027872910141013563 | 179 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0346 1.0275 0.86594 0.90343 0.90643 1.1626] | 0.055948839815259485 | 0.002924000029452145 | 192 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.0947 0.89783 0.84041 1.0817 1.0612 1.0885] | 3655.5277018691017 | 0.00042220798786729574 | 1 | Linear search failed |
| TNC | fail | [0.84504 1.1685 0.92644 0.99743 0.97931 0.94446] | 3696.7692262160544 | 0.0004242919967509806 | 1 | Linear search failed |
| TNC | fail | [0.94915 1.0925 1.134 1.214 1.0085 1.0337] | 3108.3899366752366 | 0.00041329197119921446 | 1 | Linear search failed |
| Powell | success | [1.0628 1.1363 1.0826 0.87412 1.1319 1.0909] | 81.10373809841796 | 0.0053059590281918645 | 10 | Optimization terminated successfully. |
| Powell | success | [1.0329 0.99492 0.9898 0.89521 1.1826 0.92703] | 340.8864912778873 | 0.005848417000379413 | 8 | Optimization terminated successfully. |
| Powell | success | [0.97899 1.0016 1.1641 1.0806 0.94453 0.88368] | 126.46125892223833 | 0.011354624992236495 | 14 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.0969 0.78139 1.0537 0.99939 0.98246 0.98946] | 0.13011320157649725 | 0.008890917000826448 | 782 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [1.0803 0.98667 0.83602 0.85342 1.0102 1.1705] | 2.3881949587417504 | 0.004458207986317575 | 372 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.88416 1.0084 0.91677 0.95 1.0342 1.1503] | 0.8755348578918909 | 0.008904874965082854 | 789 | Maximum number of function evaluations has been exceeded. |
