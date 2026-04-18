# LSQFIT

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-25

## Classification
- **Convexity:** Convex
- **Objective Type:** sum of squares
- **# of Variables (n):** 2
- **# of Constraints (m):** 1
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [0 0.098193] | 0.759 | 0.0129 | 63 | `xtol` termination condition is satisfied. |
| trust-constr | success | [0.059373 -0.19944] | 0.0338 | 0.0161 | 40 | `gtol` termination condition is satisfied. |
| trust-constr | fail | [0 -0.1061] | 0.19 | 0.398 | 1000 | The maximum number of function evaluations is exceeded. |
