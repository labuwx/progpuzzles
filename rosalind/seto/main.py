#!/usr/bin/env python3

from ast import literal_eval

from bioinf_common import *


ds = get_dataset()
lines = ds.split('\n')
n = int(lines[0])
u = set(range(1, n + 1))
a, b = (literal_eval(l) for l in lines[1:])

print(a | b)
print(a & b)
print(a - b)
print(b - a)
print(u - a)
print(u - b)
