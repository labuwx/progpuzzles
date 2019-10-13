#!/usr/bin/env python3

from bioinf_common import *


def bin_search(l, x, default=None, start=0, end=None):
    if end == None:
        end = len(l)
    mid = start + (end - start) // 2
    p = l[mid]
    if start == end:
        return mid if p == x else default
    elif x <= p:
        return bin_search(l, x, default, start, mid)
    else:
        return bin_search(l, x, default, mid + 1, end)


ds = get_dataset().split('\n')
A = [int(x) for x in ds[2].split()]
K = [int(x) for x in ds[3].split()]

idxs = [bin_search(A, k, default=-2) + 1 for k in K]

print(*idxs)
