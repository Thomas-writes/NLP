# BQP1VAR

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
- **# of Variables (n):** 1
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.09889192] | 0.0 | 0.00013100000796839595 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.28015984] | 0.0 | 9.429099736735225e-05 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.17719401] | 0.0 | 8.654198609292507e-05 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [0.22144062] | 0.0 | 7.78749817982316e-05 | 1 | Local minimum reached (|pg| ~= 0) |
| TNC | success | [0.37089944] | 0.0 | 7.437501335516572e-05 | 1 | Local minimum reached (|pg| ~= 0) |
| TNC | success | [0.2065345] | 0.0 | 6.708299042657018e-05 | 1 | Local minimum reached (|pg| ~= 0) |
| Powell | success | [0.32809038] | 6.088392093973408e-27 | 0.00314174999948591 | 6 | Optimization terminated successfully. |
| Powell | success | [0.06797716] | 5.6083085013053335e-27 | 0.002986999985296279 | 6 | Optimization terminated successfully. |
| Powell | success | [0.32933321] | 6.088392093973408e-27 | 0.0031196250347420573 | 6 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.38971096] | 0.0 | 0.00016429199604317546 | 6 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.11600324] | 0.0 | 0.00013716600369662046 | 6 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.43701677] | 0.0 | 0.0001307500060647726 | 6 | Optimization terminated successfully. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: TNC
- Time: 6.71e-05 s
- Iterations: 1
- Objective: 0

### Least Iterations (iter)
- Method: L-BFGS-B
- Time: 0.000131 s
- Iterations: 1
- Objective: 0

### Best Objective (f)
- Method: L-BFGS-B
- Time: 0.000131 s
- Iterations: 1
- Objective: 0
