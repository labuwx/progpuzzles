#!/usr/bin/env python3

from bioinf_common import *


def maxgap_alignments(s1, s2, gs=0, sf=None):
    if sf == None:
        sf = lambda c1, c2: 1 if c1 == c2 else 0

    n1, n2 = len(s1), len(s2)
    cache = [[None for _ in range(n2 + 1)] for __ in range(n1 + 1)]
    row = [(0, 0)]
    for j in range(1, n2 + 1):
        row.append((gs * j, j))
    for i in range(1, n1 + 1):
        prow, row = row, [(gs * i, i)]
        for j in range(1, n2 + 1):
            l = [
                (prow[j][0] + gs, prow[j][1] + 1),
                (row[j - 1][0] + gs, row[j - 1][1] + 1),
                (prow[j - 1][0] + sf(s1[i - 1], s2[j - 1]), prow[j - 1][1]),
            ]
            m = max(r[0] for r in l)
            s = max(r[1] for r in l if r[0] == m)
            row.append((m, s))

    return row[-1][1]


ds = get_dataset()
p1, p2 = from_fasta(ds).values()
print(len(p1), len(p2), len(p1) * len(p2))

mg = maxgap_alignments(p1, p2)

print(mg)
