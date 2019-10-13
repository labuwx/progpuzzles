#!/usr/bin/env python3

import operator
import regex as re
from collections import defaultdict


input = open('input').read()
input_bck = re.sub(r'(\n|!.)', '', input)
input = re.sub(r'<[^>]*>', '', input_bck)
input = re.sub(r',', '', input)

depth = score = 0
for c in input:
    if c == '{':
        depth += 1
        score += depth
    else:
        depth -= 1

m = re.findall(r'<([^>]*)>', input_bck)
com_len = len(''.join(m))

print(score)
print(com_len)
