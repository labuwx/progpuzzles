#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
s, t = ds.split()

super_seq = scsq(s, t)

print(super_seq)
