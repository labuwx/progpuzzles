#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
chains = list(from_fasta(ds).values())

dna = chains[0]
introns = chains[1:]

exons = get_exons(dna, introns)
mrna = dna2rna(exons)
prot = rna2prot(mrna)

print(prot)
