#!/usr/bin/env python3

from bioinf_common import *


def nxx(S, x):
    sl = sum(len(s) for s in S)
    ml = max(len(s) for s in S)
    res = max(
        k for k in range(1, ml + 1) if sum(len(s) for s in S if len(s) >= k) >= x * sl
    )
    return res


ds = get_dataset()
S = ds.split()

n50 = nxx(S, 0.5)
n75 = nxx(S, 0.75)

print(n50, n75)
