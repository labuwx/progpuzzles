#!/usr/bin/env python3

from collections import defaultdict
from sys import argv


def gc_cont(dna):
    gcs = sum(1 for x in dna if x in ['C', 'G'])
    return gcs / len(dna) * 100


ds = open(argv[1]).read().strip()
dna = defaultdict(str)

for l in ds.split('\n'):
    if l.startswith('>'):
        name = l[1:]
    else:
        dna[name] += l

results = ((name, gc_cont(chain)) for name, chain in dna.items())

ranked = sorted(results, key=lambda x: x[1])
winner = ranked[-1]

print(winner[0])
print(winner[1])
