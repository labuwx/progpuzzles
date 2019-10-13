#!/usr/bin/env python3

from collections import defaultdict
import itertools as it

from bioinf_common import *


def best_motif(chains):
    cache = defaultdict(lambda: ('', 0))
    idxs = it.product(*(range(len(c)) for c in chains))
    for idx in idxs:
        b = [c[i] for i, c in zip(idx, chains)]
        bs = set(b)
        p_idx = tuple(i - 1 for i in idx)
        pp, ps = cache[p_idx]
        np = b[0] if len(bs) == 1 else r'[%s]' % ''.join(bs)
        ns = len(b) - len(bs)
        cache[idx] = (pp + np, ps + ns)
    best = max(cache.values(), key=lambda x: x[1])
    return best


ds = get_dataset()
chains = list(from_fasta(ds).values())
motif = best_motif(chains)

pprint(motif)
