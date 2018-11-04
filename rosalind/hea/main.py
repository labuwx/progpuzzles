#!/usr/bin/env python3

import heapsort
from bioinf_common import *


ds = get_dataset()
A = [int(x) for x in ds.split()[1:]]

l = [(-1) * x for x in A]
h = heapsort.Heap(l)
l = [(-1) * x for x in h.d]

print(*l)
