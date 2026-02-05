# SIMBQP

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-02-05

## Classification
- **Convexity:** Convex
- **Degree:** Quadratic
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 
## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [5.0744589e+19 3.6811950e-01] | 1.2875066553464935e+40 | 0.00011724999058060348 | 0 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [8.57931597e+19 1.24674981e-01] | 3.6802331261643217e+40 | 6.0874997870996594e-05 | 0 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [-7.34773653e+18  3.86966468e-02] | 2.699461602671084e+38 | 0.00011929200263693929 | 0 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-3.90854345e+19  3.27650712e-01] | 7.638355945649782e+39 | 6.179098272696137e-05 | 0 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [9.46523929e+19 1.43077139e-01] | 4.47953773654582e+40 | 4.949999856762588e-05 | 0 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-7.10549277e+19  4.80014077e-01] | 2.5244013723647447e+40 | 4.620797699317336e-05 | 0 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [2.72724706e+19 4.20394393e-01] | 3.718938268497312e+39 | 0.00010699999984353781 | 0 | A bad approximation caused failure to predict improvement. |
| dogleg | fail | [2.25423275e+19 3.09722760e-01] | 2.54078264389322e+39 | 7.258399273268878e-05 | 0 | A bad approximation caused failure to predict improvement. |
| dogleg | fail | [7.83254433e+19 2.68740228e-01] | 3.0674375333083345e+40 | 6.645801477134228e-05 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.42071286e+19 4.71550518e-01] | 1.0092125161414736e+39 | 7.245800225064158e-05 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [7.91308100e+19 2.43731926e-01] | 3.130842546015063e+40 | 6.42079976387322e-05 | 0 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [-6.55634579e+19  2.26767223e-02] | 2.1492835027126646e+40 | 5.599998985417187e-05 | 0 | A bad approximation caused failure to predict improvement. |
