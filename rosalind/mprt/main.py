#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
prots = from_uniprot(ds.split())

pattern = r'N{P}[ST]{P}'
searcher = pmotif_search(pattern)

for id, chain in prots.items():
    idx = searcher(chain)
    if idx:
        print(id)
        print(*idx)
