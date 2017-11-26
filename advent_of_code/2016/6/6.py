#!/usr/bin/env python3

import re
from collections import Counter
from itertools import zip_longest

input = open('input').readlines()
input = list(map(list, zip_longest(*input)))

msg = ''
for line in input:
    if line == '': continue
    c = Counter(line).most_common(1)[0][0]
    msg += c

print(msg)
