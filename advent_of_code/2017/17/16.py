#!/usr/bin/env python3

step = 337

buffer, idx = [], 0
for i in range(2018):
    buffer.insert(idx, i)
    idx = (idx + step) % (i + 1) + 1
res1 = buffer[buffer.index(2017) + 1]

b1, idx = None, 0
for i in range(50000000):
    if idx == 1:
        b1 = i
    idx = (idx + step) % (i + 1) + 1

print(res1)
print(b1)
