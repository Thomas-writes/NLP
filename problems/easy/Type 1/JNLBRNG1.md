# JNLBRNG1

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.97562701 0.78556607 0.         0.        ] | -0.22473500539529453 | 0.0002394579933024943 | 5 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [0.84282821 0.89610467 0.         0.        ] | -0.22473500539529448 | 0.0001592919579707086 | 5 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [1.07497089 0.92924907 0.         0.        ] | -0.2247350053952946 | 0.00014274998102337122 | 5 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | fail | [0.88330599 0.90090067 0.         0.        ] | 0.0 | 0.00011395802721381187 | 1 | Linear search failed |
| TNC | fail | [0.93872462 1.06750449 0.         0.        ] | 0.0 | 0.00010508298873901367 | 1 | Linear search failed |
| TNC | fail | [1.05020104 1.01833167 0.         0.        ] | 0.0 | 0.00010183302219957113 | 1 | Linear search failed |
| Powell | success | [0.92899007 0.85979376 0.         0.        ] | -0.2246546740559779 | 0.005379667039960623 | 3 | Optimization terminated successfully. |
| Powell | success | [0.89838064 0.95231629 0.         0.        ] | -0.22465467291990499 | 0.005521750019397587 | 4 | Optimization terminated successfully. |
| Powell | success | [0.88258545 0.96274347 0.         0.        ] | -0.22465467285885501 | 0.005735249957069755 | 4 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.81959656 0.7527376  0.         0.        ] | -0.22473499942731737 | 0.0012329170131124556 | 100 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.83119358 0.98939181 0.         0.        ] | -0.10750698639772403 | 0.001222957973368466 | 102 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.81211662 0.7631438  0.         0.        ] | -0.22473500163515386 | 0.0011551249772310257 | 93 | Optimization terminated successfully. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: TNC
- Time: 0.000102 s
- Iterations: 1
- Objective: 0

### Least Iterations (iter)
- Method: TNC
- Time: 0.000114 s
- Iterations: 1
- Objective: 0

### Best Objective (f)
- Method: L-BFGS-B
- Time: 0.000143 s
- Iterations: 5
- Objective: -0.225
