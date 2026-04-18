# POWERSUMB

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
| L-BFGS-B | success | [1.9959 1.9388 1.8436 1.8839] | 0.00015307529274877256 | 0.0007644589641131461 | 36 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [2.1601 1.9715 1.9094 2.3127] | 0.00031727935204634293 | 0.0007251669885590672 | 40 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [2.089 2.0618 1.9338 2.2624] | 9.742742240242264e-07 | 0.0006581249763257802 | 40 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [1.9598 1.5532 1.876 1.9092] | 7.468930834447371e-06 | 0.000658750010188669 | 22 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [2.2423 2.1713 2.1513 1.9659] | 1.94643654846387e-05 | 0.0007238329853862524 | 25 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | fail | [1.9547 1.9769 2.3222 2.301] | 0.009695719532729083 | 0.0006908330251462758 | 23 | Max. number of function evaluations reached |
| Powell | success | [2.0642 1.4786 1.8818 1.7721] | 3.348727886147328e-07 | 0.006595665996428579 | 20 | Optimization terminated successfully. |
| Powell | success | [1.8159 1.7393 1.9451 1.8528] | 0.07259745191663879 | 0.0042776670306921005 | 13 | Optimization terminated successfully. |
| Powell | success | [1.9493 1.6939 1.646 2.0117] | 0.000343081979726847 | 0.010153250012081116 | 29 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.5368 2.1249 2.0659 1.9889] | 0.000393138190640999 | 0.002299749990925193 | 190 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.7445 2.0111 1.8688 1.7375] | 0.0003807933865879138 | 0.003941625007428229 | 322 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.4935 1.8427 1.8267 1.7657] | 7.978283485657319e-07 | 0.0027579169836826622 | 234 | Optimization terminated successfully. |
