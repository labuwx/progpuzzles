#!/usr/bin/env python3

from collections import Counter
from bioinf_common import *


ds = get_dataset()
nodes, edges = from_edgelist(ds)

cnt = Counter(u for e in edges for u in e)

print(*(cnt[i] for i in nodes))
