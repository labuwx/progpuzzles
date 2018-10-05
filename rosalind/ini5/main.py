#!/usr/bin/env python3

from sys import argv


ds = open(argv[1]).read()

lines = ds.split('\n')
s = '\n'.join(lines[1::2])

print(s)
