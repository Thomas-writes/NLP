# DUALC2

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-02-19

## Classification
- **Convexity:** Convex
- **Degree:** Quadratic
- **# of Variables (n):** 7
- **# of Constraints (m):** 229
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| SLSQP | fail | [-0.00721 0.087 -0.0521 0.0752 -0.0899 -0.0371 0.0493] | 924 | 0.00239 | 5 | Positive directional derivative for linesearch |
| SLSQP | fail | [0.0754 -0.0318 -0.18 0.0855 -0.00183 0.0109 0.109] | 4.33e+03 | 0.00219 | 5 | Positive directional derivative for linesearch |
| SLSQP | fail | [-0.0889 -0.0388 0.175 0.0955 0.131 -0.0606 -0.049] | 1.17e+04 | 0.00236 | 5 | Positive directional derivative for linesearch |
| COBYLA | success | [0.162 -0.101 0.137 0.215 0.061 -0.00524 0.0702] | -2.35e+05 | 0.255 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [-0.0189 0.0643 -0.0324 -0.00768 -0.0491 -0.0165 0.178] | -2.35e+05 | 0.294 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [-0.00232 0.125 -0.12 0.0184 -0.0118 0.0273 0.246] | -2.35e+05 | 0.559 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
