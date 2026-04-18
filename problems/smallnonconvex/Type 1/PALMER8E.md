# PALMER8E

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.96662 0.90662 0.9772 0.99906 1.0477 0.94885 0.80741 0.89877] | 0.006339312006098201 | 0.0033995419507846236 | 216 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.1264 1.1029 1.172 1.2189 1.0641 0.9633 0.93534 0.80547] | 0.006339395269286855 | 0.00317520898533985 | 202 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0035 0.94384 1.0575 0.95974 1.0302 1.0896 1.0262 0.85931] | 0.006339349261508922 | 0.0038962920079939067 | 261 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [0.95038 0.9154 0.89168 0.85081 1.0221 0.81828 1.0699 0.81925] | 42.901614532677314 | 0.00010329199722036719 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [1.1017 1.0478 0.98219 0.91305 1.0009 1.1919 1.1296 1.0437] | 72.95745581546707 | 8.691695984452963e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.87306 1.2278 1.0958 1.0924 0.97911 0.91539 1.0265 0.93128] | 67.2820527886428 | 8.533400250598788e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [0.82541 0.92227 0.9669 0.83902 0.85536 1.0265 0.86717 0.92] | 4.05482667833747 | 0.01263241597916931 | 13 | Optimization terminated successfully. |
| Powell | success | [0.95988 0.9527 0.98298 1.0004 0.9741 1.0607 0.99641 0.95831] | 1.6676590945153222 | 0.016621041984762996 | 20 | Optimization terminated successfully. |
| Powell | fail | [0.92623 0.93312 1.2215 1.0179 1.0669 0.97007 0.91092 1.0938] | 1.6307772395131588 | 0.03419333300553262 | 31 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [1.0719 1.0335 1.0213 1.0547 0.91885 1.0172 1.0849 0.90276] | 1.5791278785125802 | 0.012287416961044073 | 1085 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [1.0663 1.081 1.0961 0.98661 1.1361 0.83491 0.9767 1.1319] | 0.16285857078182145 | 0.010336333012674004 | 925 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.96476 1.0748 0.96909 0.92062 1.1295 0.91693 0.94542 0.94189] | 2.5624102378344014 | 0.012066708004567772 | 1072 | Maximum number of function evaluations has been exceeded. |
