import math


def solution(A):
    ps = 0
    m, msum = 0, -math.inf
    for x in A:
        ps += x
        msum = max(msum, ps - m)
        m = min(m, ps)

    return msum
