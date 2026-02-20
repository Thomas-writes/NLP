# SIMBQP

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
| L-BFGS-B | success | [11.37404198  0.        ] | 3.2899278576057705e-29 | 0.00012304203119128942 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [9.50716313 0.5       ] | 1.2547565055984384e-33 | 0.00013162498362362385 | 3 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [8.51768157 0.5       ] | 4.825188251006205e-33 | 0.00011766701936721802 | 3 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [10.69907392  0.5       ] | 0.95 | 8.195801638066769e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [9.84981968 0.        ] | 7.24454326306137e-30 | 7.299997378140688e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [10.13480443  0.5       ] | 0.9499999999999998 | 6.920902524143457e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [8.74462736 0.5       ] | 2.591601167660264e-07 | 0.0028653329936787486 | 7 | Optimization terminated successfully. |
| Powell | success | [10.22809441  0.        ] | 5.3206898158770514e-05 | 0.0004819169989787042 | 2 | Optimization terminated successfully. |
| Powell | success | [9.35886244 0.5       ] | 2.6874538178140366e-07 | 0.0027944999746978283 | 7 | Optimization terminated successfully. |
| Nelder-Mead | success | [10.07083594  0.5       ] | 7.515976027921981e-10 | 0.0005299170152284205 | 39 | Optimization terminated successfully. |
| Nelder-Mead | success | [9.17631461 0.        ] | 2.1610231414576775e-09 | 0.0005459169624373317 | 42 | Optimization terminated successfully. |
| Nelder-Mead | success | [9.37889563 0.5       ] | 8.79328824835784e-10 | 0.0005587090272456408 | 43 | Optimization terminated successfully. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: TNC
- Time: 6.92e-05 s
- Iterations: 1
- Objective: 0.95

### Least Iterations (iter)
- Method: L-BFGS-B
- Time: 0.000123 s
- Iterations: 1
- Objective: 3.29e-29

### Best Objective (f)
- Method: L-BFGS-B
- Time: 0.000132 s
- Iterations: 3
- Objective: 1.25e-33
