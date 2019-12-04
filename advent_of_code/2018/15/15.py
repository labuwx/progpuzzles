#!/usr/bin/env python3

import copy
from collections import deque, OrderedDict
import itertools as it


directions = {(0, 1), (0, -1), (-1, 0), (1, 0)}


def add(xs, ys):
    s = tuple(x + y for x, y in zip(xs, ys))
    return s


def mdist(u, v):
    return abs(u[0] - v[0]) + abs(u[1] - v[1])


def adjoint(u, v):
    return mdist(u, v) == 1


def bfs(nodes, edge, start):
    neighbours = sorted([v for v in nodes if edge(start, v)])  # reading order
    dist = {
        v: (1, v) for v in neighbours
    }  # node: (distance, first node of the shortest path)
    q = deque(neighbours)
    while q:
        v = q.popleft()
        d, p = dist[v]
        nbrs = [u for u in nodes if edge(v, u) and u not in dist.keys()]
        dist.update({u: (d + 1, p) for u in nbrs})
        q.extend(nbrs)
    dist = OrderedDict(sorted(dist.items(), key=lambda x: (x[1][0], x[0])))
    return dist


def draw_map(map, units, round=0):
    print('After %d rounds:' % round)
    for y in range(height):
        s = hs = ''
        for x in range(width):
            pos = (y, x)
            if pos in map:
                t, hp = next(
                    ((t, hp) for p, t, hp in units.values() if p == pos), (None, None)
                )
                if t == None:
                    c = '.'
                else:
                    c = t
                    hs += '%s(%03d) ' % (t, hp)
            else:
                c = '#'
            s += c
        print(s + '   ' + hs)
    print()


def simulate(map, units, elf_power=3, stop_elfdead=False):
    nc = {t: sum(u[1] == t for u in units.values()) for t in 'EG'}
    units = copy.deepcopy(units)
    # draw_map(map, units)
    round = 0
    while nc['G'] * nc['E']:
        round += 1
        order = sorted(units.keys(), key=lambda u: units[u][0])
        for u in order:
            if u not in units.keys():
                continue
            pp, tt, hh = units[u]
            enemies = {p for p, t, _ in units.values() if t != tt}
            en_adj = {add(e, d) for e in enemies for d in directions} & map
            if pp not in en_adj:
                oq = set(p for p, _, _ in units.values())
                nodes = map - oq
                dist = bfs(nodes, adjoint, pp)
                np = next(
                    (par for pos, (_, par) in dist.items() if pos in en_adj - oq), None
                )
                if np == None:
                    continue
                units[u] = (np, tt, hh)
                pp = np

            if pp in en_adj:
                i, (ep, et, eh) = min(
                    (
                        (i, (p, t, h))
                        for i, (p, t, h) in units.items()
                        if adjoint(pp, p) and t != tt
                    ),
                    key=lambda x: (x[1][2], x[1][0]),
                )
                eh -= 3 if et == 'E' else elf_power
                if eh <= 0:
                    if et == 'E' and stop_elfdead:
                        return None
                    del units[i]
                    nc[et] -= 1
                else:
                    units[i] = (ep, et, eh)
        # draw_map(map, units, round)
    hp_remained = sum(h for _, _, h in units.values())
    return round - 1, hp_remained


def main():
    global height, width
    input = open('input').read().strip()

    map, units = set(), {}
    for y, line in enumerate(input.split('\n')):
        for x, c in enumerate(line):
            if c in '.GE':
                p = (y, x)
                map.add(p)
                if c in 'EG':
                    units[len(units)] = (p, c, 200)
    height, width = y + 1, x + 1

    s1 = simulate(map, units)
    s1 = s1[0] * s1[1]

    for elf_power in it.count(4):
        if (s2 := simulate(map, units, elf_power=elf_power, stop_elfdead=True)) != None:
            break
    s2 = s2[0] * s2[1]

    print(s1)
    print(s2)


main()
