# SIM2BQP

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
| L-BFGS-B | success | [0.5] | 0.0 | 0.00015579198952764273 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.5] | 0.0 | 0.00010054197628051043 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.5] | 0.0 | 8.462497498840094e-05 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [0.5] | 0.0 | 9.429198689758778e-05 | 1 | Local minimum reached (|pg| ~= 0) |
| TNC | success | [0.5] | 0.0 | 7.429200923070312e-05 | 1 | Local minimum reached (|pg| ~= 0) |
| TNC | success | [0.5] | 0.0 | 7.212499622255564e-05 | 1 | Local minimum reached (|pg| ~= 0) |
| Powell | success | [0.5] | 1.4677799858681627e-26 | 0.0033867910387925804 | 6 | Optimization terminated successfully. |
| Powell | success | [0.5] | 1.4677799858681627e-26 | 0.0030992499669082463 | 6 | Optimization terminated successfully. |
| Powell | success | [0.5] | 1.4677799858681627e-26 | 0.0033123749890364707 | 6 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.5] | 0.0 | 0.0001816670410335064 | 6 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.5] | 0.0 | 0.00014058296801522374 | 6 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.5] | 0.0 | 0.0001366250216960907 | 6 | Optimization terminated successfully. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: TNC
- Time: 7.21e-05 s
- Iterations: 1
- Objective: 0

### Least Iterations (iter)
- Method: L-BFGS-B
- Time: 0.000156 s
- Iterations: 1
- Objective: 0

### Best Objective (f)
- Method: L-BFGS-B
- Time: 0.000156 s
- Iterations: 1
- Objective: 0
