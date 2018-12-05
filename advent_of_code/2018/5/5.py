#!/usr/bin/env python3

import itertools as it
from collections import deque


def react(chain):
    q = deque(chain)
    q.appendleft(None)

    while q[-1] != None:
        a, b = q[0], q[-1]
        if a == None or a == b or a.lower() != b.lower():
            q.rotate()
        else:
            q.pop()
            q.popleft()
    q.pop()
    return ''.join(q)


input = open('input').read().strip()

s1 = len(react(input))

cs = set(input.lower())
s2 = min(len(react(input.replace(c, '').replace(c.upper(), ''))) for c in cs)

print(s1)
print(s2)
