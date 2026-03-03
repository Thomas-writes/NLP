# HS3

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
- **Objective Type:** quadratic
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [9.9448 2.0552] | 6.864722005638483e-38 | 0.0001665419986238703 | 4 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [11.41 1.4567] | 6.129683352668918e-08 | 0.00012091700045857579 | 3 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [8.6727 0] | 4.0038889900321244e-29 | 0.00010541599476709962 | 2 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [8.994 0.60233] | 3.6279712716164125e-06 | 8.850000449456275e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [9.9285 0.20624] | 4.253433018296716e-07 | 7.483300578314811e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [10.211 0.84484] | 7.137592170688258e-06 | 7.312500383704901e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [9.5904 0.45543] | 1.737735166232911e-15 | 0.006142041995190084 | 6 | Optimization terminated successfully. |
| Powell | success | [10.339 0] | 5.720496589314726e-05 | 0.0010661249980330467 | 2 | Optimization terminated successfully. |
| Powell | success | [10.341 1.6058] | 2.3232229362818934e-21 | 0.0073099580040434375 | 6 | Optimization terminated successfully. |
| Nelder-Mead | success | [9.4592 0.42722] | 1.0815673683701653e-14 | 0.0005810000002384186 | 40 | Optimization terminated successfully. |
| Nelder-Mead | success | [10.052 0.29099] | 1.7518416502120878e-15 | 0.000581291998969391 | 41 | Optimization terminated successfully. |
| Nelder-Mead | success | [10.968 1.279] | 2.0855466425499676e-15 | 0.0005725840019294992 | 41 | Optimization terminated successfully. |
