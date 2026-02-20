# OSLBQP

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
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [2.5        0.53204527 0.46380215 0.72047052 0.6137318  0.6792473  0.36447857 0.39460075] | 6.25 | 0.0004999999655410647 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [2.5        0.4890236  0.46380761 0.43354708 0.5        0.62980493 0.39964655 0.3983327 ] | 6.25 | 0.0001457909820601344 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [2.5        0.37080712 0.43258709 0.43684279 0.5        0.4365536  0.42023401 0.3959654 ] | 6.25 | 0.0001112080062739551 | 1 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [2.5        0.51173782 0.60703539 0.59506229 0.59468622 0.57139981 0.42208912 0.44204909] | 6.25 | 0.0006093749543651938 | 2 | Local minimum reached (|pg| ~= 0) |
| TNC | success | [2.5        0.67741899 0.61569867 0.47220379 0.50287025 0.68652348 0.568571   0.43358481] | 6.25 | 0.00012141698971390724 | 2 | Local minimum reached (|pg| ~= 0) |
| TNC | success | [2.5        0.58187581 0.53122287 0.33134715 0.5        0.45883382 0.43073884 0.4904528 ] | 6.25 | 9.21249738894403e-05 | 1 | Local minimum reached (|pg| ~= 0) |
| Powell | success | [2.5        0.54894697 0.47744652 0.48209073 0.66279907 0.35973068 0.41377026 0.57779934] | 6.250336779296088 | 0.005307458981405944 | 2 | Optimization terminated successfully. |
| Powell | success | [2.5        0.4379676  0.64606373 0.4585793  0.5        0.52885535 0.66821478 0.46871463] | 6.250336779296088 | 0.005168166011571884 | 2 | Optimization terminated successfully. |
| Powell | success | [2.5        0.57541109 0.44292124 0.79845108 0.5        0.49327432 0.39728669 0.48526248] | 6.250336779296087 | 0.005313166999258101 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [2.5        0.34133789 0.62409207 0.36822633 0.5715637  0.32541231 0.60448872 0.4292163 ] | 6.250000025880992 | 0.00832341704517603 | 729 | Optimization terminated successfully. |
| Nelder-Mead | success | [2.5        0.35742839 0.50655793 0.31238797 0.5        0.62778715 0.48038397 0.5699062 ] | 6.250000006069195 | 0.003602457989472896 | 329 | Optimization terminated successfully. |
| Nelder-Mead | success | [2.5        0.52308567 0.56300381 0.47808935 0.54882771 0.47650413 0.54533187 0.67624652] | 6.250000015258672 | 0.003235875046811998 | 276 | Optimization terminated successfully. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: TNC
- Time: 9.21e-05 s
- Iterations: 1
- Objective: 6.25

### Least Iterations (iter)
- Method: L-BFGS-B
- Time: 0.0005 s
- Iterations: 1
- Objective: 6.25

### Best Objective (f)
- Method: L-BFGS-B
- Time: 0.0005 s
- Iterations: 1
- Objective: 6.25
