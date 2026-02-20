# DUALC5

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
- **# of Variables (n):** 8
- **# of Constraints (m):** 278
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| SLSQP | success | [0.0565 0.0334 -0.0752 0.0308 0.0969 0.0445 -0.0864 -0.0381] | 427 | 0.0151 | 18 | Optimization terminated successfully |
| SLSQP | success | [-0.00696 -0.157 -0.0747 0.00485 0.196 -0.0558 0.0827 -0.0613] | 427 | 0.0123 | 16 | Optimization terminated successfully |
| SLSQP | success | [0.0573 -0.0049 -0.0359 0.211 -0.00978 -0.153 0.0605 0.00441] | 427 | 0.0111 | 14 | Optimization terminated successfully |
| COBYLA | fail | [0.0494 -0.101 -0.041 0.184 -0.00112 0.198 -0.0246 -0.138] | -83.8 | 1.9 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
| COBYLA | success | [-0.06 -0.00849 -0.104 -0.0157 -0.0161 -0.0811 0.0826 -0.0597] | -83.8 | 1.48 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | fail | [0.0208 -0.164 -0.229 0.0592 -0.0734 0.144 0.00493 0.0904] | -83.6 | 1.94 | None | Return from COBYLA because the objective function has been evaluated MAXFUN times. |
