#!/usr/bin/env python3


def isprime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


max = 1


def check(l):
    global max
    n = int(''.join([str(k) for k in l]))
    if n > max and isprime(n):
        print(n)
        max = n


def forperm(l, f, t=[]):
    if l:
        for i in range(len(l)):
            p = t[:]
            p.append(l[i])
            l2 = l[:]
            del l2[i]
            forperm(l2, f, p)
    else:
        f(t)


for i in range(1, 10):
    l = list(range(1, i + 1))
    forperm(l, check)

print(max)
