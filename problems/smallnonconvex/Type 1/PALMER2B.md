# PALMER2B

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
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.1057 1.1056 1.0428 0.97562] | 0.6232669722013188 | 0.0006675830227322876 | 31 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.91155 0.99639 1.0105 0.90729] | 0.6232669721662514 | 0.0009011669899336994 | 29 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.89626 1.0364 0.8713 0.88934] | 0.6232669721715498 | 0.0006197919719852507 | 31 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [0.85557 0.98414 0.96525 1.0547] | 11325.494779971701 | 0.00042683404171839356 | 1 | Linear search failed |
| TNC | fail | [1.0673 1.1421 0.89514 0.96735] | 10574.675346796152 | 0.0004123340477235615 | 1 | Linear search failed |
| TNC | fail | [1.0779 1.4415 1.0564 1.129] | 9653.301693329158 | 0.0004077079938724637 | 1 | Linear search failed |
| Powell | success | [0.90589 0.93976 0.90591 0.97823] | 1466.6640501304219 | 0.004270415985956788 | 8 | Optimization terminated successfully. |
| Powell | success | [1.0165 1.0755 1.0288 0.78773] | 1373.8704133153988 | 0.004384082974866033 | 8 | Optimization terminated successfully. |
| Powell | success | [1.1578 0.92319 0.97297 0.6683] | 1481.9649746943821 | 0.004509416990913451 | 8 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0469 0.9966 0.94722 0.90627] | 14.172289768966218 | 0.0029573749634437263 | 225 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.059 0.94653 1.0958 1.1384] | 0.6232669765152268 | 0.0041690419893711805 | 360 | Optimization terminated successfully. |
| Nelder-Mead | fail | [0.96965 0.99779 1.0933 1.1069] | 0.6232669803489125 | 0.005739167041610926 | 470 | Maximum number of function evaluations has been exceeded. |
