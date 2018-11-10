#!/usr/bin/env python3

import re


input = open('input').read()

v = h = 0
cd = 0
visited = {(0, 0)}
dist_hq = None
for d, n in re.findall(r'(L|R)(\d+)', input):
    if d == 'L':
        cd += 1
    elif d == 'R':
        cd -= 1
    cd %= 4

    for _ in range(int(n)):
        if cd == 0:
            h += 1
        elif cd == 1:
            v += 1
        elif cd == 2:
            h -= 1
        elif cd == 3:
            v -= 1

        if dist_hq == None:
            p = (h, v)
            if p in visited:
                dist_hq = abs(v) + abs(h)
            else:
                visited.add(p)

dist = abs(v) + abs(h)
print(dist)

print(dist_hq)
