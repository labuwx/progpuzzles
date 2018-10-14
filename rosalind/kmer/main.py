#!/usr/bin/env python3

from collections import defaultdict
import itertools as it

from bioinf_common import *


ds = get_dataset()
dna = list(from_fasta(ds).values())[0]
alphabet = sorted(list(base_pairs.keys()))
k = 4

freq = defaultdict(int)
for i in range(len(dna)-k+1):
    kmer = dna[i:i+k]
    freq[kmer] += 1

print(*(
    freq[''.join(kmer)]
    for kmer in it.product(alphabet, repeat=k)
))
