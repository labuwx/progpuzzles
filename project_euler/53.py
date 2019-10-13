#!/usr/bin/env python3

from pphelp import *


k = 0
limit = 1_000_000
for n in range(101):
    r_min = next((r for r in range(n + 1) if nCr(n, r) > limit), None)
    if r_min != None:
        k += n + 1 - 2 * r_min

print(k)
