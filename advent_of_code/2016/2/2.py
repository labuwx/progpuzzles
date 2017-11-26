#!/usr/bin/env python3

import re

input = open('input').read()


v = h = 0
digits = ''
for inst in input.split('\n'):
    if inst == '': continue

    for s in inst:
        if s == 'L':
            h = max(-1, h-1)
        if s == 'R':
            h = min(1, h+1)
        if s == 'U':
            v = max(-1, v-1)
        if s == 'D':
            v = min(1, v+1)

    digit = 3 * (v+1) + (h+1) + 1
    digits += str(digit)

print(digits)
