#!/usr/bin/env python3

input = open('input').read()

jumps1 = [int(line) for line in input.split('\n') if line != '']
jumps2 = jumps1.copy()

c1, idx = 0, 0
while idx in range(len(jumps1)):
    j = jumps1[idx]
    jumps1[idx] += 1
    idx += j
    c1 += 1

c2, idx = 0, 0
while idx in range(len(jumps2)):
    j = jumps2[idx]
    jumps2[idx] += 1 if j < 3 else -1
    idx += j
    c2 += 1


print(c1)
print(c2)
