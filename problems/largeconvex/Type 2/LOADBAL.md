# LOADBAL

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
- **Objective Type:** other
- **# of Variables (n):** 31
- **# of Constraints (m):** 31
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | fail | [0.011201 0.72501 0.075964 0 0 0 0.19896 0 1.3309 0.64376 0.44426 0 0.079939 0.59812 0 0 0.4723 0.51239 0 0 95.088 94.732 18.913 69.822 70.084 18.794 18.943 69.691 19.191 18.058 19.196] | 1.48 | 0.0548 | 120 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [0 0 0.16888 0 0 0.61142 0.45494 0.20224 0 0 0.87773 0 0 0.74305 0 0 0.36136 0.80649 0 0 94.304 94.747 18.873 69.939 70.12 18.741 19.229 69.637 18.857 18.538 19.544] | 1.66 | 0.0397 | 120 | Constraint violation exceeds 'gtol' |
| trust-constr | fail | [0 0 0 0.34016 0.26798 0.43072 0 0.094234 0.44676 0 0 0.34416 0.77789 0 0 0 0 0.34467 0.80623 0 94.478 94.792 18.057 70.295 69.778 18.882 18.803 69.502 18.232 19.506 19.133] | 1.52 | 0.0414 | 120 | Constraint violation exceeds 'gtol' |
| SLSQP | success | [0 0 0.48293 0.36876 0.034015 0.6184 0 0 0 0.48989 0.38273 0 0.00014646 0.39483 0 0 0.37587 0.11388 0 0.73116 95.058 94.766 19.103 69.673 70.03 19.196 18.44 69.796 19.266 19.541 18.068] | 0.453 | 0.038 | 81 | Optimization terminated successfully |
| SLSQP | success | [0 0 0.2246 0.16488 0.22486 1.2617 0.39707 0 0 0 0.52036 0.068129 0 0.24639 0 0.52053 0.07743 0 0 0 94.805 94.175 18.688 70.488 70.471 19.128 19.382 70.657 19.09 18.597 18.621] | 0.453 | 0.0225 | 47 | Optimization terminated successfully |
| SLSQP | fail | [0.055378 0 0 0 0.11292 0 0.90124 0.059999 0.95457 0 0.041382 0.24336 0 0.13301 0.046861 0.28245 0 0 0.81242 0 95.523 95.479 18.67 69.601 70.22 19.908 18.261 69.365 19.32 19.509 19.676] | 0.453 | 0.0473 | 100 | Iteration limit reached |
| COBYLA | fail | [0 0.50136 1.0317 0.13085 0 0 0.5457 0 0 0 0 0 1.2754 0 0 0.68388 0 0.44142 1.2269 1.2577 95.236 95.747 18.819 69.134 69.359 19.146 18.636 71.737 18.045 18.865 18.48] | 0.421 | 9.81 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | fail | [0 0.17473 0.23871 0 0 1.0036 1.4814 0.042935 0.7345 0.55313 0.23983 0 0 0 0 0 0.37609 0.06961 0 0.33045 95.46 94.89 18.651 69.452 70.798 18.252 18.84 70.183 18.82 18.841 18.8] | 0.421 | 9.98 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | success | [0.11488 0 0 0.45116 0 0 0.15515 0 0.30482 0.2126 0 0 0.97395 0.82387 0.37147 0 0 0 0 0.32096 95.166 94.62 18.586 69.663 70.601 19.518 18.73 69.419 19.944 18.864 18.951] | -4.27e+06 | 1.24 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
