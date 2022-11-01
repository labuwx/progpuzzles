import math


def solution(A):
    m, mp = math.inf, 0
    for x in A:
        mp = max(mp, x - m)
        m = min(m, x)

    return mp
