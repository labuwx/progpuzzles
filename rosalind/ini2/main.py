#!/usr/bin/env python3

from sys import argv


ds = open(argv[1]).read()
a, b = [int(x) for x in ds.split()]

c2 = a**2 + b**2

print(c2)
