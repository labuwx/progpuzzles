#!/usr/bin/env python3

import itertools as it
import re


def simul(fw, delay=0):
    sev = 0
    caought = False
    for d, r in fw.items():
        if (d+delay) % (2*r-2) == 0:
            caought = True
            sev += d * r
    return sev, caought


input = open('input').read()

fw = {}
for line in input.split('\n'):
    if line == '': continue
    m = re.match(r'^(?P<depth>\d+): (?P<range>\d+)$', line)
    d = int(m.group('depth'))
    r = int(m.group('range'))
    fw[d] = r

sev = simul(fw)[0]
min_delay = next(delay for delay in it.count() if not simul(fw, delay)[1])

print(sev)
print(min_delay)
