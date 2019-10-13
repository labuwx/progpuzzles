#!/usr/bin/env python3

import itertools as it
import re
from collections import defaultdict
from datetime import datetime


input = open('input').read().strip().split('\n')
rx = re.compile(
    r'^\[(?P<dt>.*?)\] (?:(?P<sleep>falls asleep)|(?P<wake>wakes up)|(?P<change>Guard #(?P<id>\d*) begins shift))$'
)

records = []
for l in input:
    m = rx.match(l)
    dt = datetime.strptime(m.group('dt'), r'%Y-%m-%d %H:%M')
    if m.group('change'):
        e = 0
        id = int(m.group('id'))
    elif m.group('sleep'):
        e = 1
        id = None
    else:
        e = 2
        id = None
    records.append((dt, e, id))

records.sort()

slept = defaultdict(lambda: [0] * 60)
for i in range(len(records)):
    dt, e, id = records[i]
    if e == 0:
        cid = id
    elif e == 1:
        start = dt.minute
    else:
        stop = dt.minute
        for t in range(start, stop):
            slept[cid][t] += 1

id_ms = max(slept.keys(), key=lambda id: sum(slept[id]))
s1 = id_ms * max(range(60), key=lambda t: slept[id_ms][t])

id2, t = max(it.product(slept.keys(), range(60)), key=lambda x: slept[x[0]][x[1]])
s2 = id2 * t

print(s1)
print(s2)
