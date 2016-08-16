import functools
import itertools
import networkx as nx
import numpy as np
import operator
import pprint
import statistics
import sympy as sp
from math import factorial as fact
from statistics import median

pprint = pprint.PrettyPrinter(indent=4).pprint
np.seterr(all='warn', over='raise')


def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return n > 1


def forperm(f, l, r=None):
    for p in itertools.permutations(l, r):
        f(p)


def is_anagram(a, b):
    return Counter(a) == Counter(b)


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
    k = int((2*n) ** 0.5)
    return k*(k+1) == n


def mexp(m, n, mod=None):
    prod = m if n%2 else np.identity(m.shape[0], dtype=object)
    if n:
        prod = prod * mexp(m, n//2, mod) ** 2
    return prod%mod if mod else prod


def linrec(cl, init, n, mod=None):
    terms = np.matrix([1] + init, dtype=object).transpose()
    k = len(terms)

    m = [[1] + [0]*(k-1)] + \
        [[0]*(i+2) + [1] + [0]*(k-i-3) for i in range(k-2)] + \
        [cl]
    m = np.matrix(m, dtype=object)

    m = mexp(m, n, mod)
    term = (m*terms).item(1)
    return term%mod if mod else term


def fib(n, mod=None):
    return linrec([0, 1, 1], [0, 1], n, mod)


def spc_rand(s, n):
    return linrec([500003, 31, 103, 7], [s, 1237, 345892], n-1, 1000001)


def rpn_eval(expr):
    expr = expr
    operators = {
        '+': (operator.add, 2),
        '-': (operator.sub, 2),
        '*': (operator.mul, 2),
        '/': (operator.truediv, 2),
        '^': (operator.pow, 2),
        '%': (operator.mod, 2),
        '_': (lambda x: -x, 1),
    }
    stack = []
    try:
        for token in expr:
            if token in operators:
                if operators[token][1] == 1:
                    stack.append(operators[token][0](stack.pop()))
                elif operators[token][1] == 2:
                    stack.append(operators[token][0](stack.pop(-2), stack.pop()))
            else:
                stack.append(token)
        if len(stack) != 1:
            raise
    except:
        return None
    else:
        return stack[0]


def fastexp(x, n, mod):
    if n <= 0:
        return 1

    y = (fastexp(x, n//2, mod) % mod) ** 2
    if n%2:
        y *= x

    return y % mod


def factors(n):
    factors = []
    for p in range(2, n+1):
        k = 0
        while n%p == 0:
            k += 1
            n //= p
        if k:
            factors.append((p, k))
    return factors


def divsum(n):
    fs = factors(n)
    pr = 1
    for d, k in fs:
        pr *= (d ** (k+1) - 1) // (d -1)
    return pr - n

