#!/usr/bin/env python3

import numpy as np


input = np.loadtxt('input', dtype=int)

cnt1 = 0
for l in input:
    a, b, c = sorted(l)
    if a + b > c:
        cnt1 += 1

cnt2 = 0
for l in input.T.reshape(input.shape[0], 3):
    a, b, c = sorted(l)
    if a + b > c:
        cnt2 += 1

print(cnt1)
print(cnt2)
