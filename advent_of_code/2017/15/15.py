#!/usr/bin/env python3

af, bf = 16807, 48271
m = 2147483647


a, b = 634, 301
total = 0
for _ in range(40000000):
    a = (a * af) % m
    b = (b * bf) % m
    if (a-b) % 2**16 == 0:
        total += 1

print(total)


a, b = 634, 301
total = 0
for _ in range(5000000):
    fnd = False
    while not fnd:
        a = (a * af) % m
        fnd = a%4 == 0
    fnd = False
    while not fnd:
        b = (b * bf) % m
        fnd = b%8 == 0
    if (a-b) % 2**16 == 0:
        total += 1

print(total)
