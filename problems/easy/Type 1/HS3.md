# HS3

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
| L-BFGS-B | success | [9.24530775 1.68869502] | 5.189469748456545e-07 | 0.0006252499879337847 | 3 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [9.13305909 0.57693805] | 9.170919789928699e-36 | 0.00017583300359547138 | 3 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [11.18744588  0.27410758] | 9.231596414689994e-35 | 0.00013037503231316805 | 3 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [8.78336452 0.60594946] | 3.671747448141968e-06 | 8.100003469735384e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [10.70577849  3.17280734] | 0.00010066706402423882 | 8.370802970603108e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [8.31046424 0.91612725] | 8.392891432368011e-06 | 6.920797750353813e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [10.30312996  0.57645593] | 6.229822299853567e-21 | 0.006442875019274652 | 6 | Optimization terminated successfully. |
| Powell | success | [10.74552417  0.        ] | 5.720496589314726e-05 | 0.0010805000201798975 | 2 | Optimization terminated successfully. |
| Powell | success | [9.77730112 0.93308599] | 3.1211828090299806e-21 | 0.006864082999527454 | 6 | Optimization terminated successfully. |
| Nelder-Mead | success | [10.1455197   1.42224674] | 1.7845475066546068e-15 | 0.0005779589992016554 | 41 | Optimization terminated successfully. |
| Nelder-Mead | success | [10.89743077  1.68104546] | 2.05886444824837e-15 | 0.0005647499929182231 | 41 | Optimization terminated successfully. |
| Nelder-Mead | success | [9.86540467 1.21341784] | 1.176443658555811e-14 | 0.0005564590101130307 | 40 | Optimization terminated successfully. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: TNC
- Time: 6.92e-05 s
- Iterations: 1
- Objective: 8.39e-06

### Least Iterations (iter)
- Method: TNC
- Time: 8.1e-05 s
- Iterations: 1
- Objective: 3.67e-06

### Best Objective (f)
- Method: L-BFGS-B
- Time: 0.000176 s
- Iterations: 3
- Objective: 9.17e-36
