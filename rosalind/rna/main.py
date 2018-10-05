#!/usr/bin/env python3

from collections import Counter
from sys import argv


ds = open(argv[1]).read().strip()
rna = ds.replace('T', 'U')

print(rna)
