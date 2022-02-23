#!/usr/bin/env python3

from collections import Counter, defaultdict, deque


# limitation
# if there is a loop of big caves that later would turn out to be impossible to finish
# this algorithm will not terminate


START_NODE, END_NODE = 'start', 'end'


def parse_input(input):
    edges = [l.strip().split('-') for l in input.split('\n')]
    return edges


def traverse(nbrs, revisit_small_cave=False):
    q = deque([(START_NODE, {START_NODE}, None)])
    path_cnt = 0
    while q:
        u, visited, revisited_cave = q.pop()

        if u == END_NODE:
            path_cnt += 1
            continue

        for v in nbrs[u]:
            if v.isupper() or v not in visited:
                q.append((v, visited | {v}, revisited_cave))
            elif revisit_small_cave and revisited_cave is None:
                q.append((v, visited | {v}, v))

    return path_cnt


def main():
    input = open('input').read().strip()
    # input = open('input_test_3').read().strip()
    edges = parse_input(input)

    nbrs = defaultdict(set)
    for u, v in edges:
        if u != END_NODE and v != START_NODE:
            nbrs[u].add(v)
        if v != END_NODE and u != START_NODE:
            nbrs[v].add(u)

    s1 = traverse(nbrs, revisit_small_cave=False)
    s2 = traverse(nbrs, revisit_small_cave=True)

    print(s1)
    print(s2)


main()
