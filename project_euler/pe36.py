#!/usr/bin/env python3



def digits(n, b):
    return []


def dp(n):
    ds = digits(n, 10)
    return ds == reversed(ds)


def bp(n):
    ds = digits(n, 2)
    return ds == reversed(ds)


s = 0
for n in range(1, 1000000):
    if dp(n) and bp(n):
        s += n

print(s)

