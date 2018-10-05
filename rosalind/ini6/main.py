#!/usr/bin/env python3

import collections
from sys import argv


ds = open(argv[1]).read()

cnt = collections.Counter(ds.split())

for w, n in cnt.items():
    print(w, n)


