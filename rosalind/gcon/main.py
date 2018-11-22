#!/usr/bin/env python3

from math import inf

from bioinf_common import *


def spec_edist(s1, s2):
    gs = -5

    n1, n2 = len(s1), len(s2)
    cache = [[None for _ in range(n2 + 1)] for __ in range(n1 + 1)]
    cache[0][0] = (0, -inf, -inf)
    # for i in range(1, n1 + 1): cache[i][0] = (-inf, gs, -inf)
    # for j in range(1, n2 + 1): cache[0][j] = (-inf, -inf, gs)
    for i in range(1, n1 + 1): cache[i][0] = (-inf, -inf, gs)
    for j in range(1, n2 + 1): cache[0][j] = (-inf, gs, -inf)
    for i, j in it.product(range(1, n1 + 1), range(1, n2 + 1)):
        cache[i][j] = (
            max(
                cache[i-1][j][0],
                cache[i-1][j][1] + gs,
                cache[i-1][j][2] + gs
            ),
            max(
                cache[i][j-1][0] + gs,
                cache[i][j-1][1],
                cache[i][j-1][2] + gs
            ),
            max(cache[i-1][j-1]) + blosum62_scores[(s1[i-1], s2[j-1])]
        )

    # for row in cache:
        # print('\t'.join(str(e) for e in row))

    return max(cache[-1][-1])


ds = get_dataset()
p1, p2 = from_fasta(ds).values()
# p1, p2 = 'WWW', 'DNP'

edist = spec_edist(p2, p1)
print(edist)
