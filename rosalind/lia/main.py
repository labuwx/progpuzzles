#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
k, n = (int(x) for x in ds.split())

s = 2 ** k
p = sum(nCr(s, i) * 3**(s-i) for i in range(n, s+1)) / 4**s

print(p)
