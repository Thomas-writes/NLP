# PSPDOC

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-02

## Classification
- **Convexity:** Convex
- **Objective Type:** sum of squares
- **# of Variables (n):** 4
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [-1 3.4124 3.6087 3.137] | 2.414213562373261 | 0.00029312500555533916 | 11 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [-1 2.8984 2.7173 2.9013] | 2.4142135623781624 | 0.0002127499901689589 | 11 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| L-BFGS-B | success | [-1 3.6138 3.1034 3.0805] | 2.414213562395463 | 0.0002103750011883676 | 11 | CONVERGENCE: NORM OF PROJECTED GRADIENT <= PGTOL |
| TNC | fail | [-1 2.4656 2.9205 3.2497] | 4.166543479604343 | 0.0002876670041587204 | 0 | Linear search failed |
| TNC | fail | [-1 3.0536 2.2491 2.9798] | 4.922261003119665 | 0.00026020800578407943 | 0 | Linear search failed |
| TNC | fail | [-1 3.0849 2.4875 2.6662] | 4.783130804683827 | 0.0002384999970672652 | 0 | Linear search failed |
| Powell | success | [-1 3.161 2.771 2.8337] | 2.414255062317139 | 0.003892749999067746 | 4 | Optimization terminated successfully. |
| Powell | success | [-1 2.8024 2.796 3.0507] | 2.4142577272865955 | 0.005549334004172124 | 4 | Optimization terminated successfully. |
| Powell | success | [-1 3.9679 2.3642 3.2419] | 2.41425401318665 | 0.004053666998515837 | 4 | Optimization terminated successfully. |
| Nelder-Mead | success | [-1 2.7733 2.8474 2.9352] | 2.414213612878913 | 0.0031285000004572794 | 247 | Optimization terminated successfully. |
| Nelder-Mead | success | [-1 3.0666 2.8829 2.9928] | 2.414215989652174 | 0.003387958000530489 | 274 | Optimization terminated successfully. |
| Nelder-Mead | success | [-1 2.9445 2.5927 2.6628] | 2.414213609131436 | 0.0027547089994186535 | 230 | Optimization terminated successfully. |
