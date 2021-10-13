#!/usr/bin/env python3

from collections import deque
import heapq
import itertools as it
import re


pattern = re.compile(
    r'/dev/grid/node-x(?P<x>\d+)-y(?P<y>\d+) \s+ (?P<size>\d+)T \s+ (?P<used>\d+)T \s+ (?P<free>\d+)T \s+ (?P<usepc>\d+)%',
    flags=re.VERBOSE,
)

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def manhattan(p1, p2):
    return sum(abs(c1 - c2) for c1, c2 in zip(p1, p2))


def neighbours(nodes, p):
    return (q for d in dirs if (q := cadd(p, d)) in nodes)


def convert_game(nodes):
    # just 1 sliding hole
    holes = [p for p, u in nodes.items() if u['used'] == 0]
    assert len(holes) == 1
    hole = holes[0]

    # check: unmergeable
    for u, v in it.permutations(nodes.values(), r=2):
        assert u['used'] == 0 or v['used'] == 0 or u['free'] < v['used']

    # find movables with bfs
    movables, qu = set(), deque([hole])
    while qu:
        p = qu.popleft()
        if p in movables:
            continue
        movables.add(p)
        qu.extend(
            q for q in neighbours(nodes, p) if nodes[q]['used'] <= nodes[p]['size']
        )

    # check: free movement
    for (p1, u1), (p2, u2) in it.permutations(nodes.items(), r=2):
        assert p1 not in movables or p2 not in movables or u1['used'] <= u2['size']

    # simplify to a sliding hole puzzle
    return {p for p in nodes if p in movables}, hole


def find_dist(nodes, hole, datpos, u):
    qu = deque([(hole, 0)])
    seen = set()
    while qu:
        v, d = qu.popleft()

        if u == v:
            return d
        if v in seen:
            continue

        seen.add(v)
        qu.extend((q, d + 1) for q in neighbours(nodes, v) if q != datpos)
    assert False


def main():
    input = open('input').read().strip()
    # input = open('input_test').read().strip()
    nodes = {
        (int(m['x']), int(m['y'])): {k: int(m[k]) for k in ['size', 'used', 'free']}
        for m in pattern.finditer(input)
    }
    node_from = max(p for p in nodes.keys() if p[1] == 0)
    node_to = min(p for p in nodes.keys() if p[1] == 0)
    assert nodes[node_from]['size'] > 0

    s1 = sum(
        p1 != p2 and 0 < df1['used'] <= df2['free']
        for (p1, df1), (p2, df2) in it.product(nodes.items(), repeat=2)
    )

    nodes, hole0 = convert_game(nodes)

    rnd = it.count()
    qu = [(manhattan(node_from, node_to), 0, next(rnd), node_from, hole0)]
    seen = set()
    while qu:
        _, d, _, datpos, hole = heapq.heappop(qu)
        sv = datpos, hole

        if sv in seen:
            continue
        else:
            seen.add(sv)

        if datpos == node_to:
            s2 = d
            break

        for u in neighbours(nodes, datpos):
            bfsd = find_dist(nodes, hole, datpos, u)
            ndist = d + bfsd + 1
            v = (ndist + manhattan(u, node_to), ndist, next(rnd), u, datpos)
            heapq.heappush(qu, v)

    print(s1)
    print(s2)


main()
