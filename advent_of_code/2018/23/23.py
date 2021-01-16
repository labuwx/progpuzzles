#!/usr/bin/env python3

import heapq
import itertools as it
import math
import re


def manhattan(p1, p2=None):
    if p2 is None:
        p2 = (0,) * len(p1)
    return sum(abs(c1 - c2) for c1, c2 in zip(p1, p2))


def inrange(bot, pos):
    center, rad = bot
    return manhattan(center, pos) <= rad


def inters(b1, b2):
    return manhattan(b1[0], b2[0]) <= b1[1] + b2[1]


def merge(l1, l2):
    l = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        x1, x2 = l1[i], l2[j]
        if x1 < x2:
            i += 1
        elif x1 > x2:
            j += 1
        else:
            l.append(x1)
            i += 1
            j += 1
    return l


def bounding_planes(bot):
    (x, y, z), r = bot
    plns = (
        (-r + x + y + z, r + x + y + z),  # x+y+z = c
        (-r + x + y - z, r + x + y - z),  # x+y-z = c
        (-r + x - y + z, r + x - y + z),  # x-y+z = c
        (-r + x - y - z, r + x - y - z),  # x-y-z = c
    )
    return plns


def bound_intersection(bounds):
    bound = ((-math.inf, math.inf),) * len(bounds[0])
    for bnd in bounds:
        bound = tuple(
            (max(m1, m2), min(M1, M2)) for (m1, M1), (m2, M2) in zip(bnd, bound)
        )
    return bound


# solve system of linear inequalities
def solve(bounds):
    ((a, A), (b, B), (c, C), (d, D)) = bounds
    m = (3 * a + b + c - D) / 4
    M = (3 * A + B + C - d) / 4
    s = math.ceil(m)

    return s if s <= M else None


rx = re.compile(r'^pos=<(?P<px>-?\d+),(?P<py>-?\d+),(?P<pz>-?\d+)>, r=(?P<r>\d+)$')


def main():
    input = open('input').read().strip().split('\n')
    nanobots = [
        ((int(m['px']), int(m['py']), int(m['pz'])), int(m['r']))
        for m in (rx.fullmatch(l) for l in input)
    ]

    maxbot = max(nanobots, key=lambda bot: bot[1])
    s1 = sum(inrange(maxbot, bot[0]) for bot in nanobots)

    # the spheres (octahedra in Eucl^3) around the bots form a Helly family of order 2
    # proof: the bounded area is described by 4 pairs of parallel planes
    # proof: which are given by 4 Real intervals
    # proof: Real intervals are Helly-2 and the 4 coordinates are independent in this regard
    inters_map = [
        [j for j, b2 in enumerate(nanobots) if i < j and inters(b1, b2)]
        for i, b1 in enumerate(nanobots)
    ]

    rnd = it.count()
    ins_max, selections = 0, []
    q = [(-len(nanobots), 0, next(rnd), [], list(range(len(nanobots))))]
    while q:
        *_, sel, rem = heapq.heappop(q)

        # the queue is sorted by this metric, we will not miss bigger / additional sets of bots
        if len(sel) + len(rem) < ins_max:
            break

        if ins_max < len(sel):
            ins_max = len(sel)
            selections = []

        if len(rem) == 0 and len(sel) == ins_max:
            selections.append(sel)

        for i in rem:
            nrem = merge(rem, inters_map[i])
            nsel = sel + [i]
            heapq.heappush(
                q, (-len(nsel) - len(nrem), -len(sel), next(rnd), nsel, nrem)
            )

    s2 = min(
        solve(bound_intersection([bounding_planes(nanobots[i]) for i in sel]))
        for sel in selections
    )

    print(s1)
    print(s2)


main()
