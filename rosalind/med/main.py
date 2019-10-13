#!/usr/bin/env python3

from bioinf_common import *


def quickselect(l, k):
    p = l[0]
    l1 = [x for x in l if x < p]
    l3 = [x for x in l if x > p]
    n1, n2 = len(l1), sum(1 for x in l if x == p)
    if k < n1:
        return quickselect(l1, k)
    elif k < n1 + n2:
        return p
    else:
        return quickselect(l3, k - n1 - n2)


ds = get_dataset()
*A, k = (int(x) for x in ds.split()[1:])

x = quickselect(A, k - 1)

print(x)
