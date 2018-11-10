#!/usr/bin/env python3

import re


keymap = {
    (0, -2) : '1',
    (-1, -1) : '2',
    (0, -1) : '3',
    (1, -1) : '4',
    (-2, 0) : '5',
    (-1, 0) : '6',
    (0, 0) : '7',
    (1, 0) : '8',
    (2, 0) : '9',
    (-1, 1) : 'A',
    (0, 1) : 'B',
    (1, 1) : 'C',
    (0, 2) : 'D',
}


input = open('input').read()

v = h = 0
h2, v2 = -1, 0
digits, digits2 = '', ''
for inst in input.strip().split('\n'):
    for s in inst:
        hlim, vlim = 2-abs(v2), 2-abs(h2)
        if s == 'L':
            h = max(-1, h-1)
            h2 = max(-1*hlim, h2-1)
        if s == 'R':
            h = min(1, h+1)
            h2 = min(hlim, h2+1)
        if s == 'U':
            v = max(-1, v-1)
            v2 = max(-1*vlim, v2-1)
        if s == 'D':
            v = min(1, v+1)
            v2 = min(vlim, v2+1)

    digit = 3 * (v+1) + (h+1) + 1
    digits += str(digit)

    digits2 += keymap[(h2,v2)]

print(digits)
print(digits2)
