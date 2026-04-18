# PFIT3LS

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.0126 -0.006857 1.163] | 3.5632506035735915e-10 | 0.011357666982803494 | 743 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.83394 0.0074644 0.93259] | 8.093312075487964e-10 | 0.008793790999334306 | 580 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.97586 -0.08383 0.90879] | 133.02604024408177 | 0.002268333046231419 | 130 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.1188 -0.17894 1.0555] | 39734.07955229674 | 8.920894470065832e-05 | 1 | Unable to progress |
| TNC | fail | [0.82509 -0.062308 0.90761] | 39734.07955229674 | 7.983401883393526e-05 | 1 | Unable to progress |
| TNC | fail | [1.1324 -0.062434 1.1965] | 39734.07955229674 | 7.299997378140688e-05 | 1 | Unable to progress |
| Powell | success | [0.86965 0.18992 0.87151] | inf | 0.0045248339883983135 | 3 | Optimization terminated successfully. |
| Powell | success | [0.97157 0.025239 0.87259] | 192.76563709398016 | 0.003004125028382987 | 2 | Optimization terminated successfully. |
| Powell | success | [0.89237 0.04572 0.90819] | 176.07061952228864 | 0.0029647909686900675 | 2 | Optimization terminated successfully. |
| Nelder-Mead | fail | [1.0964 0.058491 0.98229] | 35.56610855481343 | 0.004099791985936463 | 344 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.8253 -0.010928 1.0264] | 7377.537522648575 | 0.004295999999158084 | 343 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.96011 0.072016 0.82583] | 62.054084472252 | 0.004025166039355099 | 345 | Maximum number of function evaluations has been exceeded. |
