#!/usr/bin/env python3

import itertools as it


input = open('input').read()
input = [int(x) for x in input.split()]

s1 = sum(input)

reached, f, s2 = {0}, 0, None
for d in it.cycle(input):
    f += d
    if f in reached:
        s2 = f
        break
    reached.add(f)

print(s1)
print(s2)
