#!/usr/bin/env python3

import re

input = open('input').read()

v = h = 0
cd = 0
for d, n in re.findall(r'(L|R)(\d+)', input):
    if d == 'L':
        cd += 1
    elif d == 'R':
        cd -= 1
    cd %= 4

    if cd == 0:
        h += int(n)
    elif cd == 1:
        v += int(n)
    elif cd == 2:
        h -= int(n)
    elif cd == 3:
        v -= int(n)

dist = abs(v) + abs(h)
print(dist)
