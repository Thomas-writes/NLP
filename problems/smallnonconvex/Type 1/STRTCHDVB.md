# STRTCHDVB

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
- **# of Variables (n):** 10
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [0.99122 -1.0627 -1.0685 -0.88947 -1.0151 -1.1087 -1.1149 -1.001 -0.99828 -1.0404] | 8.948251862812872e-09 | 0.0038954169722273946 | 20 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [1.1029 -1.0652 -0.92209 -1.0814 -0.99805 -0.93606 -1.0371 -0.95398 -1.0261 -1.1402] | 2.370112653446758e-08 | 0.000423458986915648 | 18 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [1.044 -0.96734 -0.9771 -1.0283 -1.0694 -1.0437 -1.0088 -1.0058 -0.72238 -0.93562] | 2.5177009327699922e-08 | 0.0007702080183662474 | 41 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [0.83744 -0.96829 -0.97144 -1.0957 -0.92102 -0.99012 -1.0045 -0.95423 -0.94044 -1.1413] | 1.8971335086828408e-09 | 0.001048958976753056 | 13 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [0.95397 -1.1236 -0.92443 -1.0656 -1.1184 -1.1645 -1.162 -0.96314 -1.2573 -1.0523] | 3.585278267165487e-09 | 0.00047624995931982994 | 11 | Converged (|f_n-f_(n-1)| ~= 0) |
| TNC | success | [1.0573 -0.89421 -1.0598 -1.0358 -0.99627 -0.93728 -1.0418 -0.89133 -1.223 -0.88067] | 1.4630907800992876e-09 | 0.0005070000188425183 | 11 | Converged (|f_n-f_(n-1)| ~= 0) |
| Powell | success | [1.044 -1.1266 -0.87768 -0.89535 -1.0326 -0.99991 -0.95875 -0.95255 -1.0265 -0.93945] | 2.8571100695049288e-06 | 0.004031499964185059 | 4 | Optimization terminated successfully. |
| Powell | success | [1.0771 -1.0249 -0.82848 -0.86725 -1.0573 -0.96469 -0.95672 -1.0627 -0.817 -0.9522] | 0.6814951106017181 | 0.0028399580041877925 | 3 | Optimization terminated successfully. |
| Powell | success | [1.0444 -1.0646 -1.0188 -0.88339 -1.1213 -0.90666 -1.0205 -0.95957 -0.98573 -0.93988] | 2.8725586929798857e-06 | 0.0026022089878097177 | 3 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0697 -1.0046 -1.1824 -1.0511 -1.1894 -0.85632 -1.0583 -0.83328 -0.87136 -0.92145] | 4.8502032712491175e-09 | 0.013032125018071383 | 1117 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.88537 -1.0191 -0.94743 -0.99096 -0.89566 -0.84891 -1.058 -0.98712 -1.0002 -1.1034] | 6.368932362670372e-14 | 0.009812875010538846 | 871 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.95867 -1.0105 -1.2131 -0.88779 -1.0083 -0.93083 -0.94281 -1.1063 -0.95139 -1.0485] | 1.7535801649743656e-12 | 0.011218749976251274 | 978 | Optimization terminated successfully. |
