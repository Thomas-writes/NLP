# HS2

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
- **Objective Type:** sum of squares
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [-1.9616 1.5] | 0.05042618789360708 | 0.0029344170034164563 | 13 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [-1.8812 1.5] | 0.05042618789363516 | 0.00023174998932518065 | 6 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [-2.0188 1.5] | 0.050426187893607075 | 0.0002997919946210459 | 14 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | fail | [-2.1931 1.5] | 326.1156556073407 | 0.0004126249987166375 | 1 | Linear search failed |
| TNC | fail | [-2.1003 1.5] | 284.35043098726777 | 0.00040241699025500566 | 1 | Linear search failed |
| TNC | fail | [-1.7751 1.5] | 132.44421043801825 | 0.000396332994569093 | 1 | Linear search failed |
| Powell | success | [-1.9286 1.5] | 0.05043667166954254 | 0.0012932919926242903 | 2 | Optimization terminated successfully. |
| Powell | success | [-2.0214 1.5] | 0.050436671669542535 | 0.0012374169891700149 | 2 | Optimization terminated successfully. |
| Powell | success | [-1.7629 1.5] | 0.050436671669542514 | 0.0012975839927094057 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [-1.7971 1.5] | 4.941229488130307 | 0.0006707499996991828 | 49 | Optimization terminated successfully. |
| Nelder-Mead | success | [-1.9792 1.5] | 4.941232536901648 | 0.0006029170035617426 | 45 | Optimization terminated successfully. |
| Nelder-Mead | success | [-1.6746 1.5] | 4.9412300045013255 | 0.0006068329967092723 | 41 | Optimization terminated successfully. |
