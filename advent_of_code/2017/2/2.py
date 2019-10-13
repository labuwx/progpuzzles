#!/usr/bin/env python3

import itertools as it
import numpy as np


input = np.loadtxt('input', delimiter='\t', dtype=int)

imin = input.min(axis=1)
imax = input.max(axis=1)
s1 = (imax - imin).sum()

s2 = 0
for line in input:
    for a, b in it.combinations(line, 2):
        if a % b == 0:
            s2 += a // b
            break
        if b % a == 0:
            s2 += b // a
            break

print(s1)
print(s2)
