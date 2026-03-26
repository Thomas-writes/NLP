# VESUVIOLS

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
- **Objective Type:** sum of squares
- **# of Variables (n):** 8
- **# of Constraints (m):** 0
- **Bounds type: Type 1UC** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| CG | fail | [-0.076834 0.015794 0.006333 0.18678 -0.079742 0.092866 -0.086803 0.01262] | 3.31e+03 | 0.189 | 895 | Desired error not necessarily achieved due to precision loss. |
| CG | fail | [0.10444 -0.024683 -0.072581 -0.05454 -0.08896 0.20749 -0.043889 0.11444] | 1.5e+03 | 0.296 | 1600 | Maximum number of iterations has been exceeded. |
| CG | fail | [0.010711 -0.067162 -0.067685 -0.047517 0.089617 0.11186 0.11858 -0.074942] | 3.45e+03 | 0.133 | 582 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [0.11945 -0.19769 -0.13793 0.11413 0.027225 6.7249e-06 0.03403 -0.14526] | 3.46e+03 | 0.00668 | 40 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-0.17035 -0.036209 0.037761 -0.03387 -0.11726 0.19264 -0.13847 -0.010303] | 1.5e+03 | 0.0309 | 231 | Desired error not necessarily achieved due to precision loss. |
| BFGS | fail | [-0.036224 0.035541 0.019712 -0.22582 -0.064569 0.060274 -0.018284 -0.078701] | 3.45e+03 | 0.0592 | 490 | Desired error not necessarily achieved due to precision loss. |
| dogleg | fail | [-0.023282 0.023233 0.0026164 0.0032897 -0.064148 0.23844 -0.052681 0.11392] | 6.83e+04 | 0.000506 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.12944 0.055147 -0.19687 -0.052597 0.13976 -0.1511 -0.13708 0.13125] | 6.2e+04 | 0.000329 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| dogleg | fail | [0.039561 -0.058535 0.041457 0.071243 -0.24336 0.05017 -0.019854 0.017689] | 1.94e+04 | 0.000323 | 0 | A linalg error occurred, such as a non-psd Hessian. |
| trust-ncg | fail | [-0.032803 -0.12067 0.10531 0.16997 -0.026281 0.1197 0.0042077 -0.0037433] | 4.43e+03 | 0.00459 | 15 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.01758 -0.065802 -0.027722 0.15959 0.19712 -0.00035123 0.071576 -0.10343] | 5.49e+03 | 0.00082 | 1 | A bad approximation caused failure to predict improvement. |
| trust-ncg | fail | [0.11115 -0.0346 0.0018049 0.068887 0.096908 -0.020138 0.093168 -0.053101] | 1.49e+04 | 0.00261 | 7 | A bad approximation caused failure to predict improvement. |
