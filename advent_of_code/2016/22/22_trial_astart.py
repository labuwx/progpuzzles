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


def state(v):
    _, _, _, dnode, map = v
    return (dnode, tuple((map.items())))


def main():
    input = open('input').read().strip()
    input = open('input_test').read().strip()
    nodes = {
        (int(m['x']), int(m['y'])): {
            k: int(m[k]) for k in ['size', 'used', 'free', 'usepc']
        }
        for m in pattern.finditer(input)
    }
    node_from = max(p for p in nodes.keys() if p[1] == 0)
    node_to = min(p for p in nodes.keys() if p[1] == 0)

    s1 = sum(
        p1 != p2 and 0 < df1['used'] <= df2['free']
        for (p1, df1), (p2, df2) in it.product(nodes.items(), repeat=2)
    )

    rnd = it.count()
    v = (
        manhattan(node_from, node_to)
        + (1 if nodes[node_to]['free'] < nodes[node_from]['used'] else 0),
        0,
        next(rnd),
        node_from,
        {p: v['used'] for p, v in nodes.items()},
    )
    q = [v]
    seen = set()
    while q:
        v = heapq.heappop(q)
        sv = state(v)
        _, d, _, dnode, map = v

        if sv in seen:
            continue
        else:
            seen.add(sv)

        if dnode == node_to:
            s2 = d
            break

        for p, u in map.items():
            for dir in dirs:
                np = cadd(p, dir)
                if (
                    np not in nodes
                    or u > nodes[np]['size'] - map[np]
                    or (map[np] + u) > nodes[node_to]['size']
                ):
                    continue
                nmap = dict(map)
                nmap[np] += nmap[p]
                nmap[p] = 0
                ndnode = np if p == dnode else dnode
                if ndnode != node_to and (nodes[node_to]['size']) < nmap[ndnode]:
                    continue
                v = (
                    d
                    + 1
                    + manhattan(ndnode, node_to)
                    + (
                        1
                        if (nodes[node_to]['size'] - map[node_to]) < nmap[ndnode]
                        else 0
                    ),
                    d + 1,
                    next(rnd),
                    ndnode,
                    nmap,
                )
                heapq.heappush(q, v)

    print(s1)
    print(s2)


main()
