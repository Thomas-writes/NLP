# KOEBHELB

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
| L-BFGS-B | success | [7.5322 0.31806 0.001] | 114.17234411325983 | 0.00015483300376217812 | 0 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [10.838 0.44585 0.001] | 114.17234411325983 | 9.487499482929707e-05 | 0 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | fail | [9.2176 -0.78878 0.75298] | 114.17234411325983 | 0.00031637499341741204 | 0 | ABNORMAL:  |
| TNC | fail | [9.7923 -1.2259 3.3793] | 114.17234411325983 | 0.00039004100835882127 | 0 | Linear search failed |
| TNC | success | [9.8176 1.3033 0.001] | 114.17234411325983 | 9.829200280364603e-05 | 1 | Local minimum reached (|pg| ~= 0) |
| TNC | fail | [10.235 0.25078 0.32798] | 114.17234411325983 | 0.0003792079951381311 | 0 | Linear search failed |
| Powell | success | [10.519 0.59781 0.60224] | 114.17234411325983 | 0.0008738329925108701 | 1 | Optimization terminated successfully. |
| Powell | success | [10.37 0.87453 0.001] | 114.17234411325983 | 0.0006816670065745711 | 1 | Optimization terminated successfully. |
| Powell | success | [9.1497 -1.0766 0.001] | 114.17234411325983 | 0.0017203339957632124 | 2 | Optimization terminated successfully. |
| Nelder-Mead | success | [9.4597 0.8732 0.001] | 114.17234411325983 | 0.0004402499907882884 | 14 | Optimization terminated successfully. |
| Nelder-Mead | success | [11.229 -1.6053 0.001] | 112.2244365828551 | 0.0009440830035600811 | 64 | Optimization terminated successfully. |
| Nelder-Mead | success | [10.012 0.83469 0.001] | 114.17234411325983 | 0.00042383300024084747 | 14 | Optimization terminated successfully. |
