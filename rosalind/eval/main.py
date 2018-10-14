#!/usr/bin/env python3

from operator import mul
from functools import reduce

from bioinf_common import *


ds = get_dataset().split('\n')
n, s = int(ds[0]), ds[1]
l = len(s)
gcc = (float(x) for x in ds[2].split())

P0 = (reduce(mul, (x/2 if b in ['C', 'G'] else (1-x)/2 for b in s), 1)
      for x in gcc)

E = [(n-l+1)*p for p in P0]

print(*E)
