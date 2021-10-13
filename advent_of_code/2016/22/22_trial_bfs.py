#!/usr/bin/env python3

from collections import deque
import itertools as it
import re


pattern = re.compile(
    r'/dev/grid/node-x(?P<x>\d+)-y(?P<y>\d+) \s+ (?P<size>\d+)T \s+ (?P<used>\d+)T \s+ (?P<free>\d+)T \s+ (?P<usepc>\d+)%',
    flags=re.VERBOSE,
)

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def state(v):
    _, dnode, map = v
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

    v = (0, node_from, {p: v['used'] for p, v in nodes.items()})
    q = deque([v])
    seen = {state(v)}
    while q:
        d, dnode, map = q.popleft()
        if dnode == node_to:
            s2 = d
            break

        for p, u in map.items():
            for dir in dirs:
                np = cadd(p, dir)
                if np not in nodes or u > nodes[np]['size'] - map[np]:
                    continue
                nmap = dict(map)
                nmap[np] += nmap[p]
                nmap[p] = 0
                ndnode = np if p == dnode else dnode
                v = (d + 1, ndnode, nmap)
                sv = state(v)
                if sv not in seen:
                    seen.add(sv)
                    q.append(v)

    print(s1)
    print(s2)


main()
