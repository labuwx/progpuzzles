#!/usr/bin/env python3

from pphelp import *


k = 0
num, denom = 1, 2
for _ in range(1000):
    tnum, tdenom = simplify(num+denom, denom)
    if len(digits(tnum)) > len(digits(tdenom)):
        k += 1
    num += 2 * denom
    num, denom = simplify(denom, num)

print(k)
