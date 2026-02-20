# NASH

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
- **# of Variables (n):** 18
- **# of Constraints (m):** 24
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| SLSQP | fail | [-0.194 0.0583 -0.147 -0.0979 -0.116 0.119 -0.116 -0.0582 -0.159 0.026 -0.135 0.107 0.307 0.0671 -0.179 -0.00646 -0.013 0.251] | 0 | 0.000444 | 1 | More equality constraints than independent variables |
| SLSQP | fail | [-0.0294 0.145 0.12 -0.0512 0.0813 -0.211 -0.0634 0.0641 0.0891 0.0179 -0.000762 0.0559 0.125 0.119 0.125 0.0412 0.0891 0.12] | 0 | 0.000375 | 1 | More equality constraints than independent variables |
| SLSQP | fail | [-0.0581 -0.115 -0.148 0.0858 0.00696 0.0254 0.0114 -0.0937 -0.139 0.0242 0.0654 -0.0224 0.0929 -0.0602 -0.19 -0.0382 0.0662 -0.247] | 0 | 0.000347 | 1 | More equality constraints than independent variables |
| COBYLA | fail | [-0.155 -0.00222 0.0918 -0.101 0.0242 -0.009 -0.118 -0.0112 -0.0313 0.0457 0.0819 0.113 0.0552 -0.0693 -0.00731 -0.018 -0.0359 -0.00715] | 0 | 0.589 | None | Did not converge to a solution satisfying the constraints. See `maxcv` for the magnitude of the violation. |
| COBYLA | fail | [0.0675 0.0543 -0.129 0.084 0.0305 0.0209 0.0348 -0.0417 -0.115 -0.22 -0.00454 0.0142 -0.19 -0.0354 0.0984 -0.21 0.055 -0.0216] | 0 | 0.594 | None | Did not converge to a solution satisfying the constraints. See `maxcv` for the magnitude of the violation. |
| COBYLA | fail | [0.177 -0.00497 -0.0053 -0.0898 -0.0652 0.0313 0.0539 0.103 0.0128 -0.0847 -0.126 -0.00326 -0.0541 -0.00874 -0.000965 -0.0389 -0.0202 -0.266] | 0 | 0.595 | None | Did not converge to a solution satisfying the constraints. See `maxcv` for the magnitude of the violation. |
