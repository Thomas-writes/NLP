# KSIP

## Reproducibility
- **pycutest version:** 1.8.0
- **python:** 3.12.5
- **machine:** M3 Macbook Pro, Sequoia V15.6.1
- **tolerances:** 20 minute time limit

## General Info
- **Notes:** 
- **Last Updated:** 2026-03-03

## Classification
- **Convexity:** Convex
- **Objective Type:** quadratic
- **# of Variables (n):** 20
- **# of Constraints (m):** 1001
- **Bounds type: Type 2** 

## Runs
| method | success | start | f | time | iters | messages |
|:------|:--------:|:------|------:|------:|------:|:------|
| trust-constr | success | [2.0673 2.1399 2.1148 1.98 1.9549 1.8072 2.0959 1.8875 2.0666 1.827 2.2443 1.6226 1.7769 1.9347 2.5201 1.9423 1.9625 2.2062 1.9343 2.2907] | 0.576 | 51.8 | 139 | `gtol` termination condition is satisfied. |
| trust-constr | success | [2.1282 2.1212 2.0746 2.0618 1.9681 1.9367 2.3166 1.9802 2.218 1.7729 2.1358 2.1773 2.102 2.149 1.8248 2.2457 2.2862 1.7214 2.0361 1.626] | 0.576 | 45.7 | 108 | `gtol` termination condition is satisfied. |
| trust-constr | success | [2.3419 1.8553 2.0542 2.0452 2.1886 2.1269 2.0571 1.8289 1.8743 2.2275 2.2637 2.1336 2.1325 2.0439 1.7794 2.1252 2.1738 1.984 1.7721 1.7317] | 0.576 | 49 | 117 | `gtol` termination condition is satisfied. |
| SLSQP | success | [2.3476 2.4387 1.8651 2.3004 1.8572 2.1043 1.9839 1.6906 1.8935 2.1202 1.9468 2.1301 2.2111 1.9138 2.0929 1.7862 1.9007 2.3394 1.9852 2.0588] | 0.576 | 0.0671 | 23 | Optimization terminated successfully |
| SLSQP | success | [1.9684 2.2363 2.0208 2.135 1.7091 1.8662 1.8825 2.2199 2.1153 2.1095 2.2576 1.9713 2.2985 1.8603 2.3392 2.3525 2.2143 2.1258 1.9699 2.0281] | 0.576 | 0.0583 | 21 | Optimization terminated successfully |
| SLSQP | success | [1.9471 1.9188 2.0162 2.2854 2.1062 1.8622 1.9066 1.9646 1.7562 2.0534 2.183 1.9515 1.7099 2.1431 2.0489 1.6856 2.5852 2.0203 1.9674 2.1955] | 0.576 | 0.0646 | 23 | Optimization terminated successfully |
| COBYLA | success | [2.0917 2.1711 1.9077 2.0748 2.2794 2.1735 2.0335 1.7112 2.0219 1.8888 1.844 1.9569 2.1235 1.9456 1.7241 2.3295 1.9537 2.5696 2.0083 2.1137] | 0.576 | 16.6 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [2.0172 2.1508 2.2409 1.8411 1.9202 2.122 1.8798 1.9902 1.8399 1.9645 2.125 2.2215 1.9217 2.3004 1.9897 2.1577 1.7935 1.7226 2.0387 2.1193] | 0.576 | 20 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
| COBYLA | success | [1.5402 2.1974 2.1732 2.32 1.7042 1.5922 1.9586 1.7843 1.9727 1.9292 2.3463 2.2452 2.0654 2.0029 2.0582 1.9408 1.7611 1.8337 1.9676 2.2065] | 0.576 | 14.6 | None | Return from COBYLA because the trust region radius reaches its lower bound. |
