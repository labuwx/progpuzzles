#!/usr/bin/env python3

from collections import Counter
from sys import argv


ds = open(argv[1]).read().strip()
cnt = Counter(ds)

print(cnt['A'], cnt['C'], cnt['G'], cnt['T'])
