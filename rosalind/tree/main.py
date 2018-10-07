#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
lines = ds.split('\n')
n = int(lines[0])
n_edges = len(lines) - 1

print(n-1 - n_edges)
