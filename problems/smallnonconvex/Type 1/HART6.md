# HART6

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
- **Objective Type:** other
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.13758 0.031407 0.24979 0 0.11453 0.22595] | -3.322886891351728 | 0.0003514580021146685 | 13 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.22896 0.25621 0.36437 0.2207 0.051693 0.4511] | -3.3228868915357586 | 0.0002550409990362823 | 11 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.10305 0.2571 0.1436 0.14319 0.16408 0.19234] | -3.3228868910745906 | 0.00028362499142531306 | 14 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [0.22423 0.34654 0.30448 0.2902 0.042573 0.19574] | -3.3228868914714984 | 0.0003667499986477196 | 9 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [0.27274 0.2949 0.27323 0.26282 0.22553 0.3696] | -3.3228868915840013 | 0.0002612910029711202 | 7 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [0.20632 0.29838 0.13752 0.44589 0.22677 0.13101] | -3.322886891406468 | 0.00035837499308399856 | 9 | Converged (|f_n-f_(n-1)| ~= 0) |
| Powell | success | [0.41758 0.29471 0.14686 0.27544 0.18234 0.2404] | -3.204596554052297 | 0.0014187089982442558 | 4 | Optimization terminated successfully. |
| Powell | success | [0.21977 0.19194 0.30803 0.36067 0.29491 0.15009] | -3.204595506353318 | 0.0009805000008782372 | 3 | Optimization terminated successfully. |
| Powell | success | [0.15595 0.13914 0.19813 0 0.11273 0.2976] | -3.3228862169186346 | 0.000985207996563986 | 3 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.22505 0.14685 0.016257 0.3155 0.10096 0.10727] | -1.0609639055171338 | 0.002508125005988404 | 208 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.15518 0.29987 0.18321 0 0.36835 0.092695] | -1.7465533736482615 | 0.002473832995747216 | 199 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.26745 0.079338 0.27661 0.35954 0.22922 0.20745] | -3.3228866987883863 | 0.0029950409953016788 | 257 | Optimization terminated successfully. |
