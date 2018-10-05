#!/usr/bin/env python3

from sys import argv


ds = open(argv[1]).read().strip()
bmap = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

revc = ''.join(bmap[b] for b in reversed(ds))

print(revc)
