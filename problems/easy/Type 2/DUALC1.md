# DUALC1

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
- **# of Variables (n):** 9
- **# of Constraints (m):** 215
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| SLSQP | fail | [0.187 -0.0941 -0.0391 -0.247 0.124 -0.0729 0.092 0.0439 0.0273] | 2.12e+05 | 0.00435 | 5 | Positive directional derivative for linesearch |
| SLSQP | fail | [-0.137 0.0305 -0.0591 0.0617 -0.162 0.0449 0.172 -0.0846 0.0179] | 9.48e+04 | 0.00427 | 5 | Positive directional derivative for linesearch |
| SLSQP | fail | [0.0431 -0.125 0.0907 -0.0846 -0.0415 -0.113 0.126 0.0393 -0.0669] | 2.07e+05 | 0.00431 | 5 | Positive directional derivative for linesearch |
| COBYLA | success | [-0.103 0.0205 -0.228 -0.118 -0.0892 0.157 0.0808 -0.13 -0.0817] | -2.57e+06 | 1.83 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [-0.108 -0.0481 -0.083 -0.106 -0.11 0.0589 -0.048 -0.0105 0.0213] | -2.57e+06 | 1.32 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [0.104 0.00769 -0.118 -0.0841 0.0115 0.0532 0.0555 -0.00357 -0.028] | -2.57e+06 | 1.49 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
