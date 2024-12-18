#!/usr/bin/env python3

from collections import deque
import math


directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def tadd(a, b):
    return tuple(ax + bx for ax, bx in zip(a, b))


def sp(holes, S, E, M, T):
    inmap = lambda pos: all(0 <= pp <= M for pp in pos)
    q = deque([(0, S)])
    reached = {S}
    while q:
        d, pos = q.popleft()

        if pos == E:
            return d

        for dir in directions:
            npos = tadd(pos, dir)
            if inmap(npos) and npos not in reached and holes.get(npos, math.inf) >= T:
                reached.add(npos)
                q.append((d + 1, npos))

    return None


def main():
    input, M, T = open('input').read(), 70, 1024
    # input, M, T = open('input_test').read(), 6, 12
    S, E = (0, 0), (M, M)

    input = [tuple(int(x) for x in l.split(',')) for l in input.strip().splitlines()]
    holes = {pos: i for i, pos in enumerate(input)}

    s1 = sp(holes, S, E, M, T)

    tt, TT = 0, len(holes)
    while tt + 1 < TT:
        mid = (tt + TT) // 2
        if sp(holes, S, E, M, mid) is None:
            TT = mid
        else:
            tt = mid

    s2 = ','.join(str(x) for x in input[tt])

    print(s1)
    print(s2)


main()
