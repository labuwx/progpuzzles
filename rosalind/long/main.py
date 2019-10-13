#!/usr/bin/env python3

from bioinf_common import *


def intersection(a, b):
    l = len(a)
    k = next(i for i in range(l + 1) if b.startswith(a[i:]))
    return a[:k], a[k:], b[l - k :]


def edge(e, f):
    return e == 'START' or len(intersection(e, f)[1]) > len(e) // 2


ds = get_dataset()
dna_l = list(from_fasta(ds).values())

order = topo_sort(dna_l, edge)
superstring = ''.join(intersection(a, b)[0] for a, b in zip(order, order[1:] + ['']))

print(superstring)
