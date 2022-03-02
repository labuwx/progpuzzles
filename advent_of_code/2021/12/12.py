#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
import itertools as it


# limitation
# if there is a loop of big caves that later would turn out to be impossible to finish
# this algorithm will not terminate or just give incorrect result
#
# idea
# merge states when possible: when decisions from the past that limit future decisions are the same
#   = the exact same small caves visited
# this way there are only combination many visit not permutation many


START_NODE, END_NODE = 0, 1


def parse_input(input):
    neg_cnt, pos_cnt = it.count(-1, -1), it.count(2, 1)
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


def simplify_graph(graph):
    # convert path through big caves to multi edges
    # no big cave loops => at most 1 big cave between small caves
    scave_to_scave_cnt = Counter()
    for cave, adj_caves in graph.items():
        if cave < 0:
            continue
        for cave2 in adj_caves:
            if cave2 >= 0:
                scave_to_scave_cnt[(cave, cave2)] += 1
            else:  # cave 2 is an inbetween big cave
                for cave3 in graph[cave2]:
                    # assert cave3 >= 0
                    scave_to_scave_cnt[(cave, cave3)] += 1

    ngraph = defaultdict(list)
    for (u, v), k in scave_to_scave_cnt.items():
        ngraph[u].append((v, k))

    return ngraph


# this is a DFS (on the graph of states) where the metric is len(path) + int(revisited)
def traverse(graph, revisit_small_cave=False):
    path_cnt = 0
    init_state = (START_NODE, frozenset({START_NODE}), False)
    reach_cnt = Counter({init_state: 1})
    q = deque([init_state])
    while q:
        state = q.popleft()
        u, path, revisited = state
        n_reached = reach_cnt.pop(state)

        if u == END_NODE:
            path_cnt += n_reached
            continue

        for v, k in graph[u]:
            if v not in path:
                next_state = (v, path | {v}, revisited)
            elif revisit_small_cave and not revisited:
                next_state = (v, path, True)
            else:
                continue

            if next_state not in reach_cnt:
                q.append(next_state)
            reach_cnt[next_state] += k * n_reached

    return path_cnt


def main():
    input = open('input').read().strip()
    # input = open('input_test_3').read().strip()

    graph = parse_input(input)
    graph = simplify_graph(graph)

    s1 = traverse(graph, revisit_small_cave=False)
    s2 = traverse(graph, revisit_small_cave=True)

    print(s1)
    print(s2)


main()
