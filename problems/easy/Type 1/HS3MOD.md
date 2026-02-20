# HS3MOD

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [10.33941966  2.49925495] | 4.415667613189849e-34 | 0.00017187499906867743 | 4 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [10.43897506  2.20031653] | 1.2194008627034456e-33 | 0.00014712498523294926 | 4 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [11.57034511  1.24230581] | 6.1635079004738824e-34 | 0.00026208400959149003 | 4 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [9.59677803 0.68569367] | 6.072466645607625 | 9.454198880121112e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [9.73939076 1.75165885] | 11.189673031152969 | 8.454202907159925e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [10.4185132   0.67949563] | 6.885086633556946 | 8.158298442140222e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [9.70093023 0.56267533] | 4.29240665441781e-06 | 0.004704959050286561 | 4 | Optimization terminated successfully. |
| Powell | fail | [9.40542294 2.78236332] | 1.997459446682051e-06 | 0.008103999949526042 | 7 | Maximum number of function evaluations has been exceeded. |
| Powell | fail | [9.85414297 2.38874054] | 0.002974832418977094 | 0.007757000043056905 | 6 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [11.037111    2.18411591] | 4.6256462146541545e-10 | 0.000751374987885356 | 57 | Optimization terminated successfully. |
| Nelder-Mead | success | [8.77433697 1.92735819] | 1.1218078341810516e-10 | 0.0007798750302754343 | 56 | Optimization terminated successfully. |
| Nelder-Mead | success | [9.36920532 1.36830515] | 9.912360002664558e-11 | 0.0006954999989829957 | 45 | Optimization terminated successfully. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: TNC
- Time: 8.16e-05 s
- Iterations: 1
- Objective: 6.89

### Least Iterations (iter)
- Method: TNC
- Time: 9.45e-05 s
- Iterations: 1
- Objective: 6.07

### Best Objective (f)
- Method: L-BFGS-B
- Time: 0.000172 s
- Iterations: 4
- Objective: 4.42e-34
