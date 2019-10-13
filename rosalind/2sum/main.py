#!/usr/bin/env python3

from collections import defaultdict

from bioinf_common import *


ds = get_dataset().split('\n')
A = [[int(x) for x in l.split()] for l in ds[1:]]

for l in A:
    iperm = sorted(range(len(l)), key=lambda i: l[i])
    i, j = 0, len(l) - 1
    while i < j:
        s = l[iperm[i]] + l[iperm[j]]
        if s == 0:
            break
        elif s < 0:
            i += 1
        else:
            j -= 1

    if i == j:
        print(-1)
    else:
        i, j = sorted(iperm[m] for m in (i, j))
        print(i + 1, j + 1)
