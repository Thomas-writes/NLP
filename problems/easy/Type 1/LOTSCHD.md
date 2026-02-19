# LOTSCHD

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-02-12

## Classification
- **Convexity:** Convex
- **Degree:** Quadratic
- **# of Variables (n):** 12
- **# of Constraints (m):** 7
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.04861143 0.04583571 0.00204349 0.         0.         0.         0.03114438 0.00355443 0.         0.01264453 0.         0.        ] | 0.0 | 0.00037358299596235156 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.         0.         0.2149288  0.01172199 0.15106408 0.         0.         0.         0.         0.01633372 0.04681233 0.07767185] | 0.0 | 0.0001294999965466559 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.10422431 0.12215636 0.00179666 0.09628871 0.09375686 0.         0.         0.11924224 0.07754639 0.         0.06292676 0.        ] | 0.0 | 0.00011058399104513228 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [0.         0.09947803 0.08307247 0.02925056 0.         0.         0.         0.05786371 0.07859097 0.00669078 0.00419631 0.06646676] | 0.0 | 8.141598664224148e-05 | 0 | Local minimum reached (|pg| ~= 0) |
| TNC | success | [0.         0.         0.         0.         0.01303221 0.         0.09811556 0.15806865 0.22018172 0.10400001 0.0709312  0.08514015] | 0.0 | 7.174999336712062e-05 | 0 | Local minimum reached (|pg| ~= 0) |
| TNC | success | [0.09089813 0.08083176 0.         0.06645684 0.         0.         0.06778851 0.         0.15141857 0.06235552 0.05774855 0.01747982] | 0.0 | 6.833398947492242e-05 | 0 | Local minimum reached (|pg| ~= 0) |
| Powell | success | [0.09843692 0.01086536 0.06395475 0.         0.         0.0582486  0.21034036 0.04773381 0.11797733 0.06320349 0.         0.        ] | 3.1008996292888815e-08 | 0.011651416978565976 | 3 | Optimization terminated successfully. |
| Powell | success | [0.07395851 0.         0.02378757 0.03001108 0.03628557 0.         0.         0.         0.21892252 0.         0.0606766  0.        ] | 3.2347583798822494e-08 | 0.011432333005359396 | 3 | Optimization terminated successfully. |
| Powell | success | [0.         0.         0.09506965 0.25180478 0.         0.         0.         0.         0.09847553 0.         0.         0.08085838] | 2.0758146469309268e-08 | 0.01085762499133125 | 3 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.00978293 0.         0.11328195 0.         0.14169723 0.         0.02199657 0.         0.         0.01393513 0.         0.12317726] | 5.097252934470337e-29 | 0.019399958022404462 | 1820 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.26379372 0.07869012 0.         0.20590941 0.         0.14056428 0.09587632 0.         0.         0.11820198 0.13885724 0.05445459] | 7.186184759606379e-31 | 0.019156374997692183 | 1840 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | fail | [0.15947165 0.         0.         0.         0.         0.10641188 0.01445294 0.         0.         0.03301187 0.07364466 0.10256899] | 1.1799377924640947e-36 | 0.019194416992831975 | 1841 | Maximum number of function evaluations has been exceeded. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: TNC
- Time: 6.83e-05 s
- Iterations: 0
- Objective: 0

### Least Iterations (iter)
- Method: TNC
- Time: 8.14e-05 s
- Iterations: 0
- Objective: 0

### Best Objective (f)
- Method: L-BFGS-B
- Time: 0.000374 s
- Iterations: 1
- Objective: 0
