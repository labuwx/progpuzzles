#!/usr/bin/env python3

from collections import deque


directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def tadd(a, b):
    return tuple(ax + bx for ax, bx in zip(a, b))


def manhattan(u, v):
    return sum(abs(uu - vv) for uu, vv in zip(u, v))


def bfs(map, v):
    q = deque([(v, 0)])
    reached = {}
    while q:
        v, d = q.popleft()

        if v in reached:
            continue
        reached[v] = d

        for dir in directions:
            if map.get((u := tadd(v, dir))) == '.':
                q.append((u, d + 1))

    return reached


def main():
    input = open('input').read()
    # input = open('input_test').read()
    C1, C2 = 2, 20
    K = 100

    map = {}
    for y, l in enumerate(input.strip().splitlines()):
        for x, c in enumerate(l):
            pos = (x, y)
            map[pos] = c
            if c == 'S':
                S = pos
                map[pos] = '.'
            elif c == 'E':
                E = pos
                map[pos] = '.'

    # r_X are already sorted by distance
    r_fwd = bfs(map, S)
    r_bwd = bfs(map, E)
    dn = r_fwd[E]

    s1 = s2 = 0
    for u, du in r_fwd.items():
        for v, dv in r_bwd.items():
            md = manhattan(u, v)
            if du + dv + md <= dn - K:
                s1 += md <= C1
                s2 += md <= C2
            elif du + dv > dn - K:
                break
        if du > dn - K:
            break

    print(s1)
    print(s2)


main()
