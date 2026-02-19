# TAME

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
- **# of Variables (n):** 2
- **# of Constraints (m):** 1
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.15225852 0.03232153] | 7.703719777548943e-34 | 0.00011479199747554958 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.00393176 0.        ] | 1.88079096131566e-37 | 9.19159792829305e-05 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.         0.01900097] | 0.0 | 8.991599315777421e-05 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [0.20429271 0.18546149] | 0.0 | 0.00012675000471062958 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.         0.04887723] | 0.0 | 8.891598554328084e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.00214841 0.20621906] | 0.0 | 8.062500273808837e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [0.         0.09212206] | 0.0 | 0.0019833339902106673 | 2 | Optimization terminated successfully. |
| Powell | success | [0.04000717 0.07431267] | 0.0 | 0.0019638329977169633 | 2 | Optimization terminated successfully. |
| Powell | success | [0.         0.13223096] | 0.0 | 0.002087834000121802 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.14876638 0.        ] | 0.0 | 0.00022945800446905196 | 12 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.06227598 0.        ] | 0.0 | 0.00019887497182935476 | 12 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.        0.0260367] | 6.554278149733112e-10 | 0.0002516249951440841 | 16 | Optimization terminated successfully. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: TNC
- Time: 8.06e-05 s
- Iterations: 1
- Objective: 0

### Least Iterations (iter)
- Method: L-BFGS-B
- Time: 0.000115 s
- Iterations: 1
- Objective: 7.7e-34

### Best Objective (f)
- Method: L-BFGS-B
- Time: 8.99e-05 s
- Iterations: 1
- Objective: 0
