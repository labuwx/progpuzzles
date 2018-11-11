#!/usr/bin/env python3

import operator

from bioinf_common import *


# https://stackoverflow.com/questions/3992697/longest-increasing-subsequence
def longest_mon_subs(seq, increasing=True):
    M = [None] * len(seq)
    P = [None] * len(seq)
    L = 1
    M[0] = 0
    op = operator.lt if increasing else operator.gt

    for i in range(1, len(seq)):
        lower = 0
        upper = L

        if op(seq[M[upper-1]], seq[i]):
            j = upper
        else:
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if op(seq[M[mid-1]], seq[i]):
                    lower = mid
                else:
                    upper = mid
            j = lower

        P[i] = M[j-1]

        if j == L or op(seq[i], seq[M[j]]):
            M[j] = i
            L = max(L, j+1)

    result = []
    pos = M[L-1]
    for _ in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return result[::-1]


ds = get_dataset()
l = [int(x) for x in ds.split()[1:]]

l_inc_ss = longest_mon_subseq(l, decreasing=False)
l_dec_ss = longest_mon_subseq(l, decreasing=True)

print(*l_inc_ss)
print(*l_dec_ss)
