import functools
import numpy as np
from math import factorial as fact

np.seterr(all='warn', over='raise')


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


def mexp(m, n, mod=None):
    prod = m if n%2 else np.identity(m.shape[0], dtype=object)
    if n:
        prod = prod * (mexp(m, n//2, mod) ** 2)
    return prod%mod if mod else prod


def linrec(cl, init, n, mod=None):
    terms = np.matrix([1] + init, dtype=object).transpose()
    k = len(terms)

    m = [[1] + [0]*(k-1)]
    for i in range(k-2):
        r = [0]*(i+2) + [1] + [0]*(k-i-3)
        m.append(r)
    m.append(cl)
    m = np.matrix(m, dtype=object)


    m = mexp(m, n, mod)
    term = (m*terms).item(-1)
    return term%mod if mod else term


def fib(n, mod=None):
    return linrec([0, 1, 1], [1, 1], n, mod)

