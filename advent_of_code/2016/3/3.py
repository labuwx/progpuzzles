#!/usr/bin/env python3

import re

input = open('input').read()

cnt = 0
for line in input.split('\n'):
    if line == '': continue
    a, b, c = sorted(int(x) for x in line.split(' ') if x != '')
    if a + b > c:
        cnt += 1

print(cnt)
