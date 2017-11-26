#!/usr/bin/env python3

import re

input = open('input').read()

cnt = 0
for line in input.split('\n'):
    if line == '': continue
    for blk in re.findall(r'\[?[a-z]*\]?', line):
        


print(sum)
