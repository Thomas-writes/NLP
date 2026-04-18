# PORTSNQP

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-25

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** quadratic
- **# of Variables (n):** 10
- **# of Constraints (m):** 2
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0.34366 0.30428 0.47293 0.40749 0.33336 0.53215 0.48418 0.5151 0.36818 0.41402] | 1.94 | 0.00795 | 20 | `gtol` termination condition is satisfied. |
| trust-constr | fail | [0.36314 0.49492 0.37071 0.49629 0.54008 0.48876 0.26769 0.65806 0.48503 0.39324] | 2.94 | 0.0694 | 234 | Constraint violation exceeds 'gtol' |
| trust-constr | success | [0.39767 0.39387 0.50539 0.48502 0.32738 0.44902 0.47785 0.44131 0.50045 0.31036] | 1.94 | 0.0105 | 27 | `gtol` termination condition is satisfied. |
| SLSQP | success | [0.40221 0.43152 0.38796 0.4887 0.27369 0.49847 0.353 0.53216 0.50362 0.4392] | 1.94 | 0.000541 | 3 | Optimization terminated successfully |
| SLSQP | success | [0.24928 0.45152 0.4493 0.35125 0.32693 0.52226 0.51958 0.36233 0.46993 0.57493] | 1.94 | 0.000498 | 3 | Optimization terminated successfully |
| SLSQP | success | [0.45104 0.28004 0.48361 0.58438 0.37517 0.4188 0.52792 0.22742 0.57461 0.33895] | 1.94 | 0.000495 | 3 | Optimization terminated successfully |
| COBYLA | fail | [0.40883 0.44275 0.42751 0.35706 0.50329 0.43825 0.46037 0.49071 0.49662 0.36449] | 4.1 | 2.01 | None | Did not converge to a solution satisfying the constraints. See `maxcv` for the magnitude of the violation. |
| COBYLA | fail | [0.55183 0.49582 0.45681 0.33037 0.52891 0.47648 0.55372 0.28298 0.16006 0.65013] | 4.21 | 2.02 | None | Did not converge to a solution satisfying the constraints. See `maxcv` for the magnitude of the violation. |
| COBYLA | fail | [0.36093 0.43877 0.49829 0.4731 0.29522 0.32078 0.46235 0.36188 0.51363 0.56741] | 3.47 | 2.01 | None | Did not converge to a solution satisfying the constraints. See `maxcv` for the magnitude of the violation. |
