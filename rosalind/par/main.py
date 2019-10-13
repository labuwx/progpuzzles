#!/usr/bin/env python3

from bioinf_common import *


def split(l, p):
    ll = [x for x in l if x < p] + [x for x in l if x == p] + [x for x in l if p < x]
    return ll


ds = get_dataset()
A = [int(x) for x in ds.split()[1:]]

l = split(A, A[0])
print(*l)
