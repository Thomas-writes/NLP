# PALMER3A

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
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.0946 1.0905 1.0193 1.0289 1.0607 0.97348] | 0.025622978895692462 | 0.0009665420075180009 | 51 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0008 1.0031 1.06 0.89473 0.96628 1.1038] | 0.021968750118742355 | 0.001190708004287444 | 65 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0093 1.0309 0.97594 1.0091 1.0073 1.0479] | 0.02436268133780075 | 0.0010195829963777214 | 54 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.89046 1.0001 0.95998 1.1241 1.1341 0.83157] | 3721.21618376707 | 0.00044358300510793924 | 1 | Linear search failed |
| TNC | fail | [0.9391 1.0899 1.2172 1.1009 0.88934 1.0666] | 3306.6877652029675 | 0.0004402089980430901 | 1 | Linear search failed |
| TNC | fail | [1.0513 0.96512 1.1511 1.0436 1.1273 0.96022] | 3714.999554577739 | 0.00043737499800045043 | 1 | Linear search failed |
| Powell | success | [1.0108 0.92687 1.0649 1.009 0.90644 0.92519] | 434.82814194656646 | 0.00519245900795795 | 7 | Optimization terminated successfully. |
| Powell | success | [1.1162 0.76024 0.99594 1.1427 1.1472 1.2078] | 405.38148114561204 | 0.0060632080130744725 | 8 | Optimization terminated successfully. |
| Powell | success | [1.097 0.98821 1.1174 1.1142 1.1108 1.0571] | 141.34030977344503 | 0.008818624992272817 | 11 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.93497 0.95147 0.96487 0.90274 1.06 0.88595] | 15.410076947846438 | 0.009259875005227514 | 788 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.91863 0.89752 1.2445 0.86768 0.88035 1.118] | 0.03267061656854236 | 0.008916874998249114 | 774 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.0039 0.98806 0.95108 1.0467 1.309 1.0586] | 4.212240066752445 | 0.008978166006272659 | 766 | Maximum number of function evaluations has been exceeded. |
