# PALMER1B

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
| L-BFGS-B | success | [0.98268 0.96252 0.87807 0.98468] | 3.4473546323755784 | 0.0008659590384922922 | 44 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0548 1.1345 0.95219 1.0553] | 3.4473546305530784 | 0.0008307499811053276 | 46 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [0.9806 1.0814 0.99403 0.83765] | 3.4473546305350666 | 0.0006864999886602163 | 36 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | success | [0.99018 1.1327 0.94522 0.86737] | 44714.22030972295 | 0.00010637502418830991 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [1.0076 0.97429 1.0465 1.0303] | 44728.91366317709 | 8.549995254725218e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| TNC | success | [0.99254 0.98584 0.80241 1.0666] | 44724.58891956055 | 8.724996587261558e-05 | 1 | Converged (|x_n-x_(n-1)| ~= 0) |
| Powell | success | [0.98922 1.084 1.0257 1.0089] | 33178.97682776875 | 0.004634084005374461 | 10 | Optimization terminated successfully. |
| Powell | success | [1.0786 1.1533 0.893 0.85022] | 33472.154306485376 | 0.004953000054229051 | 10 | Optimization terminated successfully. |
| Powell | success | [1.1098 1.1167 1.0905 0.93467] | 33395.49840387356 | 0.004693916998803616 | 10 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.024 1.16 0.84495 1.0228] | 119.24607862312934 | 0.00291387498145923 | 229 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.92915 1.1065 1.0294 0.97196] | 6.0891854357713635 | 0.003434583020862192 | 278 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0484 1.1117 1.1221 1.0578] | 4.352649515125863 | 0.003626750025432557 | 297 | Optimization terminated successfully. |
