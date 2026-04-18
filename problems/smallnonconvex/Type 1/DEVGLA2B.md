# DEVGLA2B

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
- **# of Variables (n):** 5
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [20.237 1 5.0976 3.2297 1] | 10643.908877437962 | 0.0004917919868603349 | 18 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [20.678 1.1918 2.2767 1 1] | 10643.423889725476 | 0.0008717079763300717 | 46 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [19.199 3.1837 1 2.8347 1] | 10698.268424988233 | 0.0006549169775098562 | 29 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [22.238 1 1 6.015 1] | 5055.6862122794755 | 0.0004435409791767597 | 9 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | fail | [21.275 2.38 1 3.2344 2.2157] | 16378.269035302486 | 0.0009366669692099094 | 22 | Max. number of function evaluations reached |
| TNC | success | [18.104 3.866 1.1273 1 1] | 10528.545103134273 | 0.0008466659928672016 | 22 | Local minimum reached (|pg| ~= 0) |
| Powell | success | [18.727 2.4814 4.4818 1.2514 2.4778] | 15568.04814869188 | 0.001492417010013014 | 2 | Optimization terminated successfully. |
| Powell | success | [20.033 1.0734 1 3.5388 5.4176] | 18137.248222434162 | 0.0018627080135047436 | 3 | Optimization terminated successfully. |
| Powell | success | [23.237 1 4.4855 4.2164 1.5823] | 39447.27878070701 | 0.0013396249851211905 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [20.075 3.7311 3.6927 1.7811 1] | 10640.458942174519 | 0.004639999999199063 | 352 | Optimization terminated successfully. |
| Nelder-Mead | success | [20.052 1 1.4599 1 1] | 10640.458942170419 | 0.007387291989289224 | 577 | Optimization terminated successfully. |
| Nelder-Mead | success | [22.266 1 1.1505 1.8269 3.5168] | 19120.065412249456 | 0.003006374987307936 | 219 | Optimization terminated successfully. |
