#!/usr/bin/env python3

from math import factorial

from bioinf_common import *


ds = get_dataset()
n, k = (int(x) for x in ds.split())
m = 1_000_000

res = factorial(k) * nCr(n, k) % m
print(res)
