#!/usr/bin/env python3

from functools import lru_cache

from bioinf_common import *


def num_matchings(rna):
    @lru_cache(None)
    def nm(a, b):
        if b < a:
            return 1

        s = nm(a+1, b)
        for k in range(a+1, b+1):
            if base_pairs_rna[rna[k]] != rna[a]: continue
            s += nm(a+1, k-1) * nm(k+1, b)

        return s

    return nm(0, len(rna)-1)


ds = get_dataset()
rna = list(from_fasta(ds).values())[0]
m = 1_000_000

nm = num_matchings(rna) % m
print(nm)
