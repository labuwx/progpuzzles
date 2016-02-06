#!/usr/bin/env python3

dl = ''

for i in range(1,1000000):
    dl += str(i)

res = 1
for e in range(7):
    res *= int(dl[10**e - 1])

print(res)

