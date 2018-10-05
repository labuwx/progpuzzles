#!/usr/bin/env python3

from sys import argv


ds = open(argv[1]).read().strip()
s, p = ds.split()

idx = [i+1 for i in range(len(s)) if s.startswith(p, i)]

print(*idx)
