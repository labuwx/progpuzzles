import functools
import numpy as np
from math import factorial as fact


def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return n > 1


def forperm(f, l, t=[]):
    if l == []:
        f(t)
    for i in range(len(l)):
        p = t[:]
        p.append(l[i])
        l2 = l[:]
        del l2[i]
        forperm(f, l2, p)


def ispan(n):
    return len(str(n)) == 9 and  \
           set(str(n)) == {str(i) for i in range(1, 10)}


def digits(n, b=10):
    ds = []
    while n:
        ds.append(n%b)
        n = n // b
    if ds == []:
        ds = [0]
    return ds


def dsum(n, b):
    return sum(digits(n, b))


def tonum(l, b):
    return reduce(lambda acc, x: b * acc + x, l[::-1], 0)


def is_curious(n):
    k = n
    s = 0
    while k:
        s += fact(k % 10)
        k //= 10
    return n == s


def denom_rec(d, n=1):
    nl = []
    while n and n not in nl:
       nl.append(n)
       n = (n % d) * 10
    return len(nl) - nl.index(n) if n else 0


def isleap(y):
    return not(y%400) or bool(y%100) and not(y%4)


def istriangle(n):
    n = 2 * n
    k = int(n**0.5)
    return k*(k+1) == n


def mexp(m1, n, mod=None):
    prod = 
    return mexp(m1


def linrec(cl, init, n):
    return


def fib(n):
    return linrec([1,1,0], [1, 1], n)

