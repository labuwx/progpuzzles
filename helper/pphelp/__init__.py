import functools as ft
import itertools as it
import networkx as nx
import numpy as np
import operator
import pprint
import statistics
import sympy as sp
from math import factorial as fact, gcd, floor, sqrt
from statistics import median

pprint = pprint.PrettyPrinter(indent=4).pprint
np.seterr(all='warn', over='raise')


def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return n > 1


def forperm(f, l, r=None):
    for p in it.permutations(l, r):
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


def tonum(l, b=10):
    l = list(l)
    return ft.reduce(lambda acc, x: b * acc + x, reversed(l), 0)


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


def triangle_num(n):
    return n * (n+1) // 2


def is_triangle(k):
    n = round(((1 + 8*k) ** 0.5 - 1) / 2)
    return k == triangle_num(n)


def pentagonal_num(n):
    return n * (3*n - 1) // 2


def is_pentagonal(k):
    n = round(((24*k + 1) ** (1/2) + 1) / 6)
    return k == pentagonal_num(n)


def hexagonal_num(n):
    return n * (2*n - 1)


def is_hexagonal(k):
    n = round(((1 + 8*k) ** 0.5 + 1) / 4)
    return k == hexagonal_num(n)


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
    p, factors = 2, []
    sqrt_n = floor(sqrt(n))
    while p <= sqrt_n:
        k = 0
        while n%p == 0:
            k += 1
            n //= p
        if k:
            factors.append((p, k))
            sqrt_n = floor(sqrt(n))
        p += 1
    if n > 1:
        factors.append((n, 1))
    return factors


def divsum(n):
    fs = factors(n)
    pr = 1
    for d, k in fs:
        pr *= (d ** (k+1) - 1) // (d -1)
    return pr - n


def nCr(n, r):
    return fact(n) / fact(r) / fact(n-r)


def is_palindrome(n):
    ds = digits(n)
    return list(reversed(ds)) == ds


def is_lychrel(n):
    assert n < 10677
    for _ in range(50 + 1):
        n_rev = tonum(reversed(digits(n)))
        n += n_rev
        if is_palindrome(n):
            return False
    return True


def simplify(num, denom):
    d = gcd(num, denom)
    return num//d, denom//d


def eratosthenes_sieve(n):
    t = [False, False] + [True] * (n-2)
    i = 2
    while True:
        for j in range(2*i, n, i):
            t[j] = False
        try:
            i = t.index(True, i+1)
        except ValueError:
            break
    # return {k for k, v in enumerate(t) if v}
    return t
