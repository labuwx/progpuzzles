#!/usr/bin/env python3

from sys import argv


ds = open(argv[1]).read()
a, b = [int(x) for x in ds.split()]

s = sum(n for n in range(a, b+1) if n%2)

print(s)


