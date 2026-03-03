# HS3MOD

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
| L-BFGS-B | success | [9.3067 0.86325] | 1.1905562285320683e-33 | 0.00029254199762362987 | 4 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [8.7015 0.4015] | 1.683318884011891e-34 | 0.00017920800019055605 | 4 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [8.0703 0] | 1.5652228349932137e-33 | 0.00016925000818446279 | 4 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [11.253 0] | 5.052460046230529 | 0.00019779200374614447 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [9.395 0] | 3.517567156278038 | 8.991699723992497e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [9.914 2.6752] | 16.96119451546237 | 8.950001210905612e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [10.911 0.79216] | 0.056356187586347674 | 0.00505900000280235 | 4 | Optimization terminated successfully. |
| Powell | success | [8.602 0.98731] | 0.17084419743761556 | 0.0049269580049440265 | 4 | Optimization terminated successfully. |
| Powell | fail | [10.522 1.3211] | 1.091960160790925e-05 | 0.007961499999510124 | 6 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [9.3142 1.7297] | 1.770398335776043e-09 | 0.0008010830060811713 | 51 | Optimization terminated successfully. |
| Nelder-Mead | success | [9.521 0.94294] | 6.147993543131666e-10 | 0.0008493339992128313 | 58 | Optimization terminated successfully. |
| Nelder-Mead | success | [9.6766 0] | 8.675590474946861e-10 | 0.0005795000033685938 | 43 | Optimization terminated successfully. |
