#!/usr/bin/env python3

from sys import argv

from codon_map import codon_map


dna = open(argv[1]).read().strip()

prots = []
for i in range(0, len(dna)//3):
    codon = dna[3*i: 3*i+3]
    prot = codon_map[codon]
    if prot is not None:
        prots.append(prot)

print(''.join(prots))
