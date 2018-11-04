#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset().split('\n')
A = [[int(x) for x in l.split()] for l in ds[1:]]

for l in A:
    llen = len(l)
    iperm = sorted(range(llen), key=lambda i: l[i])
    for i in range(llen-2):
        j, k = i+1, llen-1
        while j < k and l[iperm[i]] + l[iperm[j]] + l[iperm[k]] != 0:
            if l[iperm[i]] + l[iperm[j]] + l[iperm[k]] > 0:
                k -= 1
            else:
                j += 1

        if j != k:
            # print()
            # print(l[k], l[i], l[j])
            i, j, k = sorted(iperm[m] for m in (i, j, k))
            print(i+1, j+1, k+1)
            # print()
            break
    if j == k:
        print(-1)

