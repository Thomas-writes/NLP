# DEVGLA2B

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
- **# of Variables (n):** 5
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [20.29 1 2.1577 1 1] | 10644.734812965828 | 0.0004450839915079996 | 18 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [22.532 3.4075 1.3418 3.9611 1] | 13874.01410038041 | 0.00011970799823757261 | 1 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [22.95 2.0241 6.0836 5.0908 1] | 10640.458942179286 | 0.0012649579875869676 | 68 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [21.611 1.096 1.3335 1.9756 1] | 5055.686212279475 | 0.0006458340067183599 | 14 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [23.847 4.5215 1.0327 2.4077 1] | 5055.6862122794755 | 0.0005300830089254305 | 14 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [22.42 1.5122 1 1 2.2976] | 17159.244246217888 | 0.0005072500061942264 | 14 | Converged (|f_n-f_(n-1)| ~= 0) |
| Powell | success | [22.589 1 8.1391 2.5377 1] | 14606.385983346096 | 0.0005575830000452697 | 1 | Optimization terminated successfully. |
| Powell | success | [22.864 1 2.757 1.149 1] | 15857.103707862585 | 0.0005558749980991706 | 1 | Optimization terminated successfully. |
| Powell | success | [17.348 1.6284 1 3.9781 1] | 18091.319590250994 | 0.0005794169992441311 | 1 | Optimization terminated successfully. |
| Nelder-Mead | success | [18.111 5.2696 1.8839 2.0777 1.2286] | 5055.686286218272 | 0.004053084005136043 | 298 | Optimization terminated successfully. |
| Nelder-Mead | success | [21.528 1 5.783 1.2273 1] | 10640.458942172318 | 0.0040318749961443245 | 294 | Optimization terminated successfully. |
| Nelder-Mead | success | [24.776 1.4423 1 1.8585 1] | 10640.45894216995 | 0.0069666249910369515 | 543 | Optimization terminated successfully. |
