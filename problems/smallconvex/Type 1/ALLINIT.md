# ALLINIT

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Convex
- **Objective Type:** other
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [-0.17922 1 0.053737] | 16.705968432960997 | 0.00041487500129733235 | 13 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [-0.015633 1 0.088957] | 16.705968432884415 | 0.000298415994620882 | 12 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.035109 1 0.095279] | 16.705968432935027 | 0.00025533301231916994 | 12 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.0019684 1 -0.03315] | 31.642683773603135 | 8.954200893640518e-05 | 0 | Linear search failed |
| TNC | fail | [-0.041938 1 0.028791] | 25.985534146077928 | 0.00041312498797196895 | 1 | Linear search failed |
| TNC | fail | [0.13728 1 0.058719] | 26.683638398243016 | 0.0004266250034561381 | 1 | Linear search failed |
| Powell | success | [-0.020202 1 -0.004815] | 16.705991184029656 | 0.0067752910108538345 | 5 | Optimization terminated successfully. |
| Powell | success | [0.025338 1 -0.076732] | 16.70599069491546 | 0.006797417008783668 | 5 | Optimization terminated successfully. |
| Powell | success | [-0.31918 1 0.051766] | 16.705990960641632 | 0.006794250002712943 | 5 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.010122 1 -0.011765] | 18.006490058188092 | 0.0011517089878907427 | 85 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.19833 1 0.032506] | 18.00649003865346 | 0.001324291995842941 | 101 | Optimization terminated successfully. |
| Nelder-Mead | success | [-0.0083194 1 0.082528] | 18.006490047357072 | 0.001154291006969288 | 89 | Optimization terminated successfully. |
