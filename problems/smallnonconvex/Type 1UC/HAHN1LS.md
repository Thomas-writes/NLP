# HAHN1LS

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Nonconvex
- **Objective Type:** sum of squares
- **# of Variables (n):** 7
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [11.025 -0.31781 -0.72771 0.31841 0.4023 -0.51412 -1.1045] | 44.1 | 0.0802 | 1173 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [8.9325 -0.07227 -0.15376 1.9244 -1.562 0.56883 1.4841] | 55.6 | 0.0833 | 1400 | Maximum number of iterations has been exceeded. |
| CG | fail | [10.104 -1.2587 2.5402 -0.85132 1.4457 -0.41474 1.0493] | 41 | 0.0916 | 1400 | Maximum number of iterations has been exceeded. |
| BFGS | fail | [10.424 -1.4368 0.20743 0.3169 0.016938 -0.89801 -1.2424] | 31.6 | 0.00723 | 185 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [8.9417 -2.8173 0.64935 1.1496 0.34147 1.3514 0.10124] | 1.53 | 0.0108 | 201 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [9.159 -0.66869 0.4442 -0.64855 -1.1911 0.81672 -0.23553] | 31.6 | 0.00604 | 148 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [10.446 0.93565 0.65509 -1.1598 1.4524 1.42 -0.22518] | 2.71e+04 | 0.000169 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [9.6632 -0.18031 0.91109 -0.10778 -1.4298 -1.9436 -0.010168] | 2.08e+04 | 0.00011 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [9.2092 -1.0555 0.8481 0.77915 -2.5674 0.34752 0.88359] | 4.98e+04 | 0.000106 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [10.745 -0.38506 -2.0061 -0.41598 2.3358 1.1828 -1.321] | 5.34e+04 | 0.00496 | 53 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [9.7797 -0.69493 1.1018 1.0869 -1.2708 -1.2724 -0.029699] | 9.35e+04 | 0.00113 | 10 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [9.7884 -0.19387 -0.6902 2.6156 -0.82377 -2.0869 -0.5851] | 6.08e+04 | 0.000922 | 8 | A bad approximation caused failure to predict improvement. |
