#!/usr/bin/env python3

import regex as re


input = open('input').read()

tower = {}
for line in input.split('\n'):
    if line == '': continue
    m = re.match(r'^(?P<node>\w+) \((?P<weight>\d+)\)( ->( (?P<child>\w+),?)+)?$', line)
    node = m.group('node')
    weight = int(m.group('weight'))
    children = set(m.captures('child'))
    tower[node] = (weight, children)


nodes = tower.keys()
children = set()
children.update(*[node[1] for node in tower.values()])

root = list(nodes - children)[0]
print(root)


def least_common(lst):
    return min(set(lst), key=lst.count)

full_weights = {}
found = False
while not found:
    for node, (weight, children) in tower.items():
        if not children.issubset(full_weights.keys()): continue
        children_w = sorted(w for n, w in full_weights.items() if n in children)
        if len(set(children_w)) <= 1:
            weight_up = weight + sum(children_w)
            full_weights[node] = weight_up
        else:
            w_lc = least_common(children_w)
            diff = children_w[0] - w_lc + children_w[-1] - w_lc
            child_wrong = [n for n, w in full_weights.items() if w==w_lc and n in children][0]
            w_wrong = tower[child_wrong][0]
            print(w_wrong + diff)
            found = True
            break


