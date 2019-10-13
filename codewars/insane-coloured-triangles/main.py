#!/usr/bin/env python3

cdmap = 'RGB'


def d2c(d):
    return cdmap[d % 3]


def c2d(c):
    return cdmap.index(c)


def rncr(n, k):
    if n < k:
        return 0
    elif n == k or k == 0:
        return 1
    else:
        return 2
    # return fact(n) // fact(k) // fact(n-k)


def ncr(n, k):
    r = 1
    for nn, kk in zip(n, k):
        r = (r * rncr(nn, kk)) % 3
    return r


def inc(l):
    for i in range(len(l)):
        if l[i] < 2:
            l[i] += 1
            break
        else:
            l[i] = 0


def triangle(row):
    row = [c2d(c) for c in row]
    n = digits(len(row) - 1)
    k = [0] * len(n)
    res = 0
    for d in row:
        res = (res + ncr(n, k) * d) % 3
        inc(k)
    if not len(row) % 2:
        res = 3 - res
    return d2c(res)


def digits(n):
    ds = []
    while n:
        ds.append(n % 3)
        n //= 3
    return ds


# rrr = 'RBRGGBRBGGRRRBGBBBGG' * 10000
# for _ in range(30):
# triangle(rrr)
# print(triangle(rrr))
# print(triangle('RBRGGBRBGGRRRBGBBBGG' * 100000))
print(triangle('RBRGBRBGGRRRBGBBBGG'))
print(triangle('RBRGBRB'))
print(triangle('RGBG'))
print(triangle('RRR'))
print(triangle('GB'))
