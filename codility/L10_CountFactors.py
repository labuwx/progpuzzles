from collections import Counter


def solution(N):
    pfc = Counter()

    p = 2
    while p * p <= N:
        while N % p == 0:
            pfc[p] += 1
            N //= p
        p += 1

    if N > 1:
        pfc[N] = 1

    ndiv = 1
    for k in pfc.values():
        ndiv *= 1 + k

    return ndiv
