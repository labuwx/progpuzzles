#!/usr/bin/env python3



def digits(n, b):
    ds = []

    while n:
        ds.append(n%b)
        n = n // b

    if not ds:
        ds = [0]

    return ds


def dp(n):
    ds = digits(n, 10)
    return ds == list(reversed(ds))


def bp(n):
    ds = digits(n, 2)
    return ds == list(reversed(ds))


s = 0
for n in range(1, 1000000):
    if dp(n) and bp(n):
        s += n

print(s)

