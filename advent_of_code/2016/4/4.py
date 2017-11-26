#!/usr/bin/env python3

import re
from collections import Counter

input = open('input').read()

sum = 0
for line in input.split('\n'):
    if line == '': continue
    m = re.match(r'^(?P<name>[a-z\-]*)-(?P<idn>\d*)\[(?P<checks>[a-z]*)\]$', line)
    name = m['name'].replace('-', '')
    idn = int(m['idn'])
    checks = m['checks']

    mc = sorted(Counter(name).items(), key=lambda x: (-x[1], x[0]))
    cs = [x[0] for x in mc[:5]]

    if cs == list(checks):
        sum += idn

print(sum)
