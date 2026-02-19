# GENHS28

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
- **# of Variables (n):** 10
- **# of Constraints (m):** 8
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [-3.91005189  1.67007828  0.85620818  1.25694233  0.9716515   0.78603149  0.84373482  0.92397681  0.63430353  1.26761124] | 1.2503257013634757e-10 | 0.0016619169909972697 | 17 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [-4.11849747  1.52567313  0.63271354  1.06934857  0.74129677  1.18073098  0.39206921  1.36011965  0.93721693  1.52550875] | 8.066679207793565e-12 | 0.0003390829951968044 | 18 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [-4.03939388  1.42885521  1.03386973  1.53561818  1.60483745  1.14061071  0.69794317  1.21785133  0.88036549  0.46372752] | 6.668696641731646e-11 | 0.0003117909946013242 | 17 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | success | [-4.30431132  1.07218297  1.32145378  0.84434361  1.8340875   0.80539904  0.54313975  0.80703254  1.27398568  1.1197713 ] | 2.42252148950763 | 0.0001135829952545464 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [-3.58580634  0.72661736  0.27462157  1.74752935  1.49125856  1.05932802  1.90614303  0.37966767  0.38273931  0.99229334] | 1.5225633131567609 | 8.770899148657918e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [-3.95717002  0.60268542  1.14127888  1.14113498  1.43488266  1.34177286  1.53098333  0.91495658  0.91505107  1.42615432] | 1.6546108303337916 | 9.124999633058906e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [-3.78005851  1.33058605  1.98374431  0.95535992  1.42360328  1.11801193  1.08024208  0.62131346  0.64041028  0.92709336] | 2.7883482881528875e-16 | 0.011521290987730026 | 23 | Optimization terminated successfully. |
| Powell | success | [-3.68015813  1.46815974  1.01426207  0.46603187  1.02014494  1.00084744  1.23910773  0.90832739  0.98677686  1.47375146] | 1.8589917378729658e-23 | 0.0128340829978697 | 26 | Optimization terminated successfully. |
| Powell | success | [-3.79884887  0.68584205  0.82544535  1.06110514  1.85855326  0.43372946  0.82922961  1.7229888   0.94853098  0.76321564] | 6.434165013055929e-22 | 0.01397599998745136 | 29 | Optimization terminated successfully. |
| Nelder-Mead | fail | [-4.78452736  0.64078415  1.50454389  0.76581857  1.21641512  0.30791118  1.69490573  1.00815434  0.51689946  0.37292639] | 8.281390644742107e-08 | 0.015546167007414624 | 1417 | Maximum number of function evaluations has been exceeded. |
| Nelder-Mead | success | [-4.53932756  1.09023688  1.2161939   0.90075464  0.67967182  0.63772545  1.12194715  1.15297804  0.71899043  1.0771675 ] | 5.79663077719612e-09 | 0.01364308298798278 | 1278 | Optimization terminated successfully. |
| Nelder-Mead | success | [-4.05829492  1.08596172  1.04699934  0.22248544  0.92088456  0.89454062  1.28353061  1.28113704  0.67078438  1.05724094] | 3.863960003624152e-09 | 0.013810999982524663 | 1298 | Optimization terminated successfully. |

## Best-known results (by metric)

### Fastest successful (time)
- Method: TNC
- Time: 8.77e-05 s
- Iterations: 1
- Objective: 1.52

### Least Iterations (iter)
- Method: TNC
- Time: 0.000114 s
- Iterations: 1
- Objective: 2.42

### Best Objective (f)
- Method: Powell
- Time: 0.0128 s
- Iterations: 26
- Objective: 1.86e-23
