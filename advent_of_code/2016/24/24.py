#!/usr/bin/env python3

from collections import deque


def myint(x):
    try:
        res = int(x)
    except:
        res = x

    return res


dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def inrange(a, b, c):
    return all(ai <= bi < ci for ai, bi, ci in zip(a, b, c))


def main():
    input = open('input').read().strip().split('\n')
    map = [list(l) for l in input]
    shape = len(map[0]), len(map)

    map, maxnum = {}, 0
    for y, l in enumerate(input):
        for x, c in enumerate(l):
            v = myint(c)
            map[(x, y)] = v
            if v == 0:
                init_pos = (x, y)
            elif isinstance(v, int):
                maxnum = max(maxnum, v)

    seen = {(init_pos, frozenset({0}))}
    q = deque([(init_pos, frozenset({0}), 0)])
    s1 = None
    while q:
        pos, rnum, d = q.popleft()

        if len(rnum) == maxnum + 1:
            s1 = d if s1 == None else s1
            if pos == init_pos:
                s2 = d
                break

        adj = set()
        for dir in dirs:
            next_pos = cadd(pos, dir)
            v = map[next_pos]
            if not inrange((0, 0), next_pos, shape) or v == '#':
                continue
            next_rnum = rnum | ({v} if isinstance(v, int) else set())
            adj.add((next_pos, next_rnum))
        adj -= seen
        seen.update(adj)
        q.extend((next_pos, next_rnum, d + 1) for next_pos, next_rnum in adj)

    print(s1)
    print(s2)


main()
