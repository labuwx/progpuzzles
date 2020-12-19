#!/usr/bin/env python3

from collections import deque
import enum
import heapq
import itertools as it
import re


pattern = re.compile(r'depth: (?P<depth>\d+)\ntarget: (?P<x>\d+),(?P<y>\d+)')

Tool = enum.Enum('Tool', 'neither torch climbgear')

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

tool_map = [
    {Tool.torch, Tool.climbgear},
    {Tool.neither, Tool.climbgear},
    {Tool.neither, Tool.torch},
]


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def manhattan(p1, p2):
    return sum(abs(c1 - c2) for c1, c2 in zip(p1, p2))


def idx_to_err(depth, idx):
    return (idx + depth) % 20183


def get_type(erosion_levels, depth, pos):
    q = deque([pos])
    while q:
        x, y = q[-1]
        if (x, y) not in erosion_levels:
            if (x, y) == (0, 0):
                v = 0
            elif y == 0:
                v = x * 16807
            elif x == 0:
                v = y * 48271
            else:
                if (e1 := erosion_levels.get((x - 1, y), None)) == None:
                    q.append((x - 1, y))
                    continue
                if (e2 := erosion_levels.get((x, y - 1), None)) == None:
                    q.append((x, y - 1))
                    continue
                v = e1 * e2

            erosion_levels[(x, y)] = idx_to_err(depth, v)
        q.pop()

    return erosion_levels[pos] % 3


def main():
    input = open('input').read().strip()
    minput = pattern.match(input)
    depth = int(minput['depth'])
    target = (int(minput['x']), int(minput['y']))

    erosion_levels = {target: idx_to_err(depth, 0)}
    gett = lambda p: get_type(erosion_levels, depth, p)

    risk = sum(
        gett(pos) for pos in it.product(range(target[0] + 1), range(target[1] + 1))
    )

    rnd = it.count()
    q = [(manhattan((0, 0), target), 0, next(rnd), (0, 0), Tool.torch)]
    seen = set()
    while q:  # A* algorithm
        _, d, _, pos, tool = heapq.heappop(q)

        sv = (pos, tool)
        if sv in seen:
            # works because the heuristic is consistent
            continue
        else:
            seen.add(sv)

        if sv == (target, Tool.torch):
            s2 = d
            break

        if pos == target:
            heapq.heappush(q, (d + 7, d + 7, next(rnd), pos, Tool.torch))
            continue

        adj = (npos for dir in dirs if min(npos := cadd(pos, dir)) >= 0)
        for npos in adj:
            allowed_tools = tool_map[gett(pos)] & tool_map[gett(npos)]
            next_tools = {tool} if tool in allowed_tools else allowed_tools
            for ntool in next_tools:
                nd = d + 1 + (0 if tool == ntool else 7)
                heapq.heappush(
                    q,
                    (
                        nd
                        + manhattan(npos, target)
                        + (0 if ntool == Tool.torch else 7),
                        nd,
                        next(rnd),
                        npos,
                        ntool,
                    ),
                )

    print(risk)
    print(s2)


main()
