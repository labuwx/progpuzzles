#!/usr/bin/env python3

import itertools as it
import re


def length(step):
    step = step.upper()
    return ord(step) - ord('A') + 1 + 60


rx = re.compile(
    r'^Step (?P<from>\w+) must be finished before step (?P<to>\w+) can begin.$'
)
input = open('input').read().strip().split('\n')
input = {(m.group('from'), m.group('to')) for m in (rx.match(l) for l in input)}

steps = {e[i] for e in input for i in range(2)}

dependencies = {s: 0 for s in steps}
dependents = {s: set() for s in steps}
for a, b in input:
    dependencies[b] += 1
    dependents[a].add(b)
dependencies_orig = dict(dependencies)

order = []
while len(order) != len(steps):
    next_step = min(s for s in steps if dependencies[s] == 0)
    order.append(next_step)
    dependencies[next_step] = -1
    for d in dependents[next_step]:
        dependencies[d] -= 1
s1 = ''.join(order)

dependencies = dict(dependencies_orig)
workers, done = [None] * 5, set()
for t in it.count():
    if len(done) == len(steps):
        break
    for w in range(len(workers)):
        x = workers[w]
        if x == None:
            continue
        step, rem = x
        rem -= 1
        if rem == 0:
            done.add(step)
            workers[w] = None
            for d in dependents[step]:
                dependencies[d] -= 1
        else:
            workers[w] = (step, rem)

    for w in range(len(workers)):
        x = workers[w]
        if workers[w] != None:
            continue
        next_step = min((s for s in steps if dependencies[s] == 0), default=None)
        if next_step == None:
            break
        dependencies[next_step] = -1
        workers[w] = next_step, length(next_step)

s2 = t - 1

print(s1)
print(s2)
