# TRIGON2B

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
- **# of Variables (n):** 10
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.03848 0.22237 0.28955 0.42918 0.59329 0.51141 0.61509 0.93407 0.85256 0.75421] | 7.863677217127533 | 0.0008798749768175185 | 41 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.11942 0.0073967 0.27699 0.36112 0.60343 0.52249 0.69889 0.7529 0.88131 0.94809] | 5.03466139013179 | 0.0006075830315239727 | 33 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [-0.0086303 0.35882 0.4555 0.34863 0.36261 0.4825 0.67233 0.95499 0.79665 1.0145] | 4.937826589531543 | 0.0005032079643569887 | 27 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [0.089774 0.29795 0.31367 0.38177 0.5095 0.78089 0.63551 0.90905 0.90486 1.0349] | 2.967955829816686 | 0.0005143749876879156 | 14 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [0.20993 0.18189 0.26162 0.28128 0.46942 0.45757 0.67062 0.6903 0.94166 0.89333] | 3.4155639942420875 | 0.0005885830032639205 | 13 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.036663 0.4134 0.44631 0.39069 0.49188 0.50691 0.72681 0.90717 1.0167 1.2401] | 3.6884978637847556 | 0.0005648750229738653 | 16 | Converged (|f_n-f_(n-1)| ~= 0) |
| Powell | success | [-0.090116 0.20678 0.23352 0.36922 0.44192 0.55147 0.69371 0.69831 0.97035 0.93284] | 1.0000000011895018 | 0.001296166970860213 | 2 | Optimization terminated successfully. |
| Powell | success | [0.088963 0.2183 0.10924 0.24334 0.5545 0.49062 0.78995 0.75976 0.83749 0.98089] | 1.0000000011895018 | 0.0013383330078795552 | 2 | Optimization terminated successfully. |
| Powell | success | [-0.047273 0.106 0.26026 0.29437 0.3746 0.6124 0.99596 0.80342 0.91525 1.114] | 1.0000000011895018 | 0.0012732920004054904 | 2 | Optimization terminated successfully. |
| Nelder-Mead | fail | [-0.009228 0.094031 0.1696 0.47341 0.4048 0.73737 0.80912 0.60064 0.86376 0.86117] | 4.236716755011755 | 0.015961125027388334 | 1428 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [-0.062607 0.12149 0.29129 0.339 0.64299 0.50676 0.59561 0.74653 0.85444 0.97674] | 3.6907943296206573 | 0.012324417009949684 | 1121 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.23671 0.33958 0.24321 0.39513 0.32725 0.75349 0.77404 0.79434 1.0878 1.1188] | 2.8307763960819825 | 0.00864804198499769 | 761 | Optimization terminated successfully. |
