# LEVYMONT6

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
- **# of Variables (n):** 3
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [-7.8806 8.7759 9.3284] | 2.8684221661625715e-13 | 0.0006335000070976093 | 31 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [-7.1928 6.3742 8.9053] | 1.0366902025083415 | 0.00024329200095962733 | 9 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [-8.9562 7.9778 7.5223] | 1.7179455125818818e-12 | 0.0005324999947333708 | 32 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [-8.3453 6.618 8.2204] | 9.33771570834526 | 0.00023350000265054405 | 10 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [-8.8421 7.8662 9.5351] | 12.502860200858775 | 0.00021791701146867126 | 11 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [-9.1662 8.2088 8.1769] | 9.360525966711245 | 0.00031895800202619284 | 14 | Converged (|f_n-f_(n-1)| ~= 0) |
| Powell | success | [-8.2209 6.716 7.5534] | 3.1096420679608534 | 0.00044770899694412947 | 2 | Optimization terminated successfully. |
| Powell | success | [-9.3603 8.3676 8.8869] | 3.1096397872021533 | 0.0006607920076930895 | 3 | Optimization terminated successfully. |
| Powell | success | [-8.7982 6.7809 8.3378] | 3.1096420679608534 | 0.00040366699977312237 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [-7.1201 8.677 9.0005] | 12.502860235767779 | 0.0008294580038636923 | 58 | Optimization terminated successfully. |
| Nelder-Mead | success | [-7.0009 7.5254 7.0202] | 9.360525983458691 | 0.000868333998369053 | 67 | Optimization terminated successfully. |
| Nelder-Mead | success | [-6.8576 6.8451 7.397] | 9.337715727969881 | 0.0009365000005345792 | 76 | Optimization terminated successfully. |
