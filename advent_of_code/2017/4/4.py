#!/usr/bin/env python3

input = open('input').read()

c1 = c2 = 0
for passwd in input.split('\n'):
    if passwd == '':
        continue
    parts = passwd.split(' ')
    parts_s = [str(sorted(word)) for word in parts]
    if len(parts) == len(set(parts)):
        c1 += 1
    if len(parts_s) == len(set(parts_s)):
        c2 += 1

print(c1)
print(c2)
