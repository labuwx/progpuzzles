#!/usr/bin/env python3

import re
from collections import Counter

input = open('input').read()
alphabet = [chr(i) for i in range(97, 97 + 26)]

sum = 0
for line in input.strip().split('\n'):
    m = re.match(r'^(?P<name>[a-z\-]*)-(?P<idn>\d*)\[(?P<checks>[a-z]*)\]$', line)
    name = m['name']
    idn = int(m['idn'])
    checks = m['checks']

    mc = sorted(Counter(name.replace('-', '')).items(), key=lambda x: (-x[1], x[0]))
    cs = [x[0] for x in mc[:5]]

    if cs == list(checks):
        sum += idn
        dec_name = ''.join(' ' if c == '-' else alphabet[(alphabet.index(c) + idn) % 26] for c in name)
        if 'pole' in dec_name:
            print(idn, dec_name)

print(sum)
