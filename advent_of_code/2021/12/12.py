#!/usr/bin/env python3

from collections import Counter, defaultdict
from heapq import heappush, heappop
import itertools as it


# limitation
# if there is a loop of big caves that later would turn out to be impossible to finish
# this algorithm will not terminate
#
# idea
# merge states when possible: when decisions from the past that limit future decisions are the same
#   = the exact same small caves visited
# small_cnt is used to visit all states that lead to the same merged state, before visiting the merged state


START_NODE, END_NODE = -1, -2


def parse_input(input):
    neg_cnt, pos_cnt = it.count(-3, -1), it.count()
    node_map = {'start': START_NODE, 'end': END_NODE}
    graph = defaultdict(set)

    for l in input.split('\n'):
        uv = []
        for us in l.strip().split('-'):
            if (u := node_map.get(us)) is None:
                u = next(neg_cnt if us.isupper() else pos_cnt)
                node_map[us] = u
            uv.append(u)
        u, v = uv

        if u != END_NODE and v != START_NODE:
            graph[u].add(v)
        if v != END_NODE and u != START_NODE:
            graph[v].add(u)

    for u in graph:
        graph[u] = list(graph[u])

    return graph


def traverse(graph, revisit_small_cave=False):
    heap_cnt = it.count()
    init_key = START_NODE, frozenset(), False
    q = [(0, next(heap_cnt), *init_key)]
    reach_cnt = Counter({init_key: 1})
    path_cnt = 0
    while q:
        small_cnt, _, *key = heappop(q)
        u, visited, cave_revisited = key
        n_reached = reach_cnt[tuple(key)]

        if u == END_NODE:
            path_cnt += n_reached
            continue

        for v in graph[u]:
            if v < 0:
                next_visited = visited
                next_cave_revisited = cave_revisited
                next_small_cnt = small_cnt
            elif v not in visited:
                next_visited = visited | {v}
                next_cave_revisited = cave_revisited
                next_small_cnt = small_cnt + 1
            elif revisit_small_cave and not cave_revisited:
                next_visited = visited | {v}
                next_cave_revisited = True
                next_small_cnt = small_cnt + 1
            else:
                continue

            next_key = v, next_visited, next_cave_revisited
            if next_key not in reach_cnt:
                x = next_small_cnt, next(heap_cnt), *next_key
                heappush(q, x)
            reach_cnt[next_key] += n_reached

    return path_cnt


def main():
    input = open('input').read().strip()
    # input = open('input_test_3').read().strip()
    graph = parse_input(input)

    s1 = traverse(graph, revisit_small_cave=False)
    s2 = traverse(graph, revisit_small_cave=True)

    print(s1)
    print(s2)


main()
