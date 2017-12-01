#!/usr/bin/env python3

import re

input = open('input').read()

cnt = 0
for line in input.split('\n'):
    if line == '': continue
    gabba, brackets, aib = False, False, False
    for i in range(len(line) - 3):
        if line[i] in '[]':
            brackets = not brackets
            continue
        if set(line[i:i+4]) & set('[]'): continue
        abba = (line[i:i+2] == line[i+3:i+1:-1]) and (line[i] != line[i+1])
        aib |= abba and brackets
        gabba |= abba
    if gabba and not aib:
        cnt += 1


print(cnt)
