#!/usr/bin/env python3

import heapsort
from bioinf_common import *


ds = get_dataset()
A = [int(x) for x in ds.split()[1:]]

l = heapsort.sort(A)

print(*l)
