#!/usr/bin/env python3

import collections

from bioinf_common import *


ds = get_dataset()

cnt = collections.Counter(ds.split())

for w, n in cnt.items():
    print(w, n)
