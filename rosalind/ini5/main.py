#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()

lines = ds.split('\n')
s = '\n'.join(lines[1::2])

print(s)
