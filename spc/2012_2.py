#!/usr/bin/env python3

from pphelp import *


def F(n, mod=None):
    return linrec([0, 1, 1], [1, 3], n - 1, 1234567)


print(F(20))
print(F(5000, 1234567))
print(F(50000, 1234567))
print(F(5000000, 1234567))
print(F(5000000000, 1234567))
print(F(5000000000000, 1234567))
