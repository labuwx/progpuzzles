#!/usr/bin/env python3

from math import log

from bioinf_common import *


ds = get_dataset()
lines = ds.split('\n')
dna = lines[0]
gc_conts = [float(x) for x in lines[1].split()]

res = [
    sum(log(gcc / 2 if b in ['G', 'C'] else (1 - gcc) / 2, 10) for b in dna)
    for gcc in gc_conts
]

print(*res)
