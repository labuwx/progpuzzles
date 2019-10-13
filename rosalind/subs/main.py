#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
s, p = ds.split()

idx = [i + 1 for i in range(len(s)) if s.startswith(p, i)]

print(*idx)
