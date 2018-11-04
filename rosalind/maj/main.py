#!/usr/bin/env python3

from bioinf_common import *


def majority(l, default=None):
    assert None not in l
    k, m = 0, None
    for x in l:
        if k == 0:
            m = x
        k += 1 if x == m else -1

    if l.count(m) <= len(l)//2:
        m = default

    return m


ds = get_dataset().split('\n')
L = [[int(x) for x in l.split()] for l in ds[1:]]
maj =[majority(l, default=-1) for l in L]

print(*maj)
