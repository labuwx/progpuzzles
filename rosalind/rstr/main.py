#!/usr/bin/env python3

from operator import mul
from functools import reduce

from bioinf_common import *


ds = get_dataset().split()
n, x = int(ds[0]), float(ds[1])
dna = ds[2]

p0 = reduce(mul, (x/2 if b in ['C', 'G'] else (1-x)/2 for b in dna), 1)
p = 1 - (1-p0)**n

print(p)
