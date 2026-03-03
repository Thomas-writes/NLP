# PALMER8A

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
- **# of Variables (n):** 6
- **# of Constraints (m):** 0
- **Bounds type: Type 1** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| L-BFGS-B | success | [1.0472 1.0981 1.1028 0.93445 0.97346 0.93888] | 0.07400969804401865 | 0.0016791250091046095 | 94 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.1069 0.96633 1.1077 1.0598 1.0548 0.98535] | 0.07400970114826672 | 0.0017753749998519197 | 109 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| L-BFGS-B | success | [1.0687 1.1848 0.93965 1.0122 1.0801 1.0411] | 0.07400969795229642 | 0.0013580419908976182 | 77 | CONVERGENCE: RELATIVE REDUCTION OF F <= FACTR*EPSMCH |
| TNC | fail | [1.1494 1.073 1.0703 0.96616 1.0353 1.0457] | 10136.865475122066 | 0.0004239160043653101 | 1 | Linear search failed |
| TNC | fail | [1.056 1.0205 0.84288 1.0376 1.0255 0.95157] | 10329.502927582551 | 0.0004257499967934564 | 1 | Linear search failed |
| TNC | fail | [1.0291 0.97836 1.2057 0.98786 0.90059 0.95566] | 9942.606988598396 | 0.0004152920009801164 | 1 | Linear search failed |
| Powell | success | [0.83295 1.0373 0.92361 0.96468 0.88895 1.11] | 6.969710550431914 | 0.013232458994025365 | 18 | Optimization terminated successfully. |
| Powell | success | [1.0495 1.1537 0.97274 1.0334 1.1489 1.0129] | 6.96976086348158 | 0.01239929100847803 | 19 | Optimization terminated successfully. |
| Powell | success | [1.0874 1.0178 1.0659 0.99411 1.1028 0.92969] | 77.23179902997984 | 0.015207333999569528 | 16 | Optimization terminated successfully. |
| Nelder-Mead | success | [1.0979 1.1371 0.94355 1.0903 0.81063 0.99815] | 6.955776197169085 | 0.006032667006365955 | 508 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.82258 0.90687 0.95043 0.88564 0.9093 0.86405] | 4.641766352863065 | 0.0052966670045861974 | 454 | Optimization terminated successfully. |
| Nelder-Mead | success | [0.87561 0.83512 1.0758 0.78916 0.97537 0.90376] | 4.641766353347284 | 0.005425416995421983 | 455 | Optimization terminated successfully. |
