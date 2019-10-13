#!/usr/bin/env python3

import regex as re


input = open('input').read()

graph = {}
for line in input.split('\n'):
    if line == '':
        continue
    m = re.match(r'^(?P<node>\d+) <->( (?P<child>\d+),?)+$', line)
    node = int(m.group('node'))
    children = set(map(int, m.captures('child')))
    graph[node] = children


reached = {node: (children | {node}) for node, children in graph.items()}
change = True
while change:
    change = False
    for rnode in set(reached.keys()):
        reach = reached[rnode]
        reach2 = reach.union(*[reached[node] for node in reach])
        if len(reach) < len(reach2):
            change = True
            for node in reach:
                reached[node] = reach2

reached = {node: frozenset(reach) for node, reach in reached.items()}

print(len(reached[0]))
print(len(set(reached.values())))
