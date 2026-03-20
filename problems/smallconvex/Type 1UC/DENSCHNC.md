# DENSCHNC

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-03

## Classification
- **Convexity:** Convex
- **Objective Type:** sum of squares
- **# of Variables (n):** 2
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | success | [1.3553 3.374] | 0.183 | 0.000476 | 10 | Optimization terminated successfully. |
| CG | success | [2.3201 3.7121] | 0.183 | 0.000532 | 10 | Optimization terminated successfully. |
| CG | success | [2.0328 3.0971] | 0.183 | 0.000381 | 9 | Optimization terminated successfully. |
| BFGS | success | [1.5674 2.8827] | 1.36e-11 | 0.000628 | 18 | Optimization terminated successfully. |
| BFGS | success | [1.9553 3.0633] | 3.28e-15 | 0.000743 | 20 | Optimization terminated successfully. |
| BFGS | success | [1.9538 2.8843] | 9.15e-17 | 0.000814 | 19 | Optimization terminated successfully. |
| dogleg | success | [2.1057 2.7908] | 2.55e-11 | 0.000373 | 9 | Optimization terminated successfully. |
| dogleg | success | [2.2743 2.8977] | 1.93e-18 | 0.000363 | 10 | Optimization terminated successfully. |
| dogleg | success | [2.355 3.0155] | 3.36e-16 | 0.000367 | 10 | Optimization terminated successfully. |
| trust-ncg | fail | [1.6834 2.8055] | 0.113 | 0.000709 | 31 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [1.9284 3.3546] | 0.158 | 0.000953 | 45 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [2.3491 3.1941] | 0.186 | 0.000874 | 36 | A bad approximation caused failure to predict improvement. |
