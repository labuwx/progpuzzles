#!/usr/bin/env python3


from collections import defaultdict, deque


def topo_sort(G, start):
    seen, branch, left = set(), deque(), deque()
    q = deque([start])
    while q:
        v = q.pop()
        if v in seen:
            continue
        seen.add(v)

        q.extend(G.get(v, []))

        while branch and v not in G.get(branch[-1], set()):
            left.append(branch.pop())
        branch.append(v)
    return list(branch) + list(left)[::-1]


def count_paths(G, start, end, include):
    pathcnt = defaultdict(lambda: defaultdict(int))
    pathcnt[start][0] = 1

    toporder = topo_sort(G, start)
    for u in toporder:
        for v in G.get(u, []):
            for visited, k in pathcnt[u].items():
                pathcnt[v][visited + (v in include)] += k
    return pathcnt[end][len(include)]


def main():
    input = open('input').read()
    # input = open('input_test_1').read()
    # input = open('input_test_2').read()

    G = {}
    for l in input.strip().splitlines():
        u, *vs = l.split()
        G[u[:-1]] = set(vs)

    s1 = count_paths(G, 'you', 'out', set())
    s2 = count_paths(G, 'svr', 'out', {'dac', 'fft'})

    print(s1)
    print(s2)


main()
