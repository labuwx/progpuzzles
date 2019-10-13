#!/usr/bin/env python3

import re

input = open('input').read()

cnt, cnt2 = 0, 0
for line in input.split():
    gabba, brackets, aib = False, False, False
    aba, bab = set(), set()
    for i in range(len(line) - 2):
        if line[i] in '[]':
            brackets = not brackets
            continue
        if set(line[i : i + 3]) & set('[]'):
            continue
        if (not brackets) and line[i] == line[i + 2] != line[i + 1]:
            aba.add(line[i + 1] + line[i] + line[i + 1])
        if brackets and line[i] == line[i + 2] != line[i + 1]:
            bab.add(line[i : i + 3])
        if i < len(line) - 3 and line[i + 3] not in '[]':
            abba = (line[i : i + 2] == line[i + 3 : i + 1 : -1]) and (
                line[i] != line[i + 1]
            )
            aib |= abba and brackets
            gabba |= abba

    if gabba and not aib:
        cnt += 1
    if aba & bab:
        cnt2 += 1


print(cnt)
print(cnt2)
