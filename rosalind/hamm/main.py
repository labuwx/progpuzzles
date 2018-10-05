#!/usr/bin/env python3

from sys import argv


ds = open(argv[1]).read().strip()
s1, s2 = ds.split()

dist = sum(1 for a, b in zip(s1, s2) if a != b)

print(dist)
