# PENTAGON

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
- **Objective Type:** other
- **# of Variables (n):** 6
- **# of Constraints (m):** 15
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | fail | [-1.0435 0.10801 0.24072 -0.99213 0.88733 0.79132] | 0.000166 | 0.494 | 1000 | The maximum number of function evaluations is exceeded. |
| trust-constr | success | [-0.98332 -0.24005 -0.0099701 -1.0273 0.85261 0.77593] | 0.000146 | 0.0247 | 48 | `gtol` termination condition is satisfied. |
| trust-constr | success | [-1.0846 0.15105 0.0094389 -1.0333 0.87652 0.85102] | 0.000137 | 0.0306 | 60 | `gtol` termination condition is satisfied. |
| SLSQP | success | [-1.1003 -0.0040582 -0.08341 -1.0893 1.0694 0.65425] | 0.000153 | 0.00162 | 16 | Optimization terminated successfully |
| SLSQP | success | [-1.2277 0.045515 -0.12919 -1.0875 0.9646 0.84017] | 0.000155 | 0.00116 | 11 | Optimization terminated successfully |
| SLSQP | success | [-1.03 0.081687 -0.090993 -0.95593 0.85177 0.85677] | 0.000167 | 0.00142 | 12 | Optimization terminated successfully |
| COBYLA | fail | [-0.80595 -0.090959 0.11099 -0.94469 0.92352 0.78615] | 0.0272 | 2.32 | None | Did not converge to a solution satisfying the constraints. See `maxcv` for the magnitude of the violation. |
| COBYLA | fail | [-0.9263 -0.1462 0.035658 -1 0.99261 0.77769] | 0.0178 | 2.47 | None | Did not converge to a solution satisfying the constraints. See `maxcv` for the magnitude of the violation. |
| COBYLA | success | [-0.96079 0.13157 0.014609 -0.99943 0.91512 0.85319] | 0.000146 | 0.0978 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
