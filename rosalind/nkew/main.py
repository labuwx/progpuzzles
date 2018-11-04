#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
lines = [l for l in ds.split('\n') if l]
inp = [(g, nodes.split()) for g, nodes in zip(lines[::2], lines[1::2])]

distances = []
for nws, (u, v) in inp[:]:
    g = from_newick(nws)
    d = nw_distance(g, u, v)
    distances.append(d)

print(*distances)
